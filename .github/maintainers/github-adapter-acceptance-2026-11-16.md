# GitHub Adapter Live Acceptance — 2026-11-16

## Result and Boundary

Basic GitHub MCP operations passed on an account whose billing UI showed
**GitHub Free** and **Copilot Free**. One new private repository and one new
private user Project were created solely for this test and subsequently deleted
with explicit user confirmation. No paid feature, subscription, Actions run,
Codespace, or additional AI model invocation was requested for this acceptance
run. This is evidence about the tested operations, not an audit of unrelated
account charges or the AI client's usage limits.

The existing connected GitHub tool catalog lacked repository creation, Project
management and native sub-issue mutations. The test therefore used the official
`github/github-mcp-server v2.1.0` through an isolated Python JSON-RPC stdio
acceptance harness. It did not extract credentials from the existing connector
or alter its configuration. The separate browser OAuth requested `repo,project`;
the token remained in server memory. An initial request including `delete_repo`
was rejected by automatic approval review and was not executed. The tested route
omitted that scope and used authorized UI cleanup instead.

## Targets and Identity

| Resource | Created identity |
| --- | --- |
| Owner | `dobosolution` |
| Repository | `delivery-system-mcp-test-20261116-5da065`, numeric ID `1459708129` |
| Project | `Delivery System MCP Test 2026-11-16 5da065`, number `1`, node ID `PVT_kwHOALjyhs4Br0TN` |
| Parent | `SPEC-001`, issue `#1`, API ID `6416750517`, Project item `306531921` |
| Task | `TASK-001-001`, issue `#2`, API ID `6416750674`, Project item `306531944` |

The identities remain in this evidence after deletion; these are not active
integration targets. Only synthetic test content was sent to GitHub. GitHub
confirmed both resources were private before issue writes.

## Verified Operations

Thirty MCP calls covered authentication, target discovery/creation, reads,
writes, inventory and post-cleanup searches. The runtime catalog and selected
responses are retained as [structured evidence](artifacts/github-adapter-2026-11-16/acceptance.json)
and [tool schemas](artifacts/github-adapter-2026-11-16/catalog.json), without
credentials, authorization URLs, browser session values or raw authentication
logs. The official Darwin arm64 release artifact's SHA-256 was verified before
execution; its digest is in the structured evidence.

| Check | Actual result |
| --- | --- |
| Authentication | Official local server browser OAuth; `get_me` returned the expected account. |
| Repository and Project access | Separate reads confirmed exact identities and private visibility. |
| Visible IDs | Created `SPEC-001: MCP adapter acceptance test` and `TASK-001-001: Verify GitHub adapter workflow`. |
| Native hierarchy | Read the child's absent parent, called `sub_issue_write/add` with numeric API ID, then verified `get_parent` and the parent's child list. |
| Updates | Updated task title/body and closed it with `completed`; independent issue read confirmed all values and preservation of unmanaged text. |
| Project mapping | Added both issues, discovered the Status field/options, updated the task to `Done`, then independently read back that value. |
| Reconciliation | Enumerated open and closed issues and Project items; exactly two issues and two distinct items matched the map. A second inspection found the existing native relation, so no replacement or repeat mutation was needed. |
| Pre-cleanup inventory | Read both bodies, states, hierarchy, Project items/status and both comment lists; retained synthetic snapshots before removing access/targets. |
| Cleanup | GitHub UI confirmed deletion of the exact Project and repository after user confirmation; MCP searches then returned zero matching Projects and repositories. |
| Runtime retirement | Stopped the isolated server successfully. No global or project client profile was installed, and existing account grants were not revoked. |

## Limits and Follow-up

This is a live protocol acceptance test, not execution of the copyable integration
prompt in a fresh AI-client session. Automatic configuration loading, repeated
model-driven setup, production deactivation-prompt behavior, conflict handling,
concurrent writes, and organization/Enterprise policies remain unverified. The
second inspection verified reconciliation inputs and absence of duplicates; it
is not a full repeated prompt test. No additional model process was started.

Removing disposable targets is separately authorized test cleanup. It does not
prove that normal deactivation preserves production history or performs a full
knowledge migration. The copied synthetic snapshots are acceptance evidence,
not an adopting project's migrated knowledge base.

The tested MCP catalog supports removing Project items but not deleting a Project
itself. UI cleanup must not be reported as a successful MCP Project deletion.
OAuth scopes can cover other account resources; only the newly registered test
targets were mutated. No upstream commit, push, tag or release was performed.

GitHub's [official availability statement](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/extend-copilot-with-tools-and-context/set-up-the-github-mcp-server)
says MCP availability is independent of plan, with feature-specific licensing
still applying. The adapter README now distinguishes this from authentication
and tool/permission gaps.
