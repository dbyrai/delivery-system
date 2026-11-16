# GitHub MCP Adapter Setup

Use the [shared MCP setup](../mcp-setup.md), then apply this product profile.
This adapter must configure and verify MCP access; copying instructions or
preparing manual steps alone is not a completed connection. No synchronization
service or remote object is installed merely by selecting the adapter.

## Account Plan Is Separate from Authentication

The official MCP server is available regardless of GitHub plan; individual paid
features still require their own licenses. Do not assume a paid Copilot plan is
required for basic issue/sub-issue/Project operations from another MCP client.
Read the [account and test prerequisites](README.md#free-accounts-and-live-test-requirements),
then verify the selected account, permissions, actual tools, and target. An
unconnected profile or missing token is an authentication gap, not a pricing result.

## Endpoint and Authentication

For GitHub.com, the official hosted Streamable HTTP endpoint is
`https://api.githubcopilot.com/mcp/`. Use an already configured connection when
its host, authenticated identity, target scope, and capabilities match. Verify
GitHub Enterprise Cloud/Server support against its edition and official server
instructions; do not send a private Enterprise Server token to the public host.

Authenticate through the selected client's supported OAuth flow or a securely
supplied, least-privilege PAT. For PAT-authenticated Codex, GitHub documents
`bearer_token_env_var = "GITHUB_PAT_TOKEN"`. This is a variable name, not a secret.
The actual token belongs in the client's approved secret/environment mechanism,
not project files, command arguments, chat, or logs. A GUI client's process may
not inherit the shell's environment; verify availability without printing values.

Preview project-scoped configuration from the project root. The example selects
only a read tool documented by the official server; confirm its exact name in
the deployed catalog. Add the other discovered tools only after reviewing them.

```sh
python3 addons/configure_mcp.py --adapter github-projects --client codex \
  --url https://api.githubcopilot.com/mcp/ \
  --bearer-token-env-var GITHUB_PAT_TOKEN --tool issue_read
```

After reviewing the destination and current configuration, repeat with `--apply`
to merge the selected profile. See the shared guide for `claude-code` and `vscode`
configuration, authentication, client trust, and reload requirements. A matching
existing profile must be reused rather than creating a second credential grant.
The helper writes configuration only; it does not authenticate, discover tools,
or prove a live connection. Do not replace a pre-existing global profile to fit
this example.

The GitHub server can filter toolsets and tools, including a read-only mode.
If the deployed catalog omits Projects or hierarchy tools, inspect its actual
server filters and client allowlist; do not assume repository access includes
Project access. Enable only the approved tools needed for the selected workflow.
A read-only connection is useful discovery access, not a full write adapter.

### Local Official Server with Browser OAuth

If the existing connector lacks Projects or native hierarchy operations, the
official local server is another supported route. Release `v2.1.0` provides
built-in browser OAuth in its official binaries; a PAT is not required for this
route. Obtain the binary for the host platform from the official release and
verify its published checksum before use. For example, after replacing the
absolute binary path:

```toml
[mcp_servers.delivery_github]
command = "/absolute/path/to/github-mcp-server"
args = ["stdio", "--toolsets", "context,repos,issues,projects", "--oauth-scopes", "repo,project"]
enabled_tools = []
```

This is an alternative profile, not an instruction to replace a working shared
connection. Start with discovery, review the actual catalog, then enable only
the required tools and reload the client. Keep the callback process alive during
browser approval. Official local OAuth retains its token in memory; restarting
can require authentication again. A pre-existing PAT environment variable takes
precedence, so verify the intended authentication route without printing secrets.

The OAuth `repo` and `project` scopes can cover more than the selected test
targets: a project-scoped client file does not narrow GitHub's account grant.
Review the consent screen and restrict operations to approved targets. Do not
request `delete_repo` merely to test this adapter. Repository and Project deletion
are separate cleanup operations, not normal adapter deactivation. In the tested
`v2.1.0` catalog, `projects_write` can remove items but cannot delete the Project
itself; arrange authorized cleanup before creating disposable targets.

See the [versioned OAuth guide](https://github.com/github/github-mcp-server/blob/v2.1.0/docs/oauth-login.md)
and [official release](https://github.com/github/github-mcp-server/releases/tag/v2.1.0).

## Connection and Operation Preflight

1. Start or reload the chosen MCP client. Complete authentication using its
   secure UI or secret mechanism. Run MCP initialization and list the actual
   tools; record server/client versions and schemas, excluding secrets.
2. Use allowed reads to confirm the exact repository and existing parent issues.
   Read the selected Project owner, identity, items, and fields separately.
3. Populate this matrix with actual tool names, supported methods, target access,
   and evidence before creating any issue for a parent/child workflow:

| Required operation | Official server examples to inspect | Required evidence |
| --- | --- | --- |
| Read/search existing issue identities | `issue_read`, available issue search | Existing marker lookup across relevant states, exact repository scope |
| Create and update title/body/state | `issue_write` methods | Schemas and access path; title includes stable Delivery ID |
| Add an existing task under its parent | `sub_issue_write` with `method=add` | Native relation supported; numeric sub-issue API ID distinguished from issue number |
| Read both hierarchy directions | `issue_read` with `get_parent` and `get_sub_issues` | Child parent and parent child-list can be read |
| Read and update selected Project fields | `projects_get`, `projects_list`, `projects_write` | Selected fields/items supported independently of issue writes |

These names are examples from current official source, not a guarantee about the
active server. A tool's presence is not proof of write permission. Inspect schema
and access evidence without an unauthorized probe; verify actual writes only
within the approved test plan. Where fine-grained tools replace combined methods,
map their discovered operations instead. No hardcoded complete-tool claim is valid.

If create is supported but update, hierarchy, or read-back is missing, stop before
creating a flat replacement structure. Record the missing operation and configure
a supported MCP server/toolset/client profile. A separate authorized API route
can be proposed, but manual instructions or another transport must not be labelled
completed MCP setup. Do not bypass client policy, add unrestricted tools, or use
comments/closing keywords to emulate hierarchy mutations.

## Native Hierarchy and Visible Names

Use the existing stable IDs in visible titles, for example:

```text
SPEC-001: Minimal Local Team Task Tracking
  TASK-001-001: Create the minimal local task tracker
  TASK-001-002: Validate task input
```

Each task is a native GitHub sub-issue of its actual parent issue. Shared Project
membership, a checklist, a comment, or a body URL is not this relationship. Preserve
existing stable IDs and remote issue identities. For an adopted project with a
different ID convention, keep its identifiers and record their title format.
A new parent without an existing ID receives a unique stable ID in the project's
identity register before creation; do not renumber existing records.

Before each relation update, read its current parent. If already correct, make no
write. A different parent is a conflict requiring an explicit decision; do not
silently replace it. Re-read the child parent and the parent's paginated children
until the selected task is verified exactly once. Project field read-back is an
additional check, not a substitute for hierarchy verification. If creation succeeds
and parent assignment fails, record partial state and retry the relationship only
after reconciliation; never create another issue as the repair.

## Completion and Retirement

Mark MCP configuration, authentication, active-session tool loading, target reads,
write tests, and verified hierarchy as separate states. A configured profile or
successful search alone does not make the adapter ready for the full workflow.
Record the exact configuration path/profile and non-secret credential reference
in the durable project record. Active operational rules and hierarchy mappings
must survive deletion of optional add-on source files.

Use the [deactivation prompt](deactivation-prompt.md) to migrate required remote
knowledge before retiring access. Remove or disable only the owned MCP profile
or tool permissions after checking shared consumers. Keep native parent/child
relations and issue history unless their removal is separately authorized.

## Official References

- [Hosted endpoint and server-side tool filters](https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md)
- [GitHub's Codex authentication recipe](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-codex.md)
- [Current official MCP tool definitions](https://github.com/github/github-mcp-server/blob/main/README.md)
- [Native GitHub sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues)
- [Sub-issue API identities and permissions](https://docs.github.com/en/rest/issues/sub-issues)

Recheck these sources and the actual server catalog for the target edition during
setup. The local `v2.1.0` route was exercised with a protocol acceptance harness
against disposable GitHub Free targets. This does not verify automatic profile
loading or prompt behavior in every AI client.
