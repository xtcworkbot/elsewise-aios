---
name: new-project
description: Start a new project properly, or bring an existing folder of work into the system without losing anything. Use when the owner says "new project", "start a project", "set up a folder for", "bring in my folder", "import my projects", "move my stuff in", "I've got work in another folder", or names work that has no project folder yet.
---

# New project

Every piece of work gets one folder and one resume record, in the same shape, so any future session can pick it up cold.

## Starting a new project

1. Ask only what the files do not already say: what it is for, what finished looks like, and who owns it. If the answer is already in the conversation, use it.
2. Pick a clear professional name. Check `Projects/` so it does not clash with an existing one.
3. Create `Projects/<Name>/_index.md` from `Templates/Project.md`. Fill goal, finish line, owner, status live, today's date, and the first next step with a date.
4. Add one line under Live in `Projects/_index.md` saying what it is and pointing at its folder.
5. If it serves a priority in `Context/Priorities.md`, say which one in the goal.
6. Run `python3 Tools/check.py`, then commit.

Create subfolders only when there are real files to put in them.

## Bringing in existing work

1. Get the exact location of the existing folder. Look inside it by name first and tell the owner in a few lines what is there: how many files, what kinds, the total size, and any big video, audio or photo files.
2. Copy. Never move. Say why in one line: moving a folder can break other apps that remember where it lives, including chat history in the Claude desktop app. The original stays where it is until the owner has worked from the copy for a while and chooses to archive it.
3. Before copying, check `.gitignore` covers every large media type in the folder. Add any missing type. Large media is kept in the folder but never committed.
4. Copy the folder into `Projects/<Name>/`. If a project folder with that name already exists from onboarding, copy into it and keep its `_index.md`.
5. Compare the copy with the original: the same number of files and the same total size. If they differ, stop and say what is missing.
6. If the folder had its own `CLAUDE.md` or `AGENTS.md`, keep it. It still applies when working inside that project. Read it and tell the owner if anything in it conflicts with the main manual.
7. Read enough of the contents to write the resume record: what the project is, where it looks to be up to, and the files that matter. Mark anything you are inferring as inferred. Ask the owner to confirm the goal and the next step.
8. Write or update `Projects/<Name>/_index.md` and its line in `Projects/_index.md`. Record the original location under "Where it is up to".
9. Run `python3 Tools/check.py`. Run `git status` and confirm no large media is staged. Commit.

## Never

- Move or delete the original folder.
- Commit video, audio, raw photos or large exports.
- Invent a goal or a status for imported work. Ask.
