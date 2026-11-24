# Claude Repository Instructions

Read and follow the shared project instructions imported below. They define the workflow, optional diagnostics, role selection, and work boundaries for this repository.

@.github/copilot-instructions.md

Claude-specific agent wrappers live in `.claude/agents/`. Each wrapper delegates to the corresponding source file in `.github/agents/` and must not duplicate role guidance. Skill wrappers in `.claude/skills/` delegate the same way to `.github/skills/`.

Keep cross-tool rules in `.github/copilot-instructions.md`; keep this entry file limited to Claude-specific routing.
