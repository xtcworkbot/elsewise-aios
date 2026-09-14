---
name: make-skill
description: Turn a process that has already worked by hand into a skill that runs the same way every time, in both Claude and Codex, and prove it fires. Also fixes a skill that does not trigger or keeps getting it wrong. Use when the owner says "make that a skill", "turn this into a skill", "I want to do this the same way every time", "build a skill for", "why didn't that skill work", or "this skill keeps getting it wrong".
---

# Make skill

A skill locks in a process that has already been proven. It does not capture a hope. A skill built on a guess repeats the guess forever.

## Should this be a skill?

Three questions. If any answer is no, say so and stop.

1. Has this been done by hand, and did it work? If not, do it by hand first.
2. Does it run in the same order with the same kind of output each time? If every run needs fresh judgement about what to do next, it is not a skill.
3. Is it a process, or a whole area of work? A repeatable process is a skill. An area that needs its own ongoing judgement and reports back is a helper agent in `.claude/agents/`.

## Capture what actually happened

Best case, the process just happened in this conversation. Mine it before asking anything: the steps taken, the order, the files and tools used, what the owner corrected, and what the result looked like when they said it was right.

Then ask only for gaps:
- What words does the owner actually say when they want this? Their words, not a tidy version. These decide whether it fires.
- What does finished look like, in a way that can be checked?
- What has already gone wrong once?

Confirm the capture with the owner in one short paragraph before writing.

## Write it

1. Pick a short lowercase name with hyphens. Check `.claude/skills/` so it does not clash.
2. Write `.claude/skills/<name>/SKILL.md` using the shape in `Templates/Skill.md`. The description line does the most work: what it does, when to use it, and the owner's own trigger phrases.
3. Keep it to one file when possible. Add `references/` for detail read only when needed, or a script in `Tools/` when the same code keeps being rewritten.
4. Write the Codex pointer at `.agents/skills/<name>/SKILL.md` with the same name and description, pointing at the Claude file. Never copy the full procedure into the pointer.
5. Add the skill to the skills table in `CLAUDE.md`, then copy `CLAUDE.md` over `AGENTS.md`.

## Prove it

1. Run `python3 Tools/check.py`.
2. Ask the owner to open a fresh session and say their trigger phrase the way they normally would. Watch whether the skill fires and whether the result matches what finished looks like.
3. If it did not fire, sharpen the description with the words they actually used. If the result was wrong, fix the step that caused it. Run it again.
4. Record the first real run in `System/Platforms.md` for the engine it was tested in. Untested in the other engine stays marked untested.
5. Log the new skill in `Decisions/Log.md` in one short entry, then commit.

## Fixing a skill that is not working

1. Read the skill and the conversation where it failed.
2. Did it not fire? Fix the description with the owner's real words. Did it fire and get it wrong? Find the step, fix it, and write the mistake into the skill's "Never" section.
3. Prove it again as above.
