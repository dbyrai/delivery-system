#!/usr/bin/env python3
"""Preview or merge one project-local HTTP MCP profile. No network or login."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import tomllib
from urllib.parse import parse_qsl, urlsplit

ADAPTERS = {
    "jira": "delivery_atlassian",
    "confluence": "delivery_atlassian",
    "github-projects": "delivery_github",
    "gitlab": "delivery_gitlab",
}
CLIENTS = {
    "codex": (".codex/config.toml", "mcp_servers"),
    "claude-code": (".mcp.json", "mcpServers"),
    "vscode": (".vscode/mcp.json", "servers"),
}


class ConfigurationError(Exception):
    """A safe refusal that never includes configuration contents."""


def profile(args: argparse.Namespace) -> tuple[str, dict]:
    name = args.server_name or ADAPTERS[args.adapter]
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", name):
        raise ConfigurationError("Server name must be a simple identifier.")
    if any(ord(c) < 33 or ord(c) == 127 for c in args.url):
        raise ConfigurationError("Endpoint URL must not contain whitespace or control characters.")
    try:
        url = urlsplit(args.url)
        port = url.port
    except ValueError:
        raise ConfigurationError("Invalid endpoint URL.") from None
    if (url.scheme != "https" or not url.hostname or url.username is not None
            or url.password is not None or url.fragment or (port is not None and port < 1)):
        raise ConfigurationError("Use an HTTPS endpoint without credentials or a fragment.")
    # The official Atlassian flat-catalog switch is non-secret. No auth query strings.
    if url.query and parse_qsl(url.query, keep_blank_values=True) != [("tools", "all")]:
        raise ConfigurationError("Only the non-secret tools=all query is supported.")
    env = args.bearer_token_env_var
    if env and (not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", env)
                or env.startswith(("ghp_", "gho_", "ghu_", "ghs_", "ghr_", "github_pat_", "glpat-"))):
        raise ConfigurationError("Provide an environment variable NAME, never its value.")
    tools = list(dict.fromkeys(args.tool or []))
    if any(not re.fullmatch(r"[A-Za-z0-9_.:-]+", t) for t in tools):
        raise ConfigurationError("Tool names must be exact discovered identifiers, not wildcards.")
    if tools and args.client != "codex":
        raise ConfigurationError("--tool is Codex-only; configure other clients' tool permissions in their UI.")
    if args.discovery_only and (args.client != "codex" or tools):
        raise ConfigurationError("--discovery-only is Codex-only and cannot be combined with --tool.")
    if args.apply and args.client == "codex" and not tools and not args.discovery_only:
        raise ConfigurationError("Codex apply requires verified --tool names or --discovery-only for initial diagnostics.")
    if args.client == "codex":
        config = {"url": args.url, "startup_timeout_sec": 60, "tool_timeout_sec": 60}
        if tools or args.discovery_only:
            config["enabled_tools"] = tools
        if env:
            config["bearer_token_env_var"] = env
    else:
        config = {"type": "http", "url": args.url}
        if env:
            reference = f"${{{env}}}" if args.client == "claude-code" else f"${{env:{env}}}"
            config["headers"] = {"Authorization": f"Bearer {reference}"}
    return name, config


def toml_block(name: str, config: dict) -> str:
    # Keys and value types are controlled by profile(), not arbitrary user TOML.
    lines = [f"[mcp_servers.{name}]"]
    lines.extend(f"{key} = {json.dumps(value, ensure_ascii=True)}" for key, value in config.items())
    return "\n".join(lines) + "\n"


def merge(raw: str, client: str, name: str, config: dict) -> tuple[str, bool]:
    key = CLIENTS[client][1]
    try:
        data = tomllib.loads(raw) if client == "codex" else (json.loads(raw) if raw.strip() else {})
    except (tomllib.TOMLDecodeError, json.JSONDecodeError):
        raise ConfigurationError("Existing configuration does not parse; JSONC/comments require a manual merge.") from None
    if not isinstance(data, dict) or not isinstance(data.get(key, {}), dict):
        raise ConfigurationError("Existing configuration has an unsupported server-map shape.")
    servers = data.get(key, {})
    if name in servers:
        if servers[name] == config:
            return raw, False
        raise ConfigurationError("Named profile already differs. Review and merge that profile manually; no overwrite performed.")
    if client == "codex":
        combined = raw + ("\n" if raw and not raw.endswith("\n") else "") + "\n" + toml_block(name, config)
        try:
            parsed = tomllib.loads(combined)
        except tomllib.TOMLDecodeError:
            raise ConfigurationError("Cannot append safely to this TOML layout; merge the preview manually.") from None
        expected = dict(data)
        expected[key] = {**servers, name: config}
        if parsed != expected:
            raise ConfigurationError("Merge would change unrelated configuration; no write performed.")
        return combined, True
    data[key] = {**servers, name: config}
    return json.dumps(data, indent=2, ensure_ascii=True) + "\n", True


def apply(root: Path, client: str, name: str, config: dict) -> tuple[Path, bool]:
    root = root.resolve(strict=True)
    if not root.is_dir() or root == Path.home().resolve():
        raise ConfigurationError("Choose a project directory, not your home/global configuration directory.")
    destination = root / CLIENTS[client][0]
    # Refuse symlinked config paths instead of modifying a different project's/global config.
    for p in [destination.parent, destination]:
        if p.is_symlink() or not p.resolve().is_relative_to(root):
            raise ConfigurationError("Configuration path escapes the project or is symlinked.")
    if destination.exists() and not destination.is_file():
        raise ConfigurationError("Configuration destination is not a regular file.")
    before = destination.read_bytes() if destination.exists() else None
    try:
        raw = before.decode("utf-8") if before is not None else ""
    except UnicodeDecodeError:
        raise ConfigurationError("Existing configuration is not UTF-8; merge manually.") from None
    combined, changed = merge(raw, client, name, config)
    if not changed:
        return destination, False
    destination.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(destination.stat().st_mode) if before is not None else 0o600
    fd, temporary = tempfile.mkstemp(prefix=".delivery-mcp-", dir=destination.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            os.fchmod(stream.fileno(), mode)
            stream.write(combined.encode("utf-8"))
            stream.flush()
            os.fsync(stream.fileno())
        current = destination.read_bytes() if destination.exists() else None
        if current != before:
            raise ConfigurationError("Configuration changed during preparation; retry after review.")
        os.replace(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return destination, True


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--adapter", choices=ADAPTERS, required=True)
    p.add_argument("--client", choices=CLIENTS, required=True)
    p.add_argument("--url", required=True, help="Verified HTTPS MCP endpoint; no credentials")
    p.add_argument("--server-name", help="Reuse one agreed server profile; Atlassian adapters share a default")
    p.add_argument("--discovery-only", action="store_true", help="Codex: expose no agent tools while bootstrapping authentication/catalog diagnostics")
    p.add_argument("--tool", action="append", help="Exact discovered Codex tool name; repeat as needed")
    p.add_argument("--bearer-token-env-var", help="Environment variable NAME; never a token value")
    p.add_argument("--project-root", type=Path, default=Path.cwd())
    p.add_argument("--apply", action="store_true", help="Merge project config; default only previews the new profile")
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        name, config = profile(args)
        if args.apply:
            path, changed = apply(args.project_root, args.client, name, config)
            print(f"{'Configured' if changed else 'Already configured'}: {path} (profile {name}).")
            print("Connection NOT verified. Authenticate, reload, inspect tools and test target access separately.")
        else:
            print(toml_block(name, config) if args.client == "codex" else json.dumps({CLIENTS[args.client][1]: {name: config}}, indent=2))
            print("Preview only; no files, login, connection, package install, or remote changes.", file=sys.stderr)
        return 0
    except ConfigurationError as exc:
        print(f"Refused: {exc}", file=sys.stderr)
    except OSError:
        print("Refused: cannot read or write the selected project path; no configuration details printed.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
