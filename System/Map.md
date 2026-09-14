# System map

The answer to "where does this live" and "where does a new thing go". The manual routes here instead of carrying the detail itself.

## The shape

The root holds the two identical manuals, `README.md`, `.gitignore`, eleven folders, and the hidden wiring folders `.claude/`, `.agents/`, `.codex/`, `.git/`, plus `.gitattributes`, `.env.example` and the key file `.env`. Nothing else. A new top level folder is a decision that goes in `Decisions/Log.md` first, never a convenience.

| Folder | What it is | Who reads it |
|---|---|---|
| `Brain/` | Identity, the owner, the house rules, the voice, what to watch | Every session, loaded by the start hook |
| `Memory/` | Things learned over time, one fact per file | Every session reads the index |
| `Context/` | Business facts and priorities | When advising or drafting |
| `Projects/` | One folder per piece of work, each with its resume record | When working on or asked about a project |
| `Decisions/` | The decision log and the lessons | Before reopening a choice or repeating a mistake |
| `System/` | Map, connections, automations, platforms, intake, audits | When wiring tools or checking health |
| `Templates/` | The shapes new files follow | Every time a new project, decision, lesson, memory, connection or skill is made |
| `Outputs/` | Finished work that leaves the building | When delivering |
| `Tools/` | Scripts that do real work, and `check.py` | When running a tool or checking the system |
| `Scratch/` | Throwaway work, ignored by git, 14 day life | Nobody, after 14 days |
| `Archive/` | Superseded material, dated | Only when history is needed |

## Where a new thing goes

| The thing | Where | Not |
|---|---|---|
| A piece of work with a goal | `Projects/<Name>/`, from `Templates/Project.md` | A loose file in the root |
| Files that belong to a project, media included | Inside that project's folder | `Outputs/` or `Scratch/` |
| A finished deliverable that goes to someone | `Outputs/`, with a line in its index | The project folder |
| A business fact | The matching `Context/` file | `Memory/` |
| A preference, correction or working style | `Memory/`, from `Templates/Memory.md` | The chat |
| Why something was chosen | `Decisions/Log.md` | A project note |
| A mistake that became a rule | `Decisions/Lessons.md` | The decision log |
| A process that works by hand and should run the same way every time | `.claude/skills/<name>/`, plus its Codex pointer | `Tools/` |
| A script worth running twice | `Tools/`, with a line in its index | `Scratch/` |
| A tool or account connected | `System/Connections.md` plus `System/Connections/<Tool>.md` | Nowhere, which is how tools get forgotten |
| Something on a schedule | `System/Automations.md` | A reminder promised in chat |
| An interview | `Context/Interviews/` | `Scratch/` |
| A one-off test, dump or render | `Scratch/` | The root |
| Anything superseded | `Archive/<what> <date>/` | Deleted |

## Where a business topic goes

When the owner starts talking about a part of their business, it already has a home.

| They talk about | It goes in |
|---|---|
| How something in the business runs today, its tools, people and numbers: operations, website, marketing, socials, inventory, staff, cash flow, sales, customer service, suppliers | `Context/<Area>.md`, one file per area, from `Templates/Area.md`. Create it the first time the area comes up and add its line to `Context/_index.md` |
| A change they want to make in an area, with a finish line | A project in `Projects/`, which points at the area file it serves |
| A number they watch | The area file says where it is read from. `Brain/HEARTBEAT.md` says when to raise it |
| A tool used in that area | `System/Connections.md` and its own connection file |
| A recurring job in that area that should run the same way every time | A skill |
| A choice made about that area | `Decisions/Log.md` |

An area file describes how things are. A project describes what is being changed. Never mix the two.

## Naming

- Folders and files are named the way a professional would name them, in plain words that say what they are. `Quote Template.md`, not `qt-v2-final.md`.
- No version, date or status in a normal file name. State goes inside the file or in the index. Dated records like interviews, audits and archive folders are the exception.
- Skill folders are lowercase with hyphens, because the engines require it.
- Before using a new folder name, check git will see it: `git check-ignore -v "<path>"` prints the matching rule if git ignores it. No output means git will see it.

## Housekeeping law

1. Every folder has an `_index.md` saying what it is for. `Memory/` uses `MEMORY.md`.
2. Every new file gets one line in its folder's index, saying what it is and its state.
3. A folder either has real content or it does not exist, apart from the eleven that ship with the system.
4. Preserve before changing. Nothing is deleted. Move it to `Archive/` with the date.
5. Big media stays out of git. Video, audio, raw photos and large exports are ignored by `.gitignore`. Their folders and notes are still committed.
6. Secrets live only in `.env`, which git ignores. `.env.example` explains the file and the setup script creates `.env` from it. Markdown files name the key, never the value. `.claude/settings.json` blocks Claude from opening `.env`, and the manual tells it never to print it.
7. After a structural change, run `python3 Tools/check.py`, fix what it reports, then commit.
8. `Scratch/` is cleared of anything older than 14 days. Keep it by moving it to the right folder.

## The system check

`python3 Tools/check.py` checks that the two manuals match, the manual is under 200 lines, every path the manual names exists, every folder has an index, every Claude skill has a Codex pointer, every memory file is in the index, and nothing stray sits in the root. It changes nothing. Run it after any change to structure and before every commit.
