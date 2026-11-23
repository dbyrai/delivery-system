# Quickstart: Use the Delivery System in a New Manus Project

**Updated:** 2026-11-23 · **Goal:** Prepare a new GitHub project with the
Delivery System and make the optional Manus add-on operational.

## Overview

The Manus add-on is not an additional service or a switch in Manus. It consists
of project instructions, a setup prompt, and a durable integration record in the
repository. It uses the built-in Manus GitHub connector to access source code.
No Manus API key or self-hosted MCP server is required.

The add-on is active only after Manus has demonstrably read the correct
repository, branch, and authoritative instructions.

## Prerequisites

- A Manus account.
- A GitHub account with access to the new repository.
- A new or otherwise empty project repository.
- The Delivery System files, including `addons/manus/`, in the repository.
- A clear decision about who may authorize commits, pushes, pull requests,
  merges, and releases.

Use **Level 2 – Bootstrap a new project** for a new project. Application
implementation starts only after the project bootstrap.

## 1. Create the New Repository with the Delivery System

The easiest option is to use the Delivery System repository as the starting
point for the new project. If GitHub offers **Use this template** for the
repository, use it to create the new repository directly. Alternatively, connect
a local copy to a new GitHub repository.

The new repository must contain at least these paths:

```text
AGENTS.md
delivery-system.md
.github/copilot-instructions.md
.github/agents/
docs/project/
docs/specs/
docs/tasks/
docs/quality/
addons/manus/
```

Include hidden directories such as `.github/`. Add application files alongside
this structure and record project-specific information under `docs/`. Do not
blindly overwrite existing files.

You may remove files that exist only for maintaining the original Delivery
System repository:

```sh
rm -r -- .github/maintainers
```

Make the prepared revision available in the new repository through the normal
Git workflow. Manus cannot see local files that have not been pushed.

## 2. Connect GitHub in Manus

1. Open **Connectors** in Manus and select **GitHub**.
2. Select **Connect** and sign in to GitHub.
3. Grant the Manus Connector app access only to the required repositories.
4. Open a new Manus task and select the new repository from the GitHub menu.
5. Use the branch and pull request workflow for a reviewable project.

Depending on the granted permissions and the assignment, the GitHub connector
can read code, create commits and branches, push changes, and open pull requests.
The assignment must therefore state explicitly which actions Manus may perform.

GitHub synchronization for a web app built in Manus is a different working mode.
It exports the app to a new private repository and automatically synchronizes
with `main`. Use this mode only when the project owner has explicitly accepted
that behavior. A prompt cannot technically disable automatic synchronization.

## 3. Set Up the Manus Add-on

Select the new repository in the Manus task and send this setup request:

```text
Use only the selected new GitHub repository.
Set up the optional Manus add-on at Level 2 for a new project.

First read addons/manus/integration-prompt.md and execute that setup prompt.
Also read the project files and Manus instructions referenced by it.
Work on a new branch and open a pull request for review.
Do not implement the application, merge changes, or publish anything.

Before making changes, report the repository, branch, source revision,
authoritative files actually read, selected role, and identified blockers.
Do not invent project decisions or successful checks.
```

During setup, Manus should:

- Read `addons/manus/README.md`, `howto.md`, `instructions.md`, and
  `templates/manus-project-instructions.md`.
- Create a durable integration record, normally
  `docs/project/integrations/manus.md`.
- Adapt the project-specific Manus instructions.
- Add only a short conditional pointer to the integration record in
  `.github/copilot-instructions.md`.
- Mark unknown information as unresolved instead of inventing it.
- Avoid implementing application functionality during setup.

All ongoing rules must live in the project itself. After setup, they must not
depend on retaining the optional `addons/` directory.

## 4. Provide the Project Instructions in Manus

If the Manus project supports project instructions, add the adapted content from
`addons/manus/templates/manus-project-instructions.md` there. Record the actual
location in the integration record.

If this feature is unavailable for the Manus account, provide the instructions
at the beginning of every new task. Do not assume that Manus automatically loads
`AGENTS.md` or other repository instructions.

## 5. Verify Activation

Review the setup pull request and, once approved, merge it through the normal
GitHub process. Then start a new Manus task, select the repository again, and run
this read-only check:

```text
Use only the selected project repository and do not make any changes yet.
Read .github/copilot-instructions.md and the Manus integration record at
docs/project/integrations/manus.md.

Report the repository, branch, source revision, authoritative files actually
read, selected role, bootstrap status, and current blockers. Demonstrate that
you read the files with brief, concrete details from them.
Stop if access or authoritative sources are missing.
```

The add-on is operational when Manus:

- Identifies the correct repository, branch, and revision.
- Accurately reports concrete content from the authoritative files.
- Finds the durable integration record.
- Recognizes the project as **Level 2 – Bootstrap a new project**.
- Reports missing decisions as blockers instead of inventing answers.
- Does not implement, merge, or publish without explicit authorization.

A successful connector login alone is not sufficient evidence.

## 6. Start the Project Bootstrap

After activation has been verified, follow the bootstrap in
`delivery-system.md`. Step 0 is not applicable to a new project; complete steps
1 through 12 in order. Manus clarifies the purpose, non-goals, requirements,
security, acceptance criteria, roadmap, quality rules, first specification, and
first tasks with the project owner.

Use this follow-up request:

```text
Start the bootstrap for this new project according to delivery-system.md.
Mark step 0 as not applicable and complete steps 1 through 12 in order.
Stop at the first blocking question and ask it concretely.
Record answers or explicitly authorized deferrals in the responsible project
documents. Do not implement the application yet. Present the first specification
and first executable task plan for my approval.
```

Implementation may begin only after the bootstrap is complete or explicitly
deferred and the concrete specification and tasks have been approved.

## Common Mistakes

- **Copying only the prompt:** Manus cannot verify the rules without repository
  access.
- **Connecting only GitHub:** The connector does not automatically activate the
  Delivery System add-on.
- **Leaving files only on a local computer:** Manus sees only the revision
  available in the selected repository.
- **Assuming automatic instruction loading:** Manus must demonstrably read the
  authoritative files.
- **Starting implementation immediately:** Add-on setup and bootstrap do not
  authorize application development.
- **Confusing sync and connector modes:** Automatic `main` synchronization and
  branch/pull request work have different effects.

## Further Reading

- [Detailed Manus how-to](howto.md)
- [Setup prompt](integration-prompt.md)
- [Manus operating rules](instructions.md)
- [Test guide](test-guide.md)
- [Official Manus GitHub connector documentation](https://www.manus.im/connectors/github)
