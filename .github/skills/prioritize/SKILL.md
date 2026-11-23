---
name: prioritize
description: Re-prioritize roadmap items, specs, or backlog using MoSCoW with explicit user confirmation. Use when the user asks to prioritize, reorder the roadmap or backlog, or compare the importance of features.
---

# Prioritize

Act as the Product Manager (`.github/agents/product-manager.agent.md`).

## 1. Inventory

Read the roadmap, the specs in scope with their status and priority, and the changelog if the project keeps one. Present the inventory from `.github/skills/prioritize/template.md`, grouped by current priority, and flag blocked or at-risk items.

## 2. Evaluate

For each item or group the user wants to focus on, clarify:

| Question | Purpose |
| --- | --- |
| What breaks without this? | Identifies Must |
| Is there a workaround? | Separates Must from Should |
| What is the user impact? | Ranks Should against Could |
| What is the effort or risk? | Informs tradeoffs |
| What depends on it? | Reveals sequencing constraints |

Ask focused questions with a recommended answer for each.

## 3. Propose

Present the proposal from `.github/skills/prioritize/template.md` with a rationale per item. Flag dependencies and be honest when there are more Musts than available capacity.

## 4. Apply

Only after explicit user confirmation: update the `Priority` field of affected specs and the roadmap order, then summarize what changed.

## Rules

- Never change priorities or the roadmap without explicit user confirmation.
- Give a rationale for every proposed change.
- Do not reprioritize delivered items.
