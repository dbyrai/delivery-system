---
name: spec
description: Write a specification directly when requirements are already clear, skipping discovery. Use when the user asks to write a spec or has already clarified the requirements.
---

# Spec

Act as the Product Manager (`.github/agents/product-manager.agent.md`). Use the `new-feature` skill instead when the idea still needs exploration.

## 1. Gather Input

Confirm what should be specified and whether open questions remain. If important questions are unresolved, recommend `new-feature`; if the user wants to proceed anyway, keep them visible under Open Questions as blocking unless explicitly deferred.

## 2. Write

1. Determine the next spec number from the existing files and the naming in `docs/specs/README.md`.
2. Create the spec from `docs/specs/template.md` (or the project's equivalent).
3. Fill all sections from the user's input and link relevant requirements and baseline documents.
4. Set status `Draft`, tag requirements with their priority, and list dependencies and risks.

## 3. Review

Present the spec, highlight assumptions, and ask whether priorities are correct and anything is missing. Iterate until the user confirms. Change the status only on explicit user confirmation.

## 4. Handoff

Once approved without blocking questions, offer a handoff to the Project Manager for task breakdown.

## Rules

- Never invent requirements; ask when something is unclear.
- Reference the roadmap to position the feature.
- Do not create tasks or implement anything in this workflow.
