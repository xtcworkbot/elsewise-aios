---
name: save
description: Checkpoint the session so nothing is lost and the next session, in either engine, can pick up cold. Use when the owner says "save", "save this", "log this", "wrap it up", "that's me for today", "I'm off", "call it a night", "switching to Codex", "switching to Claude", before a long break, or at any meaningful checkpoint without being asked.
---

# Save

Saving is the assistant's job. A sign-off means finish the save before the goodbye. It never means start new work.

## Steps

1. Work out what changed this session: work done, decisions made, corrections given, things learned, promises made, anything still running.
2. For each project touched, update its `_index.md`: where it is up to with proof, the next step with a date, waiting on, promises, decisions, and new files. Update "Last updated" with today's date and the engine.
3. Update `Projects/_index.md` if a project started, finished, is waiting, or was parked.
4. Add any decision worth not reopening to `Decisions/Log.md`, from `Templates/Decision.md`.
5. Add any correction to `Decisions/Lessons.md`, from `Templates/Lesson.md`. Update `Brain/STANDARD.md` if a house rule changed.
6. Save anything else worth remembering with the remember skill's rules.
7. Add one line to the top of the table in `System/Sessions.md`: today's date, the engine, what was done, the next step.
8. If work is still running, write down its real state. Never say it finished.
9. Read back every file you changed to prove it saved.
10. Run `python3 Tools/check.py`. Fix anything it reports.
11. Run `git status`. Make sure no secrets or large media are staged. Commit with a plain message saying what the session did.
12. If `git remote -v` shows `origin`, push to it, following the backup skill. A failed push never blocks the save. Say it failed and move on.

If nothing meaningful changed, do not write empty entries. Say so.

## Reply

```
Saved. {One line on the main thing done.}
Backed up to GitHub. {Or: not backed up, and why.}
Next time: {the next step, and where it lives}.
```

If a save failed, say exactly what failed instead.
