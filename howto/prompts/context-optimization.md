# Context Optimization Migration Prompt

## Use

Use this prompt for an existing repository after reading the [context optimization guide](../context-optimization.md) and the [v1 to v2 upgrade guide](../upgrades/v1-to-v2.md). New projects already receive the v2 structure and do not need a separate optimization pass.

Make these guides and the v2 instruction files available in the target workspace. If their paths differ, adjust the references in the prompt before use. Run the prompt from the target repository; it does not authorize changes to a source template or another project.

## Prompt

```text
Migrate this repository's Delivery System instructions to the v2 context-loading
structure described in howto/context-optimization.md and
howto/upgrades/v1-to-v2.md.

Read the applicable repository instructions and these two guides first. Check
git status and preserve all existing user changes. Identify the adopted v1
baseline, target v2 source, existing documentation roots, project-specific
constraints, custom roles, and diagnostic default. If a required source is
missing or conflicting, ask one focused question before dependent changes.

Use .github/copilot-instructions.md as the canonical shared source for workflow,
source precedence, language, approvals, diagnostics, and work boundaries.
Keep AGENTS.md as a thin reference and CLAUDE.md as a native import of that
shared file. Do not move the common workflow into AGENTS.md or duplicate it
between the entry points.

Follow the canonical routing table. Load project context, delivery-handbook
sections, specs, tasks, architecture, and quality documents only when relevant
to the classified task. Always follow applicable linked questions, security
requirements, acceptance criteria, and verification gates. Less context is an
optimization goal; it does not justify skipping a required source or promise
that a particular model context window will suffice.

Select one primary role from the role index and read that role's profile.
Selecting a role must not automatically create a subagent. Keep shared role
profiles focused on role-specific rules with name and description metadata.
Keep .codex/agents/*.toml and .claude/agents/*.md limited to registration
metadata and a reference to the corresponding .github/agents/*.agent.md.
Preserve custom roles and tool-specific restrictions.

Compare the target repository, its adopted baseline, and the v2 source before
editing. Apply only the agreed instruction and guide changes. Do not copy the
template docs tree over completed project documents, rename existing task IDs,
move documentation roots, weaken security or approval gates, or remove a
project rule merely because it is duplicated. Identify the canonical owner
and preserve the rule there before removing a duplicate.

Preserve existing Delivery diagnostics: on/off behavior, any explicit persistent
default, chat overrides, and task-only override semantics. Use the compact
early diagnostic block only when enabled and report only sources actually
loaded. Guides should explain and link canonical rules rather than maintain
another authoritative copy.

Measure relevant file sizes before and after migration. Validate local links,
heading anchors, import targets, YAML frontmatter, and TOML adapters with
available tools. Run git diff --check. Review a fresh-project bootstrap path
and an existing-project migration path in a disposable copy, checking that
project rules, documentation, IDs, diagnostic settings, and blocking gates
survive. Confirm that ordinary read-only requests do not trigger blanket
loading of the handbook and unrelated project context.

Do not install tools, change authentication, or claim live model compatibility
from static checks. If Claude or Copilot runtime tests are unavailable, record
the exact limitation and leave those checks explicitly deferred.

Record the adopted version and migration verification in an existing project
overview or equivalent project record; do not invent a new required metadata
file. Report changed files, rule ownership, size comparison, checks and
results, preserved customizations, and remaining limitations. Explain how to
restore only migration changes if acceptance fails, preserving unrelated work.

Do not commit, push, tag, publish, or begin a follow-up task. Leave the result
reviewable for the project owner.
```
