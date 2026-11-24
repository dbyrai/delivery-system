from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]
ADDON = ROOT / "addons/security-auditor"


class SecurityAuditorAddonTests(unittest.TestCase):
    def test_package_is_independent_of_kiro(self):
        for path in ADDON.rglob("*"):
            if path.is_file():
                text = path.read_text(encoding="utf-8")
                with self.subTest(path=path.relative_to(ROOT)):
                    self.assertNotIn("Kiro", text)
                    self.assertNotIn(".kiro/", text)

    def test_auditor_and_reviewer_are_distinct(self):
        readme = (ADDON / "README.md").read_text(encoding="utf-8")
        role = (ADDON / "security-auditor.agent.md").read_text(encoding="utf-8")
        self.assertIn("independent, read-only review", readme)
        self.assertIn("Edit only the findings log", role)
        self.assertIn("separate security-reviewer role", role)

    def test_automation_is_explicitly_optional(self):
        readme = (ADDON / "README.md").read_text(encoding="utf-8")
        prompt = (ADDON / "integration-prompt.md").read_text(encoding="utf-8")
        self.assertIn("activate them only on explicit decision", readme)
        self.assertIn("Only if I explicitly choose automation", prompt)

    def test_activated_sources_do_not_import_addon_files(self):
        active = [
            ADDON / "record.md",
            ADDON / "security-auditor.agent.md",
            ADDON / "templates/security-findings.md",
            ADDON / "adapters/claude-agent.md",
            ADDON / "adapters/claude-stop-hook.js",
            ADDON / "adapters/codex-agent.toml",
        ]
        for path in active:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertNotIn("addons/", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
