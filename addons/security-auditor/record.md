# Security Auditor

<!-- Durable project record created by the optional Security Auditor add-on.
Replace every {placeholder} with a confirmed project decision or mark it as an
open question. This record must stay usable after the add-on directory is removed. -->

**Status**: Active
**Owner**: {accountable role}
**Adopted From**: Delivery System Security Auditor add-on {version or commit}

## Scope

Load this record for routine security audits and work on the findings log. The role profile is `.github/agents/security-auditor.agent.md`; the log is `docs/quality/security-findings.md`.

## Triggers

- After each completed implementation task: {always | on request | via hook}
- At milestone or sprint boundaries: {yes | no}
- On explicit request from the Technical Lead, Project Manager, or user.
- Code paths in scope: {for example src/, apps/, packages/}

Automated hooks are optional and only active where this record names them:
{none | Claude Code Stop hook}.

## Severity And Handoff

| Severity | Action |
| --- | --- |
| Critical | Hand off immediately; blocks Done for the affected task |
| High | Hand off immediately to the responsible owner |
| Medium | Record; schedule in the next planning |
| Low | Record; address opportunistically |

Whether open Critical or High findings block a release: {project decision, see security policy}.

## Relationship To Other Roles

- `security-reviewer`: independent, read-only review on explicit request; does not write the log.
- Implementation owners fix findings; the auditor verifies before marking them `Done`.
- With the SCRUM record active, sprint planning treats open Critical and High findings as Must candidates.
