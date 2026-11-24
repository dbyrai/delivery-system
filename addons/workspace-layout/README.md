# Workspace Layout Add-on

This optional add-on separates the Delivery System from application source code.
A private workspace repository holds shared instructions, templates, and private
project records; a separately versioned application repository lives in a
configurable subdirectory. The add-on is inactive until explicitly installed.

Use this layout when the application repository must remain free of delivery
tooling or when security findings and other confidential records must not be
stored in a public repository. The standard single-repository layout remains the
default and requires no changes.

## Contents

| Source | Activated as | Purpose |
| --- | --- | --- |
| [templates/workspace-layout.md](templates/workspace-layout.md) | `.github/workspace-layout.md` | Durable root-level routing and path rules |
| [record.md](record.md) | `<private-docs-root>/project/integrations/workspace-layout.md` | Decision, ownership, verification, and migration |
| [templates/gitignore.snippet](templates/gitignore.snippet) | workspace `.gitignore` entry | Keep the nested repository out of workspace commits |
| [integration-prompt.md](integration-prompt.md) | Run manually | Reconcile and activate the layout |
| [deactivation-prompt.md](deactivation-prompt.md) | Run manually | Migrate or remove layout routing safely |

## Required Decisions

- Relative application repository directory; it is not fixed to `app/`.
- Project documentation root inside the application repository.
- Private documentation root inside the workspace repository.
- Whether the application repository is public.
- Owners and commit/push/release boundaries for both repositories.
- Migration and rollback plan for existing project documents.

## Activation Rules

Use the [integration prompt](integration-prompt.md). Activation installs a
self-contained `.github/workspace-layout.md`, records the adopted source revision,
and adds one short pointer from `.github/copilot-instructions.md`. The installed
file and durable record must work after `addons/workspace-layout/` is removed.

The add-on never creates, clones, initializes, or pushes the application
repository without separate authorization. It never moves project documents
until the owner approves an exact migration plan. Existing files are reconciled,
not overwritten.

## Verification

Verify all four cases before treating the layout as operational:

1. Standard layout remains unchanged when the add-on is inactive.
2. Private workspace with a private application repository.
3. Private workspace with a public application repository; confidential records
   and links remain entirely in the private documentation root.
4. Deactivation or migration preserves both Git histories and retained records.

For the active layout, also verify `git -C <application-directory>` boundaries,
workspace ignore rules, documentation links, bootstrap/adoption paths, and each
installed add-on's record lookup. Record checks actually run.
