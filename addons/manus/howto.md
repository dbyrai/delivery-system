# How-to: Develop with Manus, GitHub, and the Delivery System

**Updated:** 2026-11-17 · **Goal:** One GitHub repository per application project;
Manus plans and implements according to its delivery rules.

## Required Order Before Implementation

**Prepare the repository → configure Manus and verify source access → bootstrap
the project → approve specs/tasks → implement → verify and publish.** Copying
delivery files and configuring the add-on do not complete project bootstrap.

| Order | Required outcome before proceeding | Guidance |
| --- | --- | --- |
| A. Prepare repository and delivery files | Correct project state available in GitHub; existing files preserved | Sections 1–2 |
| B. Configure Manus and verify reads | Actual branch, project instructions, and relevant rules demonstrably loaded | Section 3 |
| C. Bootstrap the project | Step 0 handled appropriately; steps 1–12 completed or explicitly deferred; decisions recorded | Sections 4–5 |
| D. Verify implementation readiness | Bootstrap gate satisfied; selected specs/tasks approved; no unresolved dependent blockers | Completion check in section 5 |
| E. Implement and verify | Approved plan executed with tests, status, and acceptance evidence | Section 6 |
| F. Review and publish | Approved source revision; existing Git/release rules followed | Section 7 |

For an already adopted project, verify and preserve its bootstrap evidence.
Address specific gaps without restarting bootstrap. New projects and first-time
adoption require step C. Manus prepares documents and asks the project owner for
missing decisions; it must not invent answers.

## 1. Choose the Project and GitHub Working Mode

You need a Manus account and access to the selected GitHub repository. The account
holder connects GitHub in Manus. This add-on configures no separate API integration.
Preserve application data and configuration. Do not overwrite an application README
with the Delivery System template README.

Official Manus documentation describes two GitHub paths:

| GitHub path | Documented behavior | Delivery System use |
| --- | --- | --- |
| GitHub connector | Connect GitHub under Connectors in Manus and select repository access; branches and PRs supported | Recommended for an existing repository with a review process |
| Manus web-app GitHub sync | Export to a new private repository; automatic pushes to `main` and updates before edits | Use only after explicitly accepting this project's sync behavior |

Sources: [Manus GitHub connector](https://www.manus.im/connectors/github) and
[Manus GitHub Integration](https://manus.im/docs/website-builder/github-integration).
The documented web-app export is not a general import of arbitrary existing
repositories. Verify the available connector functionality for an existing project.
The interface and capabilities can change.

Before edits, establish the repository URL, working branch, read/write access,
and active sync behavior. If project rules require branches and PRs, proceed only
when that path is actually supported. For automatic main sync, clarify and authorize
its commit/push behavior first. Do not use a conflicting mode for implementation.
A prompt saying “do not push” does not technically disable automatic sync.

## 2. Prepare the Delivery System in the Repository

Preserve an existing Delivery System's documentation root, instructions, and IDs.
Otherwise, selectively adopt generic files: `delivery-system.md`,
`.github/copilot-instructions.md`, relevant `.github/agents/`, and appropriate
`docs/` templates. Reconcile existing files rather than overwriting them.
`AGENTS.md` can remain a router; do not assume Manus loads it automatically.

Run the [integration prompt](integration-prompt.md) in the target project. It prepares
durable project instructions and an integration record, for example
`docs/project/integrations/manus.md`. Record actual paths, entry level, repository,
branch, access mode, owner, operating rules, authorization, test commands, and
pending checks. Reference canonical role/workflow guidance rather than duplicating it.

Adapt the [project instruction template](templates/manus-project-instructions.md).
Use Manus project instructions if that feature is available; otherwise provide
them at the start of every new task. Record the actual location. Do not invent a
Manus configuration filename or assume automatic rule discovery.

If another tool prepares the files, the authorized Git owner must first make that
revision available in the target repository. Local edits on your computer are not
automatically available in Manus.

## 3. Verify Repository Reads and Instructions in Manus

Select the correct repository and use this start prompt. Adapt example paths:

```text
Use only the selected project <repository URL>.
Working mode: <GitHub connector with branch/PR or explicitly authorized sync>.
Read .github/copilot-instructions.md and the Manus integration record at
<actual path>. Select the relevant role and load only the necessary project
context, including linked blockers.

Before changes, report the repository, branch, source revision, binding files
actually read, selected role, bootstrap status, and ready/blocked tasks.
Demonstrate reading with brief concrete details from the relevant files.
Report missing access or authoritative sources and stop dependent work.
Do not invent project decisions or passed checks. Start with this inventory only.
```

Reading chat content alone does not verify repository integration. Resolve missing
access before substantial implementation with incomplete instructions.

## 4. Level 1: Adopt an Existing Project

1. **Review the current state:** Identify code, documentation, IDs, architecture,
   CI/CD, test commands, and existing changes. Preserve others' work.
2. **Establish adoption status:** For completed bootstrap, address relevant gaps
   only. For first-time adoption, perform handbook step 0, then bootstrap in order.
   Use existing knowledge instead of replacing completed documents.
3. **Select scope:** Choose an approved spec with ready tasks or an explicitly
   approved application plan. Keep existing IDs.
4. **Execute:** Use the implementation loop in section 6.

```text
Work in the existing project under the delivery instructions you read.
Verify adoption/bootstrap status and preserve completed documentation.
Then execute only <approved spec/task IDs> within <allowed paths>.
Follow dependencies, linked questions, and <agreed checkpoints>.
Use <working branch>. Commit/push/PR authority: <specific approved scope>.
Do not publish automatically. Report blocked prerequisites concretely.
```

## 5. Level 2: Bootstrap a New Project

1. **Prepare the repository:** Connect a new project repository containing the generic
   delivery structure. If Manus needs an initial technical container, create only
   explicitly agreed scaffolding; no feature implementation before bootstrap.
   Authorize a web-app export as a separate operation.
2. **Run bootstrap:** Follow the [handbook sequence](../../delivery-system.md#bootstrap-sequence).
   Mark step 0 not applicable and complete steps 1–12 in order. The handbook's
   detailed requirements remain authoritative.
3. **Resolve questions:** Manus asks for missing requirements. Record answers or
   explicit deferrals in the appropriate sources. Do not create dependent tasks
   or implement features while their prerequisites remain blocked.
4. **Approve the plan:** Review requirements, the first spec, task file, and quality
   rules. Record bootstrap completion or explicit deferrals. A deferral does not
   authorize operations that remain blocked for another reason.
5. **Build:** Execute the approved spec/task plan using section 6.

```text
Set up the new project <project goal> using delivery-system.md.
Mark bootstrap step 0 not applicable and work through steps 1–12 in order.
Write project decisions in the established documentation root; keep the handbook
generic. Stop at the first blocker, ask focused questions, and record answers or
explicit deferrals in the appropriate sources. Do not invent requirements or
start feature implementation before completed or explicitly deferred bootstrap.
Prepare the first spec and ready tasks with criteria and verification once their
source blockers are resolved. Present the plan for approval.
```

### Bootstrap Steps in Order

This overview also applies to first-time adoption in section 4. It summarizes the
[canonical bootstrap sequence](../../delivery-system.md#bootstrap-sequence);
the handbook's detailed requirements remain authoritative. Substitute the project's
established documentation root for `docs/` when applicable.

| Step | What Manus clarifies or prepares with the owner | Required output |
| --- | --- | --- |
| 0 | Existing project: review repository, docs, code, CI/CD, and risks; new project: mark not applicable | Review, e.g. `docs/project/existing-repository-review.md` |
| 1 | Remove copied placeholders and unrelated project assumptions | Adapted files; unknowns explicitly recorded |
| 2 | Define purpose, goals, non-goals, stakeholders, and boundaries | `docs/project/overview.md` |
| 3 | Clarify high-level functional, non-functional, and security requirements | `docs/specs/requirements.md` |
| 4 | Adapt the functional baseline | `docs/specs/baseline/functional-requirements.md` |
| 5 | Review non-functional baseline and measurable quality targets | `docs/specs/baseline/non-functional-requirements.md` |
| 6 | Clarify security, privacy, access, and data handling | `docs/specs/baseline/security-policy.md` |
| 7 | Define global acceptance criteria | `docs/specs/baseline/acceptance-criteria.md` |
| 8 | Plan initial milestones, scope, and dependencies | `docs/project/roadmap.md` |
| 9 | Define the Definition of Done and verification strategy | `docs/quality/dod-checklist.md`, `docs/quality/test-strategy.md` |
| 10 | Review relevant roles and their use in Manus | Relevant `.github/agents/` profiles and documented Manus setup |
| 11 | Create the first detailed spec from clarified requirements, or explicitly defer it | Spec based on `docs/specs/template.md` |
| 12 | Create the first task file with IDs, roles, criteria, and checks, or explicitly defer it | Tasks based on `docs/tasks/template.md` |

**Question gate:** Stop at the first blocking question, ask it concretely, and
record the answer or explicit deferral at its source before continuing bootstrap.
Do not generate implementation tasks from a blocked spec or implement a blocked
task. A deferral permits only the explicitly chosen continuation; it does not
resolve other prerequisites automatically.

### Bootstrap Completion and Implementation Approval

Before section 6, apply the [Bootstrap Completion Check](../../delivery-system.md#bootstrap-completion-check)
to the actual project state. Use an existing bootstrap record or, if absent, the
durable integration record. Record each step, status, output reference, open
question, and answer/deferral. Do not introduce a competing project plan.

- Step 0 is complete or not applicable to the new project.
- Steps 1–12 are complete or explicitly deferred by the owner.
- Source blockers and linked question files are resolved or explicitly deferred,
  with decisions recorded in the appropriate sources.
- Project sources, quality rules, and required verification commands are available.
- The selected implementation scope is approved and its specs/tasks satisfy
  readiness criteria. Deferred initial specs/tasks are not executable assignments.

Before implementation, Manus should report this check with actual document
references. The owner reviews the plan and grants any missing implementation
authority. Existing explicit authorization remains valid within its scope.
“Bootstrap done” without evidence is insufficient for implementation handoff.

## 6. Build the Application from Specs and Tasks

Define the approved plan using the [implementation template](templates/implementation.md).
Manus works in the repository, updates progress and verification in the existing
task format, and follows relevant role profiles. Profiles do not automatically
create separate Manus agents.

```text
Implement <approved spec/task references> in the agreed repository and branch.
Before each task, check its sources, questions, dependencies, and acceptance
criteria. Independently execute ready tasks within this plan; do not ask again
for authorization already granted.

Run required tests and build/lint/type checks. Record actual commands and results
per task. Report missing environments separately. Respect <agreed review and
acceptance checkpoints>. Stop dependent work on blockers, scope conflicts, or
missing authority, and ask a concrete question.

Keep task status, overview, and evidence consistent. Done requires project-specific
acceptance criteria, DoD evidence, and required acceptance. At checkpoints, provide
task IDs, diff/commit references, test results, and open issues.
Commit/push/PR authority: <specific permission>. Merge and release only under
project authorization.
```

The approved plan may cover multiple specs through a complete application.
Authorization and checkpoints define autonomy; there is no blanket stop after
each task. Reconcile concurrent local and Manus edits before continuing.

## 7. Review, Resume, and Publish

The responsible owner reviews the diff, criteria coverage, and evidence against
the correct revision. Run missing or environment-specific checks. Record rework
against the existing task rather than creating a conflicting second plan.

In a new Manus chat, reload project instructions. Read the current repository,
branch, open state, and next ready tasks. Chat history does not replace durable
project records.

Merges, releases, and deployment use existing authorization and pipelines. This
add-on publishes no application and installs no automation. Verify both entry
levels using the [test guide](test-guide.md).
