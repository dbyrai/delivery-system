# Security Auditor Integration Prompt

Copy this prompt into an agent with access to the target Delivery System project.

```text
Set up the optional Security Auditor add-on for this Delivery System project.

Read the applicable project instructions, the project security policy, and
addons/security-auditor/README.md. Identify the project root, the existing
documentation root, and which AI tools use the repository. Inspect the working
tree so you can preserve existing changes. Verify that the shared instructions
contain the Optional Process Add-ons section; if it is missing, report that the
routing update is required and stop.

Check for existing files at the target paths in the README. Never overwrite an
existing different file; report it and ask how to merge. Show me the open
decisions in addons/security-auditor/record.md (triggers, code paths in scope,
release blocking, owner). Ask one focused question at a time with a recommended
answer and record explicit deferrals.

After my confirmation:
1. Write the completed record to <docs-root>/project/integrations/security-auditor.md.
2. Copy the role profile to .github/agents/security-auditor.agent.md and add a
   security-auditor row to .github/agents/README.md.
3. Copy the findings log template to <docs-root>/quality/security-findings.md.
4. Copy the adapter for each tool in use (Claude Code, Codex, Kiro) to the path
   listed in the README. GitHub Copilot uses the shared role profile directly.
5. Only if I explicitly choose automation, install the selected hook as described
   in the README and name it in the record.
6. Adjust docs paths in copied files if the documentation root is not docs/.

Activated files must not reference addons/. Read back every written file, compare
the working tree with its initial state, and report paths, decisions, deferrals,
and checks actually run. Activation authorizes no audit run, code changes,
commits, or pushes.
```
