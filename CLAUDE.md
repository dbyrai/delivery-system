# Claude Repository Instructions

Use `.github/copilot-instructions.md` as the primary project instruction file.

Claude-specific agent wrappers live in `.claude/agents/`, but they must not duplicate role guidance. Each wrapper delegates to the corresponding source file in `.github/agents/`.

For bootstrapping a new project from this structure, read `delivery-system.md` first.

Role-specific guidance lives in `.github/agents/`:

Use `.github/agents/README.md` as the role index, then read the relevant `.github/agents/*.agent.md` file before editing.

Keep changes scoped to the requested task.
