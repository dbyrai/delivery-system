# GitHub Projects Integration Instructions

Apply the [shared lifecycle](../README.md) and existing project gates. Select
this add-on explicitly; no external write is authorized by these instructions.

## Discover and Decide

- Inspect existing repository instructions, documentation roots, task IDs,
  decisions, issue templates, and active delivery tooling. Preserve them.
- Resolve the GitHub host, exact repository, Project owner and URL, and whether
  the scope covers issues, pull requests, Project fields, or selected subsets.
- Read the actual tool's capabilities. Confirm authenticated identity, access to
  the target resources, and support for each requested operation. Issue access
  does not prove Project field access. If unavailable, provide manual steps and
  label the connection unverified rather than claiming it is active.
- Resolve authoritative sources per field, direction, trigger, owner, and conflict
  policy before dependent changes. Do not introduce a second task backlog by
  default. Record explicit deferrals and leave dependent work inactive.
- Inspect existing Project workflows before setup; do not enable or replace them
  automatically. Reuse prior action authorization within its actual scope.

Check visibility before copying repository content into external issues or boards.
Do not expose confidential source material to a broader audience.

## Mapping Contract

Record the selected mapping in the project's existing documentation root. The
following is an example, not a required schema or a decision for the user:

| Delivery information | GitHub representation | Decision required |
| --- | --- | --- |
| Stable task ID, such as `TASK-010-001` | Issue body marker or agreed field | Marker, uniqueness scope, and authoritative source |
| Task title and acceptance criteria | Issue title/body sections | Managed sections and preservation of other content |
| Task status | Project Status field and issue open/closed state | Explicit mapping; these states are separate |
| Owner | Issue assignee or selected Project field | Account mapping and handling of unmapped users |
| Spec and verification evidence | Repository links in issue | Stable links and allowed visibility |
| Implementation | Linked pull request URL | Evidence requirements independent of merge state |

Persist host, repository identity, issue URL/number, Project identity, item ID,
and selected field/option identifiers as available. Do not treat issue numbers
as globally unique or confuse them with Project item IDs. Preserve existing task
IDs; verify an existing match before creating an issue or adding another item.
A draft item must not silently become a repository issue or replace an existing
issue. Verify conversion behavior and obtain any missing authorization first.

## Execution and Failure Handling

Start with authorized read-only inspection. Prepare a concrete change preview
showing each target, managed field, current value, and intended value. Apply only
resolved, authorized operations, checking the current remote state first. If
concurrent edits conflict with the agreed source, stop that update and surface
both values; do not overwrite unrelated issue text or comments.

Read back changed issues and Project fields separately. Report partial success
and remaining work. Before retrying an uncertain create or membership update,
look up the recorded stable ID and existing item to avoid duplicates. Do not
close issues or mark tasks done merely because a pull request exists or merges;
apply the project's acceptance gates. Inspect closing keywords in proposed text
and avoid unintended lifecycle changes.

## Durable Handoff

Record the connection owner, targets, verified capabilities, credential-location
reference (never the secret), source and mapping decisions, authorization scope,
manual or automated trigger, failure handling, verification results, and removal
steps in the project. Update only relevant project routing to that durable record.
Copy needed operational rules into it instead of linking runtime behavior back to
`addons/`. No recurring job or webhook is installed by this add-on.

For shutdown, follow the [removal guidance](README.md#removal). Do not delete
remote work or revoke shared access as a shortcut for removing local instructions.

## Product References

- [Projects and their items](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [Project field types](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields)
- [Linking pull requests to issues and closing behavior](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)

Recheck official documentation for the target GitHub edition and the actual tool
before using capabilities beyond those verified during setup.
