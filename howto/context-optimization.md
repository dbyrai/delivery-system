# Context Optimization

## Purpose

This guide explains the v2 Delivery System structure for maintainers and teams adopting it in their own repositories. New projects receive the optimized instructions directly from the template. Existing projects can use the [v1 to v2 upgrade guide](upgrades/v1-to-v2.md) and the [migration prompt](prompts/context-optimization.md).

The goal is to spend context on the current task instead of repeatedly loading the entire delivery handbook, project history, and every role. This does not guarantee that a particular model or context window, including a 32K window, will be sufficient. Measure the selected files and verify behavior in the tools you actually use.

The [shared AI instructions](../.github/copilot-instructions.md) are the canonical operating rules. This guide explains their organization; it does not define a second workflow or permission policy.

## Responsibilities

| Location | Responsibility |
| --- | --- |
| `.github/copilot-instructions.md` | Shared workflow, source precedence, task routing, language, work boundaries, diagnostics, and approval rules |
| `AGENTS.md` | Thin Codex entry point referencing the shared instructions |
| `CLAUDE.md` | Claude entry point importing the shared instructions |
| `.github/agents/README.md` | Role selection index |
| `.github/agents/*.agent.md` | Selection metadata and the selected role's specific working rules |
| `.codex/agents/*.toml` | Codex registration metadata and a reference to the shared role profile |
| `.claude/agents/*.md` | Claude selection metadata and a reference to the shared role profile |
| `delivery-system.md` | Bootstrap, specs, tasks, templates, and delivery artifacts |
| `docs/project/` | Product context, project decisions, and roadmap |
| Relevant specs, architecture, tasks, and quality documents | Requirements, constraints, acceptance criteria, and verification for the current task |

Keep each global rule in its canonical file. A role profile can explain a role-specific application, such as reviewing an API contract, without copying the common precedence, language, Git, or completion rules. Tool adapters register and route roles; selecting a role is not permission to start another agent.

Existing repositories may use different documentation roots or additional nested instructions. Preserve those boundaries and adapt references instead of relocating completed project documentation.

## Loading Context for a Task

Start with the applicable tool entry point and shared instructions. Classify the request, select one primary role, and locate the relevant documents through file names, indexes, links, or a focused search. Then read the selected role profile and the necessary task sources.

The routing table in the [shared instructions](../.github/copilot-instructions.md) determines what must be loaded. These examples illustrate the intended effect:

| Example request | Expected context |
| --- | --- |
| Explain one task ID | Task naming rules and the referenced task, if any; unrelated product history is unnecessary |
| Change product scope | Project overview and relevant decisions, followed by affected requirements |
| Create tasks from a spec | Relevant delivery sections, task template, source spec, and all linked blocking questions |
| Fix a feature bug | Relevant task, spec, architecture or contract, affected code, and verification instructions |
| Review a security change | Applicable security requirements and decisions, affected contract or architecture, and evidence |
| Bootstrap a new project | The bootstrap sequence and its required documents, in order |

Task-dependent loading changes when material is read, not whether applicable gates must be satisfied. Follow linked blockers and security, policy, acceptance, and verification requirements even when they make the context larger. Do not infer that an unread document has no constraints. If a required source is missing or its applicability is unclear, surface that issue before dependent work.

Reuse unchanged material already available in the current task. After a new session or loss of context, reload the instructions and sources needed to establish the current state. Bound search results, logs, and diffs to the affected area; expand them when evidence requires it.

## Optional Diagnostics

The diagnostic setting remains owned by the [shared instructions](../.github/copilot-instructions.md). Its default is off. The chat instructions `Delivery diagnostics: on` and `Delivery diagnostics: off` control the visible output without changing files or bypassing reading, verification, or approval requirements.

When enabled, the compact early block reports task type, selected role, role file, sources actually loaded, and planned subagent count. It should appear before detailed task analysis and implementation. Sources read afterward must not be presented as already loaded. A task-only override ends with that task; a chat-wide choice remains local to that chat.

For a persistent default, edit `Delivery diagnostics default` in the shared file. During migration, preserve an existing explicit project choice rather than silently restoring the template default.

## Tool Integration

The v2 structure retains the shared source introduced in v1.1. `CLAUDE.md` imports `.github/copilot-instructions.md`; it does not import a second copy through `AGENTS.md`. Codex follows the reference in `AGENTS.md`, and Copilot surfaces that support repository instructions use the shared file directly.

Support for instruction and agent formats depends on the client and version. Consult the [Copilot instruction support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support), [Copilot custom agent format](https://docs.github.com/en/copilot/reference/custom-agents-configuration), and [Claude instruction documentation](https://code.claude.com/docs/en/memory) when adopting another client. A local model does not by itself determine which repository files its host supplies.

Static parsing and valid references demonstrate structure, not model compliance. At preparation time, Claude live tests were unavailable because no authenticated subscription was available, and Copilot CLI was not installed. Those runtime checks remain deferred; do not report either integration as live-tested. Reassess this limitation when the relevant tool becomes available.

## Verify the Result

Measure file sizes before and after the change:

```sh
wc -l -w AGENTS.md CLAUDE.md .github/copilot-instructions.md delivery-system.md
wc -l -w .github/agents/*.agent.md .codex/agents/*.toml .claude/agents/*.md
git diff --check
```

Count the sources actually selected for representative tasks as well. Smaller role files do not establish a smaller start context if the host automatically loads unrelated instructions. Explain what was measured and avoid treating word counts as exact model token counts.

Verify these scenarios in a disposable copy:

1. **New project:** start from the v2 template and ask for a small read-only explanation. Confirm that routing does not require the full handbook or unrelated project documents. Then start bootstrap and confirm that its existing sequence and blocking-question gates still apply.
2. **Existing project:** preserve a customized rule, completed overview and task, task ID, documentation root, and diagnostic default. Follow the upgrade guide and confirm that only agreed instruction changes are applied and every preserved item survives.
3. **Blocking source:** use a spec linked to an unanswered question. Confirm that task creation or implementation remains blocked until resolution or an explicitly recorded deferral.
4. **Diagnostics:** check default output, an on/off chat override, and a task-only override. A static review can establish the rule text; actual output and persistence require a live session in each target tool.

Parse YAML frontmatter and TOML adapters with available parsers, check every role reference and import target, and inspect remaining duplicate global rules. Record which checks ran, which passed, and which were deferred. The [upgrade guide](upgrades/v1-to-v2.md) includes the migration-specific acceptance checklist.
