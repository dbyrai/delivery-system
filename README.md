# dbyrai Delivery System

dbyrai helps software teams move from vibe coding to structured AI engineering with a verifiable Delivery System.

This repository exists to make AI-assisted software work more durable, reviewable, and repeatable. It provides a reusable project structure for capturing context, requirements, tasks, agent roles, quality expectations, and delivery evidence before AI-generated output is treated as finished software.

## Why This Repository Exists

AI can make exploration and prototyping much faster. That speed is useful, but long-lived software needs more than prompt output. Teams still need clear goals, explicit scope, reviewable decisions, acceptance criteria, testing expectations, and a shared source of truth.

The Delivery System gives humans and AI agents a common operating model:

- capture project context before implementation starts
- define goals, non-goals, requirements, and open questions
- turn requirements into scoped tasks with ownership and verification steps
- use role-specific agent guidance for frontend, backend, QA, DevOps, project management, and content work
- keep acceptance evidence, risks, and decisions close to the work

In short: this repo is the working structure behind dbyrai's approach to structured AI engineering.

## Website

Official website: [dbyrai.com](https://dbyrai.com)

The public website explains the product story: moving from vibe coding to verifiable software delivery through a structured Delivery System.

## What Is Included

- `AGENTS.md` - Codex entrypoint and repository-level AI guidance
- `.github/copilot-instructions.md` - project instructions for AI assistants
- `.github/agents/` - role-specific guidance for GitHub Copilot, ChatGPT Codex, Claude Code, and other AI-assisted project workflows
- `.claude/agents/` - Claude Code wrappers that delegate to the shared `.github/agents/` role guidance
- `delivery-system.md` - bootstrap process for starting a new project from this structure
- `docs/project/` - project overview, roadmap, and decisions
- `docs/specs/` - requirements and specification templates
- `docs/specs/baseline/` - baseline functional, non-functional, security, and acceptance requirements
- `docs/tasks/` - implementation task templates and task artifacts
- `docs/quality/` - Definition of Done, test strategy, and manual test structure
- `addons/` - optional MCP adapters, configuration helper, and AI prompts for external delivery tools
- `howto/` - optional walkthroughs and prompt examples for trying the Delivery System

The agents are intentionally kept global. They describe stable role behavior instead of assuming a specific product, architecture, or delivery process. During project bootstrap, review the agents against the project overview and scope. Keep them generic when possible, but adapt them when a project needs clearer ownership, terminology, or workflow rules.

## Intended Users

This repository is intended for:

- developers using AI coding tools in real software projects
- technical founders who want faster delivery without losing engineering discipline
- teams that need requirements, tasks, reviews, and quality gates to remain visible
- AI agents and assistants that need structured project context before making changes

## Core Workflow

1. Clarify the intent.
   Capture the product goal, boundaries, assumptions, and acceptance criteria.

2. Shape the delivery system.
   Convert the idea into requirements, tasks, role guidance, handoffs, quality checks, and documentation structure.

3. Guide AI work.
   Use agent roles and project instructions so every AI-assisted change has context, ownership, and review expectations.

4. Verify the result.
   Treat builds, tests, acceptance evidence, and open risks as part of delivery.

## Getting Started

Start with the bootstrap guide:

```text
delivery-system.md
```

Then work through the project source of truth:

```text
docs/project/overview.md
docs/specs/requirements.md
docs/project/roadmap.md
docs/quality/dod-checklist.md
docs/quality/test-strategy.md
```

When using this repository as a template, keep project-specific knowledge in `docs/` and keep implementation work gated by unresolved open questions.

For a practical walkthrough, see:

```text
howto/new-project-ai-bootstrap-prompts.md
```

## Shared AI Instructions

Maintain common workflow rules in [`.github/copilot-instructions.md`](.github/copilot-instructions.md) and role guidance in [`.github/agents/`](.github/agents/README.md). Tool-specific entry files route to these shared sources so changes do not need to be copied between tools.

| Tool | Entry point | Shared instructions |
| --- | --- | --- |
| Codex | `AGENTS.md` | Explicit instruction to read `.github/copilot-instructions.md` |
| Claude Code | `CLAUDE.md` | Imports `.github/copilot-instructions.md` using `@` syntax |
| GitHub Copilot | `.github/copilot-instructions.md` | Uses the shared file directly on supported surfaces with repository instructions enabled |

The files in `.claude/agents/` and `.codex/agents/` reference the same role profiles. Global rules come from the tool entry points and repository instructions rather than being repeated in each adapter. Other assistants need access to these files and an entry instruction to read them. For a web chat without repository access, supply the shared instructions and relevant project files as context. Verify instruction loading in each tool; these documents guide model behavior and are not an enforcement mechanism.

## Context-Aware Workflow in v2

The default [shared instructions](.github/copilot-instructions.md#task-routing-and-context-loading) classify the task before loading project documents. The full bootstrap handbook, overview, baselines, and all roles are no longer mandatory reading for every request. Linked blockers, security requirements, acceptance criteria, and authorization gates remain binding.

- New projects use the optimized instructions directly; no separate optimization prompt is needed.
- Read [Context Optimization](howto/context-optimization.md) for file responsibilities and focused loading examples.
- Use the [migration prompt](howto/prompts/context-optimization.md) to adapt an existing repository, preserving its local rules.
- Existing v1 adopters should follow the [v1-to-v2 upgrade guide](howto/upgrades/v1-to-v2.md). This is a workflow migration, not a bulk replacement of completed project documents.

Reducing unnecessary context is a goal, not a guarantee for a particular context-window size or model. Tool-specific instruction support varies; inspect the active client and distinguish static checks from live verification.

## Optional Integration Add-ons

Use the [add-on guide](addons/README.md) to select Jira, Confluence, GitHub Projects,
or GitLab adapters and a copyable AI adaptation prompt. Setup configures and
verifies MCP in the actual client; copying files alone establishes no connection.
Adapters require visible stable IDs and native ticket/task hierarchy. Their
instructions are loaded only for the selected integration.
Project-specific decisions and durable operating rules stay in the project's
existing documentation root.

The optional [Matt Pocock skills add-on](addons/mattpocock-skills/README.md)
offers a [selection prompt](addons/mattpocock-skills/integration-prompt.md)
for project-local debugging, TDD, and decision-clarification methods. Its
activation creates a single integration entry for task-based method selection.

The optional [Security add-on](addons/security/README.md) provides a skill catalog,
project-local activation for software and infrastructure reviews, and a shared
Security Reviewer role with adapters for Codex and Claude Code.

The optional [Manus add-on](addons/manus/README.md) guides direct development
in Manus with a GitHub project repository. It covers adopting existing projects
and bootstrapping new ones, then implementing approved specs and tasks. The
[Manus how-to](addons/manus/howto.md) includes setup prompts and a
[graphical workflow](addons/manus/workflow.md). No external Manus API is required;
actual repository access and instruction loading must be verified in Manus.

The optional [Kiro workflow add-on](addons/kiro/README.md) supplies an opt-in
steering template and maps Kiro-native specs to authoritative project documents.
It installs no root `.kiro/` files until explicitly activated.

Existing v2.0 projects can follow the [v2.1 adoption guide](howto/upgrades/v2.0-to-v2.1.md).
Adoption is optional. Users can delete individual add-ons or the entire `addons/`
directory and remove associated links; see the [removal instructions](addons/README.md#removing-instruction-files).
Deleting instructions does not disable an already configured external connection.

## Optional Delivery Diagnostics

When following the [shared AI instructions](.github/copilot-instructions.md#optional-diagnostic-gate), you can enable a compact diagnostic block showing the task type, selected role and role file, project sources actually loaded, and planned subagent count. It is emitted after routing and before detailed analysis; documents are not loaded merely to fill its fields. Diagnostic output is **off by default**. Reading, review, and approval obligations still apply when the block is hidden.

Send either instruction in the chat:

```text
Delivery diagnostics: on
```

```text
Delivery diagnostics: off
```

The latest explicit choice applies for the rest of that chat until changed. To limit it to one task, say “Delivery diagnostics: on for this task only”; the previous setting resumes afterward. These are natural-language instructions for the agent, not terminal commands or an application setting.

For a persistent project default, change `Delivery diagnostics default: off` to `Delivery diagnostics default: on` in `.github/copilot-instructions.md`. Chat instructions override that default without modifying files and do not automatically carry over to other chats.

## Adoption Paths

The Delivery System can be used in two ways:

- for a new project, by starting from this repository structure before implementation begins
- for an existing project, by adding the structure after a short repository review

For existing projects, do a pre-bootstrap review before copying or adapting files. The goal is to understand the current repository shape, not to rewrite it. Review the existing README, architecture notes, package layout, build commands, test setup, deployment files, ownership boundaries, and any current documentation. Capture the result in `docs/project/overview.md`, `docs/project/decisions.md`, or a dedicated review note before starting the bootstrap sequence.

Example review flow:

```text
1. Inspect repository structure and identify applications, packages, services, and shared libraries.
2. Read existing README, docs, CI configuration, package manifests, and deployment files.
3. Identify current source-of-truth files and documentation gaps.
4. Record known goals, constraints, risks, commands, owners, and open questions.
5. Start the Delivery System bootstrap using that review result as input.
```

Example layout for an existing single-project repository:

```text
existing-product/
  src/
  tests/
  package.json
  README.md
  AGENTS.md
  delivery-system.md
  .github/
    copilot-instructions.md
    agents/
  .claude/
    agents/
  docs/
    project/
      overview.md
      decisions.md
      roadmap.md
    specs/
    tasks/
    quality/
```

## Monorepo Adoption

The Delivery System can also be integrated into a large monorepo with multiple subprojects. In that case, keep shared repository-wide guidance at the root and give each independently delivered subproject its own `docs/` structure.

Example monorepo layout:

```text
company-platform/
  AGENTS.md
  delivery-system.md
  .github/
    copilot-instructions.md
    agents/
  .claude/
    agents/
  docs/
    project/
      overview.md
      decisions.md
      roadmap.md
    quality/
  apps/
    customer-web/
      src/
      docs/
        project/
        specs/
        tasks/
        quality/
    admin-portal/
      src/
      docs/
        project/
        specs/
        tasks/
        quality/
  services/
    billing-api/
      src/
      docs/
        project/
        specs/
        tasks/
        quality/
    notification-worker/
      src/
      docs/
        project/
        specs/
        tasks/
        quality/
  packages/
    ui/
    config/
```

Use the root `docs/` for shared product, architecture, security, and delivery decisions. Use each subproject's `docs/` for local requirements, tasks, acceptance criteria, and verification evidence.

## Current Status

This repository currently contains the Delivery System structure, templates, baseline documentation, and AI agent guidance. Project-specific requirements are still being defined in the documentation files.

Some documentation files intentionally contain `TBD` placeholders. They mark project-specific fields that should be filled, removed, or recorded as open questions during project bootstrap.

## Documentation Principles

- `docs/` is the source of truth for project knowledge.
- Open questions must be recorded instead of guessed.
- Requirements should be linked to specs and tasks.
- Tasks should include acceptance criteria and verification expectations.
- Decisions should be recorded once and linked where needed.
- Quality checks and delivery evidence should be part of the normal workflow.

## Relationship To dbyrai

dbyrai is the product layer around this Delivery System. The repository documents the operating model; the website explains the public positioning and value proposition.

The goal is not to reject fast AI-assisted exploration. The goal is to make the next step practical: turning AI-assisted work into software that can be reviewed, maintained, and shipped with confidence.

## Maintaining This Repository

The [maintainer release workflow](.github/maintainers/releasing.md) describes branches, reviews, versioning, and GitHub releases for the original Delivery System repository. It applies only to maintaining this upstream repository and introduces no release requirements for projects adopting the template.

Upstream helper tests, live adapter acceptance reports, and their evidence belong under `.github/maintainers/`. They are not application tests or project documentation for adopting projects.

When using this repository as a template, you can remove the upstream maintainer files. From the root of your new project, run this command in a POSIX shell (such as Bash or Zsh):

```sh
rm -r -- .github/maintainers
```

This deletes only upstream maintainer documentation, tests, and acceptance evidence. Keep `.github/agents/` and `.github/copilot-instructions.md` for the Delivery System. After removing the directory, remove this README section as well so its link does not point to a deleted file.

## License

This project is licensed under the [Apache License 2.0](LICENSE.md).
