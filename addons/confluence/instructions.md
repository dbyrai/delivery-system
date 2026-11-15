# Confluence Integration Instructions

Apply the [shared lifecycle](../README.md) and the project's canonical workflow.
Load only documentation relevant to the selected publication or import scope.

## Discovery and Decisions

Resolve and record before dependent changes:

- Site, edition/version, space identifier, parent page, content owner, audience,
  approved access method, and actual read/write capabilities.
- Existing pages, local source files, publication conventions, integrations, and
  access restrictions. Do not infer an audience from space visibility alone.
- Authority per document or section: local source, Confluence source, or an
  explicitly divided ownership model. Preserve existing project authority until
  a decision changes it; reconcile conflicting project rules in the same change.
- Link-only, one-way publication, or agreed import; selected files/sections;
  publication trigger and operator; inclusion of comments and attachments.
- Handling of page moves, renames, stale content, and local/remote edits.

Ask focused questions when decisions are missing. Do not publish all of `docs/`
or introduce automatic two-way synchronization by default.

## Page Mapping and Rendering

Prepare an explicit mapping. This example describes decisions to make, not
preconfigured page names or ownership:

| Project content | Confluence representation | Decision to record |
| --- | --- | --- |
| Selected source file or section | Existing or planned page | Stable source reference and page ID/URL |
| Document heading | Page title | Naming and rename ownership |
| Document hierarchy | Space and parent page | Approved destination and audience |
| Requirements and criteria | Rendered body with stable IDs and source links | Authority and rendering format |
| Diagrams and supporting evidence | Links or approved attachments | Visibility and supported rendering |
| Publication evidence | Source revision and remote version | Operator, timestamp, and verification |

Identify pages by verified IDs and stored mappings rather than title alone.
Check the mapping and approved parent scope before creating pages. Preserve
existing local document paths and requirement/task IDs.

For Confluence Cloud, the page API exposes body representations and version
information used during updates. Check the selected tool's supported format;
do not assume Markdown is a native page body or that a conversion is lossless.
Re-read the current version before updating. See the
[official page reference](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).

Preview headings, lists, tables, links, code, diagrams, and attachments. Preserve
source IDs and use links where a representation is unsupported. Include an agreed
source reference and revision when publishing a derived copy. Change only managed
content; do not replace an entire page containing unowned material. If the tool
cannot safely update selected sections, use a dedicated page or defer the write.

## Permissions, Execution, and Conflicts

Record required view/create/update permissions and a reference to the access
configuration, without secrets. Check the proposed destination's audience and
restrictions before publishing sensitive project content. Do not broaden access
or change restrictions merely to make publication succeed.

Prepare a concrete preview identifying target pages, managed sections, and
content differences. Reuse authorization already granted for those operations;
obtain missing authorization before external writes. Selecting setup alone does
not authorize publication, comments, invitations, moves, or deletion. Respect
any publication approvals required by the actual site.

If the remote page changed since the preview, stop that update and reconcile
ownership and versions. Do not force an overwrite or blindly replay a stale
payload. After ambiguous creation results, check page identity/mapping before
retrying. Record partial successes, respect service/tool limits, and surface
permission or rendering failures without changing the audience or scope.

## Durable Record and Verification

Record the agreed targets, authority, page mappings, managed boundaries, formats,
access references, permitted actions, trigger/operator, revision tracking,
conflict/retry behavior, verification, and retirement in the existing project
documentation root. Link the record from documentation-relevant project guidance.
Transfer all ongoing rules into the project so deleting `addons/` cannot remove
required operational knowledge.

Verify a representative document preview, including a table, code/link content,
and any selected rich content. For authorized writes, read the resulting page
back and inspect its rendering, source revision, identity, and audience. Otherwise
report preview-only verification. Repeat preparation to check that no duplicate
page is proposed. Verify that local sources, IDs, unrelated page content, and
project gates remain intact and that the durable record works after removing
the add-on from a temporary project copy.
