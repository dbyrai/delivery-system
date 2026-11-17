# GitHub Projects Adapter

Adapt the Delivery System to a selected GitHub repository and a user- or
organization-owned Project. This optional adapter configures MCP access and
adapts delivery rules through its setup prompt. It does not supply a background synchronization service.

## Prerequisites and Use

1. Read the [shared add-on lifecycle](../README.md).
2. Identify the repository, Project owner and URL, and the intended issue scope.
3. Follow [MCP setup](mcp-setup.md): configure the selected client, authenticate,
   load its tools, and verify repository and Project access separately.
4. Read the [integration instructions](instructions.md), then copy the
   [integration prompt](integration-prompt.md) into your AI tool. Read/create
   support alone is insufficient: update and native hierarchy must be supported
   before creating the selected ticket/task structure.

GitHub Projects can contain issues and pull requests and provide custom fields.
A Project item and its underlying repository issue are distinct resources;
verify the actual tool's support for both before promising updates. See
[About Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
and [Understanding fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields).

## Free Accounts and Live-test Requirements

GitHub states that its MCP server is available to all users regardless of plan.
GitHub Free is therefore not, by itself, a blocker for this adapter's standard
issue, sub-issue, and Project tests. Paid-only GitHub/Copilot features keep their
own license requirements and are outside the basic test scope. Authentication,
repository/Project access, and the actual MCP toolset must still be verified;
sub-issue management requires at least triage permission. The AI client's own
plan and usage limits are separate. See [MCP availability](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/extend-copilot-with-tools-and-context/set-up-the-github-mcp-server)
and [sub-issue permissions](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues).

If authentication or a test target is missing, record live tests as **Not run**
with that reason; do not describe them as blocked by GitHub Free without evidence.

## Scope

Select repository issues, Project membership and fields, and pull request links
as needed. Preserve Delivery task IDs alongside GitHub identifiers. The add-on
does not merge pull requests, configure Actions, publish releases, or enable
background automation merely by being selected.

## Required Ticket Structure

Tickets and tasks have visible stable ID prefixes, for example `SPEC-001: ...`
and `TASK-001-001: ...`. Tasks are native sub-issues of their actual parent issue.
A link in a description or common Project membership is not a parent/child
relationship. The adapter verifies both relation directions and never creates
replacement duplicates to compensate for a missing update/hierarchy capability.

## Removal

Use the [deactivation prompt](deactivation-prompt.md) to retire an active
integration with AI assistance. It uses the durable project record and also
works when the optional add-on files have already been removed.

Unused instructions can be deleted with this directory; remove its index link
and other references. After setup, retain the project's integration record and
working rules independently of these files. Deleting this add-on does not remove
issues, Project items, credentials, or automations.

To disable an active integration, first identify its recorded connections and
owners. Stop only its authorized synchronization jobs or workflows, remove its
agent routing references, and revoke integration-specific access if approved.
Preserve shared access, existing issues, Project history, and pull requests.
Document the resulting source of truth and disposition of mirrored fields.
