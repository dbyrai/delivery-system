# Task Artifacts

Use this directory for supporting material that belongs to a specific task but would make the main task file too noisy.

Examples:

- Screenshots
- Logs
- Export notes
- Research notes
- Test evidence
- Data samples
- External references
- Manual verification evidence

## Naming

Use the complete task ID according to the [task ID rules](../README.md#file-names-and-task-ids):

```text
TASK-010-001-api-response-example.md
TASK-010-002-test-evidence.md
```

For larger tasks, create a folder:

```text
TASK-010-001/
  notes.md
  screenshots/
  logs/
```

## Rules

- Do not store secrets or sensitive data.
- Summarize large external artifacts instead of copying them wholesale.
- Link artifacts from the relevant task file.
