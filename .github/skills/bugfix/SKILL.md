---
name: bugfix
description: Fast-track investigation and minimal fix of a concrete, reproducible bug without a new spec or task file. Use when the user reports a specific defect or asks to fix something that does not work as intended.
---

# Bugfix

Primary role: the developer owning the affected area; involve the Technical Lead for root causes that cross boundaries. This is the fast path for localized defects, not for new behavior.

## When Not to Use

- The request is new behavior described as a bug: stop and suggest `new-feature`.
- The fix requires an architecture change: escalate to the Technical Lead and record a decision.
- The bug belongs to a task with unresolved blocking questions: resolve or defer them first.

## 1. Understand

Establish actual behavior, expected behavior, reproduction steps, and the affected component. Skip questions the report already answers. Check the source spec or acceptance criteria when expected behavior is unclear.

## 2. Investigate

Locate the relevant code, trace the failure path, identify the root cause, and assess the blast radius. If the optional `diagnosing-bugs` method is active, use it for hard-to-reproduce defects. Present the root cause, proposed fix, and risk (low, medium, high). Wait for confirmation before implementing when risk is medium or higher.

## 3. Fix

Make the smallest correct change following existing patterns. Add or update a regression test where the project has test infrastructure. Run the project's documented verification commands for the affected area.

## 4. Document

Update the changelog or release notes if the project keeps them. Record a decision only if the fix changes an agreed behavior or boundary.

## 5. Report

State the root cause, changed files, verification actually run, and any follow-up.

## Rules

- Fix only what is broken; no refactors or features.
- Preserve authorization, data isolation, and other security gates. For security-relevant bugs, fix and recommend an independent security review.
- If the bug turns out to be missing functionality, stop and suggest `new-feature`.
