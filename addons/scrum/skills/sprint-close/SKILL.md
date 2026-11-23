---
name: sprint-close
description: Close a sprint by comparing plan and result, measuring velocity, running the retro, and writing docs/sprints/{N}/report.md for the next planning. Use when the user asks to close a sprint, prepare the sprint review or retro, or write the sprint report.
---

# Sprint Close

Act as the Project Manager (`.github/agents/project-manager.agent.md`). Load the SCRUM record (`project/integrations/scrum.md` under the documentation root). Use the user's language in discussion; the report follows the shared language policy. The report is the source of truth for velocity and feeds the `sprint-planning` skill.

## Step 0: Inputs

Confirm, never guess:

1. Sprint number: suggest the highest `docs/sprints/{N}/` with `planning.md`, no `report.md`, and a passed end date.
2. Period: from `planning.md` (latest correction wins) or the roadmap.
3. Mode: **Full** (steps 1-6), **Data only** (1-4 and 6, retro left open), or **Retro only** (5-6 on an existing report).

If the sprint has not ended, offer a screen-only preview.

## Data

`docs/sprints/{N}/planning.md`, task files in `docs/tasks/`, Git history and merged pull/merge requests in the period, the previous report, `docs/quality/dod-checklist.md`, and contract history only when the Contracts record is active.

## Step 1: Plan Versus Result

Fill the `Planning vs. Result` table of the report template in `docs/sprints/README.md`, with Planned = committed, added mid-sprint, unplanned, or removed and Result = Done, Carry-over, Dropped, or Not started. Flag discrepancies (Done without merge, merge without Done, unsized work) and ask the responsible developer instead of deciding. Rate the sprint goal: Achieved, Partially, or Missed, with one sentence.

## Step 2: Velocity

- Committed = points committed at planning; mid-sprint additions listed separately.
- Velocity = points Done (DoD met) at sprint end, including unplanned items.
- Commitment accuracy = completed committed points / committed points x 100.
- Unsized delivered work is listed separately and never counted.
- Velocity per person-day = velocity / available person-days.
- Extend the velocity history from the previous report and compute the three-sprint average and trend (within +/-10 % = stable).

## Step 3: Capacity

Per developer: available days (ask if not recorded), allocated points, actual points.

## Step 4: Scope, Contracts, Carry-Over

Fill scope changes with reasons, contract status changes (Contracts record active only), completed tasks, and carry-over with reasons.

## Step 5: Retro (Interactive)

1. Ask the status of each previous action item (Done, In progress, Dropped); unfinished ones carry over.
2. Propose data-based observations from steps 1-4, marked as proposals.
3. Record what went well and what did not in the user's words; never invent retro content.
4. Agree at most three new action items with owner and target sprint.
5. Agree one to five learnings for planning, each confirmed by the user.

## Step 6: Write

Show the draft of `docs/sprints/{N}/report.md` following the template in `docs/sprints/README.md`; write it after confirmation. If the next sprint's `planning.md` exists, offer to carry open action items and learnings into it after confirmation.

## Rules

- Never estimate story points; unsized work stays unsized.
- Done means Definition of Done, not only merged.
- Keep the report format stable; `sprint-planning` reads velocity history, learnings, and action items.
- Name data gaps in the report.
