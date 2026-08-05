# AI Project Instructions

These instructions define the default behavior for Kiro and other AI assistants working in this repository.

## Project Context

TODO - Describe the project on a high level technical perspective

The authoritative project knowledge lives in `docs/`. Treat those files as the source of truth for requirements, architecture, decisions, and quality expectations.

## Source Of Truth Order

Use this priority order when making decisions:

1. Direct user instructions in the current task or Kiro spec
2. Relevant files in `docs/`
3. Kiro steering files in `.kiro/steering/`
4. Existing repository structure and code conventions
5. Agent role guidance in `.github/agents/`
6. General engineering best practices

If two sources conflict, follow the higher-priority source and mention the conflict in the response or handoff.

## Kiro Spec-Driven Development

This project uses Kiro's spec-driven workflow:

- **Specs** define requirements, design, and acceptance criteria before implementation begins.
- **Tasks** are generated from specs and executed sequentially.
- Each task has clear acceptance criteria and verification steps.
- Do not start implementation without an approved spec or explicit user instruction.
- Use `docs/specs/` for project-level specifications and `.kiro/specs/` for Kiro-native spec files.

## Default Behavior

- Read relevant files before changing anything.
- Keep changes focused on the requested task.
- Prefer existing structure, naming, tooling, and style.
- Do not invent requirements, business rules, APIs, user flows, or project facts.
- Preserve user-provided text, labels, URLs, and quoted content unless explicitly asked to edit them.
- Make assumptions visible when they affect behavior, scope, or future implementation.
- Surface blockers, missing information, or ambiguity before making risky changes.

## Open Question Gating

Open questions are blocking unless the user explicitly marks them as non-blocking or deferred.

- Do not create implementation tasks from a requirement or spec while that requirement or spec has unanswered open questions.
- Do not start implementing an individual task while that task has unanswered open questions.
- Resolve questions through step-by-step dialogue with the user.
- When multiple options exist, present viable options with clear explanations and an AI recommendation.
- Record the chosen answer or deferral in the relevant file before proceeding.

## Documentation Policy

- Keep documentation clear, practical, and maintainable.
- Prefer concise sections, checklists, examples, and decision records over long narrative text.
- When adding project details, place them under `docs/` unless the file clearly belongs elsewhere.
- Link related documents instead of duplicating large sections.
- Mark unresolved items as open questions or assumptions.

## Code Policy

- Source code may be created or edited when the task asks for implementation.
- Follow the repository's existing tooling and patterns.
- Avoid broad refactors unless required for the requested work.
- Keep secrets, credentials, private tokens, and sensitive data out of the repository.
- Include appropriate verification for code changes (tests, linting, type checks, builds).

## Language Policy

- Chat responses may use the user's language.
- User-facing application text must be in the defined applications main language.
- Code, API paths, config keys, variable names, and technical documentation remain in English.
- Comments and inline documentation should be concise and useful, in English.

## Agent Roles

Specialized agent guidance lives in `.github/agents/`. Use these roles as working modes:

- `project-manager`: planning, sequencing, task breakdown, stakeholder-ready status
- `technical-lead`: architecture, cross-role decisions, review, risk management
- `devops-engineer`: infrastructure, environments, deployment, operations
- `backend-developer`: backend services, APIs, data models, integrations
- `frontend-developer`: frontend application, UI behavior, routing, client-side integration
- `qa-engineer`: test strategy, automated/manual verification, acceptance checks
- `content-editor`: content structure, editorial quality, metadata, documentation review

If a task spans multiple roles, identify the primary owner and list required collaborators.

## Delivery Standards

Every completed task should make clear:

- What changed
- Which files were affected
- How the work was verified
- Which assumptions, risks, or follow-up tasks remain

For implementation, keep final summaries short and include relevant commands that were run.
