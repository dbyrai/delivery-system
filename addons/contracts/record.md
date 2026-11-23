# Contract System

<!-- Durable project record created by the optional Contracts add-on. Replace every
{placeholder} with a confirmed project decision or mark it as an open question.
This record must stay usable after the add-on directory is removed. -->

**Status**: Active
**Owner**: {accountable role}
**Adopted From**: Delivery System Contracts add-on {version or commit}

## Scope

Load this record for work that defines, changes, or consumes an interface between modules, applications, layers, or external consumers. The provider owns the contract. A contract exists before dependent code is written.

## Types

| Type | File prefix | Scope |
| --- | --- | --- |
| API (frontend-backend, module-module) | `api-` | application-wide or module-internal |
| UI component | `ui-` | application-wide or module-internal |
| Authentication or tenant context | none | application-wide |
| Event or async message | `event-` | application-wide or module-internal |
| Database | `database-` | application-wide |
| Configuration or feature flag | `config-` | application-wide |

Remove types the project does not use.

## Files

- Application-wide: `docs/contracts/app-wide/{name}.md`
- Module-internal: `docs/contracts/{module}/{type}-{name}.md`
- Template and index: `docs/contracts/template.md`, `docs/contracts/README.md`

## Lifecycle

| Status | Meaning | Dependent tasks may start |
| --- | --- | --- |
| Draft | Shape may change | No |
| Review | Stable for reference | Yes (minimum) |
| Final | Locked; changes need versioning | Yes |
| Deprecated | Being replaced; migration deadline documented | Yes, migrate |

## Versioning And Breaking Changes

- Application-wide: semantic versioning (major = breaking, minor = additive, patch = documentation). Breaking change: flag it, discuss, {Product Owner} decides, bump major, write a migration note, notify consumers.
- Module-internal: Git history only; the responsible developer decides and updates all consumers in the module.

## Specs And Tasks

- Specs list required contracts in a `Contracts` table: Contract, Type, Role (provider or consumer), Status.
- Tasks list required contracts as checkboxes; all must exist with status `review` or higher before implementation starts.
- With the SCRUM record active, contract readiness is part of DoR Spec and DoR Task.
