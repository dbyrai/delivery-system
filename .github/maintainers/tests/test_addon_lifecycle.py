from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]


class AddonLifecycleTests(unittest.TestCase):
    def test_core_declares_generic_opt_in_contract(self):
        instructions = (ROOT / ".github/copilot-instructions.md").read_text(encoding="utf-8")
        section = instructions.split("## Optional Add-ons", 1)[1].split("\n## ", 1)[0]
        self.assertIn("inactive by default", section)
        self.assertIn("durable project record", section)
        self.assertIn("must not import instructions from `addons/`", section)
        self.assertNotIn("SCRUM", section)
        self.assertNotIn("Kiro", section)

    def test_addon_guide_defines_complete_lifecycle(self):
        guide = (ROOT / "addons/README.md").read_text(encoding="utf-8")
        for state in ("Distributed", "Prepared", "Active", "Verified", "Inactive"):
            with self.subTest(state=state):
                self.assertIn(f"**{state}**", guide)
        self.assertIn("explicit opt-in", guide)
        self.assertIn("must not import instructions from `addons/`", guide)


if __name__ == "__main__":
    unittest.main()
