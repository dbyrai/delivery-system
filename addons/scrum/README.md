# SCRUM Add-on

Use this optional add-on when a project works in sprints with story-point estimation, readiness gates, and velocity tracking. The core Delivery System stays process-neutral; this add-on adds those rules as one project record plus skills.

## Contents

| Path | Activated as |
| --- | --- |
| [record.md](record.md) | `<docs-root>/project/integrations/scrum.md`: team decisions, cadence, story points, velocity |
| [templates/dor-checklist.md](templates/dor-checklist.md) | `<docs-root>/quality/dor-checklist.md`: DoR Spec and DoR Task |
| [templates/sprints-README.md](templates/sprints-README.md) | `<docs-root>/sprints/README.md`: planning and report templates |
| [templates/tech-debt.md](templates/tech-debt.md) | `<docs-root>/quality/tech-debt.md`: technical-debt log |
| [skills/](skills/) | `.github/skills/<name>/` (`SKILL.md` and `template.md` if present) plus wrappers for the tools in use |

Skills: `sprint-planning` (refinement and planning prep), `sprint-close` (report, velocity, retro), `dor-readiness-check` (one spec against DoR), and `dod-readiness-check` (finished work against DoD).

Activation also adds a `Points` column to the Task Order table in the task template. The [Contracts add-on](../contracts/README.md) is independent; when both are active, the skills include contract readiness.

## Activate

Copy the [integration prompt](integration-prompt.md) into an agent with access to the project. It inspects the project, asks for the open process decisions in the record (task-file author, estimators, cadence, capacity defaults), and copies the files after confirmation. The [shared routing](../../.github/copilot-instructions.md#optional-process-add-ons) loads the record only for sprint, estimation, readiness, or velocity work. Everything activated works after the `addons/` directory is removed.

## Deactivate

Use the [deactivation prompt](deactivation-prompt.md). It removes the record and skill copies and keeps sprint reports and filled logs unless you decide otherwise.

## Origin

Adapted from the Project Foundation Kit's SCRUM rules, Definition of Ready, sprint documents, and skills.
