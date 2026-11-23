# Security Auditor Deactivation Prompt

```text
Deactivate the Security Auditor add-on in this Delivery System project.

Read the applicable project instructions and locate
project/integrations/security-auditor.md under the documentation root. Verify its
identity, inspect working-tree changes, and find all references to it, to
.github/agents/security-auditor.agent.md, its tool adapters, any installed hooks
and hook settings, and docs/quality/security-findings.md.

Report open Critical and High findings first. Ask me what to remove, archive, or
keep. By default keep the findings log as project history. Stop installed hooks
before removing their scripts. Remove only confirmed items, remove the role index
row, check remaining links, and report the result. The core security-reviewer
role is not part of this add-on and stays in place.
```
