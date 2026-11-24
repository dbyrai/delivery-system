# Workspace Layout Integration Prompt

```text
Activate the optional Workspace Layout add-on for this Delivery System project.

Read the applicable project instructions, addons/workspace-layout/README.md,
its routing template and record. Inspect the working tree, current documentation
root, existing repositories, ignore rules, symbolic links, and installed add-on
records. Preserve local changes and do not assume an app/ directory.

Confirm one decision at a time: relative application directory, application
repository identity and visibility, project and private documentation roots,
owners and Git/release authority, documents to migrate, confidential content,
and rollback plan. Reject absolute paths, path traversal, unexpected symbolic
links, or a private root located inside a public application repository.

Show the exact planned file and migration changes before writing. After explicit
confirmation, reconcile the completed routing template into
.github/workspace-layout.md, create the durable record under the confirmed
private documentation root, add the application directory to the workspace
.gitignore, and add one short conditional pointer from the canonical shared
instructions to .github/workspace-layout.md.

Copy required templates and baselines into the project documentation root only
when their migration was approved. Never overwrite completed documents. Do not
create, clone, initialize, move, commit, push, merge, publish, or change remote
repository access without separate authorization covering that action.

Activated files must not reference addons/. Verify standard-layout isolation,
both Git roots, ignore behavior, documentation links, privacy boundaries,
configured add-on records, and rollback. Report actual and pending checks.
```
