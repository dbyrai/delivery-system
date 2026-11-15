# Tasks

Use this directory for implementation tasks derived from specs.

Start with one task file per spec. Split into one file per task when a task becomes large, long-lived, independently owned, or needs its own artifact history.

## Files

- `template.md` – template for task files associated with a spec
- `artifacts/` – supporting notes, evidence, exports, screenshots, logs, and references for tasks

## File Names and Task IDs

Recommended file names:

```text
001-project-foundation-tasks.md
010-authentication-tasks.md
020-dashboard-tasks.md
```

New tasks receive IDs in the format `TASK-<spec-number>-<sequence>`. Use at least three digits for each number. The spec number matches the numeric prefix of the associated spec and task file and must be unique within the project.

Example for `docs/specs/010-authentication.md` and `docs/tasks/010-authentication-tasks.md`:

```text
TASK-010-001
TASK-010-002
TASK-010-003
```

For spec `020`, the sequence starts again at `001`: `TASK-020-001`.

- Assign new sequence numbers in ascending order per spec, even when its tasks are split across multiple files.
- Use the same complete ID in the overview, detail heading, dependencies, and artifacts.
- Keep assigned IDs when reordering tasks or moving them into separate files. Do not reuse deleted IDs; gaps are allowed. The table order describes execution order, not the ID.
- Existing projects may retain their previous IDs. If a migration is explicitly agreed, update all references and artifact links and document the mapping from old IDs to new IDs.

## Task Rules

- Every task links to a source spec or requirement.
- Every task has exactly one primary owner.
- Every task describes its expected verification.
- Every task file includes a `Task Order` table near the top with the columns `Task`, `Title`, `Owner`, `Status`, and `Blocker`.
- The overview and detail sections describe the same tasks. Keep IDs, titles, owners, statuses, and blockers consistent in both places. Individual tasks use `Not Started`, `In Progress`, `Blocked`, and `Done`; `Draft` and `Ready` describe the task file as a whole.
- Keep implementation notes separate from acceptance criteria.
- Put large supporting material under `docs/tasks/artifacts/` and link to it from the task.
- Do not create tasks while the source requirement or spec contains unanswered blocking questions, unresolved points, or unresolved linked question files.
- Do not start implementation while the task itself contains any of these blockers.
- Resolve open questions through step-by-step user dialogue. When multiple options exist, document the options, relevant pros and cons, and the selected decision. Record explicit deferrals.
