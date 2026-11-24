# Sprint Documents

This directory contains per-sprint documents: a `planning.md` created at the start of each sprint and a `report.md` created at the end.

## Structure

```
docs/sprints/
├── README.md           # This file (templates + instructions)
├── 1/
│   ├── planning.md     # Sprint 1 planning prep (start of sprint)
│   └── report.md       # Sprint 1 report (end of sprint)
├── 2/
│   ├── planning.md
│   └── report.md
└── ...
```

A sprint folder holds two documents:

- **`planning.md`** — created at the *start* of the sprint by the `sprint-planning` skill. Holds the groomed version backlog and the sprint planning recommendation.
- **`report.md`** — created at the *end* of the sprint. Holds velocity, capacity, and retro notes.

## Planning Document Template

Each sprint's `planning.md` is created by the `sprint-planning` skill (Phase A writes the `## Backlog`
chapter; Phase B writes the `## Sprint Planning` chapter in full-flow mode).

---

```markdown
# Sprint {N} Planning

**Target Version**: {e.g. 0.5 — MVP}
**Sprint**: {N}
**Prepared**: {YYYY-MM-DD}

> A version may span multiple sprints. Version and sprint number are independent.

## Sprint Goal


## Backlog

Features planned for the target version and not yet done. Rows are features/specs (one per spec).

| Feature / Spec | Short Description | Spec Status | MoSCoW | Prio | Effort | Refinement |
|----------------|-------------------|-------------|--------|------|--------|------------|
|                |                   |             |        |      |        |            |

- **Spec Status**: Planned | Draft | In Review | Approved | In Progress | Done | Blocked | none (from the spec file's Status field)
- **MoSCoW**: Must | Should | Could | Won't
- **Prio**: ordinal rank within the version (1 = first)
- **Effort**: story points (1 | 2 | 3 | 5 | 8 | 13) if a sized task exists, else `—`
- **Refinement**: Ready | Needs Refinement

### Open Questions (Refinement Meeting)

Items marked "Needs Refinement" above, with the questions to resolve before they can be specced.

- **{Feature}**: {open question}

## Sprint Planning

_(Full-flow mode only — Phase B output.)_

### Velocity (Last 3 Sprints)
{table or note if insufficient data}

### Ready Tasks
{table: Task, Title, Module, Size, Priority}

### Contract Dependencies
{table: Task, Contract, Status, DoR Met; only when the Contracts add-on is active}

### Remediation
{table: ID, Source, Area, Severity / Priority, In scope this sprint?, Note}

### Capacity
{available days, recommended load}

### Recommendation
{suggested sprint scope with rationale}

### Not Ready
{tasks that fail DoR and what is missing}
```

---

## Report Template

Each sprint report follows this template. The `sprint-close` skill reads these reports for velocity calculation.

---

```markdown
# Sprint {N} Report

**Period**: {YYYY-MM-DD} – {YYYY-MM-DD}
**Status**: {Completed | In Progress}

## Planning vs. Result

**Sprint Goal**: {goal from planning.md}
**Goal Rating**: {Achieved | Partially | Missed} — {one sentence why}

| Item | Planned | Size | Result | Note |
|------|---------|------|--------|------|
|      | {committed \| added mid-sprint \| unplanned \| removed} | | {Done \| Carry-over \| Dropped \| Not started} | |

## Velocity

| Points | Committed (tasks) | Completed (tasks) | Carry-Over (tasks) |
|--------|-------------------|-------------------|--------------------|
| 1      |                   |                   |                    |
| 2      |                   |                   |                    |
| 3      |                   |                   |                    |
| 5      |                   |                   |                    |
| 8      |                   |                   |                    |
| 13     |                   |                   |                    |
| **Total points** | | | |

Velocity = sum of story points of completed tasks (Fibonacci scale 1, 2, 3, 5, 8, 13).

**Sprint Velocity**: {total points completed}
**Commitment Accuracy**: {completed committed / committed × 100}%
**Velocity per Person-Day**: {velocity / available person-days}
**Unsized Work Delivered**: {list or "none" — not counted in velocity}

### Velocity History

| Sprint | Committed | Completed | Accuracy | Person-Days | Velocity / PD |
|--------|-----------|-----------|----------|-------------|---------------|
|        |           |           |          |             |               |

**3-Sprint Average**: {avg} · **Trend**: {increasing | stable | decreasing}

## Capacity

| Developer | Available Days | Allocated (weighted) | Actual (weighted) |
|-----------|---------------|---------------------|-------------------|
| {Name}    |               |                     |                   |
| {Name}    |               |                     |                   |
| **Total** |               |                     |                   |

## Scope Changes

{Tasks added or removed mid-sprint. Include reason for each change.}

| Task | Change | Reason |
|------|--------|--------|
|      |        |        |

## Contract Status

{Contracts that changed status during this sprint; omit when the Contracts add-on is not active.}

| Contract | Previous Status | New Status | Impact |
|----------|----------------|------------|--------|
|          |                |            |        |

## Completed Tasks

| Task | Title | Developer | Size | Module |
|------|-------|-----------|------|--------|
|      |       |           |      |        |

## Carry-Over

{Tasks not completed, moving to next sprint.}

| Task | Title | Developer | Size | Reason |
|------|-------|-----------|------|--------|
|      |       |           |      |        |

## Blockers & Learnings

{Filled during the Sprint Retro with the `sprint-close` skill. Agent observations are marked as proposals.}

### Previous Action Items

| Action Item | Owner | Status |
|-------------|-------|--------|
|             |       | {Done \| In progress \| Dropped} |

### What went well
-

### What did not go well
-

### Action items

| Action Item | Owner | Target Sprint |
|-------------|-------|---------------|
|             |       |               |

### Learnings for Planning

Rules the `sprint-planning` skill applies in the next sprints.

-
```

---

## How These Documents Are Created

**`planning.md`** (start of sprint):
1. **Agent-assisted**: The `sprint-planning` skill writes the `## Backlog` chapter (Phase A) and, in full-flow mode, the `## Sprint Planning` chapter (Phase B)
2. **Stored**: `docs/sprints/{sprint-number}/planning.md`

**`report.md`** (end of sprint):
1. **Agent-assisted**: The `sprint-close` skill builds Planning vs. Result, velocity and task sections from `planning.md`, the task files and git
2. **Retro**: `sprint-close` records "Blockers & Learnings" interactively during the Sprint Retro
3. **Stored**: `docs/sprints/{sprint-number}/report.md`

## Velocity Reference

The `sprint-close` and `sprint-planning` skills read the last 3 sprint reports to calculate:
- Average velocity (and velocity per person-day)
- Trend (increasing / stable / decreasing)
- Per-developer breakdown

It also applies the open **Action items** and **Learnings for Planning** of the latest report.

See the project's SCRUM record (`docs/project/integrations/scrum.md`) for story points, velocity, and capacity rules.
