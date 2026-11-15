# GitHub Projects Add-on

Adapt the Delivery System to a selected GitHub repository and a user- or
organization-owned Project. This optional add-on provides setup guidance and an
AI prompt; it installs no connector or synchronization service.

## Prerequisites and Use

1. Read the [shared add-on lifecycle](../README.md).
2. Identify the repository, Project owner and URL, and the intended issue scope.
3. Have an authorized tool or manual access path available. Verify repository
   access and Project access separately; do not paste credentials into chat.
4. Read the [integration instructions](instructions.md), then copy the
   [integration prompt](integration-prompt.md) into your AI tool.

GitHub Projects can contain issues and pull requests and provide custom fields.
A Project item and its underlying repository issue are distinct resources;
verify the actual tool's support for both before promising updates. See
[About Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
and [Understanding fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields).

## Scope

Select repository issues, Project membership and fields, and pull request links
as needed. Preserve Delivery task IDs alongside GitHub identifiers. The add-on
does not merge pull requests, configure Actions, publish releases, or enable
background automation merely by being selected.

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
