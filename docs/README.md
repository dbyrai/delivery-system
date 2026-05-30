# Documentation

This directory is the source of truth for project knowledge.

Use it to document requirements, project context, implementation tasks, quality standards, decisions, and manual verification steps. AI assistants should read the relevant files in this directory before making project assumptions.

For using this repository as a reusable project starter, see `delivery-system.md` in the repository root.

## Structure

- `project/` - project overview, roadmap, decisions, stakeholders, and delivery context
- `specs/` - requirements and specification documents
- `specs/baseline/` - global requirements that apply across all specs
- `tasks/` - implementation task breakdowns derived from specs
- `tasks/artifacts/` - task-specific supporting information, evidence, exports, notes, or references
- `quality/` - Definition of Done, test strategy, review standards, and verification guidance
- `quality/manual-tests/` - manual test cases and step-by-step checks

## Source Of Truth

When files conflict, use this order:

1. Current user instruction
2. `docs/project/decisions.md` or decision records
3. Relevant spec files in `docs/specs/`
4. Baseline requirements in `docs/specs/baseline/`
5. Task files in `docs/tasks/`
6. Agent guidance in `.github/agents/`

Document unresolved conflicts as open questions.
