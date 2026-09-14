# Elsewise AIOS

Your own AI operating system. One folder that turns Claude Code or Codex into an assistant that knows who you are, how your business works, what you are chasing and how you like to work. It keeps everything organised, remembers what matters, and gets sharper every week.

Built by Elsewise, from months of running a real business on this exact system every day.

## What you get

- An assistant you name and shape. Its role, its personality, the minds it draws on, and how it talks to you.
- A brain that loads itself. Every new session starts knowing who it is, who you are, your goal, your open projects and what it has learned.
- House rules that were paid for. Answer the question asked. Check before claiming. Decide instead of handing you a menu. Never a yes man. Always ask before spending money, messaging people, publishing, deleting or widening access.
- A filing system that runs itself. Every folder knows what it holds, every new thing has one right home, and the assistant creates and files things the same way every time.
- Memory that belongs to you. Stored in this folder, shared by Claude and Codex, never locked inside one app.
- Ten skills out of the box. Setup, a daily brief, deep interviews, projects, memory, saving, linking, a health check, a weekly improvement habit, and building your own skills.
- Both engines. Claude Code and Codex read the same files, the same rules and the same memory. Switch whenever you like.

## Getting started

1. Get the folder onto your computer. Click the green Code button on GitHub and choose Download ZIP, then unzip it into your home folder. Or clone it if you know git.
2. Run the setup. On a Mac, open Terminal in the folder and run `bash Tools/setup.sh`. On Windows, double click `Tools\setup.cmd`. It installs anything missing, creates your key file and checks the wiring. Run it again any time.
3. Open the folder in VS Code, or in the Claude Code or Codex app.
4. Start a chat with Claude Code or Codex in this folder. The first time, it asks you to sign in.
5. Type `/onboard` in Claude Code, or `$onboard` in Codex.
6. Answer the questions properly. It takes 30 to 40 minutes and it is the best time you will spend on this system. Everything is saved as you go.
7. When it finishes, close the chat and open a new one. Ask your assistant what the one thing is that you should focus on this week.

## Using it every day

| When you want to | Say or type |
|---|---|
| Know what to focus on | "What's the one thing?" or the brief skill |
| Think a plan through, or get something out of your head | "Grill me on..." |
| Start a project, or bring in an existing folder | "New project..." or "Bring in my folder..." |
| Make sure something is not forgotten | "Remember that..." |
| Wrap up | "Save" or "That's me for today" |
| Make something findable | "Link this..." |
| Check the system is working | "Audit my system" |
| Take a job off your plate | "Level up" |
| Lock in a process you have proven | "Make that a skill" |

In Claude Code, skills are typed with a slash, like `/brief`. In Codex, with a dollar sign, like `$brief`. You can also just ask in plain words.

## What is in the folder

| Folder | What it holds |
|---|---|
| `Brain/` | Who your assistant is, who you are, the house rules, the voice, what it watches |
| `Memory/` | What it learns over time |
| `Context/` | Your business, offer, customers, team and priorities |
| `Projects/` | One folder for each piece of work |
| `Decisions/` | Why things were chosen, and lessons learned |
| `System/` | The map, your connected tools, automations and health checks |
| `Templates/` | The shapes every new file follows |
| `Outputs/` | Finished work |
| `Tools/` | Scripts that do real work |
| `Scratch/` | Throwaway work |
| `Archive/` | Old material. Nothing is ever deleted |

`CLAUDE.md` and `AGENTS.md` are the assistant's manual. They are identical: Claude reads one, Codex reads the other.

## Keeping it healthy

- Run the audit skill a week after setup, then every month.
- Run the level-up skill once a week. One small improvement each time.
- Big video and audio files stay out of the save history automatically. Your passwords and keys go in the `.env` file the setup made, which is never saved to history and which Claude is blocked from reading. `.env.example` explains it.
- `python3 Tools/check.py` checks the wiring any time.

## Needs

- A Mac or a Windows computer. The setup script installs everything below. On Windows, start with Claude Code. Codex on Windows is not tested yet.
- A paid Claude plan for Claude Code, or a ChatGPT plan for Codex. In Codex, hooks and custom agents may need turning on in its settings. Skills work without that.
- Git, for save points. Python 3, for the hooks and the check script. Node, for some tools. On Windows the check command is `python Tools\check.py`.
- Keep the folder out of iCloud Drive, OneDrive and Dropbox. Syncing breaks the save history.
