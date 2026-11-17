"""Local config integration checks. These never connect or authenticate an MCP server."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest

SCRIPT = Path(__file__).resolve().parents[3] / 'addons/configure_mcp.py'
spec = importlib.util.spec_from_file_location('configure_mcp', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ConfigureMCPTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def run_cli(self, client='codex', *extra, adapter='gitlab', url='https://gitlab.example.test/api/v4/mcp'):
        return subprocess.run([sys.executable, str(SCRIPT), '--adapter', adapter,
                               '--client', client, '--url', url,
                               '--project-root', str(self.root), *extra],
                              capture_output=True, text=True)

    def test_preview_does_not_write_or_connect(self):
        r = self.run_cli()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(list(self.root.iterdir()), [])
        self.assertIn('no files, login, connection', r.stderr)
        self.assertEqual(tomllib.loads(r.stdout)['mcp_servers']['delivery_gitlab']['url'], 'https://gitlab.example.test/api/v4/mcp')

    def test_discovery_bootstrap_exposes_no_agent_tools(self):
        r = self.run_cli('codex', '--discovery-only', '--apply')
        self.assertEqual(r.returncode, 0, r.stderr)
        p = self.root/'.codex/config.toml'
        self.assertEqual(tomllib.loads(p.read_text())['mcp_servers']['delivery_gitlab']['enabled_tools'], [])
        original = p.read_bytes()
        r = self.run_cli('codex', '--tool', 'get_issue', '--apply')
        self.assertEqual(r.returncode, 2)  # Reviewed manual allowlist merge, no silent widening.
        self.assertEqual(p.read_bytes(), original)
        self.assertEqual(self.run_cli('vscode', '--discovery-only', '--apply').returncode, 2)

    def test_codex_merge_preserves_unrelated_content_and_is_idempotent(self):
        p = self.root / '.codex/config.toml'
        p.parent.mkdir()
        original = '# Keep comment\nmodel = "project-model"\n[mcp_servers.existing]\nurl = "https://other.test/mcp"\n'
        p.write_text(original)
        r = self.run_cli('codex', '--tool', 'get_issue', '--apply')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(p.read_text().startswith(original))
        parsed = tomllib.loads(p.read_text())
        self.assertEqual(parsed['mcp_servers']['delivery_gitlab']['enabled_tools'], ['get_issue'])
        before = p.read_bytes()
        again = self.run_cli('codex', '--tool', 'get_issue', '--apply')
        self.assertEqual(again.returncode, 0, again.stderr)
        self.assertIn('Already configured', again.stdout)
        self.assertEqual(p.read_bytes(), before)
        conflict = self.run_cli('codex', '--tool', 'create_issue', '--apply')
        self.assertEqual(conflict.returncode, 2)
        self.assertEqual(p.read_bytes(), before)

    def test_apply_requires_exact_codex_tools(self):
        for extra in [[], ['--tool', '*'], ['--tool', 'get_*']]:
            with self.subTest(extra=extra):
                r = self.run_cli('codex', *extra, '--apply')
                self.assertEqual(r.returncode, 2)
                self.assertFalse((self.root/'.codex').exists())

    def test_json_clients_keep_other_configuration_and_use_env_reference(self):
        for client, rel, key, ref in [
            ('claude-code', '.mcp.json', 'mcpServers', '${GITHUB_PAT_TOKEN}'),
            ('vscode', '.vscode/mcp.json', 'servers', '${env:GITHUB_PAT_TOKEN}'),
        ]:
            with self.subTest(client=client):
                p = self.root / rel
                p.parent.mkdir(exist_ok=True)
                before = {'unrelated': {'setting': True}, key: {'existing': {'url': 'https://other.test'}}}
                p.write_text(json.dumps(before))
                r = self.run_cli(client, '--bearer-token-env-var', 'GITHUB_PAT_TOKEN', '--apply', adapter='github-projects')
                self.assertEqual(r.returncode, 0, r.stderr)
                data = json.loads(p.read_text())
                self.assertEqual(data['unrelated'], before['unrelated'])
                self.assertEqual(data[key]['existing'], before[key]['existing'])
                self.assertEqual(data[key]['delivery_github']['headers']['Authorization'], f'Bearer {ref}')
                self.assertEqual(self.run_cli(client, '--tool', 'read', '--apply').returncode, 2)

    def test_shared_atlassian_profile_reused(self):
        for adapter in ['jira', 'confluence']:
            r = self.run_cli('codex', '--tool', 'search', '--apply', adapter=adapter,
                             url='https://mcp.atlassian.com/v2/mcp?tools=all')
            self.assertEqual(r.returncode, 0, r.stderr)
        data = tomllib.loads((self.root/'.codex/config.toml').read_text())
        self.assertEqual(list(data['mcp_servers']), ['delivery_atlassian'])

    def test_refuses_secret_urls_without_echoing(self):
        for url in ['https://user:secret-DO-NOT-ECHO@service.test/mcp',
                    'https://service.test/mcp?token=secret-DO-NOT-ECHO',
                    'http://service.test/mcp', 'https://service.test/mcp#secret-DO-NOT-ECHO']:
            with self.subTest(url=url):
                r = self.run_cli(url=url)
                self.assertEqual(r.returncode, 2)
                self.assertNotIn('secret-DO-NOT-ECHO', r.stdout+r.stderr)
                self.assertEqual(list(self.root.iterdir()), [])

    def test_invalid_config_refused_and_not_printed(self):
        for client, rel, text in [
            ('codex', '.codex/config.toml', 'secret-DO-NOT-ECHO = ['),
            ('vscode', '.vscode/mcp.json', '{ // secret-DO-NOT-ECHO\n }'),
        ]:
            with self.subTest(client=client):
                p = self.root/rel
                p.parent.mkdir(exist_ok=True)
                p.write_text(text)
                extra = ['--tool', 'get_issue'] if client == 'codex' else []
                r = self.run_cli(client, *extra, '--apply')
                self.assertEqual(r.returncode, 2)
                self.assertEqual(p.read_text(), text)
                self.assertNotIn('secret-DO-NOT-ECHO', r.stdout+r.stderr)

    def test_symlinked_config_directory_refused(self):
        elsewhere = self.root/'unrelated'
        elsewhere.mkdir()
        (self.root/'.codex').symlink_to(elsewhere, target_is_directory=True)
        r = self.run_cli('codex', '--tool', 'get_issue', '--apply')
        self.assertEqual(r.returncode, 2)
        self.assertEqual(list(elsewhere.iterdir()), [])

    def test_inline_toml_layout_refused_without_rewriting(self):
        raw = 'mcp_servers = { existing = { url = "https://other.test" } }\n'
        with self.assertRaises(module.ConfigurationError):
            module.merge(raw, 'codex', 'delivery_gitlab', {'url': 'https://target.test'})


if __name__ == '__main__':
    unittest.main()
