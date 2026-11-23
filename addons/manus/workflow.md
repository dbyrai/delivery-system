# Workflow: Manus Develops in GitHub Using the Delivery System

Both entry levels run directly in Manus with the same project repository.
The diagram shows delivery gates; connector and sync are working modes, not
additional integration levels. Live verification remains pending.

![Two entry levels and a shared implementation loop](workflow.svg)

## Editable Diagram Source

```mermaid
flowchart TD
    A[Connect Manus to the GitHub project and verify working mode] --> B[Read project instructions and repository sources]
    B --> C{Entry level}
    C -->|1: Existing project| D[Review current state and adoption; preserve completed documents]
    C -->|2: New project| E[Step 0 not applicable; complete bootstrap 1 through 12]
    D --> F{Delivery already adopted?}
    F -->|Yes| G[Select approved specs and tasks]
    F -->|No| H[Repository review step 0; bootstrap 1 through 12]
    H --> I[Record questions and decisions in project sources]
    E --> I
    I --> J{Bootstrap and source blockers resolved or explicitly deferred?}
    J -->|No| I
    J -->|Yes| G
    G --> K{Plan approved and next task ready?}
    K -->|Blocked| L[Ask a focused question; stop dependent work]
    L --> G
    K -->|Yes| M[Manus implements within the allowed scope]
    M --> N[Run checks; document status and evidence]
    N --> O{Required checkpoint reached?}
    O -->|No, another ready task| K
    O -->|Yes or plan implemented| P[Review diff, criteria, and test evidence]
    P -->|Rework| M
    P -->|Accepted, more tasks| K
    P -->|Plan accepted| Q[Merge and release under existing authority and pipeline]
```

## Handoffs and Resumption

| Point | Accountable role | Evidence |
| --- | --- | --- |
| Setup | Project owner | Repository, mode, branch, access, actual instruction reads |
| Project clarification | Domain owner; Manus prepares | Bootstrap status, answers/deferrals, approved sources |
| Execution | Manus following the relevant role profile | Task IDs, allowed scope, diff, and actual checks |
| Acceptance | Reviewer/owner under project rules | Criteria coverage, DoD, and required approval |
| Publication | Existing release owner | Approved commit and existing deployment process |

Within the approved plan, Manus may continue without another task assignment.
Blockers, dependencies, and agreed acceptance gates limit progression. A deferral
does not automatically remove other prerequisites. In a new chat, read the current
repository and task state again.

Documented web-app sync may transfer code before delivery acceptance. Establish
its behavior before implementation; a push does not satisfy acceptance criteria.
See the [how-to](howto.md) for details and start prompts.
