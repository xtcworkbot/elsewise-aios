---
name: remember
description: Save something worth knowing next session into the shared memory, in the right place and shape, without duplicates. Use when the owner says "remember this", "don't forget", "note that", "from now on", "always do it this way", "never do that again", or corrects how the work is done, or when you learn something about them that a future session would need.
---

# Remember

Memory lives in `Memory/` inside this folder, so Claude and Codex share it. A tool's built-in memory is a cache and never the record.

## First, is this a memory at all?

Put it where it belongs instead, if it is one of these:

| It is | It goes in |
|---|---|
| A fact about the business, the offer, customers or team | The matching `Context/` file |
| The state of a project | That project's `_index.md` |
| Why something was chosen | `Decisions/Log.md` |
| A correction that changes a house rule | `Decisions/Lessons.md`, and `Brain/STANDARD.md` if the rule itself changes. A preference about how they like things done is a `feedback_` memory here |
| A tool's details | `System/Connections/` |

What is left is a memory: who the owner is and how they like things done, a correction to how you work, an ongoing goal or deadline that the files do not make obvious, or where something lives outside this folder.

## Writing it

1. Read `Memory/MEMORY.md`. If an existing memory covers this, update that file instead of creating a new one.
2. Pick the type: `user_`, `feedback_`, `project_` or `reference_`. Name the file with the type and a few plain words, lowercase with underscores, for example `feedback_short_replies.md`.
3. Write it from `Templates/Memory.md`. One fact per file. For feedback and project memories include why it matters and how to apply it. Turn relative dates like "next Friday" into the real date.
4. Add one line to `Memory/MEMORY.md` under Memories: a short title, the file name, and a hook under 150 characters.
5. If a memory turns out to be wrong, move its file to `Archive/` and remove its line from the index.
6. Run `python3 Tools/check.py`.

## Reply

One line: what was remembered and where.
