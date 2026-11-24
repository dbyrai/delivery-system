from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[3]
ADDON = ROOT / "addons/scrum"


class ScrumAddonTests(unittest.TestCase):
    def test_package_has_expected_skills(self):
        expected = {
            "dod-readiness-check",
            "dor-readiness-check",
            "sprint-close",
            "sprint-planning",
        }
        actual = {path.parent.name for path in (ADDON / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, expected)
        for name in expected:
            text = (ADDON / f"skills/{name}/SKILL.md").read_text(encoding="utf-8")
            match = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
            self.assertIsNotNone(match, name)
            self.assertEqual(match.group(1).strip(), name)

    def test_package_is_independent_of_kiro(self):
        for path in ADDON.rglob("*"):
            if path.is_file():
                text = path.read_text(encoding="utf-8")
                with self.subTest(path=path.relative_to(ROOT)):
                    self.assertNotIn("Kiro", text)
                    self.assertNotIn(".kiro/", text)

    def test_activated_sources_do_not_import_addon_files(self):
        for folder in (ADDON / "record.md", ADDON / "skills", ADDON / "templates"):
            paths = [folder] if folder.is_file() else list(folder.rglob("*"))
            for path in paths:
                if path.is_file():
                    with self.subTest(path=path.relative_to(ROOT)):
                        self.assertNotIn("addons/", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
