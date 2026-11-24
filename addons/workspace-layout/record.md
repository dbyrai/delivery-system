# Workspace Layout

**Status**: Active | Inactive
**Owner**: {accountable owner}
**Adopted From**: Delivery System Workspace Layout add-on {version or commit}

## Repositories And Roots

- Workspace repository: {identity and visibility}
- Application repository: {identity and visibility}
- Application directory: {relative path}
- Project documentation root: {relative path}
- Private documentation root: {relative path}

## Authority

| Content | Authoritative repository/root | Owner |
| --- | --- | --- |
| Application code and public project documents | {path} | {owner} |
| Delivery System and private project records | {path} | {owner} |

## Privacy Decisions

- Content prohibited from the application repository: {list}
- Link policy between public and private documents: {decision}
- Security findings location: {path}

## Git And Release Boundaries

- Workspace commit/push/merge/release authority: {decision}
- Application commit/push/merge/release authority: {decision}
- Application Git command root: `git -C {relative path}`

## Migration And Verification

- Migrated documents and source revisions: {list}
- Standard-layout regression: {result}
- Nested-repository and ignore checks: {result}
- Public/private path and link checks: {result}
- Installed add-on compatibility: {result}
- Rollback/deactivation check: {result}
