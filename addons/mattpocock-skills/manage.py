#!/usr/bin/env python3
"""List the pinned catalog or activate reviewed methods in one project document."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
from urllib.request import urlopen


ADDON = Path(__file__).resolve().parent
REPOSITORY = "https://github.com/mattpocock/skills"
RAW = "https://raw.githubusercontent.com/mattpocock/skills"
RECORD = "mattpocock-skills.md"
ROUTING_SECTION = "## Optional Matt Pocock Methods"
STATUSES = {
    "ready": "empfohlen und aktivierbar",
    "dependency": "adaptierte Referenz",
    "catalog": "nur im Katalog",
    "adapt": "Anpassung erforderlich",
    "omit": "mit diesem Add-on nicht aktivierbar",
}


def resolve_selection(skills, names):
    selected = {}
    pending = list(dict.fromkeys(names))
    while pending:
        name = pending.pop(0)
        if name in selected:
            continue
        skill = skills.get(name)
        if skill is None:
            raise ValueError(f"Unbekannter Skill: {name}")
        if skill["status"] not in {"ready", "dependency"}:
            raise ValueError(f"{name}: {STATUSES[skill['status']]}")
        selected[name] = skill
        pending.extend(skill["dependencies"])
    return dict(sorted(selected.items()))


def destination(root, docs_root):
    rules = root / ".github/copilot-instructions.md"
    if not rules.is_file():
        raise ValueError("Starte den Befehl im Wurzelverzeichnis des Delivery-System-Projekts.")
    if ROUTING_SECTION not in rules.read_text(encoding="utf-8").splitlines():
        raise ValueError("Die gemeinsamen Delivery-Regeln enthalten die Anbindung für Matt Pocock noch nicht.")
    if docs_root.is_absolute() or not docs_root.parts or any(part.startswith(".") for part in docs_root.parts):
        raise ValueError("Gib ein vorhandenes Dokumentationsverzeichnis im Projekt an.")
    directory = root / docs_root
    if not directory.is_dir() or directory.resolve() != directory or root not in directory.parents:
        raise ValueError("Das Dokumentationsverzeichnis muss im Projekt liegen und darf keine Links enthalten.")
    target = directory / "project" / "integrations" / RECORD
    check_integration_path(target)
    return target


def check_integration_path(target):
    if target.parent.resolve() != target.parent:
        raise ValueError("Der Integrationspfad darf keine symbolischen Links enthalten.")


def verify_sources(revision, selected, source_dir):
    sources = {path: digest for skill in selected.values() for path, digest in skill["sources"].items()}
    for path, expected in sources.items():
        source = (
            urlopen(f"{RAW}/{revision}/{path}", timeout=15)
            if source_dir is None
            else (source_dir / path).open("rb")
        )
        with source as response:
            content = response.read(256 * 1024 + 1)
        if len(content) > 256 * 1024:
            raise ValueError(f"Upstream-Datei ist zu groß: {path}")
        header = f"blob {len(content)}\0".encode("ascii")
        actual = hashlib.sha1(header + content, usedforsecurity=False).hexdigest()
        if actual != expected:
            raise ValueError(f"Upstream-Datei stimmt nicht mit der geprüften Quelle überein: {path}")


def render_record(revision, selected):
    sections = [
        "# Matt-Pocock-Methoden für das Delivery-System",
        f"Quelle ist das [Repository von Matt Pocock]({REPOSITORY}/tree/{revision}) in Revision `{revision}`. "
        "Dieser Eintrag enthält für das Delivery-System angepasste Methoden.",
        "## Geltung\n\n"
        "Lies die geltenden Projektanweisungen und die kanonischen Delivery-Regeln vor der Verwendung. "
        "Die gemeinsamen Delivery-Regeln bestimmen, wann dieser Eintrag geladen wird. Verwende die gewählte Methode "
        "samt ihren hier genannten Referenzen. Die zugehörige Aufgabe, Projektquellen, Rollen und Freigaben "
        "bestimmen den Umfang. Offene Blocker, Bootstrap, Akzeptanz und Verifikation richten sich nach dem Projekt. "
        "Dieser Eintrag erteilt keine Berechtigung für externe Schreibvorgänge, Delegation oder Git- und Release-Aktionen. "
        "Bei einem Konflikt gilt die Projektregel. Melde den Konflikt und überspringe den betroffenen Methodenschritt. "
        "Die verlinkten Upstream-Dateien dienen der Herkunftsdokumentation.",
    ]
    for name, skill in selected.items():
        source_links = ", ".join(
            f"[{Path(path).name}]({REPOSITORY}/blob/{revision}/{path})" for path in skill["sources"]
        )
        steps = "\n".join(f"{index}. {step}" for index, step in enumerate(skill["method"], start=1))
        sections.append(f"## `{name}`\n\n{skill['description']}\n\n{steps}\n\nQuellen · {source_links}")
    license_text = (ADDON / "LICENSE.upstream").read_text(encoding="utf-8").rstrip()
    sections.append(f"## Upstream-Lizenz\n\n```text\n{license_text}\n```")
    return "\n\n".join(sections) + "\n"


def activate(target, revision, selected, source_dir=None):
    check_integration_path(target)
    record = render_record(revision, selected).encode("utf-8")
    if target.is_symlink() or target.exists():
        if not target.is_symlink() and target.is_file() and target.read_bytes() == record:
            return "Auswahl bereits aktiv"
        raise ValueError(f"Vorhandener Eintrag bleibt erhalten: {target}")

    verify_sources(revision, selected, source_dir)
    check_integration_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".mattpocock-", dir=target.parent) as staging:
        draft = Path(staging) / RECORD
        draft.write_bytes(record)
        os.link(draft, target)
    return "Auswahl aktiviert"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="Katalog der festgelegten Revision zeilenweise anzeigen")
    setup = commands.add_parser("activate", help="Ausgewählte Methoden projektlokal aktivieren")
    setup.add_argument("skills", nargs="+", help="Namen aus dem Katalog")
    setup.add_argument("--docs-root", type=Path, default=Path("docs"))
    setup.add_argument("--source-dir", type=Path, help="Temporäres Verzeichnis mit den exakten Upstream-Dateien")
    args = parser.parse_args()

    try:
        catalog = json.loads((ADDON / "catalog.json").read_text(encoding="utf-8"))
        revision, skills = catalog["revision"], catalog["skills"]
        if args.command == "list":
            print(f"Upstream-Revision {revision}")
            for group in ("engineering", "productivity"):
                print(f"\n{group.capitalize()}")
                for name, skill in skills.items():
                    if skill["group"] != group:
                        continue
                    dependencies = ", ".join(skill.get("dependencies", []))
                    detail = f" · Referenz: {dependencies}" if dependencies else ""
                    print(f"- {name} [{STATUSES[skill['status']]}{detail}] — {skill['description']}")
            return 0

        selected = resolve_selection(skills, args.skills)
        target = destination(Path.cwd(), args.docs_root)
        state = activate(target, revision, selected, args.source_dir)
        print(f"{state}: {target}\nMethoden und Referenzen: {', '.join(selected)}")
        return 0
    except (OSError, ValueError) as error:
        print(f"{error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
