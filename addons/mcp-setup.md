# Shared MCP Adapter Setup

Each optional package under `addons/` is an adapter: its instructions, configuration
helper, identity/hierarchy contract, verification, and deactivation process connect
the Delivery System to the selected external system. An adapter is operational
only after its MCP connection and required operations have been verified. Copying
files or writing a mapping document is preparation, not activation.

## Configure the Actual Client

1. Identify the active client and version, project, confirmed service endpoint,
   authentication method, and existing MCP profile. Inspect configuration metadata
   without printing credentials. Reuse a matching existing connection, including
   a validated stdio proxy; do not shadow it with a second project/global profile.
2. Follow the selected adapter's `mcp-setup.md`. Its server endpoint, edition,
   prerequisites, and capability checks apply. Selection authorizes preparing and
   applying the necessary scoped MCP configuration; reuse established connection
   approval. Resolve any new trust, install, access, or sharing decision before it
   is needed. External ticket/page writes still require their actual action scope.
3. Preview the actual configuration change. Use the helper below for supported
   project-local HTTP profiles, or adapt the documented official client format
   for a reviewed existing/global/stdio profile. Preserve unrelated servers and
   settings. Store credentials through the client's approved OAuth or environment
   mechanism, never in a committed project file, chat, command argument, or log.
4. Apply the reviewed profile, authenticate in the selected client, and handle any
   browser consent with the user. Reload/reconnect that client when needed.
   Inspect `initialize` and `tools/list` results through the client's MCP diagnostics;
   then confirm the tools are exposed to the actual agent session. A successful
   separate diagnostic process does not prove the current session loaded them.
5. Read the exact target identity and one representative resource. Record the
   server/client versions, exposed names and schemas, permissions, operation
   matrix, and errors without tokens. Do not classify a 401/404, a config listing,
   Git SSH access, or a catalog alone as a successful project connection.
6. Before creating tickets, prove a supported route for all required operations:
   parent/child creation or attachment, updates, stable-ID title/marker preservation,
   and reciprocal hierarchy read-back. Distinguish schema support, resource
   permission, client tool filter, and action authorization. Use narrowly scoped
   authorized tests when necessary; never probe writes without authorization.

## Executable Configuration Helper

Requires Python 3.11 or later. From the target project root, preview one profile:

```sh
python3 addons/configure_mcp.py --adapter gitlab --client codex \
  --url https://gitlab.example.com/api/v4/mcp --tool get_issue
```

`get_issue` is an example name to verify against the actual server catalog, not
a promise of full adapter capability. If no authenticated catalog exists yet,
use `--discovery-only` instead of `--tool` for an initial Codex profile. It emits
`enabled_tools = []`: the client may authenticate and perform MCP initialization/
catalog diagnostics, but exposes no tools to the agent. After discovery, review
and manually merge the exact allowlist into that profile; the helper deliberately
refuses to overwrite a different existing entry. Do not call an undocumented tool
or treat discovery mode as an operational adapter.

Add `--apply` after reviewing the preview:

```sh
python3 addons/configure_mcp.py --adapter gitlab --client codex \
  --url https://gitlab.example.com/api/v4/mcp --tool get_issue --apply
```

The helper supports `--adapter jira|confluence|github-projects|gitlab`,
`--client codex|claude-code|vscode`, `--server-name NAME`, and
`--project-root PATH`. `--bearer-token-env-var ENV_NAME` records only an environment
variable reference, never its value. Do not pass a token as that argument. The
helper does not read environment secrets, run packages, log in, call the endpoint,
or claim a live connection. It uses project-local paths only:

| Client | File | Server map | Tool controls |
| --- | --- | --- | --- |
| Codex | `.codex/config.toml` | `mcp_servers` | Exact `--tool` names, or initial `--discovery-only` with no agent tools |
| Claude Code | `.mcp.json` | `mcpServers` | Set client permissions/consent separately; helper rejects `--tool` |
| VS Code / Copilot | `.vscode/mcp.json` | `servers` | Select tools and approvals in the client; helper rejects `--tool` |

Codex profiles use `bearer_token_env_var`; Claude Code uses `${ENV_NAME}` header
references; VS Code uses `${env:ENV_NAME}`. Ensure the running client actually
receives the variable. Do not print it to verify availability. OAuth profiles
omit that option. Jira and Confluence share default name `delivery_atlassian`;
GitHub uses `delivery_github`, GitLab `delivery_gitlab`. Use a distinct agreed
name for a different host, account, or access policy. Sharing an endpoint does
not automatically grant permission to use every product it exposes.

Apply is additive and idempotent: identical entries are retained, different
same-name entries are refused for manual review, and unrelated configuration is
preserved. The helper does not replace existing profiles to widen an allowlist.
Codex TOML comments are retained; JSON objects are preserved semantically but
formatting is normalized. JSONC/commented JSON is refused for manual merge.
Symlinked/escaping config destinations and credentials in endpoint URLs are
refused. Only the non-secret `?tools=all` query is supported for the Atlassian
flat catalog. No home/global configuration is modified by this helper.

For Codex OAuth, use the actual selected profile and supported local CLI:

```sh
codex mcp login delivery_gitlab
```

Run it from the target project and first verify that the installed client resolves
that project's profile; trusted-project configuration and managed policy affect
loading. If it cannot, adapt the supported configuration scope explicitly rather
than duplicating or overwriting global settings. For Claude Code use `/mcp` and
its Authenticate action; in VS Code use MCP server management and authentication.
Consult the current client documentation and record actual results.

## First-Connection Prompt Testing

Test a new project's integration prompt in an isolated copy with no integration
record, remote mapping, or project MCP profile. Keep the real project, global
profiles, and OAuth stores intact. Record the exact prompt and supplied setup
answers, and distinguish real model execution from deterministic helper tests.

When using Codex CLI, `codex exec --ignore-user-config` prevents loading the user
config for that execution; it is not an option for every `codex mcp` subcommand
and does not itself clear authentication. For isolated MCP-only login diagnostics,
use a separate empty `CODEX_HOME` and only the newly generated non-secret profile
if that installed CLI needs a user-scope config. Do not copy real user config,
credentials, or OAuth caches into the test. Let the model runner use its ordinary
account login internally; never inspect or duplicate that authentication.

Protected project configuration paths and network access may require the
client's normal command approval. Prepare the exact configuration/endpoint change
and request scoped escalation when necessary; preserve authorization already
given. Do not bypass the sandbox or report a denied write as applied. A browser
consent step is a real user handoff, not a completed connection. Keep the client's
OAuth callback listener alive for a bounded, reported waiting period while the
user completes consent. Do not terminate the proxy as soon as it emits an
authorization URL; that can prevent the callback from ever completing. Do not
claim the browser opened without evidence. After user confirmation, resume and
verify initialization/catalog/target reads; on decline or expiry, stop cleanly
and report the actual incomplete state. If a reviewed
proxy is needed after a native OAuth failure, obtain only the missing dependency/
connection decision, use an isolated auth store, and retest the actual MCP flow.
Keep the stored working connection available while a fresh test is incomplete. In the
isolated Codex CLI 0.164.0 test, the project file did not automatically expose MCP
tools when user configuration was ignored, even with a trust override. Explicitly
loading only the reviewed, non-secret generated server profile as a supported
startup configuration made the tools available in a new model session. Record
that distinction; successful direct protocol probes do not prove automatic
project-file loading. Never pass literal credentials in startup arguments.

## Required Ticket Identity and Hierarchy

Use the existing Delivery IDs. For a numbered spec such as `001`, a new parent
may use `SPEC-001: <title>` and its children `TASK-001-001: <title>`,
`TASK-001-002: <title>`, and so on. Preserve any already assigned alternative
stable IDs; do not silently renumber them. Record both the Delivery identifier
and the external ID/key/URL. Titles and managed identity markers must carry the
same ID. Role names are not account identifiers.

Ticket adapters must put each task under its correct parent using the service's
native hierarchy. Description links, checklists, board membership, and related-item
links do not meet this requirement. Resolve the actual parent type/level, child
type, target project, and supported operation before creating either. Verify the
child's parent reference and the parent's child list. If only flat issue creation
is supported, mark hierarchy setup blocked and do not create misleading substitutes.
Confluence publishes the corresponding page tree and links to the native tickets;
a page tree alone does not implement the ticket/task hierarchy.

For existing incorrectly structured objects, prepare an in-place repair plan
using their mapped IDs. Read their content and relationships first, then change
only the approved title/type/parent fields. Preserve other content and current
parents; conflicting relationships require a decision. Never create replacements
or delete remote work to hide a failed update or unsupported hierarchy operation.
A server rejecting Quick Actions, commands in comments, or another operation is
a capability boundary; do not encode commands to evade validation.

## Adapter State and Durable Evidence

Record each state separately in the project's integration record:

| State | Evidence required |
| --- | --- |
| Prepared | Targets, scope, authority, and concrete config preview; no live success implied |
| MCP connected | Authentication, current session catalog, and target read verified |
| Operational for selected workflow | Required create/update/hierarchy/read-back paths and scoped tests verified |
| Partial / blocked | Exact missing operation, dependency, or permission; completed objects and next owner |
| Inactive | Migration/disposition completed as agreed; owned mechanisms stopped and shutdown verified |

A read-only connection can be MCP connected while the full workflow is blocked.
Do not reset a user's explicit external source-of-truth decision to local docs
because a tool cannot update it. Preserve cached local copies and stop dependent
operations until a supported, authorized route is selected. A manually completed
UI repair is evidence of that repair, not proof of an MCP update capability.

Transfer the endpoint/profile ownership, client location, auth-store reference,
operation matrix, hierarchy rules, mappings, conflicts, and teardown into the
project's durable record. Keep that record and active configuration independent
of `addons/`. If a proxy/launcher would execute a file under `addons/`, move that
runtime file into a durable project-owned location before allowing instruction
removal. The shipped helper runs during setup only and is not a runtime dependency.

## Troubleshooting and Deactivation

Separate DNS/reachability, CA trust, transport, OAuth issuer/resource/consent,
client loading/filtering, server catalog, target permissions, and unsupported
operations. Keep certificate validation enabled. Repair trust with the selected
client's CA mechanism. Use only reviewed, pinned proxies when the native path
fails; do not silently swap servers, broaden tokens, or claim feature parity.
The GitLab guide includes a specific observed proxy case, not a universal fix.

After the deactivation prompt's knowledge migration and retention decisions,
remove/disable only the owned MCP profile or its scoped tools. Retain a shared
Atlassian or multi-project profile while another integration uses it. Track local
profile cleanup, provider grants, proxy cache, external automation, and pending
work separately. Removing configuration does not revoke provider access; deleting
OAuth caches must be scoped and authorized. Preserve remote hierarchy and IDs.

## Client References

- [Codex MCP configuration](https://developers.openai.com/codex/mcp/)
- [Codex configuration reference](https://developers.openai.com/codex/config-reference/)
- [Claude Code MCP setup and project environment expansion](https://code.claude.com/docs/en/mcp)
- [VS Code MCP setup](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)

Client formats were checked against official documentation. File generation tests
do not establish authenticated client behavior or product capability.
