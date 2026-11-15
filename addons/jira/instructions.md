# Jira Integration Instructions

Apply the [shared lifecycle](../README.md) and the project's canonical workflow.
Load only the project sources relevant to this integration.

## Discovery and Decisions

Before dependent changes, establish and record:

- Site URL, edition/version, target project key and ID, integration owner, and
  allowed issue types. Confirm the target through authorized read-only discovery.
- Current task/spec structure, stable IDs, existing Jira links, and any existing
  synchronization. Do not replace IDs or create a second issue for the same task.
- Authority per field: requirements, acceptance criteria, task status, assignment,
  and evidence. Preserve the project's documented authority until an explicit
  decision changes it; update any conflicting project instructions together.
- Link-only, one-way publication, one-way import, or individually agreed field
  directions. Define the trigger and operator; this add-on supplies no scheduler.
- The available connector/API operations, credential reference, required
  permissions, and readable/writable project scope. Keep secrets out of outputs.

Ask focused questions for unresolved decisions. Do not guess project keys or
workflow values, and do not proceed with actions depending on unanswered questions.

## Mapping

Prepare a mapping before creating or updating issues. This is a design example,
not an assumed Jira configuration:

| Delivery content | Candidate Jira representation | Decision to record |
| --- | --- | --- |
| Stable task ID | Agreed description marker or existing custom field | Exact location and duplicate lookup |
| Task title | Summary | Authoritative source |
| Spec and acceptance criteria | Source links and selected description content | Content ownership and format |
| Task status | A project workflow status reached through a valid transition | Allowed status/transition mapping |
| Owner | Verified Jira account | Assignment authority; preserve role versus person distinction |
| Blocker and verification evidence | Agreed field, link, or description section | Representation and update direction |

Discover creation/edit metadata for the selected project and issue type rather
than inventing mandatory fields. Jira Cloud REST v3 descriptions use Atlassian
Document Format; do not send raw Markdown as if it were that format. Inspect the
connector's accepted format and preview the resulting content. Retrieve valid
transitions for each issue; do not treat status as an arbitrary editable string.
See the [official issue reference](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/).

Keep the original Delivery task ID stable and store the external issue ID, key,
and URL in the mapping. Search the agreed scope and existing mapping before
creation. A title match alone is insufficient to establish identity.

## Execution and Failure Handling

Prepare a concrete change preview with target issues, field differences, and any
new records. Reuse authorization already granted for those operations; obtain
missing authorization before external writes. Setup selection alone is not bulk
issue creation or deletion permission. Do not comment, notify, assign, or transition
issues outside the agreed scope.

Re-read affected remote values before updates. If a value changed since the
preview, stop that update and reconcile it with the authoritative source. For an
ambiguous creation result, check whether the issue exists before retrying. Record
partial results without duplicating successful operations. Respect service and
tool rate limits; report permission, validation, or unavailable-tool errors
without broadening access automatically.

## Durable Record and Verification

Create or update an integration record under the existing project documentation
root. Include decisions above, exact mappings, permitted operations, trigger and
operator, external IDs/URLs, access references, verification evidence, recovery,
and retirement steps. Link it from the project's task-relevant workflow guidance.
The record must contain all ongoing rules; do not leave mandatory references to
files under `addons/`.

Validate with one representative existing task and a prepared preview. If a write
is authorized, verify the resulting issue by reading it back and check that its
criteria, source link, status, and stable ID match. Otherwise report preview-only
verification and the missing access/action. Exercise repeated preparation to
confirm no duplicate is proposed. Preserve existing IDs, unrelated issues,
project rules, and unresolved-question gates. Verify the durable record remains
usable after the add-on instructions are removed from a temporary project copy.
