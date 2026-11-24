from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]


class WorkspaceLayoutAddonTests(unittest.TestCase):
    def test_layout_is_inactive_by_default(self):
        self.assertFalse((ROOT / ".github/workspace-layout.md").exists())

    def test_package_is_complete(self):
        addon = ROOT / "addons/workspace-layout"
        for relative in (
            "README.md",
            "integration-prompt.md",
            "deactivation-prompt.md",
            "record.md",
            "templates/workspace-layout.md",
            "templates/gitignore.snippet",
        ):
            with self.subTest(path=relative):
                self.assertTrue((addon / relative).is_file())

    def test_installed_template_is_self_contained_and_configurable(self):
        template = (ROOT / "addons/workspace-layout/templates/workspace-layout.md").read_text(encoding="utf-8")
        self.assertIn("{relative-application-directory}", template)
        self.assertIn("{private-docs-directory}", template)
        self.assertNotIn("addons/", template)
        self.assertNotIn(".kiro", template.lower())

    def test_prompt_protects_repository_and_privacy_boundaries(self):
        prompt = (ROOT / "addons/workspace-layout/integration-prompt.md").read_text(encoding="utf-8")
        self.assertIn("do not assume an app/ directory", prompt)
        self.assertIn("private root located inside a public application repository", prompt)
        self.assertIn("Do not", prompt)


if __name__ == "__main__":
    unittest.main()
