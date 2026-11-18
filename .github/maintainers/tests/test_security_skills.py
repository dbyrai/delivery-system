import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ADDON = Path(__file__).resolve().parents[3] / "addons/security"
SOFTWARE = "security-review"
INFRASTRUCTURE = "infra-security"
CATALOG_ONLY = "codeql"
RECORD = Path("project/integrations/security-skills.md")


class SecuritySkillsTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.scratch = Path(scratch.name).resolve()
        self.project = self.scratch / "test-delivery-system"
        self.docs = self.project / "docs"
        self.docs.mkdir(parents=True)
        self.target = self.docs / RECORD
        self.rules = self.project / ".github/copilot-instructions.md"
        self.rules.parent.mkdir()
        self.rules.write_text("# Delivery rules\n\n## Optional Security Methods\n", encoding="utf-8")
        self.addon = self.project / "addons/security"
        shutil.copytree(ADDON, self.addon)
        self.sources = self.scratch / "sources"
        catalog_path = self.addon / "catalog.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        self.source_files = {}
        for name in (SOFTWARE, INFRASTRUCTURE):
            source = catalog["skills"][name]["source"]
            filename = self.sources / source["repository"] / source["revision"] / source["path"]
            filename.parent.mkdir(parents=True, exist_ok=True)
            content = f"# Synthetic {name} reference\n\nThis text must stay outside the project record.\n".encode()
            filename.write_bytes(content)
            source["sha256"] = hashlib.sha256(content).hexdigest()
            self.source_files[name] = filename
        catalog_path.write_text(json.dumps(catalog), encoding="utf-8")

    def run_cli(self, *arguments):
        return subprocess.run(
            [sys.executable, "-B", str(self.addon / "manage.py"), *arguments],
            cwd=self.project,
            capture_output=True,
            text=True,
            timeout=10,
        )

    def activate(self, *arguments):
        return self.run_cli("activate", *arguments, "--source-dir", str(self.sources))

    def project_files(self):
        return {path: path.read_bytes() for path in self.project.rglob("*") if path.is_file()}

    def test_list_lists_methods_without_changing_project(self):
        before = self.project_files()
        result = self.run_cli("list")
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in (SOFTWARE, INFRASTRUCTURE, CATALOG_ONLY):
            self.assertIn(name, result.stdout)
        self.assertEqual(self.project_files(), before)

    def test_activation_is_idempotent_and_scoped(self):
        before = self.project_files()
        result = self.activate(SOFTWARE, INFRASTRUCTURE, SOFTWARE)
        self.assertEqual(result.returncode, 0, result.stderr)
        content = self.target.read_bytes()
        record = content.decode("utf-8")
        self.assertIn("## Geltung", record)
        for name in (SOFTWARE, INFRASTRUCTURE):
            heading = f"## `{name}`"
            self.assertEqual(record.count(heading), 1)
        self.assertNotIn(f"## `{CATALOG_ONLY}`", record)
        self.assertNotIn("This text must stay outside", record)

        result = self.activate(INFRASTRUCTURE, SOFTWARE)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.project_files(), {**before, self.target: content})

    def test_invalid_or_catalog_only_selection_leaves_no_record(self):
        for name in ("missing-security-method", CATALOG_ONLY):
            with self.subTest(name=name):
                result = self.activate(SOFTWARE, name)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertFalse(self.target.parent.exists())

    def test_source_mismatch_leaves_no_partial_activation(self):
        self.source_files[INFRASTRUCTURE].write_bytes(b"unexpected source bytes")
        before = self.project_files()
        result = self.activate(SOFTWARE, INFRASTRUCTURE)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertFalse(self.target.parent.exists())
        self.assertEqual(self.project_files(), before)

    def test_existing_record_is_preserved(self):
        self.target.parent.mkdir(parents=True)
        self.target.write_bytes(b"Existing project customization\n")
        before = self.project_files()
        result = self.activate(SOFTWARE)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertEqual(self.project_files(), before)

    def test_custom_docs_root_writes_only_selected_method(self):
        custom_docs = self.project / "knowledge"
        custom_docs.mkdir()
        result = self.activate(INFRASTRUCTURE, "--docs-root", "knowledge")
        self.assertEqual(result.returncode, 0, result.stderr)
        record = (custom_docs / RECORD).read_text(encoding="utf-8")
        self.assertIn(f"## `{INFRASTRUCTURE}`", record)
        self.assertNotIn(f"## `{SOFTWARE}`", record)
        self.assertFalse(self.target.parent.exists())

    def test_activation_requires_exact_routing_heading(self):
        self.rules.write_text("# Delivery rules\n\n### Optional Security Methods\n", encoding="utf-8")
        result = self.activate(SOFTWARE)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertFalse(self.target.parent.exists())

    def test_destination_rejects_outside_paths_and_symlinks(self):
        external_dir = self.scratch / "external"
        external_dir.mkdir()
        (self.project / "alias").symlink_to(external_dir, target_is_directory=True)
        for docs_root in ("alias", "../external", str(external_dir)):
            with self.subTest(docs_root=docs_root):
                result = self.activate(SOFTWARE, "--docs-root", docs_root)
                self.assertNotEqual(result.returncode, 0, result.stdout)

        self.target.parent.parent.mkdir()
        self.target.parent.symlink_to(external_dir, target_is_directory=True)
        result = self.activate(SOFTWARE)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertEqual(list(external_dir.iterdir()), [])

    def test_existing_record_symlink_is_preserved(self):
        external_file = self.scratch / "external-record.md"
        external_file.write_bytes(b"Unrelated project record\n")
        self.target.parent.mkdir(parents=True)
        self.target.symlink_to(external_file)
        result = self.activate(SOFTWARE)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertTrue(self.target.is_symlink())
        self.assertEqual(external_file.read_bytes(), b"Unrelated project record\n")


if __name__ == "__main__":
    unittest.main()
