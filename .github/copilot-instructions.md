# Shared AI Project Instructions

These are the canonical cross-tool workflow rules. Paths are relative to the repository root. Tool entry files route here; role files define only role-specific behavior. `docs/` is the project source of truth; do not assume a stack, product, or deployment target from an unfilled template.

## Source of Truth

Apply this order within the repository; applicable tool/system safety policies remain in force:

1. Direct user instructions for the current work, including explicit exceptions or deferrals.
2. Relevant documentation under the project's existing documentation root: recorded decisions, specs, architecture, requirements, and task acceptance criteria. Do not treat a task as permission to bypass its source requirements or security policy. Surface contradictions rather than silently choosing a convenient interpretation.
3. Existing repository structure and code conventions.
4. Selected role guidance under `.github/agents/`.
5. General engineering practices.

## Task Routing and Context Loading

1. Check the working-tree state before edits. Preserve unrelated and uncommitted user changes.
2. Classify the request and identify affected paths using file names, indexes, or focused search before reading large files. Treat follow-up questions as part of the current task unless the user changes the objective.
3. Select exactly one primary owner using the compact [role index](agents/README.md), then read only that role's complete file. Selecting a role does not launch a subagent.
4. Load sources using the table below. Reuse unchanged instructions already in the current context; reload only when changed, missing, or uncertain. Do not recursively reread entry files or imports.
5. Follow linked dependencies, unresolved question files, acceptance criteria, and applicable security/operational constraints before acting. If a required source is unavailable, report the gap; do not assume it was read or that a gate passed.

| Request | Sources to load as needed |
| --- | --- |
| Question or small review | Affected files and directly relevant references |
| Product, goals, or scope | Project overview and relevant decisions |
| Bootstrap or adoption | Relevant sections of `delivery-system.md`, then each current step's files in order |
| Spec or task creation/change | Relevant delivery rules, template, source requirement/spec, linked questions, and affected artifact |
| Implementation or bug fix | Relevant task, source spec/requirements, applicable architecture/security rules, affected code, and verification commands |
| Architecture or security decision | Relevant specs, decisions, architecture, security baseline, and impacted interfaces |
| Release, operations, or migration | Relevant release/runbook/upgrade instructions, affected configuration, verification and rollback expectations |

The overview, full delivery handbook, all baseline files, and all roles are not universal startup reading. Classify mixed requests by all affected concerns; routing is never an exemption from required acceptance or safety gates. Keep existing documentation roots, including subproject roots, and resolve their nearest applicable instructions before using generic paths.

## Optional Add-ons

Files under `addons/` are distribution packages and are inactive by default. An add-on is active only when its setup flow has created a durable project record under the applicable documentation root and added a short conditional pointer to that record from these shared instructions. Load an active record only when the current request concerns its scope; do not scan or load unrelated add-ons.

An active record must contain the operational rules needed after `addons/` is removed, identify its owner and source revision, and describe scope, activation state, verification, and removal. It must not import instructions from `addons/`. If the record or conditional pointer is absent, continue with the core workflow. Add-on activation grants no authority to change external systems, install automation, commit, push, merge, or publish.

## Optional Matt Pocock Methods

After choosing the primary role and checking the applicable delivery gates, select a method only when the current assignment calls for it. Honor an explicit method request or opt-out. Otherwise use `diagnosing-bugs` for hard-to-reproduce defects or performance regressions, `tdd` when the assignment calls for test-first work, `grill-me` for a request to work through open design decisions, or `to-questionnaire` when the user wants questions for someone else to answer.

For a matching assignment, look for `project/integrations/mattpocock-skills.md` under the applicable documentation root (normally `docs/`). Use the nearest applicable active entry, falling back to the project entry if needed. Locate sections by heading and load just `Geltung`, the selected method, and its named references in the entry. If the entry or method is absent, continue with the normal workflow. Other assignments skip this lookup. The existing primary role performs the work within task scope and project rules. The method grants no authority to change gates, delegate, or write externally.

## Optional Security Methods

After selecting the primary role and checking delivery gates, use `security-review` for an assigned security review of application code or `infra-security` for an assigned security review of infrastructure, containers, or CI/CD configuration. Use both when both are in scope. Honor an explicit method choice or opt-out within that scope. Skip the lookup for unrelated work.

Look for `project/integrations/security-skills.md` under the applicable documentation root. Prefer the nearest active entry containing the requested method and fall back to the project entry. Read `Geltung` and the selected sections alongside the project security policy. If a method is absent, continue under the existing project rules and report the missing method when explicitly requested. Report checks actually run and coverage gaps. Activation alone grants no authority to install tools, change CI, or access live systems.

Use the shared [Security Reviewer role](agents/security-reviewer.agent.md) for an explicitly requested independent security review. For a second review within an ongoing assignment, delegate to the project's `security-reviewer` when the client supports it and delegation is permitted. If the client cannot provide a separate reviewer, report that limitation. The current assistant can run a read-only review using the shared role and identify it as a single review. The role is available even when no optional Security method is active.

## Shared Skills

Workflow skills live in `.github/skills/<name>/SKILL.md`; tool wrappers in
`.claude/skills/` and `.agents/skills/` only delegate there. Use a skill when the
user invokes it or the request clearly matches its description. A skill sequences
work for the primary role it names; it does not override source authority,
delivery gates, work boundaries, or authorization rules in this file.

## Optional Diagnostic Gate

Delivery diagnostics default: off

Diagnostics control visible output only; all gates still apply when hidden. `Delivery diagnostics: on` or `Delivery diagnostics: off` in a user message overrides this default for the chat until changed. A choice explicitly limited to one task restores the previous setting afterward. Chat changes do not modify files or carry over to other chats; change this default only when asked to set a persistent project preference.

When enabled, emit this compact gate after classification and role selection, before detailed domain/code analysis or edits. List only sources actually loaded; if needed, report missing sources separately. Do not bulk-read documents merely to populate the gate.
When using an optional method, add `- selected method: <Name> (<Reason>)` for each selected method to the diagnostic gate and include its entry in the loaded project sources.

```text
Delivery System:
- task type: <Classification>
- selected agent: <Primary owner>
- agent file: <Path read>
- loaded project sources: <Paths actually read or none>
- planned subagents: <Count>
```

## Blocking Questions and Delivery Gates

- Open questions are blocking unless the user explicitly resolves or defers them. Read linked question files; capture the chosen answer or explicit deferral in the relevant requirement, spec, task, decision, or question file before proceeding.
- Do not create implementation tasks from sources with unresolved blocking questions or implement a task with unresolved blockers. Ask focused questions in sequence; explain viable options and material tradeoffs when a decision is needed.
- Run bootstrap steps in order when bootstrapping or adopting a project. Implementation requires a completed or explicitly deferred bootstrap. Do not rerun bootstrap or replace completed documents for routine work in an already adopted project.
- Keep task scope tied to source requirements and acceptance criteria. Do not invent business rules, endpoints, user flows, or security policies.

## Work, Security, and Authorization Boundaries

- Make the smallest complete change for the request. No unrelated refactors, upgrades, redesigns, architecture, CI/CD, formatting, or automatic follow-up tasks.
- Keep secrets and sensitive data out of code, logs, documentation, and artifacts. Never weaken authentication, authorization, privacy, or other project safety gates to save context. Use existing deployment processes; do not replace a pipeline with direct uploads without explicit authorization.
- No automatic commits, pushes, rebases, resets, releases, or destructive operations. Clarify who performs the requested Git/publication steps; authorization already given for the current task remains valid. Commit only approved related changes and verify the published commit matches the approved source.
- Default to zero subagents. Delegate only for an explicit workflow requirement, a clearly bounded parallel task, a necessary independent specialist review, or a user request. Assign one primary owner and separate write scopes; communicate shared-worktree constraints and review the results before completion.
- Preserve user-provided wording, existing project rules, and customizations unless the requested change requires adapting them. Report conflicts explicitly.

## Verification and Handoff

Use checks proportional to the changed behavior and risk: relevant tests, lint/type checks, builds, document links/formats, or repeatable manual checks. Bound searches, diffs, and logs to affected paths. Do not report an unrun or blocked check as passed. Distinguish static format checks from actual model/client behavior.

For small work, report the result, affected files, and verification briefly. For larger or risky work, also state limitations, unresolved items, risks, and the next owner when a handoff is required. Avoid repeating project context or full logs; link evidence. Stop after final verification without starting another task.

## Language and Documentation

Chat may use the user's language. Repository deliverables, including `project`, `specs`, and `tasks`, use English unless the user explicitly requests another language. Keep code syntax, commands, IDs, configuration keys, API paths, and literal source values unchanged. Keep project facts in the existing documentation root and link rather than duplicate them. Mark assumptions and unresolved questions; keep operational rules here and use guides only to explain them.
