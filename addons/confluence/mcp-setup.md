# Confluence MCP Adapter Setup

Configure and verify a real MCP connection using the
[shared MCP setup contract](../mcp-setup.md). Preparing page mappings alone does
not activate this adapter, and a browser login does not prove MCP access.

## Endpoint, Authentication, and Shared Ownership

For Atlassian Cloud use the official HTTP endpoint
`https://mcp.atlassian.com/v2/mcp` and the client's interactive OAuth flow. Select
the intended site, account, and space; respect organization access policies.
Keep secrets in the client-managed credential store, never in project files.

Check for an existing `delivery_atlassian` MCP profile used by Jira. Reuse it only when
endpoint, account, site access, and ownership match. Discover and authorize the
required Confluence operations separately; Jira access is not page access.
Changing or disabling a shared profile must preserve the Jira adapter.

For Data Center, select an administrator-approved MCP server and verify the
specific deployment's endpoint, authentication, and page schemas. The official
Cloud endpoint is not a Data Center compatibility guarantee. If no suitable
server is available, report **Blocked: MCP connection unavailable** rather than
claiming that documentation or manual publication completes adapter setup.

## Configure and Discover

Use `addons/configure_mcp.py` to preview the project configuration with
`--adapter confluence`, the actual client, `--server-name delivery_atlassian`, the verified
URL and, for Codex, explicit discovered tool names via `--tool`. Other clients
use their own tool controls; do not pass Codex-only flags to them or claim
equivalent enforcement. Review before adding `--apply`. Follow
the shared guide for discovery bootstrap, client-specific files, authentication,
and safe merging. Example command shape:

```sh
python3 addons/configure_mcp.py --adapter confluence --client codex \
  --server-name delivery_atlassian --url https://mcp.atlassian.com/v2/mcp \
  --tool VERIFIED_READ_TOOL --apply
```

For a new Codex connection without an authenticated catalog, replace the example
`--tool` option with `--discovery-only` for the initial configuration. Authenticate
and inspect the catalog as described in the shared guide, then review and manually
merge the exact operational allowlist before using tools.

Replace the example tool token with a real authenticated catalog entry before
execution. If Jira already uses this profile, review the combined allowlist and
ownership rather than adding a conflicting profile or a second OAuth grant.
Reload the selected client's MCP session and verify actual agent-visible tools.

Atlassian v2 can expose operations through deferred discovery and distinct
read/write execution paths. Inspect operation schemas and permission groups.
A broad write executor is not a per-page capability restriction; preview only
approved operations. Use a supported flat catalog if needed for exact tool
allowlisting and verify its behavior in the actual client.

## Page and Ticket Hierarchy Gate

Confluence is the documentation adapter, not a replacement ticket engine. The
required ticket/task hierarchy must live natively in Jira or another selected
issue system. A Confluence checklist, page link, or embedded Jira view is not
evidence that a Jira task has its native parent set. Verify that hierarchy with
the linked ticket adapter before calling the combined workflow ready.

For selected documentation, map each parent ticket/spec to a stable parent page
and any selected task documents to child pages. Use visible IDs in titles, for
example `SPEC-001: <title>` and `TASK-001-001: <title>`, preserving existing IDs.
Do not create duplicate task pages when only linking to canonical tickets is the
agreed scope. In a page-based mapping, record and verify the native page parent;
links in page bodies do not create a page-tree relationship.

| Required operation | Preflight evidence | Completion evidence after authorization |
| --- | --- | --- |
| Initialize and select target | Authenticated catalog plus site/space reads | Correct space ID and parent page ID recorded |
| Find/read pages | Exact source marker/ID lookup and page read | Existing identity/version reused |
| Create parent/child pages in selected scope | Create schema with native parent parameter | Correct ID-prefixed titles and child parent ID read back |
| Update selected content/title | Accepted representation, managed boundaries and version schema | Content/version read-back; unrelated sections preserved |
| Verify page hierarchy | Native parent and child listing operations | Parent and child observations agree |
| Verify ticket/task hierarchy if paired | Linked issue adapter's native parent/children operations | Actual canonical work objects verified; page tree not substituted |

Missing page create/update/parent/read-back support is **Connected, workflow
blocked** before creating unrelated flat pages. If the chosen scope is reference
only, state that limited scope explicitly; it is not full publication/hierarchy
support. A separately approved MCP bridge can be proposed where required, never
silently installed or represented as the official server's capability.

## Verification and Retirement

Perform only authorized representative writes; read back identity, parent,
content, source revision, audience, and rendered formatting. Repeat preparation
to confirm no duplicate parent or child is proposed. Record partial failures,
permission errors, stale versions, and unsupported formats rather than forcing
an overwrite or changing visibility. Page creation commonly publishes content:
preview destination and audience before any write.

Transfer actual configuration/profile ownership, operation schemas/matrix,
source mapping, hierarchy, permissions, versions, verification, and teardown
rules to the durable project record. Keep required configuration outside
`addons/`. On deactivation, inventory remote-only knowledge and complete agreed
migration first. Retire only this adapter's rules and dedicated connection; do
not disable shared Atlassian access needed by Jira. Preserve native page/ticket
relationships and content unless a separate change is authorized.

## Official References

- [Atlassian MCP setup and endpoint](https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/)
- [OAuth configuration](https://support.atlassian.com/atlassian-ai-gateway/docs/configure-oauth-2-1/)
- [MCP tools and operation discovery](https://support.atlassian.com/atlassian-ai-gateway/docs/supported-tools/)
- [Confluence page body, parent ID, and versioned updates](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/)

Recheck target capabilities and client behavior during setup; these references
do not establish authenticated access or cross-edition compatibility.
