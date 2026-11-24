---
name: new-feature
description: Take a raw feature idea through discovery and requirement clarification to a reviewed spec draft. Use when the user describes a new feature idea, asks for a new capability, or wants to explore requirements before a spec exists.
---

# New Feature

Act as the Product Manager (`.github/agents/product-manager.agent.md`). Use the `spec` skill instead when requirements are already clear.

## 1. Understand the Idea

Ask the user to describe the idea and identify the problem, affected users or roles, and what success looks like. Read the roadmap and related specs to position the feature. Do not assume requirements.

## 2. Clarify Requirements

Work through open decisions until none remain unresolved or undeferred. Cover at least:

1. Scope boundaries: what is in, what is explicitly out.
2. Affected users and roles.
3. Edge cases and failure behavior.
4. Dependencies on existing features, contracts, or decisions.
5. Security, privacy, and policy impact.
6. Priority for this iteration (Must, Should, Could, Won't).

Use the clarification rounds in `.github/skills/_shared/clarification-rounds.md`. If the optional `grill-me` method is active and the user wants a deeper interview, use it instead. Flag unclear technical feasibility as an open question for the Technical Lead.

## 3. Draft the Spec

Create the spec from `docs/specs/template.md` (or the project's equivalent) following the naming in `docs/specs/README.md`. Fill every section from the clarified answers, set status `Draft`, tag requirements with their priority, and keep remaining questions visible under Open Questions.

## 4. Review

Present the draft and ask whether it captures the intent, whether priorities are right, and what is missing. Iterate until the user confirms. Change the status to `In Review` or `Approved` only on explicit user confirmation.

## 5. Handoff

When the spec is approved and has no blocking questions, offer a handoff to the Project Manager for task breakdown.

## Rules

- Distinguish confirmed scope from your recommendations.
- Never invent requirements, business rules, or user flows.
- Do not create tasks or implement anything in this workflow.
