# AI Agent Roles

This directory defines role-specific operating instructions for AI agents working in this repository.

Use these files as scoped role prompts. They are not standalone project plans; they complement the repository specs, task files, and `.github/copilot-instructions.md`.

Claude subagent wrappers may live in `.claude/agents/`, but they should only delegate to these `.github/agents/*.agent.md` files instead of duplicating role guidance.

## Tool Integration

| Tool | Config Location | Notes |
| --- | --- | --- |
| Kiro | `.kiro/steering/`, `.kiro/specs/` | Spec-driven workflow (requirements → design → tasks) |
| GitHub Copilot / Codex | `.github/copilot-instructions.md` | Project instructions |
| Claude Code | `.claude/agents/` | Wrappers delegating to `.github/agents/` |

## Available Agents

| Agent | File | Primary Ownership |
| --- | --- | --- |
| Project Manager | `project-manager.agent.md` | Planning, sequencing, stakeholder communication, task breakdown |
| Technical Lead | `technical-lead.agent.md` | Architecture, technical decisions, review, risk management |
| DevOps Engineer | `devops-engineer.agent.md` | Infrastructure, environments, deployment, operations |
| Backend Developer | `backend-developer.agent.md` | Backend services, APIs, data models, integrations |
| Frontend Developer | `frontend-developer.agent.md` | Frontend application, UI behavior, routing, client-side integration |
| QA Engineer | `qa-engineer.agent.md` | Integration tests, acceptance verification, regression checks |
| Content Editor | `content-editor.agent.md` | Content structure, editorial quality, metadata, documentation review |

## How To Select An Agent

1. Identify the dominant work area.
2. Select the agent whose ownership best matches that area.
3. If the work crosses roles, keep one primary owner and list collaborators.
4. Use the Technical Lead for architectural decisions, cross-role conflicts, and final technical approval.
5. Use the Project Manager for sequencing, task creation, dependency tracking, and stakeholder-ready summaries.

All tools share this agent role guidance.
When working in Kiro spec-driven mode:
- Tasks derive from specs in `.kiro/specs/` or `docs/specs/`.
- Follow the spec's requirements and design before implementing.
- Mark tasks complete only when acceptance criteria are met.
- Reference the source spec when reporting completion.

## Typical Ownership

| Work Area | Primary Agent | Required Collaboration |
| --- | --- | --- |
| Infrastructure and local environments | DevOps Engineer | Technical Lead, QA Engineer |
| Deployment and operations | DevOps Engineer | Technical Lead, Project Manager |
| Backend services and APIs | Backend Developer | Frontend Developer, Technical Lead |
| Data models and integration contracts | Backend Developer | Frontend Developer, Content Editor |
| Frontend application and UI behavior | Frontend Developer | QA Engineer, Technical Lead |
| Client-side integration | Frontend Developer | Backend Developer, QA Engineer |
| Testing and acceptance verification | QA Engineer | Frontend Developer, Technical Lead |
| Content and documentation quality | Content Editor | Project Manager, Technical Lead |
| Project sequencing and reporting | Project Manager | All agents |

## Standard Agent Workflow

Each agent should:

1. Read the relevant specs, tasks, and current files before acting.
2. Confirm scope, assumptions, dependencies, and non-goals.
3. Make the smallest useful change that satisfies the task.
4. Verify the result with appropriate commands or review checks.
5. Provide a concise handoff with changed files, verification, risks, and next steps.

When creating or updating task files, keep a `Task-Reihenfolge` table near the top with the columns `Task`, `Titel`, `Owner`, `Status`, and `Blocker`.

## Handoff Format

Use this format when transferring work between roles:

```markdown
## Handoff

**From**: [Agent]
**To**: [Agent]
**Scope Completed**: [Brief summary]
**Files/Artifacts**: [Paths or links]
**Verification**: [Commands/checks performed]
**Open Items**: [Known gaps or decisions needed]
**Risks**: [Relevant risks, if any]
```

## Guardrails

- Do not invent requirements that are not present in specs, tasks, or user instructions.
- Do not expand scope without calling it out.
- Do not overwrite another role's deliverables without reviewing their current content.
- Do not treat generated examples as verified facts.
- Do not mark work complete unless acceptance criteria and verification are clear.
