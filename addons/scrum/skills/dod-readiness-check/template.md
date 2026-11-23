# DoD Readiness Report Template

## Severity

| Severity | Meaning |
| --- | --- |
| Critical | Not done: unmet Must criterion, failing build or tests, committed secret, violated contract |
| High | Likely defects or rework: unhandled edge states, missing evidence for a risky change |
| Medium | Non-blocking gap: documentation not updated, follow-ups not captured |
| Low | Hygiene: missing changed-files summary, cosmetic drift |

## Report

```markdown
## DoD Readiness: {Task or Feature} ({task path})

**Source Spec**: {spec path}
**Verdict**: DONE | PARTIALLY DONE | NOT DONE
**DoD**: {met}/{total} criteria met
**Acceptance Criteria**: {met}/{total} satisfied

| # | Area | Criterion | Result (Pass / Fail / N/A / Unknown) | Evidence |
| --- | --- | --- | --- | --- |

| # | Severity | Area | Finding | Evidence | Recommendation |
| --- | --- | --- | --- | --- | --- |

**Summary**: Critical {n}, High {n}, Medium {n}, Low {n}
```

## Verdict

- Any Critical: NOT DONE.
- No Critical, at least one High: PARTIALLY DONE.
- Only Medium or Low: DONE with noted follow-ups.
