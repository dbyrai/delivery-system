# Jira Add-on

Use this optional add-on to connect Delivery System requirements and tasks to a
selected Jira project. It supplies instructions and an adaptation prompt; it
installs no connector and runs no synchronization service.

## Prerequisites and Scope

Identify the Jira site, Cloud or Data Center edition, project, responsible owner,
and an approved access method. A Jira account alone does not establish that the
current AI tool can read or write issues. Check its actual available operations
and permissions before promising a workflow.

Possible uses include linking existing issues, preparing new issues from ready
tasks, and reconciling agreed status fields. Each use requires a project-specific
mapping and source-of-truth decision. Existing Delivery System gates still apply:
a Jira issue does not make an unresolved requirement ready for implementation.

## Use

1. Read the [shared add-on lifecycle](../README.md).
2. Select the Jira add-on and copy the [integration prompt](integration-prompt.md)
   into the AI tool used for the project.
3. Follow the [Jira instructions](instructions.md) to establish the target,
   available capabilities, authority, mapping, and permitted actions.
4. Review the prepared changes and verify the resulting integration record.

No project key, issue type, custom field, transition, account, or synchronization
direction is predefined by this add-on.

## Removal

Unused files under `addons/jira/` can be removed; remove their index references
as well. After setup, first verify that the project's durable integration record
contains its rules and is linked from task-relevant project guidance without a
runtime dependency on this directory.

Deleting this directory does not disconnect Jira. To retire an active integration,
stop its agreed triggers or jobs, remove only the related local routing, and
revoke dedicated credentials or app grants through the established access owner.
Check whether grants or jobs serve other projects before changing them. Preserve
issue links and mapping history as delivery evidence. Deleting Jira issues is a
separate action requiring explicit scope and authorization.

## Official References

- [Jira Cloud issue operations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/): creation metadata, editing, and transitions.
- [Jira Cloud REST API overview](https://developer.atlassian.com/cloud/jira/platform/rest/v3/): API version and content representations.
- [Jira Data Center REST API](https://developer.atlassian.com/server/jira/platform/rest/v10000/api-group-issue/): an edition-specific reference, not a Cloud compatibility guarantee.

Cloud references were reviewed for this add-on. Verify the deployed edition,
current documentation, and selected connector again during setup.
