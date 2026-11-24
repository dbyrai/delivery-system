# Shared Workflow Skills

These skills provide reusable workflows on top of the canonical project
instructions. Tool-specific wrappers delegate here and contain no additional
workflow rules.

| Skill | Purpose | Required project source |
| --- | --- | --- |
| `bootstrap` | Run the documented bootstrap sequence interactively | `delivery-system.md`; Product Manager role for project definition |
| `new-feature` | Clarify an idea before drafting a specification | Product Manager role; `docs/specs/template.md` |
| `spec` | Write a specification from already clarified requirements | Product Manager role; `docs/specs/template.md` |
| `bugfix` | Investigate and fix a concrete defect without inventing feature scope | Relevant implementation role and project verification rules |
| `prioritize` | Apply confirmed MoSCoW priorities | Product Manager role; the `Priority` field in `docs/specs/template.md` |

The Product Manager role and updated specification template are release
prerequisites for these skills. Merge or adopt those sources before activating
this package. Optional tool add-ons provide their own wrappers and are not a
prerequisite for the shared skills.
