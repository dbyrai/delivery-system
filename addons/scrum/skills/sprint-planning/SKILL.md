---
name: sprint-planning
description: Prepare a sprint in two phases. Phase A (refinement prep) re-prioritizes the version backlog and writes docs/sprints/{N}/planning.md; Phase B (planning prep) gathers velocity, capacity, ready tasks, and remediation candidates read-only. Use when the user asks to prepare refinement, sprint planning, or the next sprint.
---

# Sprint Planning

Act as the Product Manager (`.github/agents/product-manager.agent.md`). Load the SCRUM record (`project/integrations/scrum.md` under the documentation root) for cadence, estimation, and capacity rules. Use the user's language in discussion; written documents follow the shared language policy.

## Data

- `docs/sprints/{N}/planning.md` and `docs/sprints/{N}/report.md` (templates in `docs/sprints/README.md`)
- `docs/specs/` and `docs/tasks/` for status and readiness; `docs/quality/dor-checklist.md`
- `docs/contracts/` for contract status, only when the Contracts record is active
- `docs/quality/tech-debt.md` and `docs/quality/security-findings.md`, when present
- Git history for delivered work; an external tracker only as a read-only extra source named in the SCRUM record

## Step 0: Mode And Inputs

Ask for the mode: **Full** (A then B), **Refinement only** (A), or **Planning only** (B, screen-only unless the user asks to save). Then confirm, never guess:

1. Sprint number: suggest the highest numeric folder in `docs/sprints/` plus one.
2. Target version: suggest the next planned version from the roadmap or changelog. Version and sprint are independent.

## Phase A: Refinement Prep

1. **Re-prioritize**: run the `prioritize` skill inline and finish it with explicit user confirmation.
2. **Feature list**: collect specs planned for the target version and not yet delivered (roadmap, spec status, changelog). One row per spec.
3. **Remediation candidates**: read the quality logs. Always surface open High/Critical security findings as Must candidates; add Medium/Low findings and tech-debt items that touch in-scope areas or block planned work. State explicitly when a log is missing or has no relevant entries.
4. **Backlog table**:

   ```markdown
   | Feature / Spec | Short Description | Spec Status | MoSCoW | Prio | Effort | Refinement |
   | --- | --- | --- | --- | --- | --- | --- |
   ```

   Effort is the human estimate in story points if a sized task exists, otherwise `-`.
5. **Refinement status**: `Ready` when the spec passes DoR Spec (and, with the Contracts record active, its required contracts are at least `review`); otherwise `Needs Refinement` with the open questions listed for the refinement meeting. A missing task file is not a blocker; it is the task-file author's first step after handoff. Refinement status lives only in `planning.md`.
6. **Write** the header and `## Backlog` chapter of `docs/sprints/{N}/planning.md` after the user confirms the content.

## Phase B: Planning Prep (Read-Only)

1. **Velocity**: from the last three reports compute per-sprint velocity, average, trend, and velocity per person-day. If the previous report is missing, recommend `sprint-close` first. Apply the latest report's open action items and learnings for planning and say which ones changed the recommendation.
2. **Ready tasks**: list candidate tasks passing DoR Task (points set, linked spec, owner, no blockers), sorted by roadmap order.
3. **Contract dependencies** (Contracts record active only): `| Task | Required Contract | Contract Status | DoR Met |`; flag contracts below `review`.
4. **Remediation**: `| ID | Source | Area | Severity / Priority | In scope this sprint? | Note |`. Open High/Critical security findings are Must unless the user explicitly defers them. Unsized remediation is a gap to size, not committed work.
5. **Capacity**: ask for available developers and absences; compute person-days and the recommended load from the SCRUM record.
6. **Recommendation**: tasks within capacity by priority, load against capacity, risks, and tasks not ready with what is missing. If a High/Critical finding does not fit, flag it as a risk instead of dropping it.

In Full mode write Phase B under `## Sprint Planning` in `planning.md`.

## Rules

- Phase B never changes task or spec status.
- Never estimate story points, author task files, or commit sprint scope; the people named in the SCRUM record decide.
- Change the roadmap only through the confirmed `prioritize` step.
- Name data gaps honestly.
