# Codex Repository Instructions

Read and follow the shared project instructions in `.github/copilot-instructions.md`. They define the workflow, optional diagnostics, role selection, and work boundaries for this repository.

Use `.github/agents/` as the shared source for role guidance. Files under `.codex/agents/` are tool-specific wrappers and must not duplicate that guidance. Skill wrappers under `.agents/skills/` delegate the same way to `.github/skills/`.

Keep cross-tool rules in `.github/copilot-instructions.md`; keep this entry file limited to Codex-specific routing.
