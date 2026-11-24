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
    return sorted(
        path.name[: -len(".agent.md")]
        for path in (ROOT / ".github/agents").glob("*.agent.md")
    )


class RoleAdapterTests(unittest.TestCase):
    def test_every_role_is_indexed_and_wrapped_for_core_tools(self):
        index = (ROOT / ".github/agents/README.md").read_text(encoding="utf-8")
        for role in roles():
            with self.subTest(role=role):
                self.assertIn(f"[{role}.agent.md]({role}.agent.md)", index)
                self.assertEqual(
                    front_matter(ROOT / f".github/agents/{role}.agent.md")["name"],
                    role,
                )
                pointer = f"Read and follow `.github/agents/{role}.agent.md`."
                claude = ROOT / f".claude/agents/{role}.md"
                codex = ROOT / f".codex/agents/{role}.toml"
                self.assertEqual(front_matter(claude)["name"], role)
                self.assertIn(pointer, claude.read_text(encoding="utf-8"))
                self.assertEqual(toml_fields(codex)["name"], role)
                self.assertIn(pointer, codex.read_text(encoding="utf-8"))

    def test_no_orphan_core_role_wrappers(self):
        known = set(roles())
        for folder, suffix in ((".claude/agents", ".md"), (".codex/agents", ".toml")):
            for wrapper in (ROOT / folder).glob(f"*{suffix}"):
                self.assertIn(wrapper.name[: -len(suffix)], known, wrapper)

if __name__ == "__main__":
    unittest.main()
