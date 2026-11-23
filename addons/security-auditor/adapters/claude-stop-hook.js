#!/usr/bin/env node
// Optional Claude Code Stop hook from the Delivery System Security Auditor add-on.
// Once per distinct set of changed code files, asks Claude to run a security audit
// before finishing. Disable for a session with SECURITY_AUDIT=off.
// Adjust CODE to the code paths named in the project's Security Auditor record.

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { execSync } = require('child_process');

const CODE = /^(src|apps|modules|packages|lib)\/.+\.(php|ts|tsx|js|jsx|mjs|py|go|rb|java|cs|rs|sql)$/;
const root = process.env.CLAUDE_PROJECT_DIR || process.cwd();
const stateFile = path.join(root, '.claude', '.security-audit-state');

let input = '';
process.stdin.on('data', (c) => (input += c));
process.stdin.on('end', () => {
  try {
    if (process.env.SECURITY_AUDIT === 'off') return;
    if (JSON.parse(input || '{}').stop_hook_active) return;

    const git = (cmd) => execSync(cmd, { cwd: root, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
    const files = [
      ...git('git diff HEAD --name-only').split('\n'),
      ...git('git ls-files --others --exclude-standard').split('\n'),
    ].filter((f) => CODE.test(f));
    if (files.length === 0) return;

    const hash = crypto.createHash('sha1');
    for (const f of files.sort()) {
      hash.update(f);
      try { hash.update(fs.readFileSync(path.join(root, f))); } catch (e) {}
    }
    const digest = hash.digest('hex');
    let previous = '';
    try { previous = fs.readFileSync(stateFile, 'utf8').trim(); } catch (e) {}
    if (previous === digest) return;
    fs.writeFileSync(stateFile, digest);

    process.stdout.write(JSON.stringify({
      decision: 'block',
      reason:
        'Code changed. Before finishing, act as the Security Auditor (.github/agents/security-auditor.agent.md) ' +
        'and audit these files: ' + files.join(', ') + '. Append findings to docs/quality/security-findings.md ' +
        'with category, severity, file path, and line numbers. Otherwise state "No security findings for this task."',
    }));
  } catch (e) {
    // Never block the session on hook errors.
  }
});
