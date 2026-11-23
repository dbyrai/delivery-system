# v2.4.0-rc.1 Release Notes

## Summary

Delivery System v2.4.0-rc.1 adds the optional Manus add-on as a preview for
external live validation. It guides direct work with a GitHub repository in
Manus without requiring a separate Manus API integration or self-hosted service.

## Changes

- Added two entry levels: adopt an existing project or bootstrap a new project.
- Added setup, operating, implementation, review, handoff, and deactivation
  guidance for direct GitHub project work in Manus.
- Added reusable assignment, implementation, and project-instruction templates.
- Added a graphical workflow and a test guide for live Manus verification.
- Added a first-time-user quickstart for creating and connecting a new project.
- Added release-candidate guidance to the maintainer release workflow.
- Breaking changes: none. The add-on is optional and does not change the core
  bootstrap or existing integrations.

## Updating Existing Projects

- Required actions: none for projects that do not use Manus.
- To test Manus, adopt `addons/manus/` and the Manus discovery links selectively.
- Preserve existing project documents, task IDs, approval rules, and completed
  bootstrap state.
- Record the exact release-candidate tag or commit in the test evidence.

## Verification and Preview Limits

The package is reviewed and checked locally before publication. Live behavior in
Manus, including repository selection, instruction loading, branch and pull
request behavior, blocker handling, cross-tool handoff, and deactivation, remains
to be verified by the external pilot described in `addons/manus/test-guide.md`.

This release candidate must not be described as production-ready. Record the
tester, date, Manus interface, exact revision, expected and actual results,
sanitized evidence, runtime, and costs. Resolve or explicitly accept findings
before publishing v2.4.0.
