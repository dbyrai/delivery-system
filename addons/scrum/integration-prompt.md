# SCRUM Integration Prompt

Copy this prompt into an agent with access to the target Delivery System project.

```text
Set up the optional SCRUM add-on for this Delivery System project.

Read the applicable project instructions and addons/scrum/README.md. Identify the
project root, the existing documentation root, and which AI tools use the
repository (Claude Code, Codex, GitHub Copilot). Inspect the working tree so you
can preserve existing changes.

Check for existing files at the target paths listed in the README. Never
overwrite an existing different file; report it and ask how to merge.

Show me the open decisions in addons/scrum/record.md (task-file author, who
estimates, sprint length and ceremonies, board location, planning buffer,
ramp-up capacity). Ask one focused question at a time with a recommended answer.
Record explicit deferrals as open questions in the record.

After my confirmation:
1. Write the completed record to <docs-root>/project/integrations/scrum.md.
2. Copy the templates to <docs-root>/quality/dor-checklist.md,
   <docs-root>/sprints/README.md, and <docs-root>/quality/tech-debt.md.
3. Copy each skill folder (SKILL.md and template.md if present) to
   .github/skills/<name>/ and create a wrapper for
   each supported tool in use, matching the existing wrappers:
   .claude/skills/<name>/SKILL.md and .agents/skills/<name>/SKILL.md, each with
   the skill's name and description in front matter and the single line
   "Read and follow `.github/skills/<name>/SKILL.md`."
4. Add a Points column to the Task Order table in the task template and link
   the DoR checklist from the quality README.
5. Add a short conditional pointer to the project's canonical shared instructions:
   load the SCRUM record only for sprint, estimation, readiness, or velocity work.
   Do not import files from addons/ in active instructions.
6. Adjust docs paths in copied files if the documentation root is not docs/.

Activated files must not reference addons/. Read back every written file, compare
the working tree with its initial state, and report paths, decisions, deferrals,
and checks actually run. Activation authorizes no sprint planning, tracker
writes, automation, commits, or pushes.
```
