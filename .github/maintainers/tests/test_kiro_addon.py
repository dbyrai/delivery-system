from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]


class KiroAddonTests(unittest.TestCase):
    def test_kiro_is_not_active_in_template_root(self):
        self.assertFalse((ROOT / ".kiro").exists())

    def test_package_is_complete_and_self_contained(self):
        addon = ROOT / "addons/kiro"
        required = [
            "README.md",
            "integration-prompt.md",
            "deactivation-prompt.md",
            "record.md",
            "templates/delivery-system.md",
        ]
        for relative in required:
            with self.subTest(path=relative):
                self.assertTrue((addon / relative).is_file())

        steering = (addon / "templates/delivery-system.md").read_text(encoding="utf-8")
        self.assertTrue(steering.startswith("---\ninclusion: always\n---\n"))
        self.assertIn(".github/copilot-instructions.md", steering)
        self.assertNotIn("addons/", steering)

    def test_activation_is_explicit_and_removable(self):
        readme = (ROOT / "addons/kiro/README.md").read_text(encoding="utf-8")
        self.assertIn("explicit activation", readme)
        self.assertIn("contains no root `.kiro/` directory", readme)
        self.assertIn("after `addons/kiro/` is removed", readme)


if __name__ == "__main__":
    unittest.main()
