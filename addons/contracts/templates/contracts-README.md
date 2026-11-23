# Contracts

Contracts define agreements between system boundaries — modules, apps, layers, and external consumers. They enable independent development by different developer + agent teams.

## Overview

For the contract system rules (types, ownership, lifecycle, breaking changes), see the project's Contracts record (`docs/project/integrations/contracts.md`).

## Directory Structure

```
docs/contracts/
├── README.md              # This file
├── template.md            # Contract document template
├── app-wide/              # Contracts shared across modules
│   └── ...
└── {module}/              # One directory per module, e.g. api-*, event-*, ui-*
```

## Naming Convention

| Scope | Path | Example |
|---|---|---|
| App-wide | `docs/contracts/app-wide/{name}.md` | `auth-context.md` |
| Module-internal | `docs/contracts/{module}/{type}-{name}.md` | `orders/api-intake.md` |

Type prefixes: `api-`, `ui-`, `event-`, `database-`, `config-`

## Contract Template

Use [`template.md`](template.md) when creating new contracts.

## Quick Reference

| Status | Meaning | Can dependent tasks start? |
|---|---|---|
| Draft | Shape may change | No |
| Review | Stable for reference | Yes (DoR minimum) |
| Final | Locked, changes need versioning | Yes |
| Deprecated | Being replaced | Yes, but migrate soon |
