import re
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def front_matter(path):
    match = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        raise AssertionError(f"{path} has no front matter")
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"')
    return fields


def skills():
    return sorted(path.parent.name for path in (ROOT / ".github/skills").glob("*/SKILL.md"))


class SkillAdapterTests(unittest.TestCase):
    def test_every_skill_is_wrapped_for_core_tools(self):
        self.assertTrue(skills())
        for skill in skills():
            source = front_matter(ROOT / f".github/skills/{skill}/SKILL.md")
            with self.subTest(skill=skill):
                self.assertEqual(source["name"], skill)
                for folder in (".claude/skills", ".agents/skills"):
                    wrapper = ROOT / folder / skill / "SKILL.md"
                    self.assertEqual(
                        front_matter(wrapper),
                        {"name": skill, "description": source["description"]},
                    )
                    self.assertIn(
                        f"Read and follow `.github/skills/{skill}/SKILL.md`.",
                        wrapper.read_text(encoding="utf-8"),
                    )

    def test_no_orphan_core_skill_wrappers(self):
        known = set(skills())
        for folder in (".claude/skills", ".agents/skills"):
            for wrapper in (ROOT / folder).glob("*/SKILL.md"):
                self.assertIn(wrapper.parent.name, known, wrapper)

    def test_addon_skills_have_matching_front_matter(self):
        for path in (ROOT / "addons").glob("*/skills/*/SKILL.md"):
            with self.subTest(skill=path):
                fields = front_matter(path)
                self.assertEqual(fields["name"], path.parent.name)
                self.assertTrue(fields["description"])

if __name__ == "__main__":
    unittest.main()
