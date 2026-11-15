# AI Project Instructions

These instructions define the default behavior for AI assistants working in this repository. They are intended to be usable by GitHub Copilot, Codex, Claude, and other AI coding agents.

## Mandatory Workflow

Before every new task, read the applicable tool entry file (such as `AGENTS.md` or `CLAUDE.md`, when present), these shared instructions in `.github/copilot-instructions.md`, `delivery-system.md`, and `docs/project/overview.md`. Paths in these shared instructions are relative to the repository root. Instructions already loaded in the current context count as read; do not recursively reload entry files or these shared instructions. Then select the appropriate agent using `.github/agents/README.md` and read its complete agent file. Load only relevant specs, architecture documents, task files, and source files in addition to these instructions.

### Optional Diagnostic Gate

Delivery diagnostics default: off

The diagnostic gate controls only whether the following block is displayed. All applicable reading, role, verification, and approval obligations remain in effect when diagnostics are disabled.

- `Delivery diagnostics: on` in a user message enables the output.
- `Delivery diagnostics: off` in a user message disables the output.
- The latest explicit user choice applies for the rest of the chat until changed. A choice explicitly limited to one task applies only to that task; the previous setting resumes afterward.
- Without an explicit chat choice, use `Delivery diagnostics default` from this file. For a persistent project default, the user can set this value to `on` or `off`. Changing the setting in chat does not modify files or automatically carry over to other chats.

When diagnostics are enabled, display this diagnostic gate before analyzing or implementing a new task, using only values actually established. When diagnostics are disabled, omit the block; necessary clarification questions and blocker notices still apply.

```text
Delivery System:
- tool entry file: <Path read or not applicable>
- shared instructions loaded: yes/no
- delivery-system.md read: yes/no
- project overview read: yes/no
- selected agent: <Agent>
- agent file: <Path read>
- relevant spec(s): <Files read or none>
- relevant architecture documents: <Files read or none>
- relevant task(s): <Files read or none>
- planned subagents: <Count>
```

### Work Boundaries Regardless of Diagnostics

Selecting an agent initially applies only its role instructions. The default is `planned subagents: 0`. Subagents are permitted only when explicitly required by the workflow, for clearly separated parallel work, for a necessary independent specialist review, or when explicitly requested by the user.

Use as little context as possible and as much as necessary. Do not independently expand scope, overwrite others' changes, perform unrequested refactoring, upgrades, architecture, CI/CD, or formatting changes, or automatically commit, push, rebase, or reset. Limit tests and tool output to the affected area. Stop after final verification and do not independently start a follow-up task.

## Project Context

This repository is the working space for a project that will be specified in more detail over time.

The authoritative project knowledge should live in `docs/`. When project details, requirements, architecture notes, workflows, or decisions are added there, treat those files as the source of truth.

Until detailed documentation exists, do not assume a specific framework, stack, product domain, deployment target, or architecture. Ask for clarification only when a reasonable local assumption would create risk; otherwise keep work small, explicit, and easy to revise.

## Source Of Truth Order

Use this priority order when making decisions:

1. Direct user instructions in the current task
2. Relevant files in `docs/`
3. Existing repository structure and code conventions
4. Agent role guidance in `.github/agents/`
5. General engineering best practices

If two sources conflict, follow the higher-priority source and mention the conflict in the response or handoff.

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

- Do not create implementation tasks from a requirement or spec while that requirement or spec has unanswered open questions, unresolved points, or references to unresolved question files.
- Do not start implementing an individual task while that task has unanswered open questions, unresolved points, or references to unresolved question files.
- When a requirement, spec, or task links to a question file such as `q-001.md`, `Q-001.md`, or any similarly named open-question artifact, read that file and resolve every blocking question before creating tasks or implementing the task.
- Resolve questions through step-by-step dialogue with the user. Ask one focused question or decision at a time when possible.
- When multiple options exist, present the viable options with clear explanations. Include pros and cons when the tradeoff matters, and provide an AI recommendation when useful.
- Record the chosen answer, decision, or explicit deferral in the relevant requirement, spec, task, decision record, or question file before proceeding.

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
- Include appropriate verification for code changes, such as tests, linting, type checks, builds, or a clear note when verification is not possible.

## Language Policy

- Chat responses may use the user's language.
- Repository deliverables should be written in English unless the user explicitly requests another language.
- Keep code syntax, commands, configuration keys, API paths, and literal values unchanged.
- Comments and inline documentation should be concise and useful.

## Agent Roles

Specialized agent guidance lives in `.github/agents/`. Use these roles as working modes, not as fixed project assumptions:

- `project-manager`: planning, sequencing, task breakdown, stakeholder-ready status
- `technical-lead`: architecture, cross-role decisions, review, risk management
- `devops-engineer`: infrastructure, environments, deployment, operations
- `backend-developer`: backend services, APIs, data models, integrations
- `frontend-developer`: frontend application, UI behavior, routing, client-side integration
- `qa-engineer`: test strategy, automated/manual verification, acceptance checks
- `content-editor`: content structure, editorial quality, metadata, documentation review

If a task spans multiple roles, identify the primary owner and list required collaborators or handoffs.

## Delivery Standards

Every completed task should make clear:

- What changed
- Which files were affected
- How the work was verified
- Which assumptions, risks, or follow-up tasks remain

For reviews, lead with concrete findings and file references. For implementation, keep final summaries short and include relevant commands that were run.
