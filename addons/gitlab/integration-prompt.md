# GitLab Adapter Setup Prompt

Copy the prompt into the target project's AI tool. Include known non-secret
GitLab project details. This prompt configures and verifies a real MCP connection;
a mapping document alone is not an operational adapter.

```text
Configure and adapt the GitLab MCP-backed Delivery System adapter for this project.

For issue operations, use the numeric project ID discovered through authenticated
search when supported by the schema. Do not pre-percent-encode a namespace path
for an MCP tool unless its schema requires that format; avoid double encoding.
A failed path lookup needs a scoped numeric-ID read check before being classified
as a missing issue capability or permission failure.

Read applicable project/tool instructions, the existing integration record,
addons/README.md, addons/mcp-setup.md, addons/gitlab/instructions.md, and
addons/gitlab/mcp-setup.md. Load only relevant project sources. Preserve local
changes, existing documentation roots, stable IDs, established authority, current
integrations, and CI/CD boundaries. Missing add-on files must be supplied rather
than pretended read; active project rules remain authoritative.

Confirm the HTTPS GitLab host and exact target identity. Inspect existing MCP
profiles without exposing credentials; reuse a matching working profile. Configure
or repair the chosen client's scoped MCP profile, complete its supported OAuth
flow, reload or start a new session when required, initialize MCP, retrieve all
pages of tools/list and actual schemas, and read the target project/version.
Use the shared helper for supported configuration formats; preview its changes
before applying and never overwrite unrelated profiles. Keep secrets in the
client's private store. Do not infer issue access from a Git remote or saved file.
This setup request authorizes scoped MCP configuration, not arbitrary GitLab writes.

Require visible stable ID-prefixed names: the parent ticket/spec uses its existing
SPEC-style identifier, and each task title its own TASK-style identifier. Preserve
existing project ID conventions. Tasks must be native GitLab Task children under
the correct parent issue, with both task-parent and parent-child read-back. Body
links, checkboxes, related-item links, or plain unparented issues do not satisfy
this requirement.

Before creating tickets, complete the actual capability/permission matrix for
search/read, parent create/reuse, native child Task create/conversion, native
parent assignment, title/content/status updates, and bidirectional hierarchy
verification. Inspect the current catalog and target version, not guessed tool
names. Tool presence is not write permission. A read-only profile is not a fully
working write adapter. If any required operation is absent, report this workflow
as blocked and prepare a supported execution path for selection before creating
or changing objects. Do not silently downgrade to documentation-only/manual setup.

Prefer native HTTP; preserve an already working connection. For a concrete
native OAuth compatibility failure, diagnose the recorded error and metadata,
then use the documented pinned proxy path only when selected and appropriate.
Never disable TLS/issuer checks, use unpinned @latest, or bypass note validation
with Quick Actions. A proxy does not add missing update or hierarchy tools.
Do not install external services or change instance settings implicitly.

Resolve remaining blocking decisions one at a time: per-field authority, exact
parent/type mapping, managed content/status/account fields, direction and trigger,
owner, conflict policy, and allowed writes. Reuse decisions and authorization
already granted for this scope. Record explicit deferrals and keep dependent
operations inactive. Preserve external authority when the project selected it.

Prepare a concrete local/configuration diff and remote change preview. Locate
mapped objects across relevant states and result pages before creating anything.
For existing unstructured issues, prepare a correction of their titles/types/
parentage while preserving IDs, content, comments, checklists, and history; do not
create replacements or reparent unrelated work. Reuse/create the parent before
children, apply only resolved and authorized operations, and request only missing
external-write authorization once the plan is concrete. Preserve unrelated issue
sections, shared boards, and all CI/CD. No merge, release, webhook, or background
synchronization is part of this setup.

Read back every changed object and both directions of native hierarchy. Perform
a scoped authorized update and repeat the same preparation to verify no duplicate
parent, task, or relation is created. On partial or uncertain results, reconcile
using stable IDs before retrying. Do not equate a merged MR or closed issue with
acceptance of a Delivery task. Record actual results and unrun checks separately.

Keep the durable project record self-contained: selected MCP profile/endpoint,
versions, auth/session evidence, actual capability matrix, target identifiers,
ID-prefixed titles, native hierarchy, source authority, non-secret access reference,
authorized actions, triggers, conflicts/retries, tests, limitations, and retirement.
Make runtime configuration and ongoing rules independent of removable addons/
files. Route future relevant work to that record. If live access is unavailable,
report the blocked phase and exact next owner action; do not claim an active or
complete adapter.

Explain deactivation separately from deleting optional files. Inventory remote
knowledge and obtain the user's migration/retention decision before disabling
needed read access, then verify required migration and scoped MCP shutdown while
preserving shared access, native hierarchy/history, and CI/CD. Summarize changed
files, verified operations, blocked/partial states, and remaining work. Do not
commit, push, or publish unless separately authorized.
```
