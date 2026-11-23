---
name: bootstrap
description: Walk through the Delivery System bootstrap sequence (steps 0-12) interactively, one step at a time, stopping at blocking open questions. Use when the user asks to bootstrap, set up, or adopt the Delivery System for a new or existing project.
---

# Bootstrap

Orchestrate the bootstrap sequence in `delivery-system.md`. That handbook defines the steps, required outputs, gates, and completion check; this skill only sequences the interaction and does not replace it.

Primary role: Product Manager for project definition (overview, requirements, roadmap, acceptance); involve the Technical Lead for stack and architecture questions. Load the role files only when acting in that role.

## Start

1. Check the working tree and whether a bootstrap was already completed. Do not rerun completed steps or replace completed documents; continue at the first open or deferred step.
2. Ask whether this is a brand-new project or an existing repository. For an existing repository, run Step 0 and write the review note described in `delivery-system.md`. For a new project, record Step 0 as not applicable.
3. Confirm the repository shape (single project or monorepo, documentation root) and which AI tools will use it.

## Each Step

1. Name the step and its target files.
2. Read the step's required output in `delivery-system.md` and the current target files.
3. Ask one focused question at a time for unknown facts. Present viable options with tradeoffs and a recommendation when a decision is needed.
4. Draft the content and show it to the user before writing.
5. Check every required-output bullet. If a blocking question remains, record it in the target file and stop until the user resolves or explicitly defers it.
6. Write the confirmed content and continue with the next step.

## Completion

When the user considers the bootstrap finished, report the status of each item in the handbook's completion check honestly. List unmet and deferred items. Do not declare completion while a blocking item is open. Point to the `spec` or `new-feature` skill for the next detailed spec.

## Rules

- Never guess project facts; ask or record an open question or deferral.
- Write project-specific answers into the documentation root; keep `delivery-system.md` generic.
- Repository deliverables follow the shared language policy.
- Do not start implementation during bootstrap.
