# Upgrade from v1 to v2

## Scope

This guide is for repositories that adopted any v1 Delivery System version and want to adopt v2. New projects should start from the v2 template and follow its bootstrap sequence directly.

v2 changes the context-loading contract: the shared instructions classify the task and route to relevant sources instead of requiring the full delivery handbook and project overview for every request. Role profiles and tool adapters become smaller. Applicable security, blocking-question, acceptance, verification, and approval gates still apply.

Read the [rationale](../context-optimization.md), then use the [migration prompt](../prompts/context-optimization.md) if an assistant will prepare the changes. The canonical workflow is in [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md); this guide explains the upgrade rather than replacing that workflow.

## Files to Review

| Files | Required review when adopting v2 |
| --- | --- |
| `.github/copilot-instructions.md` | Merge task-dependent loading and shared workflow rules, preserving project-specific constraints and explicit diagnostic defaults |
| `AGENTS.md` | Retain a thin reference to the shared source and any necessary Codex-specific routing |
| `CLAUDE.md` | Use the native import of the shared file and preserve relevant Claude-specific instructions |
| `.github/agents/README.md` | Review role routing and references without removing custom roles |
| `.github/agents/*.agent.md` | Retain selection metadata and role-specific rules; move any duplicated global rule to its canonical owner before removing it |
| `.codex/agents/*.toml`, `.claude/agents/*.md` | Retain registration metadata and corresponding role references; preserve tool-specific restrictions |
| `delivery-system.md` | Adopt delivery-specific guidance and links without turning the handbook into a mandatory read for every task |
| `README.md`, relevant how-to files | Update entry points, explanation, and upgrade links |

The listed paths describe this template. In an existing project, keep its established documentation roots and adjust links to them. Completed overviews, decisions, specs, tasks, quality records, evidence, and application files are project knowledge, not disposable template content.

## Prepare a Reviewable Migration

1. Check `git status --short` and identify all existing local changes, including untracked files. Preserve them separately from the proposed migration; do not reset or overwrite them.
2. Identify the version or commit originally adopted by the project and obtain the v2 source from the upstream repository. Compare three inputs: the adopted baseline, the current project files, and the v2 source. If the adopted baseline is unknown, record that limitation and review changes manually rather than assuming an unchanged template.
3. Inventory custom rules, security and approval requirements, roles, tool configuration, documentation roots, task IDs, and diagnostic defaults. For older v1 projects, optional diagnostics may be absent; preserve an explicit setting wherever it currently lives when moving it to the shared file.
4. Record baseline file sizes and capture the project state using the team's established review or backup process. Use an isolated branch or copy when appropriate, without moving unrelated work into the migration commit.
5. Establish which files will change and which project content must remain unchanged. Resolve conflicts in applicable instructions before applying dependent changes.

## Apply the Changes

Merge the affected instruction files selectively. Do not replace the repository or its `docs/` tree with a fresh template. When two copies of a rule differ, preserve the project-specific requirement and identify its canonical owner rather than deleting the stricter text to reduce size.

Keep `.github/copilot-instructions.md` as the shared workflow source. v1.1 projects already use that source; retain the design. Earlier v1 projects or customized projects may have rules in `AGENTS.md`, `CLAUDE.md`, role profiles, or adapter files. Consolidate global rules while preserving necessary tool-specific behavior and project restrictions.

Keep the existing documentation roots, completed documents, and task IDs. ID renaming is a separate migration and is not required by this upgrade. A previously completed bootstrap does not need to be rerun simply because instruction loading changed.

Apply the routing policy without weakening its linked gates. A task may load fewer files initially, but it must still read an applicable blocking question or security constraint before work that depends on it. A missing required source is a limitation to resolve, not permission to proceed without it.

Retain an explicit `Delivery diagnostics default` value. Projects without an explicit setting use the template's off default. A chat-wide override does not become a persistent file change; a task-only override must still end with its task. Do not enable mandatory diagnostics as part of the migration.

## Acceptance Checklist

Use a disposable copy for the scenario checks. Record static review separately from actual tool execution.

- [ ] The adopted baseline, target version, changed files, and preserved customizations are recorded.
- [ ] The shared workflow has one canonical owner, and tool entry points do not copy its full rule text or create import loops.
- [ ] Local links, heading anchors, role references, and import targets resolve.
- [ ] Shared role profiles have valid selection metadata; YAML frontmatter and TOML adapters parse with available parsers.
- [ ] No custom role, tool restriction, security rule, approval requirement, blocking question, or acceptance gate was dropped.
- [ ] Completed documentation, existing task IDs, evidence, and established documentation roots remain intact.
- [ ] **New-project scenario:** a fresh v2 copy can enter bootstrap, keeps the sequence and question gates, and does not require an optimization prompt first.
- [ ] **Existing-project scenario:** a customized rule, completed overview and task, original task ID, and explicit diagnostic default survive the selective migration.
- [ ] A small read-only request routes to its relevant sources without requiring the full handbook and unrelated project documents.
- [ ] A task with an unanswered linked question still stops before dependent task creation or implementation unless a deferral is explicitly recorded.
- [ ] Diagnostic off/on behavior and chat/task-only override semantics are preserved in the rules; actual behavior is checked in a live target-tool session when available.
- [ ] Before/after measurements identify the files and task context measured, without presenting word counts as exact token counts or promising a fixed context-window capacity.
- [ ] `git diff --check` passes and the final diff contains only intended migration changes.

Claude and Copilot runtime verification was unavailable during v2 preparation because Claude had no authenticated subscription available and Copilot CLI was not installed. Record those checks as deferred if the same limitation applies to the adopting project. Valid formats and references alone do not establish live model compliance.

## Record Adoption and Roll Out

After the migration is reviewed and accepted, record the adopted Delivery System version, source commit or release, migration date, verification results, and remaining limitations in the existing project overview or an equivalent project record. No new metadata file is required. Use `v2.0.0` only when that release is the version actually adopted; while working from an unreleased source, record its commit and unreleased status.

Use the project's established commit, review, publication, and deployment process only with the required authorization. Updating local instructions is not authorization to publish a new project release. Do not claim tool compatibility beyond the surfaces and versions actually verified.

If acceptance fails, retain the failure evidence and return only the migration changes to the previously captured state. Use the review branch or selective restoration supported by the team's process; do not use a blanket reset that discards unrelated work. Keep project knowledge and IDs intact, retain the prior adopted version record, and resolve the defect before rolling out again.
