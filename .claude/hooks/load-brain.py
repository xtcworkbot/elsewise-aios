#!/usr/bin/env python3
"""Start of session: load the brain so the assistant wakes up knowing who it is.

Reads the identity files, the memory index, the priorities and the open projects,
and hands them to the session as context. Claude runs it from .claude/settings.json.
Codex runs the same script from .codex/hooks.json.

Before onboarding it says so instead, so the first thing a new owner sees is the
invitation to set the system up.

It reads files only, makes no model call, and always exits 0. A missing file is
never worth failing a session over.
"""
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAX_CHARS = 12000

FILES = [
    ("Who you are", "Brain/SOUL.md"),
    ("Who the owner is", "Brain/USER.md"),
    ("What to watch", "Brain/HEARTBEAT.md"),
    ("The goal and priorities", "Context/Priorities.md"),
    ("Memory index", "Memory/MEMORY.md"),
    ("Open projects", "Projects/_index.md"),
]


def read(relative):
    path = ROOT / relative
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return f"({relative} is missing.)"
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS] + f"\n\n({relative} was cut short here. Open the file for the rest.)"
    return text


def not_onboarded():
    manual = ROOT / "CLAUDE.md"
    try:
        return "{{" in manual.read_text(encoding="utf-8")
    except OSError:
        return True


def intake_status():
    try:
        for line in (ROOT / "System/Intake.md").read_text(encoding="utf-8").splitlines():
            if line.startswith("Status:"):
                return line.split(":", 1)[1].strip().rstrip(".")
    except OSError:
        pass
    return "not started"


def build_context():
    now = datetime.now().astimezone()
    stamp = now.strftime("%A %d %B %Y, %I:%M %p %Z")
    if not_onboarded():
        status = intake_status()
        return (
            f"Today is {stamp}.\n\n"
            "This AI operating system has not been set up yet. Onboarding status: "
            f"{status}.\n\n"
            "When the owner first speaks, greet them warmly in no more than two short lines. "
            "Tell them this folder becomes their own AI operating system once it knows who they "
            "are, and that setup takes about 30 to 40 minutes of conversation. "
            "Ask them to type /onboard in Claude Code or $onboard in Codex. "
            "If onboarding was started before, offer to pick up where it stopped. "
            "Do not start any other work until onboarding is finished, unless they insist."
        )
    parts = [
        f"Today is {stamp}.",
        "These are the brain files for this AI operating system, loaded at the start of the session. "
        "Act on them. They are who you are and who you work for, not background reading. "
        "The manual in CLAUDE.md or AGENTS.md carries the rules and the routes.",
    ]
    for title, relative in FILES:
        parts.append(f"===== {title}: {relative} =====\n{read(relative)}")
    return "\n\n".join(parts)


def main():
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": build_context(),
        }
    }))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
