---
name: dod-readiness-check
description: Read-only check of a finished task or feature against the Definition of Done and its source acceptance criteria, producing a severity-rated finding list. Use when the user asks whether work is done or to verify a task or feature against the DoD.
---

# DoD Readiness Check

Act as the Project Manager (`.github/agents/project-manager.agent.md`). The authoritative checklist is `docs/quality/dod-checklist.md`. This check is read-only: never modify tasks, specs, code, tests, or documentation, and never mark work done yourself.

## Step 0: Resolve The Target

Accept a task file path, a spec number or name, or a task description. If ambiguous, list candidates and ask. Read the task file and its source spec; inspect the related diff, code, tests, and documentation where evidence lives. Record the target and source spec in the report header.

## Step 1: DoD Check

Walk every criterion in the DoD checklist and mark it Pass, Fail, N/A, or Unknown with the evidence inspected. A checked box in a task file is a claim, not proof. With the Contracts record active, also check that consumed contracts are implemented as specified and provided contracts are updated when their surface changed.

Implementation quality and verification adequacy need technical depth: record your observation, mark the criterion Unknown where a code-level judgement is needed, and recommend Technical Lead sign-off.

## Step 2: Acceptance Criteria Trace

For each acceptance criterion of the source spec, confirm the delivered work satisfies it. Unmet Must or Should criteria are at least High.

## Step 3: Findings

| Severity | Meaning |
| --- | --- |
| Critical | Not done: unmet Must criterion, failing build or tests, committed secret, violated contract |
| High | Likely defects or rework: unhandled edge states, missing evidence for a risky change |
| Medium | Non-blocking gap: documentation not updated, follow-ups not captured |
| Low | Hygiene: missing changed-files summary, cosmetic drift |

```markdown
## DoD Readiness: {Task or Feature} ({task path})

**Source Spec**: {spec path}
**Verdict**: DONE | PARTIALLY DONE | NOT DONE
**DoD**: {met}/{total} criteria met
**Acceptance Criteria**: {met}/{total} satisfied

| # | Severity | Area | Finding | Evidence | Recommendation |
| --- | --- | --- | --- | --- | --- |
```

Verdict: any Critical means NOT DONE; no Critical but at least one High means PARTIALLY DONE; otherwise DONE with noted follow-ups.

## Rules

- Evidence over claims; mark Unknown when you cannot verify.
- Suggest status changes; the responsible people decide.
