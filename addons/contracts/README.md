# Contracts Add-on

Use this optional add-on when independently developed modules, applications, or teams depend on shared interfaces. It adds a contract lifecycle (draft, review, final, deprecated), ownership and breaking-change rules, and contract references in specs and tasks.

## Contents

| Path | Activated as |
| --- | --- |
| [record.md](record.md) | `<docs-root>/project/integrations/contracts.md`: types, lifecycle, versioning, spec/task rules |
| [templates/contracts-README.md](templates/contracts-README.md) | `<docs-root>/contracts/README.md` |
| [templates/contract-template.md](templates/contract-template.md) | `<docs-root>/contracts/template.md` |

Activation also adds a `Contracts` table to the spec template, a `Required Contracts` checklist to each task in the task template, and two contract items to the Definition of Done (consumed contracts implemented as specified; provided contracts updated when their surface changes).

## Activate

Copy the [integration prompt](integration-prompt.md) into an agent with access to the project. The [shared routing](../../.github/copilot-instructions.md#optional-process-add-ons) loads the record only for interface work. Everything activated works after the `addons/` directory is removed.

## Deactivate

Use the [deactivation prompt](deactivation-prompt.md). Existing contract documents remain project knowledge unless you decide otherwise.

## Origin

Adapted from the Project Foundation Kit's contract rules and templates.
