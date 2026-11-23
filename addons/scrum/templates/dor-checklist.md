# Definition Of Ready Checklist

Readiness gates the start of work; the [Definition of Done](dod-checklist.md) gates completion. Process rules and roles are in the project's SCRUM record (`docs/project/integrations/scrum.md`).

## DoR: Spec

A spec is ready for task breakdown when:

- [ ] All open questions are answered or explicitly deferred with a documented reason.
- [ ] Acceptance criteria are present and verifiable.
- [ ] Dependencies on other specs, modules, contracts, and decisions are documented.
- [ ] Non-goals are explicitly stated.
- [ ] Security requirements are identified, or marked not applicable.
- [ ] The Product Owner has reviewed and approved the spec.

**Gate**: Tasks are not created from a spec that fails DoR Spec. The `Approved` status plus a passed DoR Spec is the handoff signal for task breakdown.

## DoR: Task

A task is ready to enter a sprint when:

- [ ] The source spec passes DoR Spec and the source requirement reference is documented.
- [ ] Acceptance criteria are present and verifiable.
- [ ] Implementation notes are sufficient to start without follow-up questions.
- [ ] Story points are estimated by a human on the scale 1, 2, 3, 5, 8, 13; anything larger is split.
- [ ] An owner is assigned.
- [ ] No unresolved open questions or blockers remain.

**Gate**: Tasks that fail DoR Task do not enter the sprint's Ready column.

## How To Use

- **Refinement**: confirm DoR Spec for candidate specs, break handed-off specs into tasks, walk DoR Task, split anything above 13 points.
- **Sprint planning**: present only tasks that pass DoR Task and re-check dependencies that may have changed.
- **Implementation**: the agent checks DoR before starting and warns the responsible developer about gaps (soft block); the developer decides.

| Checklist | When | Purpose |
| --- | --- | --- |
| DoR Spec | Before creating tasks | Spec is complete enough for breakdown |
| DoR Task | Before entering a sprint | Task is clear enough for autonomous work |
| DoD | Before marking a task Done | Work meets quality and completeness standards |
