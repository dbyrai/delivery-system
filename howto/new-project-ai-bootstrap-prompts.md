# New Project AI Bootstrap Prompts

This how-to shows how to start a new project with the Delivery System and an AI assistant through a short, structured interaction.

It is meant for users who want to try the workflow themselves with GitHub Copilot, ChatGPT Codex, Claude Code, or another AI coding assistant.

## What This Demonstrates

The Delivery System helps turn a rough project idea into:

- project context
- goals and non-goals
- requirements
- open questions
- a first spec
- a first implementation task
- acceptance criteria and verification steps

This does not replace product thinking, architecture decisions, security review, or testing. It gives the AI assistant enough structure to avoid jumping straight from idea to unverified code.

## Demo Idea

Use this simple project idea:

```text
Create a small internal task tracker for a team.

Users should be able to create tasks, assign an owner, set a status, and see open work.
The first version should be simple, local, and easy to verify.
```

## Starting Repository

Start from a repository that contains the Delivery System structure:

```text
team-task-tracker/
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
      requirements.md
      baseline/
    tasks/
    quality/
```

## Prompt 1: Start The Bootstrap

```text
I want to bootstrap a new project using this Delivery System.

Project idea:
Create a small internal task tracker for a team. Users should be able to create tasks,
assign an owner, set a status, and see open work. The first version should be simple,
local, and easy to verify.

Please read delivery-system.md and the existing docs structure first.
Then start the bootstrap sequence. Ask only for information that blocks the next step.
Record assumptions and open questions in docs instead of guessing.
```

Expected AI behavior:

- read `delivery-system.md`
- read the current `docs/` files
- mark existing-project review as not applicable because this is a new project
- identify missing project context
- ask focused questions only when needed

## Prompt 2: Provide Bootstrap Answers

```text
Use these bootstrap answers:

Goal:
Help a small team track work without introducing a heavy project management tool.

Users:
Team members and one team lead.

First version:
Local web app, no authentication, no external integrations.

Out of scope:
Notifications, comments, file attachments, billing, analytics, and mobile apps.

Success:
A user can create a task, update status, assign an owner, and filter open tasks.
```

Expected AI behavior:

- update `docs/project/overview.md`
- update `docs/specs/requirements.md`
- record non-goals and assumptions
- record authentication as out of scope for the first version
- avoid implementation until requirements and first task are clear

## Prompt 3: Create The First Spec And Task

```text
Create the first detailed spec and first implementation task for the smallest useful version.

Keep the task focused on one verifiable slice:
task list, create task, status update, and open-task filtering.

Include acceptance criteria and verification steps.
```

Expected AI behavior:

- create a spec under `docs/specs/`
- create a task under `docs/tasks/`
- link the task back to the spec or requirement IDs
- include acceptance criteria
- include verification commands or manual checks
- identify the responsible agent role

## Prompt 4: Implement Only After The Task Is Ready

```text
Now implement the first task only.

Follow the task acceptance criteria.
Keep the implementation small.
After implementation, run the relevant checks and report what changed.
```

Expected AI behavior:

- read the task file
- implement only the defined slice
- avoid unrelated features
- run available checks
- report changed files, verification, risks, and follow-up work

## Expected Result

After the bootstrap and first task creation, the repository may look like this:

```text
team-task-tracker/
  AGENTS.md
  delivery-system.md
  README.md
  package.json
  src/
  tests/
  docs/
    project/
      overview.md
      decisions.md
      roadmap.md
    specs/
      requirements.md
      001-task-tracking.md
      baseline/
    tasks/
      001-task-tracking-tasks.md
      artifacts/
    quality/
      dod-checklist.md
      test-strategy.md
      manual-tests/
```

## What To Check

Before accepting the result, check that:

- assumptions are written down
- open questions are visible
- the first task is small enough to verify
- acceptance criteria are concrete
- verification steps are present
- implementation did not start before the first task was ready
