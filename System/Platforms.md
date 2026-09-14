# Platforms

How Claude Code and Codex share this folder, and what has actually been tested in each.

## How the sharing works

| Need | Claude Code | Codex | Shared |
|---|---|---|---|
| The manual | `CLAUDE.md` | `AGENTS.md` | The two files are identical |
| Skills | `.claude/skills/<name>/SKILL.md` | `.agents/skills/<name>/SKILL.md` points at the Claude file | One procedure per skill |
| Agents | `.claude/agents/<name>.md` | `.codex/agents/<name>.toml` | Same job and rules |
| Hooks | `.claude/settings.json` | `.codex/hooks.json` | Same scripts in `.claude/hooks/` |
| Memory | Built-in memory is a cache | Built-in memory is a cache | `Memory/` is the record |
| Settings and permissions | `.claude/settings.local.json`, not committed | Codex settings, not committed | Nothing secret is shared |

## Mac and Windows

| Need | Mac | Windows |
|---|---|---|
| Set up the computer | `bash Tools/setup.sh` | Double click `Tools\setup.cmd` |
| Run the check | `python3 Tools/check.py` | `python Tools\check.py` |
| Hidden files | Folders starting with a dot are hidden in Finder. Press Command Shift Full stop to show them | Shown normally in Explorer |
| Shell the assistant uses | zsh | Git Bash, which comes with Git for Windows. Without it Claude Code uses PowerShell and the hooks may not run |
| Where the Claude login lives | The Mac keychain | The user folder, in `.claude`, outside this folder |
| Codex hooks | Work | Not tested. Start with Claude Code |

Line endings are fixed by `.gitattributes`, so files edited on one machine do not show as changed on the other. Keep this folder out of iCloud Drive, OneDrive and Dropbox, because two machines syncing `.git` corrupts it.

## Tested

| Check | Claude Code | Codex |
|---|---|---|
| Manual loads in a fresh session | Not tested yet | Not tested yet |
| Start of session hook loads the brain | Not tested yet | Not tested yet |
| Reply voice hook | Not tested yet | Not tested yet |
| Skills listed and runnable | Not tested yet | Not tested yet |
| Onboarding completes | Not tested yet | Not tested yet |

Update this table with the date and result the first time each check is run on this machine.

## Which AI providers may see what

Filled by onboarding. Anything the assistant reads is sent to the provider running it: Anthropic for Claude, OpenAI for Codex. Files staying on the computer does not change that.

Not set yet.

## Switching engines

1. Run the save skill in the engine you are leaving.
2. Open the same folder in the other engine.
3. It reads the manual, the brain and the project record, then checks its own connections before using any.
4. If something may already have been sent or run, find the proof before doing it again.
