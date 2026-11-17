# GitLab Adapter

Use this optional adapter to connect the Delivery System to GitLab through MCP.
Its setup prompt must configure or reuse an actual client connection, authenticate,
and verify the requested operations. A written mapping or a successful Git push
alone is not an operational adapter. No background synchronization or pipeline is
installed automatically.

## Prerequisites and Use

1. Read the [shared adapter lifecycle](../README.md) and
   [shared MCP setup](../mcp-setup.md).
2. Identify the GitLab HTTPS host and exact project. A Git SSH remote does not
   determine the HTTPS port or grant issue/API access.
3. Follow [GitLab MCP setup](mcp-setup.md), including the capability gate for
   native parent/child tasks. Keep credentials in the selected client's store.
4. Copy the [integration prompt](integration-prompt.md) into your project AI tool.
   It performs setup; it must not stop at a documentation-only preview unless
   access or a concrete prerequisite is blocked.
5. Record actual connection, object, hierarchy, update, and repeat-test evidence
   under the project's existing documentation root.

## Required Ticket Structure

A parent ticket uses a visible stable title such as `SPEC-001: Task tracking`.
Its delivery tasks use `TASK-001-001: Create task list` and equivalent existing
IDs, and must appear as native GitLab **Task** child items under the correct
parent issue. Preserve IDs already assigned by the project.

Description markers and links supplement this relationship; they do not create
it. A GitLab Project board is a view, not the parent ticket. Verify the selected
instance and transport can create/update/read the work-item type and relationship
before creating children. If MCP lacks these operations, report the affected
adapter workflow as blocked and prepare a supported, explicitly selected path.
Do not produce unrelated plain issues as a substitute.

See the [mapping and execution contract](instructions.md) for authority, identity,
conflicts, permissions, and lifecycle checks. GitLab CI/CD and deployments remain
subject to the project's established process.

## Removal

Use the [deactivation prompt](deactivation-prompt.md) to retire the connection.
It inventories remote project knowledge and obtains the user's migration or
retention decision before stopping read access needed for that handover.

Deleting these optional files does not stop MCP access or remove remote work.
After setup, retain self-contained project rules and mappings. Remove only this
adapter's client profile, jobs, or grants within authorization; preserve shared
credentials, issues, child relationships, merge requests, and existing pipelines.
Record the resulting source of truth and verify the actual shutdown state.
