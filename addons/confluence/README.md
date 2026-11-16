# Confluence MCP Adapter

Use this optional add-on to connect selected Delivery System documentation to
Confluence. It supplies a configuration-backed MCP adapter workflow. Setup must configure,
authenticate, and verify the actual connection; no background synchronization
service is installed.

## Prerequisites and Scope

Identify the Confluence site, Cloud or Data Center edition, target space and
parent page, content owner, audience, and approved access method. Verify the
current AI tool's actual page operations and access; an account or connector name
alone does not prove write support.

Possible uses include linking existing pages, publishing selected documentation,
or importing agreed content. Decide which source owns each document or section
before setup. A Confluence copy must not silently become a competing authority
for requirements or acceptance criteria.

## Use

1. Read the [shared adapter lifecycle](../README.md) and [MCP setup](mcp-setup.md).
2. Select the Confluence add-on and copy the [integration prompt](integration-prompt.md)
   into the project's AI tool.
3. Follow the [Confluence instructions](instructions.md) to confirm scope,
   authority, page mapping, rendering, and permitted actions.
4. Verify the configured MCP connection, scoped publication operations, native
   page hierarchy, linked ticket hierarchy where selected, and durable record.

## Setup Acceptance

A prepared prompt or mapping is not an activated adapter. Follow the MCP setup
capability gate before creating objects. Report missing operations as blocked;
do not create flat replacements for required parent/child objects.

## Removal

Use the [deactivation prompt](deactivation-prompt.md) to retire an active
integration with AI assistance. It uses the durable project record and also
works when the optional add-on files have already been removed.

Unused files under `addons/confluence/` can be removed along with their index
references. After setup, first ensure all ongoing rules are in the project's
durable integration record and linked from relevant project guidance.

Before changing an Atlassian MCP profile, check whether Jira and Confluence share
it. Retire only this adapter's policy when the connection is still needed by the
other adapter; revoke a dedicated grant only within authorization.

Deleting this directory does not disconnect Confluence or remove published
pages. To retire an active integration, stop its agreed triggers/jobs, remove
only its local routing, and have the access owner revoke dedicated credentials
or app grants when no other project needs them. Retain source-to-page mappings
and publication history. Archiving or deleting remote pages and changing page
restrictions are separate operations requiring explicit scope and authorization.

## Official References

- [Confluence Cloud page operations](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/): page identity, body representation, and versioned updates.
- [Confluence Cloud REST API overview](https://developer.atlassian.com/cloud/confluence/rest/v2/): access and API context.
- [Confluence Data Center REST API](https://developer.atlassian.com/server/confluence/rest/): use edition-specific documentation for a Data Center deployment.

Cloud references were reviewed for this add-on. Recheck current deployed-version
documentation and the available connector during setup; no cross-edition
compatibility is implied.
