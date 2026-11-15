# Confluence Integration Prompt

Copy the prompt below into the AI tool used for the target project. Supply known
non-secret site/space details if available; unresolved decisions will be clarified.

```text
Integrate the optional Delivery System Confluence add-on into this project.

Read the applicable project/tool instructions, addons/README.md, and
addons/confluence/instructions.md before acting. If the add-on source is missing,
ask for it rather than claiming to have read it. Use the established project
documentation root and load only relevant sources, decisions, and security rules.
Preserve existing documentation, IDs, integrations, and delivery gates.

Inspect the project and available tools. Identify the Confluence site, edition,
space, parent page, content owner, audience, existing pages, and access method.
Check actual connector/API capabilities and current official documentation for
the deployed edition. Do not assume Markdown support, lossless conversion,
publication permission, or cross-edition compatibility. Keep tokens and other
credentials out of repository files and chat.

Resolve blocking decisions one at a time: selected documents/sections,
authoritative sources, link/publication/import direction, page identity and
hierarchy, managed content boundaries, access restrictions, allowed operations,
and publication trigger/operator. Preserve current source-of-truth rules until
an explicit decision changes them. Do not publish every project document or
create a competing requirements source by default.

Prepare local adaptations, a source-to-page mapping, and a concrete publication
or import preview. Preserve stable requirement/task IDs and record page IDs/URLs,
source revision, and remote version. Check existing mappings before creation.
Preview formatting and links; use agreed links for unsupported rich content.
Do not overwrite unowned page sections. Re-read remote versions and reconcile
concurrent edits before updates. Respect site publication approvals.

Reuse authorization already granted for the same operations and ask only for
missing authorization before external writes. Selecting this prompt is not
permission to publish, comment, change access, or delete pages. If no usable
connector exists, prepare the mapping and document live setup as incomplete.
Do not configure a new external service without authorization.

Create or update a durable project integration record covering destinations,
content ownership, mappings, rendering, permissions, non-secret access references,
permitted operations, triggers, conflict/retry handling, verification, and
retirement. Link it from relevant project instructions. Copy all ongoing rules
into the project so the configured integration remains usable after addons/ is
removed; do not require all add-ons to be loaded for ordinary project work.

Verify a representative preview and read back any authorized remote changes.
Check rendering, links, audience, revisions, duplicates, and preservation of
unrelated content. Distinguish preview/static checks from live connector checks.
Explain removing optional instructions separately from retiring the active
connection, preserving mapping history and shared access. Report changed files,
verified operations, limitations, and pending decisions. Do not commit, push,
publish a release, or create background synchronization.
```
