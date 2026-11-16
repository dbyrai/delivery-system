# Jira MCP Adapter Setup

This adapter must configure and verify an MCP connection before it is reported
ready. A mapping document or a working browser login alone is not an active
adapter. Follow the [shared MCP setup contract](../mcp-setup.md) first.

## Supported Connection Choice

For Atlassian Cloud, start with Atlassian's official HTTP MCP endpoint:
`https://mcp.atlassian.com/v2/mcp`. Authenticate through the client's interactive
OAuth consent flow and choose the correct Atlassian site. Keep credentials in
the client-managed store. An organization may restrict domains, scopes, or IPs;
do not weaken those policies to obtain a connection.

Cloud endpoint support is not proof of Jira Data Center support. For Data Center,
identify an administrator-approved MCP server, its deployment/version, endpoint,
authentication, and issue operations. If none is available, report **Blocked:
MCP connection unavailable**; do not silently install a third-party bridge or
substitute manual steps for completed setup.

Jira and Confluence may share one `delivery_atlassian` profile when endpoint, account,
site access, and ownership match. Reuse and inspect that profile before adding
another login. Coordinate any tool-policy change or later removal with both
adapters; matching provider names alone do not prove matching access.

## Configure the Actual Client

Use `addons/configure_mcp.py` from the project root to preview the project-scoped
configuration, selecting `--adapter jira`, the actual `--client`,
`--server-name delivery_atlassian`, the verified endpoint, and, for Codex, one `--tool` per discovered
allowed tool. Other client schemas have different controls; do not pass Codex-only
tool flags to them or claim equivalent tool-policy enforcement. Add `--apply` only after reviewing the preview. The shared guide
covers client-specific target files, authentication, discovery bootstrap, and
safe merging. A typical command shape is:

```sh
python3 addons/configure_mcp.py --adapter jira --client codex \
  --server-name delivery_atlassian --url https://mcp.atlassian.com/v2/mcp \
  --tool VERIFIED_READ_TOOL --apply
```

For a new Codex connection without an authenticated catalog, replace the example
`--tool` option with `--discovery-only` for the initial configuration. Authenticate
and inspect the catalog as described in the shared guide, then review and manually
merge the exact operational allowlist before using tools.

Replace `VERIFIED_READ_TOOL` with an exact tool name from the authenticated
catalog; it is not a real tool and this is not a command to run unchanged. Retain
unrelated server configuration and existing permission boundaries. If a matching
profile already exists, reuse it; if its endpoint or policy differs, reconcile
explicitly instead of overwriting it. Complete client authentication and reload
its MCP session before checking tool availability in the actual agent session.

Atlassian v2 supports deferred tool discovery and read/write execution paths.
Inspect discovered operation schemas, not only the initial tool list. If a broad
write executor is enabled, constrain its use to the approved Jira operations and
preview each mutation; enabling an executor does not limit it to a single issue
or grant authorization. Prefer a supported flat catalog when precise client
allowlisting requires one; recheck official documentation and actual tool names.

## Capability Gate Before Ticket Creation

Record actual tool/operation names, input schema, required permissions, and
verified reads for each selected operation. Schema discovery is evidence of an
available operation, not proof of a successful write in the target project.

| Required operation | Preflight evidence | Completion evidence after authorization |
| --- | --- | --- |
| Connect and identify site/project | Initialize, paginated catalog discovery, authenticated project/type metadata | Correct site, project key/ID and account recorded |
| Find/read existing work | Exact marker search and issue read | Stable ID/key/URL mapping; duplicates identified |
| Create parent ticket | Required fields and valid parent issue type | Parent summary includes stable ID; read back content |
| Create child task | Valid child/subtask type and native parent input | Child summary includes task ID and actual parent key |
| Update managed fields/status | Edit schema and valid transition operations | Authorized change read back without unowned content loss |
| Verify hierarchy | Parent field and children/subtasks read operations | Child points to correct ticket and ticket lists child |

The required work structure is a parent ticket with its own tasks natively below
it. For example, retain `SPEC-001: <title>` as the parent summary and
`TASK-001-001: <title>` for a child. Preserve existing IDs and agreed terminology;
do not turn an existing Task into a different logical object. Inspect the actual
Jira project type/hierarchy before selecting parent and child work types. A
common project uses a standard issue and subtasks, whose create metadata must
expose the intended child type and parent field. Never assume an arbitrary Task
is already a child, or an Epic can directly own a Sub-task.

If create/update/parent/read-back operations are missing, stop before creating
flat child issues. Report **Connected, workflow blocked**, with the missing
operation and supported next option. A separately approved API-backed MCP server
may supplement the official server, but is a new connection decision; do not
claim the existing MCP server can do it. No title/body hyperlink or checklist
satisfies the native hierarchy requirement.

## Success, Failure, and Retest

After scoped authorization, verify a representative parent/child pair and a
managed update; re-read summaries, type, parent reference, and the parent's child
list. Repeat the preparation and confirm existing identities are reused rather
than duplicated. Log partial results and stop dependent actions on permission,
validation, formatting, or concurrency errors. Never claim **Ready** when only
read access or object creation is verified but required hierarchy/update is absent.

Copy the endpoint/profile reference, actual operation matrix, hierarchy, versions,
non-secret access reference, source authority, tests, and shutdown procedure into
the durable project record. Record runtime limitations honestly. Keep required
configuration outside disposable `addons/` so removing instructions does not
remove the active adapter. Never store bearer tokens or API secrets in examples.

## Official References

- [Atlassian MCP setup and endpoint](https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/)
- [OAuth configuration](https://support.atlassian.com/atlassian-ai-gateway/docs/configure-oauth-2-1/)
- [MCP tools and operation discovery](https://support.atlassian.com/atlassian-ai-gateway/docs/supported-tools/)
- [Jira issue creation, child types, and parent field](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/)

These references establish the setup approach, not authenticated compatibility
with a particular client, site, or Data Center deployment. Recheck them at setup.
