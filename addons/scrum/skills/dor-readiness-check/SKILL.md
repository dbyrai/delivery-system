---
name: dor-readiness-check
description: Read-only check of exactly one spec against the Definition of Ready and of every reference it contains, producing a severity-rated finding list. Use when the user asks whether a spec is ready, to check a spec against the DoR, or names a spec for a readiness check.
---

# DoR Readiness Check

Act as the Product Manager (`.github/agents/product-manager.agent.md`). The authoritative checklist is `docs/quality/dor-checklist.md`. This check is read-only: never modify specs, tasks, contracts, or decisions.

## Step 0: Resolve Exactly One Spec

The user names one spec by number or name. If none or several are given, ask for exactly one. If several files match, list the candidates and ask. Read the resolved spec fully and record its path and title in the report header.

## Step 1: DoR Spec

Check each DoR Spec criterion against the actual content, not section titles: open questions and linked question files, verifiable acceptance criteria, documented dependencies, explicit non-goals, security requirements or a justified not-applicable, and Product Owner approval (status `Approved`). With the Contracts record active, also check that required contracts are listed and exist. Check hygiene: priority tags, owner, last-updated date. Mark a criterion Unknown, not Pass, when it cannot be determined.

## Step 2: Reference Freshness

Open every referenced target and confirm it exists and is current: related specs (not superseded), decisions or ADR files, the related task file, contracts with their status, and inline paths. Do not assume a link is valid because it looks plausible.

## Step 3: Findings

Rate every gap and write the report using `.github/skills/dor-readiness-check/template.md` (severity scale, report format, verdict rule).

## Rules

- One spec per run; read-only; verify instead of assuming.
- Every finding names the exact file and gap and has a severity.
