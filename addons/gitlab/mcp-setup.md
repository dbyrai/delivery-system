# Configure and Verify GitLab MCP

This is a required setup phase for the [GitLab adapter](README.md). Apply the
[shared client setup](../mcp-setup.md). The adapter is not ready for the requested
delivery workflow until both the MCP connection and the required operations pass.

## 1. Establish the Endpoint and Client

Confirm the actual HTTPS GitLab instance URL, target project, deployed version,
and client. The official endpoint is `https://gitlab.example.com/api/v4/mcp`;
replace the example host with the confirmed instance. Check instance access and
the target version's MCP prerequisites with its owner. Do not derive a web port
from an SSH remote or enable instance-wide features without authority.

Use the official MCP endpoint and its supported OAuth flow. A normal Git login
or an arbitrary API token is not proof of MCP authentication. Current GitLab
supports OAuth tokens with `mcp` scope; other token support is version-dependent.
See [GitLab MCP authentication and transports](https://docs.gitlab.com/user/model_context_protocol/mcp_server/).

## 2. Configure, Authenticate, and Load Tools

Inspect existing client profiles before writing. Reuse a matching endpoint and
identity instead of adding competing profiles. For a new native HTTP profile,
preview the project-scoped configuration with the shared helper, then apply it
once the preview matches the selected scope. For example, after verifying that
`get_mcp_server_version` is the server's actual permitted discovery tool:

```sh
python3 addons/configure_mcp.py --adapter gitlab --client codex --url https://gitlab.example.com/api/v4/mcp --tool get_mcp_server_version
python3 addons/configure_mcp.py --adapter gitlab --client codex --url https://gitlab.example.com/api/v4/mcp --tool get_mcp_server_version --apply
```

This writes configuration only; it does not log in or prove connectivity. Follow
the shared guide for the actual profile name, client authentication, project
trust, and reload/new-session steps. The user's explicit setup request authorizes
scoped client setup; it is not blanket authority to mutate GitLab tickets.
For Claude Code or VS Code, select the corresponding helper client and complete
its supported authentication flow. Do not invent flags or share a user-global
configuration across clients merely because they all speak MCP.

Initialize MCP, retrieve the actual tool schemas with `tools/list`, including
all pages, and read the target project identity and version where exposed.
Refresh the allowlist from the real catalog; classify tools by operation, not
only a name such as `get` or `save`. Confirm the tools are visible in the session
that will execute the adapter. A separate probe or saved configuration alone
does not prove the current chat loaded those tools.

### Use Discovered Project Identifiers Without Double Encoding

Resolve the project through authenticated search and record its numeric project
ID. Prefer that numeric ID, passed as the schema's expected string/integer, for
subsequent issue calls. A Git remote's SSH path is not an API identifier. Do not
pre-percent-encode a namespace/project path for an MCP tool unless that tool's
schema explicitly requires it; the server may encode it again and return a false
not-found result. If a path lookup fails but issue search returns a verified
numeric project ID, retry one authorized read with that ID before concluding
that permissions or the entire issue operation are unavailable. Keep `iid`
project-scoped and separate from the issue API ID.

## 3. Gate the Requested Workflow Before Ticket Creation

Record a matrix with actual tool name/schema, authenticated target read, required
permission, test result, and limitations for every selected operation:

| Operation | Required evidence |
| --- | --- |
| Read/search | Exact project identity; stable-marker lookup across relevant states and all result pages |
| Parent ticket | Create or reuse the intended issue, with `SPEC-<number>:` visible in its title |
| Child tasks | Native GitLab Task creation/conversion and native parent assignment to that issue |
| Content/status update | Supported update of selected managed fields and chosen workflow state |
| Hierarchy read-back | Child type and parent identity from the task, and matching child list from the parent |
| Repeat without duplicates | Stable IDs and native mappings reused; no second parent, child, or relation |

Do not discover a missing parent or update operation only after bulk creation.
Tool presence is not effective write permission; a read-only configuration is
not a working write adapter. Test writes only inside the approved object/field
scope, read results back, and leave unsupported required workflows blocked.

An issue with links or checkboxes is not a native Task hierarchy. GitLab's
[Tasks](https://docs.gitlab.com/user/tasks/) documentation describes tasks under
issues, and [Child items](https://docs.gitlab.com/user/work_items/child_items/)
distinguishes them from other planning types. Verify this on the deployed
version. A link-only mode does not satisfy the required parent/child workflow.

## 4. Native OAuth Failure and Controlled Proxy Path

Try native HTTP first unless a working matching profile already exists. Preserve
that working profile and its approved scope. If authentication fails, isolate
endpoint/DNS, TLS trust, OAuth metadata/issuer, login, tool discovery, and resource
permission. Do not loop through registration or report a private 404 as proof
that the project does not exist.

A local test on GitLab MCP 19.2 with Codex CLI 0.164.0 recorded an
`Authorization server issuer mismatch` before browser login. A pinned
`mcp-remote` 0.16.6 stdio proxy subsequently authenticated. This is a recorded
compatibility case, not a guarantee for every instance or a reason to replace a
working native connection. Recheck the versions and issuer metadata first;
select the proxy only for a concrete supported need and record the choice.

The [Codex proxy example](mcp/codex-proxy.toml.example) has no credentials. Resolve
its endpoint, Node/npx executable, private authentication-store path, and actual
read-tool allowlist before merging only the selected profile. Review/install the
pinned dependency through the existing package process. Do not use `@latest` or
silently change a global profile. Authenticate interactively, reload the client,
and rerun initialization, tool discovery, target reads, and the workflow matrix.
The example starts with a read-only tool allowlist and proxy filters. Before
scoped writes, review the exact supported tool/operation and the minimal filter/
allowlist diff, apply it only within authorization, and restore the agreed standing
scope afterward. Never enable every write tool merely to test one operation.
Use the client's supported certificate trust configuration if required; never
turn off TLS or issuer verification. Keep the auth store outside the repository,
limit its filesystem permissions, and never inspect or log its token contents.

The proxy does not add server operations. In the recorded 19.2 test, read/create
operations were available but issue-title/status/type/parent updates were not.
The note tool rejected Quick Actions. Do not encode slash commands or otherwise
bypass that validation to simulate missing update tools. Current
[GitLab MCP tool documentation](https://docs.gitlab.com/user/model_context_protocol/mcp_server_tools/)
also documents note-body restrictions; the live catalog remains decisive.

For missing required operations, select a supported MCP server/version or a
separately reviewed API/UI execution path with the user; record which operations
remain outside MCP. Do not silently downgrade the adapter to manual instructions
or call the requested hierarchy complete. Preserve existing objects and IDs
while preparing corrections; never create replacement tickets as an update path.

## 5. Completion, Durability, and Shutdown

Record separate states for configured, authenticated, tools loaded, read verified,
and required workflow verified. Include exact versions/profile reference,
capability matrix, target IDs, authority, native parent/child mappings, permitted
operations, and actual evidence in the durable project record. No saved state may
claim `ready` merely because a TOML/JSON file parses.

Keep the selected runtime profile independent of `addons/`: no executable or
configuration import may rely on a removable example file. For shutdown, use the
[deactivation prompt](deactivation-prompt.md). Complete required knowledge
migration before disabling the selected client profile or revoking dedicated
access; preserve unrelated profiles and shared OAuth grants.

## References

- [Official GitLab MCP server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)
- [Official MCP tools](https://docs.gitlab.com/user/model_context_protocol/mcp_server_tools/)
- [Official MCP troubleshooting](https://docs.gitlab.com/user/model_context_protocol/mcp_server_troubleshooting/)
- [mcp-remote maintained source and flags](https://github.com/punkpeye/mcp-remote)

The compatibility case above comes from the local GitLab test's recorded evidence.
This guide does not assert new live authentication, write, or hierarchy results.
