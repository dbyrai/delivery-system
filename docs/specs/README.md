# Specs

Use this directory for requirements and specifications.

Specs describe what must be true. Tasks describe how the work will be done.

## Files

- `template.md` - template for creating a new spec
- `requirements.md` - high-level project requirements index
- `baseline/` - global requirements that apply across all specs

## Naming

Use numbered, descriptive filenames for specs:

```text
001-project-foundation.md
010-authentication.md
020-dashboard.md
```

## Spec Rules

- Each spec should have a clear owner.
- Each requirement should be testable.
- Acceptance criteria should be explicit.
- Open questions should remain visible until resolved.
- Tasks may only be created after all blocking open questions, unresolved points, and linked question files for the source requirement or spec are answered or explicitly deferred.
- Resolve open questions through step-by-step user dialogue; when options exist, document the options, relevant pros and cons, and the selected decision.
- Do not mix detailed implementation tasks into specs; put those in `docs/tasks/`.

## Recommended Spec Flow

1. Create or update `requirements.md`.
2. Create a spec from `template.md`.
3. Link relevant baseline requirements.
4. Define acceptance criteria.
5. Resolve or explicitly defer all blocking open questions and linked question files.
6. Create a matching task file in `docs/tasks/`.
