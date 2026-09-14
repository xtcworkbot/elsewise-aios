---
name: backup
description: Set up a private GitHub repository as the live off-machine backup of this folder, then keep it current. Use when the owner says "back this up", "set up GitHub", "put this on GitHub", "is this backed up", "push to GitHub", "when was the last backup", or right after onboarding finishes. Also run by the save skill after every commit.
---

# Backup

The folder is the owner's second brain. A laptop dies, gets stolen or gets wiped. The backup is a private repository on the owner's own GitHub account that holds every save point. Only the owner and the assistant can see it. Keys in `.env` never go, because git ignores that file.

## Two jobs

1. Set up the backup, once.
2. Push to it, every save.

## Setting up, once

Do this the first time, or when `git remote -v` shows no `origin`.

1. Say in two lines what is about to happen: a private repository on their GitHub account, that only they can see, that gets a copy of every save. Wait for a yes. Setting up a backup is widening where their data lives, so it needs a clear yes.
2. If they have no GitHub account, ask them to make one at github.com in their browser first. Free is fine.
3. Check `gh --version`. If the GitHub tool is missing, run the setup script, which installs it: `bash Tools/setup.sh` on a Mac, `Tools\setup.cmd` on Windows. Then continue.
4. Run `gh auth status`. If not signed in, run `gh auth login --web --git-protocol https` and tell them a browser window will open for them to sign in to GitHub and approve. Never ask for a password or token in the chat. Wait for them to say it is done.
5. Confirm the folder is a git repository with at least one commit. If not, run the save skill first.
6. Run `python3 Tools/check.py`. It must pass, and `git status` must show no `.env` and no large media staged.
7. Create the repository, named after the assistant in lowercase with hyphens, for example `jarvis-aios`:
   `gh repo create <name> --private --source . --remote origin --push`
8. Prove it: `git remote -v` shows `origin` on github.com, and `gh repo view --json isPrivate` says true. If it is not private, stop and fix it before anything else: `gh repo edit --visibility private --accept-visibility-change-consequences`.
9. Write one row in `System/Connections.md`: GitHub, reached through the `gh` tool signed in as them, status tested, today's date. Make `System/Connections/GitHub.md` from `Templates/Connection.md`. Key name: none, the login lives in the GitHub tool, not in `.env`.
10. Log it in `Decisions/Log.md`: the backup was set up, where, and that it is private.

## Pushing, every save

After every commit, and whenever the owner asks:

1. `git push origin HEAD`. If it fails because the internet is down, say so and move on. The next save tries again. Never let a failed push block a save.
2. Prove it with `git status -sb`. The first line says whether the local copy is ahead of the backup. Zero ahead means backed up.
3. Write the date of the last successful push in `System/Connections.md` on the GitHub row.

## Checking

When the owner asks whether they are backed up, or the heartbeat raises it:

1. `git fetch origin` then `git status -sb`. Ahead by anything means the backup is behind. Push.
2. `git log -1 --format=%cd origin/main` gives the date of the last backed up save. Older than seven days while work has happened is a problem worth raising.

## Never

- Push to a repository the owner does not own. The Elsewise starter repository is never a backup.
- Make the repository public.
- Force push. If the push is rejected, stop and say so.
- Put `.env`, keys or large media in git to get them backed up. Keys are backed up by the owner, by hand, somewhere private.

## Reply

```
Backed up. {Repository name}, private, on your GitHub. Last push {date and time}.
```

Or, if it failed, exactly what failed and what happens next.
