# Delivery System

This repository can be used as a reusable starting point for new projects.

It provides a documentation structure, AI instruction files, role-based agent guidance, requirement templates, task templates, and quality checklists. The goal is to make every new project start with a clear source of truth instead of scattered notes.

## What This Delivery System Includes

- `AGENTS.md` - Codex entrypoint and repository-level AI guidance
- `.github/copilot-instructions.md` - Copilot-compatible AI instructions
- `.github/agents/` - role-specific agent instructions for GitHub Copilot, ChatGPT Codex, Claude Code, and other AI-assisted workflows
- `.claude/agents/` - Claude Code wrappers that delegate to the shared `.github/agents/` role guidance
- `docs/project/` - project overview, roadmap, and decisions
- `docs/specs/` - requirements and specification templates
- `docs/specs/baseline/` - global functional, non-functional, security, and acceptance requirements
- `docs/tasks/` - implementation task templates and task artifacts
- `docs/quality/` - Definition of Done, test strategy, and manual test structure

## Bootstrap Rules

Use this delivery system as a gated sequence, not as loose guidance.

- Complete the bootstrap steps in order.
- Do not start implementation work until the bootstrap sequence is complete or explicitly deferred by the project owner.
- Do not create implementation tasks from requirements or specs that still have unresolved open questions.
- Do not implement a task while that task has unresolved open questions.
- Record every explicit deferral in the relevant project, requirement, spec, task, decision, or question file.
- Treat `docs/` as the project source of truth after the bootstrap is complete.
- Keep `delivery-system.md` generic; write project-specific answers into `docs/`.

## How To Start A New Project

1. Copy this repository or folder structure into the new project.
2. Run the bootstrap sequence below from step 1 through step 12.
3. Stop at the first blocking open question.
4. Resolve or explicitly defer the question before continuing.
5. Start implementation only after the bootstrap sequence has a clear completed or deferred state.

## How To Adopt An Existing Project

The Delivery System can be added to an existing repository, but it should not be copied in blindly. Start with a short repository review so the bootstrap reflects the project that already exists.

Review:

- existing README files, docs, decision records, and issue/task conventions
- application, service, package, and library boundaries
- build, test, lint, type check, and deployment commands
- CI/CD configuration, environments, release process, and ownership
- security, privacy, data handling, and operational constraints
- current documentation gaps, risks, duplicated information, and open questions

Capture the result before running the bootstrap sequence. Use the review as input for `docs/project/overview.md`, `docs/project/decisions.md`, `docs/specs/requirements.md`, and the relevant quality files.

Example pre-bootstrap review note:

```text
docs/project/existing-repository-review.md
```

Suggested review outline:

```markdown
# Existing Repository Review

## Repository Shape

- Applications:
- Services:
- Shared packages:
- External integrations:

## Existing Source Of Truth

- Product context:
- Requirements:
- Architecture:
- Tasks:
- Quality:

## Commands

- Install:
- Build:
- Test:
- Lint:
- Deploy:

## Risks And Gaps

- Open questions:
- Missing documentation:
- Known delivery risks:
```

## Bootstrap Sequence

Before real project work starts, complete these steps in order. For existing projects, complete step 0 first. For brand-new projects, mark step 0 as not applicable and start at step 1.

### Step 0: Review Existing Repository Context

**Create or edit**: `docs/project/existing-repository-review.md` when adopting an existing project

**Required output**:

- Existing applications, services, packages, and ownership boundaries are identified.
- Current documentation, build commands, test commands, deployment process, and CI/CD configuration are reviewed.
- Known constraints, risks, documentation gaps, and open questions are captured.
- The bootstrap sequence uses the review result as input instead of replacing existing project knowledge.
- This step is explicitly marked as not applicable for brand-new projects.

### Step 1: Clean Copied Placeholders

**Edit**: all copied files as needed

**Required output**:

- Placeholder values marked with `TBD` are replaced, removed, or recorded as open questions.
- AI instruction files do not contain assumptions from another project.
- Any copied project-specific URLs, names, commands, credentials, or environment details are removed unless they belong to the new project.

### Step 2: Define Project Overview

**Edit**: `docs/project/overview.md`

**Required output**:

- Project purpose is defined.
- Goals and non-goals are documented.
- Stakeholders, owners, or decision makers are listed.
- Known constraints and assumptions are documented.
- Open questions are captured instead of guessed.

### Step 3: Define High-Level Requirements

**Edit**: `docs/specs/requirements.md`

**Required output**:

- High-level functional requirements are listed.
- High-level non-functional requirements are listed.
- Security, privacy, compliance, or policy expectations are listed.
- Requirements have stable IDs or clear labels.
- Open questions are captured and treated as blocking unless explicitly deferred.

### Step 4: Review Baseline Functional Requirements

**Edit**: `docs/specs/baseline/functional-requirements.md`

**Required output**:

- Applicable baseline functional requirements are kept and adjusted for the project.
- Non-applicable baseline requirements are removed or explicitly marked as not applicable.
- Missing functional baseline requirements are added.

### Step 5: Review Baseline Non-Functional Requirements

**Edit**: `docs/specs/baseline/non-functional-requirements.md`

**Required output**:

- Performance, reliability, maintainability, accessibility, and operational expectations are reviewed.
- Non-applicable expectations are removed or explicitly marked as not applicable.
- Any measurable targets that are known at bootstrap time are documented.

### Step 6: Review Security And Policy Baseline

**Edit**: `docs/specs/baseline/security-policy.md`

**Required output**:

- Authentication, authorization, data handling, secrets, privacy, and compliance expectations are reviewed.
- Unknown security or policy requirements are captured as open questions.
- No implementation task is created for a security-sensitive area while its policy questions are unresolved.

### Step 7: Review Baseline Acceptance Criteria

**Edit**: `docs/specs/baseline/acceptance-criteria.md`

**Required output**:

- Global acceptance expectations are clear enough to verify.
- Project-specific acceptance gates are added where known.
- Ambiguous acceptance expectations are rewritten or captured as open questions.

### Step 8: Define Initial Roadmap

**Edit**: `docs/project/roadmap.md`

**Required output**:

- Initial milestones, phases, or delivery slices are documented.
- Dependencies and sequencing constraints are listed.
- Work that is intentionally out of scope for the first phase is documented.

### Step 9: Review Quality Standards

**Edit**: `docs/quality/dod-checklist.md` and `docs/quality/test-strategy.md`

**Required output**:

- Definition of Done is reviewed for the project.
- Test strategy has at least an initial direction.
- Expected automated, manual, and acceptance checks are documented where known.
- Known verification gaps are captured.

### Step 10: Review Agent Roles And Tool Targets

**Edit**: `.github/agents/` as needed

**Required output**:

- Roles that fit the project are kept.
- Roles that do not fit are removed, adjusted, or explicitly left for future use.
- Agent guidance is reviewed for GitHub Copilot, ChatGPT Codex, Claude Code, and any other AI tool expected to use the repository.
- Global agent guidance remains product-neutral unless the project overview and scope require more specific role behavior.
- Project-specific agent adjustments match `docs/project/overview.md`, including goals, non-goals, ownership, terminology, and delivery boundaries.
- Any project-specific role guidance is written without duplicating project facts that belong in `docs/`.

### Step 11: Create The First Detailed Spec

**Create from**: `docs/specs/template.md`

**Required output**:

- First spec is created or explicitly deferred.
- The spec references relevant high-level requirements.
- Goals, non-goals, acceptance criteria, dependencies, risks, and open questions are documented.
- The spec is not used for task creation until blocking open questions are resolved or explicitly deferred.

### Step 12: Create The First Task File

**Create from**: `docs/tasks/template.md`

**Required output**:

- First task file is created or explicitly deferred.
- Tasks link back to the source spec or requirement.
- Each task has acceptance criteria and verification expectations.
- The responsible role or agent is identified.
- No task is marked ready while it has unresolved blocking questions.

## Bootstrap Completion Check

The bootstrap is complete only when all of the following are true:

- [ ] Step 0 is completed for existing projects or explicitly marked as not applicable for new projects.
- [ ] Steps 1 through 12 are completed or explicitly deferred.
- [ ] All blocking open questions are resolved or explicitly deferred.
- [ ] Deferrals are recorded in the relevant source files.
- [ ] The initial project source of truth lives in `docs/`.
- [ ] The first implementation task is either ready with clear acceptance criteria or intentionally deferred.
- [ ] Quality and verification expectations are clear enough for the first implementation task.

## Creating Specs

Create one spec file per meaningful feature, project area, or workstream.

Use:

```text
docs/specs/template.md
```

Recommended naming:

```text
docs/specs/001-project-foundation.md
docs/specs/010-authentication.md
docs/specs/020-dashboard.md
```

Good specs should describe:

- Problem
- Goals
- Non-goals
- Functional requirements
- Non-functional requirements
- Security and policy requirements
- Acceptance criteria
- Dependencies
- Risks
- Open questions

## Creating Tasks

Start with one task file per spec.

Use:

```text
docs/tasks/template.md
```

Recommended naming:

```text
docs/tasks/001-project-foundation-tasks.md
docs/tasks/010-authentication-tasks.md
docs/tasks/020-dashboard-tasks.md
```

Split into one file per task only when tasks become large, long-lived, independently owned, or need separate artifacts.

## Existing Project Layout Example

For an existing single-project repository, add the Delivery System around the current application structure:

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
      existing-repository-review.md
      decisions.md
      roadmap.md
    specs/
      requirements.md
      baseline/
    tasks/
      artifacts/
    quality/
      dod-checklist.md
      test-strategy.md
      manual-tests/
```

## Monorepo Layout Example

For a monorepo, keep shared delivery guidance at the root and give each independently delivered subproject its own `docs/` structure.

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
    specs/
    tasks/
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

Use root-level `docs/` for shared project context, cross-cutting decisions, platform-level requirements, security expectations, and global quality standards. Use subproject-level `docs/` for local goals, requirements, tasks, acceptance criteria, and delivery evidence.

## Using Task Artifacts

Use `docs/tasks/artifacts/` for supporting information that should not clutter the main task file.

Examples:

- Screenshots
- Logs
- Test evidence
- Export notes
- Research notes
- Data samples
- External references

Do not store secrets or sensitive data in artifacts.

## Using Manual Tests

Use:

```text
docs/quality/manual-tests/
```

for repeatable manual verification steps.

Only create a top-level `docs/manuals/` directory if the project needs user manuals, admin guides, runbooks, or operational handbooks that are not QA test cases.

## AI Usage Guidance

For ChatGPT Codex:

- Start from `AGENTS.md`.
- Then read the relevant files under `docs/`.
- Use `.github/agents/` for role-specific behavior.

For GitHub Copilot:

- Use `.github/copilot-instructions.md`.
- Keep project-specific knowledge in `docs/`.

For Claude Code:

- Start from `CLAUDE.md`.
- Use `.claude/agents/` only as wrappers.
- Keep `.github/agents/` as the shared source for role guidance.

For all AI tools:

- `docs/` is the project source of truth.
- Keep agents global unless the project overview and scope require project-specific behavior.
- Do not let copied assumptions from a previous project remain in instruction files.
- If a project detail is unknown, document it as an open question instead of guessing.

## When To Customize The Delivery System

Customize this structure when:

- The project has no software implementation and only needs documentation.
- The project has strict compliance requirements.
- The project has many independent teams or workstreams.
- The project needs separate product, design, operations, or support documentation.
- The project uses a specific delivery process that needs its own templates.

Keep the structure simple until the project needs more detail.
