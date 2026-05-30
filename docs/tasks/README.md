# Tasks

Use this directory for implementation task breakdowns derived from specs.

Start with one task file per spec. Split into one file per task only when a task becomes large, long-lived, independently owned, or needs its own artifact history.

## Files

- `template.md` - template for spec-level task files
- `artifacts/` - supporting notes, evidence, exports, screenshots, logs, or references for specific tasks

## Naming

Recommended task file naming:

```text
001-project-foundation-tasks.md
010-authentication-tasks.md
020-dashboard-tasks.md
```

Task IDs should be stable:

```text
TASK-001
AUTH-001
DASH-001
```

## Task Rules

- Every task should link to a source spec or requirement.
- Every task should have one primary owner.
- Every task should include verification expectations.
- Keep implementation notes separate from acceptance criteria.
- Put large supporting material in `tasks/artifacts/` and link to it.
- Do not create tasks until the source requirement or spec has no unanswered blocking open questions, unresolved points, or unresolved linked question files.
- Do not start task implementation until the task has no unanswered blocking open questions, unresolved points, or unresolved linked question files.
- Resolve open questions through step-by-step user dialogue; when options exist, document the options, relevant pros and cons, and the selected decision.
