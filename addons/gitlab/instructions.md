# GitLab Integration Instructions

Apply the [shared lifecycle](../README.md) and existing project gates. These
instructions do not grant external write authorization or enable background work.

## Discover and Decide

- Inspect existing project instructions, documentation roots, task IDs, issue
  conventions, repository remotes, and GitLab CI/CD boundaries without replacing
  them. Resolve the exact host and project namespace; a group board may span
  projects and is not itself an issue destination.
- Establish target instance/version and features actually available. Verify the
  authorized tool's access and supported operations for issues, labels, boards,
  milestones, and merge request references separately. Do not promise all features
  based on a generic GitLab connection. If access is unavailable, provide manual
  steps and report live setup as unverified.
- Resolve scope, authoritative source per field, direction, trigger, owner,
  mappings, conflict policy, and allowed writes before dependent changes. Preserve
  existing decisions and reuse current authorization within its actual limits.
  Record explicit deferrals and leave dependent operations inactive.
- Inspect existing automations and issue closing behavior before proposing changes.
  Do not configure webhooks, jobs, pipelines, or release processes implicitly.

Check visibility before copying repository content into external issues or boards.
Do not expose confidential source material to a broader audience.

## Mapping Contract

Record the chosen mapping in the existing project documentation root. The example
below is a starting point for decisions, not an installed configuration:

| Delivery information | GitLab representation | Decision required |
| --- | --- | --- |
| Stable task ID, such as `TASK-010-001` | Issue description marker | Uniqueness scope and authoritative source |
| Task title and acceptance criteria | Issue title and managed description sections | Managed fields and preservation of other content |
| Task status | Open/closed issue state and agreed labels or board convention | Exact mapping and allowed transitions |
| Owner | Issue assignee | Account mapping and unmapped-user handling |
| Delivery milestone | GitLab milestone, if selected and available | Existing milestone reuse and ownership |
| Spec and verification evidence | Repository links in issue | Stable paths and visibility |
| Implementation | Merge request reference | Evidence independent of merge status |

Persist the host, project identity/path, issue URL and project-scoped issue number
(`iid`), and API identifiers if the selected tool needs them. Record board scope
and chosen labels/milestones separately. Do not substitute an issue's API ID for
its project-scoped number or treat either as a Delivery task ID. Preserve existing
task IDs and check for a mapped issue before creating another one. Do not move
issues across projects as a routine mapping operation.

Board labels and closed state need an explicit contract; moving a card can change
issue data. Verify the target board's behavior and available features instead of
assuming every board supports the same workflow. Do not rename shared labels or
reorganize shared boards without authorization.

## Execution and Failure Handling

Use authorized read-only inspection first. Prepare a preview of target project,
issue, current values, and proposed changes. Protect unrelated description text,
comments, labels, and assignees; re-read current remote values before writing.
Surface concurrent edits according to the agreed conflict policy rather than
silently overwriting them. Apply only resolved and authorized changes.

Read back changed issue data and any selected board configuration separately.
Record partial success. After an uncertain creation response, search the target
project for the stable task marker before retrying. Do not equate an open merge
request or a merged change with acceptance of the Delivery task. Avoid accidental
closing patterns in generated descriptions or commit messages unless the resulting
transition is intended and authorized. GitLab documents these effects in
[Manage issues](https://docs.gitlab.com/user/project/issues/managing_issues/).

## Durable Handoff

Keep a self-contained project record of owner, targets, verified tool capabilities,
source and mapping decisions, permission scope, credential-location reference
without secrets, triggers, conflict and retry handling, verification results, and
shutdown steps. Route future relevant agent work to that record. Transfer needed
working rules into it so deleting `addons/` leaves the configured workflow usable.
No automated synchronization is installed by this add-on.

Use the [removal guidance](README.md#removal) for shutdown. Preserve the existing
CI/CD pipeline and remote work; disconnecting task integration does not authorize
deleting issues or disabling deployments.

## Product References

- [Issues and project scope](https://docs.gitlab.com/user/project/issues/)
- [Issues API identifiers](https://docs.gitlab.com/api/issues/)
- [Issue boards](https://docs.gitlab.com/user/project/issue_board/)
- [Issue and merge request crosslinks](https://docs.gitlab.com/user/project/issues/crosslinking_issues/)

Recheck current official documentation and the target instance before making
claims about edition-specific features or available tool operations.
