# Test the Manus Add-on in a GitHub Project

**Updated:** 2026-11-17 · **Status:** Preview; live Manus verification pending.

## Preparation

The tester uses their own Manus account and a GitHub test repository containing
the Delivery System. Do not share accounts. Before edits, verify access, actual
branch, connector/sync mode, and write behavior. For automatic sync, use a test
scope explicitly authorized for it. No production data or Manus API credentials.

Follow the [how-to](howto.md) and [integration prompt](integration-prompt.md).
A local package copy is not live evidence. Make prepared files available in the
selected repository through the authorized Git workflow.

## Shared Cases

| Case | Expected behavior |
| --- | --- |
| Load sources | Manus identifies the correct repository/branch and concrete contents of instructions and task files |
| Missing access | Dependent work stops; no invented context |
| Approved plan with two dependent tasks | Correct execution order without unnecessary repeated authorization |
| Blocking question in a test task | Dependent implementation stops; answer/deferral is recorded |
| Run checks | Actual commands/results traceable per task; missing checks identified |
| Review and rework | Findings addressed in the existing task; Done requires evidence and required acceptance |
| New Manus chat | Current instructions, revision, and next tasks read again |
| Concurrent change | Difference from current GitHub state identified before overwriting |
| Deactivation | Pending work preserved; only authorized add-on routing/access removed |

For a small implementation pilot, choose an approved spec with two tasks, such
as a local function followed by a dependent UI change. Define criteria and test
commands in the test project first; use existing templates and IDs.

## Level 1: Existing Project

Use a repository with code and documentation. Verify that Manus preserves existing
files and task IDs rather than replacing them with templates. A completed adoption
must not trigger a full bootstrap restart. First-time adoption must instead follow
repository review and handbook bootstrap. Then execute the approved pilot.

## Level 2: New Project

Use a fresh repository with the generic delivery structure. Step 0 must be not
applicable. Verify steps 1–12 in order, focused questions, and recorded decisions.
Deliberately leave one blocking question unanswered: no dependent tasks/features
should be generated. Then record an answer or explicit deferral, review the first
spec/task plan, and approve its concrete scope.

Before implementation, require the how-to's bootstrap completion check with step
statuses and output references. Add-on setup or a blanket chat statement must not
trigger implementation. Only then run the pilot and verify its evidence.

## Feedback

For each case, record date, Manus interface, package/repository revision, mode,
branch, steps, expected behavior, and actual result. Use **passed**, **failed**, or
**not checked**. Include diff/commit/PR references, sanitized logs, and test results.
Keep credentials and private content out of public feedback. Record observed
runtime and costs.

Both entry levels run directly in Manus. The account holder can test them without
an API adapter operated by us. Until actual evidence exists, do not claim successful
live verification or production readiness.
