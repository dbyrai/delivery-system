import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ADDON = Path(__file__).resolve().parents[3] / "addons/mattpocock-skills"
SPEC = importlib.util.spec_from_file_location("mattpocock_skills", ADDON / "manage.py")
MANAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MANAGE)
CATALOG = json.loads((ADDON / "catalog.json").read_text(encoding="utf-8"))


class ActivationTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name).resolve()
        self.docs = self.root / "docs"
        self.docs.mkdir()
        self.rules = self.root / ".github/copilot-instructions.md"
        self.rules.parent.mkdir()
        self.rules.write_text("Project rules", encoding="utf-8")
        self.revision = CATALOG["revision"]
        self.skills = CATALOG["skills"]

    def test_activation_is_scoped_and_repeatable(self):
        names = ["grill-me", "tdd", "grill-me"]
        selected = MANAGE.resolve_selection(self.skills, names)
        self.assertEqual(list(selected), ["codebase-design", "grill-me", "grilling", "tdd"])
        target = MANAGE.destination(self.root, Path("docs"))
        before = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        with patch.object(MANAGE, "verify_sources") as verify:
            MANAGE.activate(target, self.revision, selected)
            MANAGE.activate(target, self.revision, selected)
        verify.assert_called_once_with(self.revision, selected, None)
        self.assertEqual({path for path in self.root.rglob("*") if path.is_file()}, {*before, target})
        for path, content in before.items():
            self.assertEqual(path.read_bytes(), content)
        record = target.read_text(encoding="utf-8")
        for name in selected:
            self.assertIn(f"## `{name}`", record)
        self.assertNotIn("## `implement`", record)

    def test_unreviewed_skill_cannot_be_activated(self):
        with self.assertRaises(ValueError):
            MANAGE.resolve_selection(self.skills, ["tdd", "implement-spec"])
        self.assertEqual(list(self.docs.iterdir()), [])

    def test_source_mismatch_leaves_no_files(self):
        target = self.docs / MANAGE.RECORD
        selected = MANAGE.resolve_selection(self.skills, ["tdd"])
        with patch.object(MANAGE, "urlopen", return_value=io.BytesIO(b"unexpected content")):
            with self.assertRaises(ValueError):
                MANAGE.activate(target, self.revision, selected)
        self.assertEqual(list(self.docs.iterdir()), [])

    def test_existing_file_is_preserved(self):
        target = self.docs / MANAGE.RECORD
        target.write_text("Existing project content", encoding="utf-8")
        selected = MANAGE.resolve_selection(self.skills, ["tdd"])
        with patch.object(MANAGE, "verify_sources") as verify:
            with self.assertRaises(ValueError):
                MANAGE.activate(target, self.revision, selected)
        verify.assert_not_called()
        self.assertEqual(target.read_text(encoding="utf-8"), "Existing project content")

    def test_concurrent_creation_is_preserved(self):
        target = self.docs / MANAGE.RECORD
        selected = MANAGE.resolve_selection(self.skills, ["tdd"])

        def create_during_verification(*args):
            target.write_text("Concurrent change", encoding="utf-8")

        with patch.object(MANAGE, "verify_sources", side_effect=create_during_verification):
            with self.assertRaises(FileExistsError):
                MANAGE.activate(target, self.revision, selected)
        self.assertEqual(target.read_text(encoding="utf-8"), "Concurrent change")
        self.assertEqual(list(self.docs.iterdir()), [target])

    def test_paths_cannot_escape_project_or_follow_links(self):
        alias = self.root / "alias"
        alias.symlink_to(self.docs, target_is_directory=True)
        for path in (self.docs, Path("alias"), Path("../docs"), Path(".github")):
            with self.subTest(path=path), self.assertRaises(ValueError):
                MANAGE.destination(self.root, path)

        target = self.docs / MANAGE.RECORD
        target.symlink_to(self.rules)
        selected = MANAGE.resolve_selection(self.skills, ["tdd"])
        with self.assertRaises(ValueError):
            MANAGE.activate(target, self.revision, selected)
        self.assertEqual(self.rules.read_text(encoding="utf-8"), "Project rules")


if __name__ == "__main__":
    unittest.main()
