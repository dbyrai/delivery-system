# GitHub Projects Adapter Setup Prompt

Copy this prompt into your AI tool from the target project. Supply known
repository and Project URLs; clarify unknown decisions in dialogue.

```text
Configure the optional GitHub Projects MCP adapter for this project.

Read the applicable repository entry instructions and shared workflow first.
Then read addons/README.md, addons/mcp-setup.md,
addons/github-projects/mcp-setup.md, and addons/github-projects/instructions.md.
Load only task-relevant sources and preserve the working tree, existing docs
root, source decisions, IDs, issue conventions, credentials and integrations.

Treat MCP connection setup as part of this request, not an optional suggestion.
Inspect and reuse a matching existing client/profile before adding one. Confirm
the exact GitHub host, repository, Project owner and URL, client and version.
Prepare and apply the scoped MCP client configuration with the shared helper
or the established supported client mechanism. Preserve unrelated profiles;
never commit tokens or request secrets in chat. Use the selected client's secure
OAuth or environment mechanism. Complete authentication, initialize MCP and list
the tools in the actual active session; reloading may be required. Verify target
repository and Project reads separately. Record exact states and errors without
claiming a configured profile proves an authenticated connection.

Before creating any parent ticket or task, inspect the actual tool schemas and
resource permissions for lookup, create, title/body/state update, native sub-issue
assignment, child-parent read, parent-children read, and selected Project updates.
Record this operation matrix in the durable project integration record. A tool
name is not write authorization or proven target permission. Read/create-only
access does not satisfy the full requested adapter. If a required operation is
missing, configure an approved supported MCP toolset/server route and stop
unsupported writes. Do not substitute flat issues, comments, body links, Project
membership, or replacement duplicates for native parent/child hierarchy. Manual
fallback instructions must be labelled blocked/incomplete MCP setup.

Resolve only unanswered blocking decisions: authority per field, parent/task scope,
existing stable ID format, status and account mapping, direction/trigger, owner,
conflict policy and write scope. Reuse current decisions and authorizations.
Keep existing source authority until explicitly changed; record deferrals and
leave dependent operations inactive.

Prepare a concrete preview of local and remote changes. Tickets and tasks must
have their unique stable IDs in visible titles, for example SPEC-001: <title> and
TASK-001-001: <title>. Each task must be a native GitHub sub-issue of its actual
parent ticket. Search all relevant states and existing maps before creating or
linking anything. Preserve existing remote IDs, unowned text and workflows.
Distinguish numeric issue API IDs, repository issue numbers, and Project item IDs.
If a different parent already exists, stop and resolve that conflict; do not
silently replace it. Request only missing authorization once the preview is ready.
Do not merge, release, or install recurring synchronization during this setup.

Apply resolved operations within authorization and read back titles, managed
content, each child parent and the parent's paginated children, plus selected
Project fields. Verify each mapping and relation exactly once. If creation succeeds
but linking fails, record partial state and repair the existing object after
reconciliation; never create another copy. Check unintended closing keywords.

Make the durable record self-contained: targets, stable and remote IDs, native
hierarchy, source decisions, actual MCP client/profile and non-secret credential
reference, capabilities, granted actions, triggers, conflict/retry rules,
verification and deactivation steps. Route relevant future work to that record,
not addons/ files. Keep setup/configuration, authentication, active-session tools,
read tests, authorized writes, and hierarchy completion as separate results.

Explain that optional-file deletion does not disconnect MCP. Before later
retirement, inventory remote-only content and obtain the user's migration or
retention decision while required read access still works. Preserve remote
history, parent/child relations and shared access. Summarize changed files,
completed checks, partial/blocked work and remaining owner actions. Do not commit
or push unless separately authorized.
```
