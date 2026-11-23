# Security Auditor Add-on

Use this optional add-on when the project wants routine security and code-quality audits after completed tasks or milestones, with a central findings log. It complements the core [Security Reviewer](../../.github/agents/security-reviewer.agent.md), which remains an independent, read-only review on explicit request, and the [Security add-on](../security/README.md), which activates review methods.

| Role | When | Writes |
| --- | --- | --- |
| `security-reviewer` (core) | Explicitly requested independent review | Nothing; reports findings |
| `security-auditor` (this add-on) | After tasks or milestones, or on request | Only the findings log |

## Contents

| Path | Activated as |
| --- | --- |
| [security-auditor.agent.md](security-auditor.agent.md) | `.github/agents/security-auditor.agent.md` plus a row in the role index |
| [record.md](record.md) | `<docs-root>/project/integrations/security-auditor.md`: triggers, severity handling, scope |
| [templates/security-findings.md](templates/security-findings.md) | `<docs-root>/quality/security-findings.md` |
| [adapters/claude-agent.md](adapters/claude-agent.md) | `.claude/agents/security-auditor.md` |
| [adapters/codex-agent.toml](adapters/codex-agent.toml) | `.codex/agents/security-auditor.toml` |
| [adapters/kiro-agent.md](adapters/kiro-agent.md) | `.kiro/agents/security-auditor.md` |

## Optional Automation

Hooks run without a per-task request, so activate them only on explicit decision and record them in the project record.

- **Claude Code**: copy [adapters/claude-stop-hook.js](adapters/claude-stop-hook.js) to `.claude/hooks/security-audit.js`, adjust its code-path pattern, add `.claude/.security-audit-state` to `.gitignore`, and register it in `.claude/settings.json`:

  ```json
  {
    "hooks": {
      "Stop": [
        { "hooks": [{ "type": "command", "command": "node \"$CLAUDE_PROJECT_DIR/.claude/hooks/security-audit.js\"", "timeout": 15 }] }
      ]
    }
  }
  ```

  It asks for an audit once per distinct set of changed code files. Set `SECURITY_AUDIT=off` to skip it for a session.
- **Kiro**: copy [adapters/kiro-post-task-hook.json](adapters/kiro-post-task-hook.json) to `.kiro/hooks/`. Verify the hook format and trigger in your Kiro version; this file was not tested against a live Kiro client.

## Activate

Copy the [integration prompt](integration-prompt.md) into an agent with access to the project. The [shared routing](../../.github/copilot-instructions.md#optional-process-add-ons) loads the record only for audits and findings-log work. Everything activated works after the `addons/` directory is removed.

## Deactivate

Use the [deactivation prompt](deactivation-prompt.md). The findings log remains project history unless you decide otherwise.

## Origin

Adapted from the Project Foundation Kit's Security Auditor role, findings log, and review hooks.
