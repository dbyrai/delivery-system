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


def toml_fields(path):
    return dict(re.findall(r'^(\w+) = "(.*)"$', path.read_text(encoding="utf-8"), re.M))


def roles():
    return sorted(p.name[: -len(".agent.md")] for p in (ROOT / ".github/agents").glob("*.agent.md"))


def skills():
    return sorted(p.parent.name for p in (ROOT / ".github/skills").glob("*/SKILL.md"))


class RoleAdapterTests(unittest.TestCase):
    def test_every_role_is_indexed_and_wrapped_for_each_tool(self):
        index = (ROOT / ".github/agents/README.md").read_text(encoding="utf-8")
        for role in roles():
            with self.subTest(role=role):
                self.assertIn(f"[{role}.agent.md]({role}.agent.md)", index)
                self.assertEqual(front_matter(ROOT / f".github/agents/{role}.agent.md")["name"], role)
                pointer = f"Read and follow `.github/agents/{role}.agent.md`."
                claude = ROOT / f".claude/agents/{role}.md"
                kiro = ROOT / f".kiro/agents/{role}.md"
                codex = ROOT / f".codex/agents/{role}.toml"
                for wrapper in (claude, kiro):
                    self.assertEqual(front_matter(wrapper)["name"], role)
                    self.assertIn(pointer, wrapper.read_text(encoding="utf-8"))
                self.assertEqual(toml_fields(codex)["name"], role)
                self.assertIn(pointer, codex.read_text(encoding="utf-8"))
                descriptions = {
                    front_matter(claude)["description"],
                    front_matter(kiro)["description"],
                    toml_fields(codex)["description"],
                }
                self.assertEqual(len(descriptions), 1, descriptions)

    def test_no_orphan_role_wrappers(self):
        known = set(roles())
        for folder, suffix in ((".claude/agents", ".md"), (".kiro/agents", ".md"), (".codex/agents", ".toml")):
            for wrapper in (ROOT / folder).glob(f"*{suffix}"):
                self.assertIn(wrapper.name[: -len(suffix)], known, wrapper)


class SkillAdapterTests(unittest.TestCase):
    def test_every_skill_is_wrapped_for_each_tool(self):
        self.assertTrue(skills())
        for skill in skills():
            source = front_matter(ROOT / f".github/skills/{skill}/SKILL.md")
            with self.subTest(skill=skill):
                self.assertEqual(source["name"], skill)
                for folder in (".claude/skills", ".agents/skills", ".kiro/skills"):
                    wrapper = ROOT / folder / skill / "SKILL.md"
                    self.assertEqual(front_matter(wrapper), {"name": skill, "description": source["description"]})
                    self.assertIn(f"Read and follow `.github/skills/{skill}/SKILL.md`.", wrapper.read_text(encoding="utf-8"))

    def test_no_orphan_skill_wrappers(self):
        known = set(skills())
        for folder in (".claude/skills", ".agents/skills", ".kiro/skills"):
            for wrapper in (ROOT / folder).glob("*/SKILL.md"):
                self.assertIn(wrapper.parent.name, known, wrapper)

    def test_addon_skills_have_matching_front_matter(self):
        for path in (ROOT / "addons").glob("*/skills/*/SKILL.md"):
            with self.subTest(skill=path):
                fields = front_matter(path)
                self.assertEqual(fields["name"], path.parent.name)
                self.assertTrue(fields["description"])


class KiroSteeringTests(unittest.TestCase):
    def test_steering_references_shared_instructions(self):
        text = (ROOT / ".kiro/steering/delivery-system.md").read_text(encoding="utf-8")
        self.assertEqual(front_matter(ROOT / ".kiro/steering/delivery-system.md")["inclusion"], "always")
        self.assertIn("#[[file:.github/copilot-instructions.md]]", text)


if __name__ == "__main__":
    unittest.main()
