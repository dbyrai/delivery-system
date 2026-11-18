#!/usr/bin/env python3
"""List Security methods or activate reviewed adaptations in a project."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from urllib.request import urlopen


ADDON = Path(__file__).resolve().parent
ROUTING = "## Optional Security Methods"
RECORD = "security-skills.md"
MAX_SOURCE_BYTES = 256 * 1024


def source_path(source):
    return f"{source['repository']}/{source['revision']}/{source['path']}"


def source_link(source):
    if isinstance(source, str):
        return source
    return f"https://github.com/{source['repository']}/blob/{source['revision']}/{source['path']}"


def destination(root, docs_root):
    rules = root / ".github/copilot-instructions.md"
    if not rules.is_file() or ROUTING not in rules.read_text(encoding="utf-8").splitlines():
        raise ValueError("Die gemeinsamen Delivery-Regeln mit Security-Routing fehlen.")
    directory = root / docs_root
    if docs_root.is_absolute() or directory == root or root not in directory.parents:
        raise ValueError("Das Dokumentationsverzeichnis muss relativ im Projekt liegen.")
    if not directory.is_dir() or directory.resolve() != directory:
        raise ValueError("Das Dokumentationsverzeichnis muss existieren und darf keine Links enthalten.")
    return directory / "project" / "integrations" / RECORD


def verify_sources(selected, source_dir):
    for skill in selected.values():
        source = skill["source"]
        path = source_path(source)
        if source_dir is None:
            stream = urlopen(f"https://raw.githubusercontent.com/{path}", timeout=15)
        else:
            stream = (source_dir / path).open("rb")
        with stream:
            content = stream.read(MAX_SOURCE_BYTES + 1)
        if len(content) > MAX_SOURCE_BYTES or hashlib.sha256(content).hexdigest() != source["sha256"]:
            raise ValueError(f"Upstream-Quelle stimmt nicht mit der geprüften Version überein: {path}")


def render_record(selected):
    sections = [
        "# Security-Methoden für das Delivery-System",
        "## Geltung\n\n"
        "Verwende die ausgewählte Methode zusammen mit der Projekt-Sicherheitsrichtlinie und den geltenden Delivery-Regeln. "
        "Prüfe den vereinbarten Umfang anhand lokaler Dateien und vorhandener Prüfergebnisse. "
        "Ändere weder Projektdateien noch externe Systeme im Rahmen des Reviews. "
        "Gib keine Geheimnisse aus und dokumentiere Prüfgrenzen. "
        "Verwende die verlinkten Quellen zur Herkunftsdokumentation.",
    ]
    for name, skill in selected.items():
        steps = "\n".join(f"{number}. {step}" for number, step in enumerate(skill["steps"], 1))
        link = source_link(skill["source"])
        sections.append(f"## `{name}`\n\n{skill['description']}\n\n{steps}\n\n[Upstream-Quelle]({link})")
    return ("\n\n".join(sections) + "\n").encode("utf-8")


def check_destination(target):
    if target.parent.resolve() != target.parent or target.is_symlink():
        raise ValueError("Der Integrationspfad darf keine symbolischen Links enthalten.")


def activate(target, selected, source_dir):
    check_destination(target)
    record = render_record(selected)
    if target.exists():
        if target.is_file() and target.read_bytes() == record:
            return "Auswahl bereits aktiv"
        raise ValueError(f"Vorhandener Eintrag bleibt erhalten: {target}")
    verify_sources(selected, source_dir)
    check_destination(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix=".security-", dir=target.parent) as staging:
        draft = Path(staging) / RECORD
        draft.write_bytes(record)
        os.link(draft, target)
    return "Auswahl aktiviert"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="Skill-Katalog und Aktivierungsstatus anzeigen")
    setup = commands.add_parser("activate", help="Ausgewählte Methoden projektlokal aktivieren")
    setup.add_argument("skills", nargs="+")
    setup.add_argument("--docs-root", type=Path, default=Path("docs"))
    setup.add_argument("--source-dir", type=Path)
    args = parser.parse_args()

    try:
        skills = json.loads((ADDON / "catalog.json").read_text(encoding="utf-8"))["skills"]
        if args.command == "list":
            for name, skill in skills.items():
                status = "aktivierbar" if "steps" in skill else "nur im Katalog"
                print(f"- {name} [{status}] — {skill['description']} {source_link(skill['source'])}")
            return 0

        selected = {}
        for name in sorted(set(args.skills)):
            if name not in skills:
                raise ValueError(f"Unbekannter Skill: {name}")
            if "steps" not in skills[name]:
                raise ValueError(f"{name}: nur im Katalog")
            selected[name] = skills[name]
        target = destination(Path.cwd(), args.docs_root)
        print(f"{activate(target, selected, args.source_dir)}: {target}")
        print(f"Methoden: {', '.join(selected)}")
        return 0
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
