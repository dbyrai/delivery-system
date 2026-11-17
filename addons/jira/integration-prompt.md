# Jira Adapter Integration Prompt

Copy the prompt below into the AI tool used for the target project. Add known
non-secret target details if available; unresolved decisions will be clarified.

```text
Integrate the optional Delivery System Jira add-on into this project.

Read the applicable project/tool instructions, addons/README.md, and
addons/jira/instructions.md before acting. If those instructions were removed,
ask for the selected add-on source; do not pretend to have read it. Follow the
existing documentation root and load only relevant specs, tasks, decisions,
and security rules. Preserve project content, IDs, and existing integrations.

Configure this as a real MCP-backed Jira adapter. Read
addons/mcp-setup.md and addons/jira/mcp-setup.md, inspect existing
client profiles, then prepare and apply the selected client configuration within
this setup request's scope. Use addons/configure_mcp.py for supported project
profiles; reuse matching Atlassian connection ownership instead of creating a
duplicate OAuth profile. Do not overwrite other configuration or install an
unapproved bridge. Complete interactive authentication, initialize MCP, discover
actual operation schemas, reload the client as needed, and verify target reads.
A mapping-only result or browser login is not completed MCP setup. Report blocked
states and ask for missing target/access information without claiming success.

Before ticket/page writes, verify create, read, update, native-parent assignment,
and parent/children read-back for the chosen workflow. Use stable existing IDs
in visible parent and task names, for example SPEC-001 and TASK-001-001. Tasks
must be native children of their corresponding ticket; description links and
checklists do not satisfy that requirement. Choose valid Jira parent and child
work types from project metadata; do not guess Epic/Sub-task combinations.
If required operations are missing, stop before creating flat substitutes.
Record the precise missing capability and any separately approved supported
connection needed to complete it. Keep capability and action permission distinct.

Inspect the project and available tools first. Identify the Jira site, edition,
project, issue types, current links, and integration owner. Verify the actual
connector/API capabilities and current official documentation for that edition.
Do not assume access, writable fields, valid transitions, or tool compatibility.
Never request that credentials be pasted into chat or committed to the repo.

Clarify blocking decisions one at a time: authoritative source for each field,
link/import/publication direction, issue and status mappings, duplicate lookup,
permitted operations, and trigger/operator. Existing project authority remains
in force until a decision explicitly changes it. Do not bypass open-question,
bootstrap, approval, or implementation gates because an issue exists in Jira.

Prepare concrete local adaptations and a remote change preview. Keep stable
Delivery task IDs and record Jira IDs, keys, and URLs. Discover required fields
and valid transitions; handle the connector's content format correctly. Reuse
existing authorization for the same operations and ask only for missing external
write authorization. Do not create issues, post comments, assign people, or
change status merely because this setup prompt was selected. If no usable
connector exists, prepare the mapping and record that live setup is incomplete.
Do not install or configure a new external service without authorization.

Create or update a durable integration record in the existing project docs,
covering decisions, mappings, access references (no secrets), permissions,
conflict/retry behavior, verification, and retirement. Link it from the relevant
project instructions so future task work finds it without loading all add-ons.
Transfer all required ongoing rules into the project; the active integration
must remain usable if addons/ is deleted.

Verify one representative mapping, preview changes, and read back any authorized
remote writes. Check duplicates and preservation of existing task IDs and rules.
Distinguish static/preview checks from live connector checks. Explain how to
remove unused instructions and separately retire the active connection without
deleting delivery evidence or breaking shared credentials. Report changed files,
verified operations, limitations, and any pending decisions. Do not commit,
push, publish, or create a background synchronization service.
```
