# DoR Readiness Report Template

## Severity

| Severity | Meaning |
| --- | --- |
| Critical | Blocks task creation: open blocking questions, no verifiable acceptance criteria, not approved, required contract missing |
| High | Will cause rework: undocumented dependencies, missing security requirements, superseded reference |
| Medium | Workable gap: stale date, missing success indicator |
| Low | Hygiene: single missing priority tag, link formatting |

## Report

```markdown
## DoR Readiness: {Spec Title} ({spec path})

**Verdict**: READY | PARTIALLY READY | NOT READY
**DoR Spec**: {met}/{total} criteria met
**References**: {checked} checked, {issues} issues

| # | Severity | Area | Finding | Evidence | Recommendation |
| --- | --- | --- | --- | --- | --- |

**Summary**: Critical {n}, High {n}, Medium {n}, Low {n}
```

## Verdict

- Any Critical: NOT READY.
- No Critical, at least one High: PARTIALLY READY.
- Only Medium or Low: READY with the noted hygiene items.
