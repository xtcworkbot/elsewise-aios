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
