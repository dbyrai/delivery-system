# SCRUM Process

<!-- Durable project record created by the optional SCRUM add-on. Replace every
{placeholder} with a confirmed project decision or mark it as an open question.
This record must stay usable after the add-on directory is removed. -->

**Status**: Active
**Owner**: {Product Owner or accountable role}
**Adopted From**: Delivery System SCRUM add-on {version or commit}

## Scope

Load this record for work on sprints, estimation, readiness checks, velocity, or retrospectives. It adds process rules to the shared Delivery System instructions and does not replace their gates.

## Team And Decisions

| Situation | Decides |
| --- | --- |
| Module-internal technical decision | Responsible developer with the Technical Lead |
| Module-internal breaking change | Responsible developer |
| Application-wide breaking change | Product Owner |
| New requirement, scope, or priority change | Product Owner |
| Cross-module contract conflict | Affected developers and Product Owner |
| Task too large for a sprint | Product Owner (back to backlog) |

- Task-file author after spec handoff: {developer | project-manager}
- Story points are estimated by humans only: {developer | team}. Agents never estimate.
- Agents suggest status changes; they never move items in an external tracker themselves.
- Agents warn (soft block) when a task is outside the current sprint scope.

## Cadence

- Sprint length: {2 weeks}
- Ceremonies: {Planning, Daily, Review, Retro, Refinement with day and duration}
- Board transitions: Ready -> In Progress (work starts) -> Review (pull/merge request) -> Done (merged and Definition of Done met). In Progress <-> Blocked with recorded reason. Review -> In Progress for rework.
- Board location: {repository only | external tool, with docs authoritative}

## Story Points

Fibonacci scale 1, 2, 3, 5, 8, 13. Points estimate relative effort, not calendar time.

| Points | Meaning |
| --- | --- |
| 1 | Trivial, well-defined |
| 2 | Small, clear scope |
| 3 | Moderate |
| 5 | Substantial but still a single slice |
| 8 | Large, the exception |
| 13 | Very large; sprint-eligible only with confidence, otherwise split |
| >13 | Not sprint-eligible; split in refinement |

Task files record points in a `Points` column of the Task Order table.

## Readiness

Readiness levels and checklists: `docs/quality/dor-checklist.md`. Done means `docs/quality/dod-checklist.md`. Implementation agents check readiness before starting a task and report violations to the responsible developer, who decides whether to proceed.

## Velocity And Capacity

- Velocity = sum of points of tasks Done at sprint end. Carry-over counts in the sprint where it completes. Unsized work is listed separately and never counted.
- Planning target: committed points <= 3-sprint average velocity x {0.8}.
- Ramp-up capacity proxy: {8} productive days per developer per sprint until three sprint reports exist.
- Sprint documents: `docs/sprints/{N}/planning.md` and `docs/sprints/{N}/report.md`; templates in `docs/sprints/README.md`.

## Skills

`sprint-planning`, `sprint-close`, `dor-readiness-check`, and `dod-readiness-check` under `.github/skills/` with wrappers for the tools in use.

## Quality Logs

Sprint planning reads `docs/quality/tech-debt.md` and, if present, `docs/quality/security-findings.md` for remediation candidates.
