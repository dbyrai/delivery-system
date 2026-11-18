# Role Index

Use this index to select one primary owner under the [shared workflow](../copilot-instructions.md#task-routing-and-context-loading). Read only the selected role file; add another role only for an actual handoff or bounded collaboration. Tool adapters register roles and refer to these profiles; they do not own global rules.

| Role | File | Responsibility |
| --- | --- | --- |
| project-manager | [project-manager.agent.md](project-manager.agent.md) | Planning, readiness, task sequencing, dependencies, and delivery status |
| technical-lead | [technical-lead.agent.md](technical-lead.agent.md) | Architecture, cross-role decisions, integration review, and readiness |
| devops-engineer | [devops-engineer.agent.md](devops-engineer.agent.md) | Environments, infrastructure, pipelines, releases, and recovery |
| backend-developer | [backend-developer.agent.md](backend-developer.agent.md) | APIs, data models, authentication/authorization, and integrations |
| frontend-developer | [frontend-developer.agent.md](frontend-developer.agent.md) | UI, routing, accessibility, client state, and API integration |
| qa-engineer | [qa-engineer.agent.md](qa-engineer.agent.md) | Acceptance evidence, integration tests, and regression checks |
| security-reviewer | [security-reviewer.agent.md](security-reviewer.agent.md) | Explicitly requested independent, read-only security reviews |
| content-editor | [content-editor.agent.md](content-editor.agent.md) | Content structure, terminology, metadata, and documentation quality |

For mixed work, choose the role owning the main deliverable and identify any required handoff. Keep architecture decisions with the Technical Lead, implementation with its developer/operations owner, and verification evidence with QA when a separate review is required. This routing does not authorize spawning agents; the shared delegation rules apply.

Task formats and IDs belong to [task documentation](../../docs/tasks/README.md); source requirements and project facts belong in the existing project documentation. Do not repeat templates or global policies in role files. Record a concise handoff with completed scope, affected paths, verification, unresolved items, risks, and next owner when work changes hands.
