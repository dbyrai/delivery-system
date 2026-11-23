---
inclusion: always
---

# Kiro Repository Instructions

Read and follow the shared project instructions referenced below. They define the workflow, optional diagnostics, role selection, and work boundaries for this repository.

#[[file:.github/copilot-instructions.md]]

Kiro-specific wrappers live in `.kiro/agents/` and `.kiro/skills/`. Each delegates to its source in `.github/agents/` or `.github/skills/` and must not duplicate that guidance.

The project's documentation root (normally `docs/`) remains the source of truth for specs and tasks. Use Kiro-native specs under `.kiro/specs/` only when the project records that decision, and link them to the corresponding spec in the documentation root.

Keep cross-tool rules in `.github/copilot-instructions.md`; keep this steering file limited to Kiro-specific routing.
