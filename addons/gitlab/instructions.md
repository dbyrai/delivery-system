# GitLab Adapter Instructions

Apply the [shared lifecycle](../README.md) and existing project gates. Setup means
establishing a usable MCP-backed adapter, not only producing documentation.
Follow [GitLab MCP setup](mcp-setup.md) before ticket operations. Configuration and
authentication do not grant blanket permission for external content changes.

## Discover, Configure, and Verify

- Inspect existing project rules, documentation roots, task IDs, remotes,
  integration records, and CI/CD boundaries. Preserve existing source authority.
- Confirm the actual HTTPS host, project identity, instance/version, and selected
  client. Reuse a working matching MCP profile instead of duplicating it.
- Configure MCP, complete supported authentication, initialize, retrieve all tool
  schemas, and verify the tools are loaded in the execution session. Check exact
  target access separately from the catalog. Keep credential values out of files,
  process arguments, output, and chat.
- Complete a capability matrix for read/search, parent creation, native child-task
  creation or conversion, parent assignment, managed-field/status updates, and
  bidirectional hierarchy read-back. Include selected labels, boards, milestones,
  or merge-request operations separately if needed.
- A missing required capability blocks that workflow before object creation.
  Explain the exact gap and prepare a supported path for user selection; never
  claim that plain issues or description links satisfy native task hierarchy.
- Resolve authority per field, direction, trigger, owner, conflicts, account/status
  mappings, and authorized operations. Reuse existing decisions and authorization
  within their actual scope. Record explicit deferrals; do not run dependent work.

Check audience before copying content externally. Do not widen access, change
instance settings, disable TLS, or alter pipelines to make setup succeed.

## Required Ticket, Task, and Identity Contract

For a new mapping, use a parent issue representing the specification or agreed
parent ticket, and native GitLab Tasks beneath it. The visible parent title starts
with its stable identifier, for example `SPEC-001: Task tracking`; each child title
starts with its own stable task identifier, for example
`TASK-001-001: Create the task list`. Retain pre-existing equivalent project IDs;
do not renumber existing work or invent a new ID merely to fix a title.

A title marker and a description marker aid identity, but the actual task must
be under the correct parent in GitLab's native Child items hierarchy. Verify
both the task's type/parent and the parent's child list. Do not use two unrelated
issues, a generic related-items link, a Markdown list, a Project board, or a title
prefix alone as an implementation of this relationship. Resolve the actual
instance's allowed work-item types before executing the mapping.

| Delivery content | Required GitLab mapping | Evidence to persist |
| --- | --- | --- |
| Parent/spec ID | Visible parent issue title prefix and agreed description marker | Exact parent URL, project identity, `iid`, API/global ID as needed |
| Stable task ID | Visible native Task title prefix and agreed description marker | Exact child URL/IDs and verified native work-item type |
| Task-to-ticket relation | Native child Task under the selected parent issue | Child's parent identity and parent's child-list read-back |
| Title/criteria/content | Agreed managed sections | Authority, content boundary, latest values and revision evidence |
| Status | Explicit workflow-state contract | Local status versus remote state/labels; permitted transitions |
| Owner | Verified account or preserved role only | Exact role/account mapping; no guessed assignee |
| Evidence/implementation | Source and merge-request references | Verified visibility and stable links |

Do not confuse GitLab `iid`, API/global IDs, and Delivery IDs. Store the exact host
and project scope. Search existing mappings and all relevant open/closed results
before creation, including all result pages. Title similarity alone is not proof
of identity. Reuse an existing object or relation rather than creating duplicates.

For an already populated project, inventory plain issues and current parentage
first. Prepare a reviewed title/type/parent correction plan that preserves IDs,
content, comments, checklists, history, and existing relationships. Stop if a
conversion would lose fields or cannot be verified. Do not reparent an existing
task or move an object between projects without concrete scope and authorization.

## Execution, Conflicts, and Failure Handling

Prepare a concrete preview with target IDs, current values, proposed titles/types,
parent relationships, managed fields, and exact operations. Validate all required
capabilities before creating a batch. Create/reuse the parent first, then attach
or create children using supported native operations. If multiple steps are
required and one fails, record partial state and stop; do not report a completed
hierarchy or repeatedly create orphan children.

Apply only resolved, authorized changes. Re-read remote values immediately before
updates and reconcile concurrent edits rather than overwriting unrelated text,
comments, labels, or assignees. Read back each changed object and both directions
of each relationship; a create response alone is insufficient. Check intended
status transitions independently of linked or merged merge requests and preserve
acceptance gates.

On ambiguous create results, search the stable ID and stored mapping before
retrying. Respect rate limits and paginate discovery. Do not create replacement
issues to simulate updates. Note/comment tools are not arbitrary mutation APIs:
never use encoded Quick Actions or other tricks to evade a schema/validation
restriction. Missing server tools remain missing after adding a transport proxy.

## Durable Record and Completion

Record selected client profile reference, endpoint, versions, actual capability
matrix, authentication and loaded-session evidence, target IDs, source decisions,
native parent/child mappings, allowed actions, operator/trigger, conflicts/retries,
verification results, and shutdown steps. Keep a credential-store reference only.
Separate `configured`, `authenticated`, `read verified`, `workflow verified`, and
`blocked/partial`; never call setup complete while required hierarchy/update
operations are unsupported.

If the external system is authoritative, fresh-read it before dependent work and
label local copies accordingly. If unavailable, stop dependent changes rather
than treating a stale local snapshot as current. Route relevant future work to
the self-contained project record. Runtime configuration and ongoing rules must
survive deletion of `addons/`; no runtime import may point at an example here.

Verify approved parent/child creation or correction, a scoped update, repeat
execution without duplicates, and teardown separately. Record unrun live checks
honestly. No recurring synchronization, webhook, merge, release, or pipeline
change is installed by this adapter unless separately requested and approved.

For shutdown, follow the [deactivation prompt](deactivation-prompt.md). Complete
required remote-to-local knowledge migration before disabling MCP access. Remove
only the selected profile/grant and preserve shared access, remote history,
parent/child evidence, and existing CI/CD.

## Product References

- [GitLab MCP setup and authentication](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)
- [Actual product tool reference](https://docs.gitlab.com/user/model_context_protocol/mcp_server_tools/)
- [Native Tasks](https://docs.gitlab.com/user/tasks/)
- [Native child-item hierarchy](https://docs.gitlab.com/user/work_items/child_items/)
- [Issues API identity](https://docs.gitlab.com/api/issues/)

Use current documentation for the deployed version and actual schemas. These
instructions do not claim that every GitLab MCP version exposes every operation.
