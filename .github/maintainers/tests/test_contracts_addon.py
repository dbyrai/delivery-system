from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]
ADDON = ROOT / "addons/contracts"


class ContractsAddonTests(unittest.TestCase):
    def test_package_has_activation_and_removal_material(self):
        expected = (
            "README.md",
            "integration-prompt.md",
            "deactivation-prompt.md",
            "record.md",
            "templates/contracts-README.md",
            "templates/contract-template.md",
        )
        for relative in expected:
            with self.subTest(path=relative):
                self.assertTrue((ADDON / relative).is_file())

    def test_activated_files_are_durable_and_tool_neutral(self):
        for relative in (
            "record.md",
            "templates/contracts-README.md",
            "templates/contract-template.md",
        ):
            text = (ADDON / relative).read_text(encoding="utf-8")
            with self.subTest(path=relative):
                self.assertNotIn("addons/", text)
                self.assertNotIn("Kiro", text)
                self.assertNotIn(".kiro/", text)


if __name__ == "__main__":
    unittest.main()
