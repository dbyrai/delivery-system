# Clarification Rounds

A simplified interview method for resolving open decisions before a spec is written. Skills reference this file; it is not a skill of its own.

## Method

1. **List the open decisions** for the feature. Note which decisions depend on others.
2. **Ask a round**: all decisions whose prerequisites are already settled, at most five per round. A question that depends on an answer still open in this round waits for a later round.
3. **Format** each question with your recommendation:

   ```text
   ❓ **Q1 - <short title>**: <question, with the options if there are several>

   ➡️ <recommended answer and one-sentence reason>
   ```

4. **Wait** for the user's answers. Accepting a recommendation needs an explicit "ok" or equivalent; silence is not an answer.
5. **Update** the list: settled decisions may unlock new questions. Repeat from step 2.
6. **Finish** when no open decision remains or every remaining one is explicitly deferred. Summarize the settled decisions and deferrals in a short list and ask the user to confirm before writing anything.

## Rules

- Facts are your job, decisions are the user's. Look up anything the repository can answer (existing specs, roadmap, code, decisions) instead of asking.
- Ask about scope, behavior, priorities, and tradeoffs; do not ask the user to design implementation details.
- Keep unresolved items visible; they become Open Questions in the spec and stay blocking unless deferred.
- Stop early when the user asks to; record what is still open.
