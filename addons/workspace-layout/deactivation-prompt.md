# Workspace Layout Deactivation Prompt

```text
Deactivate or migrate the Workspace Layout add-on in this project.

Read the active .github/workspace-layout.md file and durable layout record. Inspect
both Git repositories, working trees, documentation roots, ignore rules, private
records, installed add-ons, and pending changes. Determine the requested target:
retain the split layout without Delivery System routing, migrate to one repository,
or replace it with another workspace. Do not assume deletion is required.

Prepare an exact content, history, privacy, link, and rollback plan. Obtain owner
decisions for every document that would move between public and private roots.
Never expose security findings or confidential records. Preserve both repositories
and their histories unless destructive action is explicitly authorized.

After the migration is complete and verified, remove only the conditional routing
pointer, add-on-owned layout file, and confirmed ignore entry. Mark the durable
record inactive or archive it with retained paths and evidence. Removing files
under addons/workspace-layout is a separate action.

Verify both Git states, document links, installed add-on records, privacy paths,
and the resulting bootstrap/adoption workflow. Do not commit, push, merge, publish,
or change remote access without separate authorization.
```
