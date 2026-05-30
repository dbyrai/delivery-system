# Test Strategy

This document defines the default approach for project verification.

## Goals

- Verify that delivered work satisfies documented requirements.
- Catch regressions in critical flows.
- Keep checks practical and maintainable.
- Make manual verification repeatable.

## Test Levels

| Level | Purpose | Typical Owner |
| --- | --- | --- |
| Unit | Validate small isolated logic | Developer |
| Integration | Validate module or service boundaries | Developer / QA |
| End-to-End | Validate complete user flows | QA |
| Manual | Validate flows that are hard to automate or need human judgment | QA / Product |

## Minimum Expectations

- Each spec should define acceptance criteria.
- Each task should define verification.
- Critical flows should have repeatable checks.
- Bug fixes should include regression coverage when practical.

## Test Evidence

Record useful evidence in the task file or under `docs/tasks/artifacts/`.

Examples:

- Commands run
- Test output summaries
- Screenshots
- Manual test results
- Known failures and explanations

## Open Questions

- Supported environments: TBD
- Required automated test framework: TBD
- Release sign-off process: TBD
