# v2.1.0 Release Notes — Draft

Publication is pending maintainer review and authorization. These notes describe
the prepared source, not an already published release.

## Summary

The Delivery System gains optional integration add-ons for Jira, Confluence,
GitHub Projects, and GitLab. Each adapter includes mandatory MCP setup,
a client configuration helper, and prompts for adapting and retiring the connection.

## Changes

- Added: `addons/README.md` with selection, a shared setup lifecycle, durable
  project records, and separate removal of instructions versus active connections.
- Added: four MCP-backed adapters, each with a README, operation instructions,
  product MCP setup, integration prompt, and deactivation prompt.
- Added: `addons/configure_mcp.py` previews and merges project HTTP profiles for
  Codex, Claude Code, and VS Code without credentials or implicit login.
- Added: mandatory native ticket/task hierarchy and visible stable ID titles,
  with update/parent/read-back capability gates before ticket creation.
- Added: pinned GitLab proxy example and explicit unsupported-operation handling;
  proxy authentication does not supply missing update/hierarchy tools.
- Added: deactivation prompts require a remote/local knowledge inventory and a
  user decision about migration or external retention before dependent shutdown.
- Added: a selective adoption guide for existing v2.0.0 projects.
- Changed: root README and delivery handbook include optional discovery links.
- Breaking changes: none. No mandatory bootstrap steps, role-adapter changes,
  preconfigured connections, credentials, or synchronization services are introduced.

Each add-on covers actual tool capability discovery, source authority, stable
mapping, scoped authorization, conflict/retry handling, verification, and teardown.
Required ongoing rules are transferred into the project before optional add-on
files are removed. Product references link to official documentation; actual
client and hosting capabilities must be checked during each project's setup.

## Updating Existing Projects

- Required actions: none for projects retaining their v2.0 workflow.
- Optional changes: copy `addons/README.md`, `addons/mcp-setup.md`,
  `addons/configure_mcp.py`, selected adapter directories, and
  `howto/upgrades/v2.0-to-v2.1.md`; remove index entries for omitted add-ons.
  Merge discovery links only where useful. Follow the
  [adoption guide](../../howto/upgrades/v2.0-to-v2.1.md).
- Preserve existing documentation roots, completed content, task IDs, integration
  rules, diagnostic defaults, and security/approval boundaries. Do not replace
  project documents with this template.
- Verification after adoption: check links and mappings, resolve target-specific
  decisions, verify actual access, and confirm durable records survive removal
  of optional instructions. External writes require their applicable authorization.

## Verification and Limits

Local Markdown links, anchors, fences, whitespace, unchanged core files, and
selective adoption/removal scenarios were checked. Independent QA reviewed the
instructions and prompts. See the [verification record](v2.1.0-verification.md).
Ten local configuration tests pass, including discovery bootstrap, selective
merging, idempotency, environment references, and unsafe-input refusal. Follow-up
tests verified GitLab authentication and reads under the documented client/version
conditions. A [GitHub Free live test](github-adapter-acceptance-2026-11-16.md)
verified native sub-issue hierarchy, issue updates and Project Status updates
through the official MCP server; both disposable targets were removed afterward.
The owner also [reported successful Jira and Confluence reads, writes and updates](atlassian-verification-2026-11-17.md)
in separate projects and accepted that tested scope. These external results were
not independently rerun here. They do not establish V2 connector compatibility,
native Jira subtask writes, duplicate-free repeated setup, migration or
deactivation. Full fresh-session prompt compliance and support for every
client/server edition remain unverified; target-specific validation is required
during setup.
