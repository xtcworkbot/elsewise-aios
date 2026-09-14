#!/usr/bin/env python3
"""Every message: put the reply voice in front of the assistant.

Reads the "How I reply to you" section of Brain/VOICE.md and adds it to each
message as context, so the way the assistant talks to the owner never drifts
over a long session. One source for both engines. Never write reply rules
anywhere else.

It governs the words, never the depth of the work.

Off switch: create an empty file named reply-style.OFF next to this script.
Always exits 0.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HEADING = "## How I reply to you"


def reply_section():
    text = (ROOT / "Brain" / "VOICE.md").read_text(encoding="utf-8")
    if HEADING not in text:
        return ""
    section = text.split(HEADING, 1)[1]
    section = section.split("\n## ", 1)[0]
    lines = [l for l in section.splitlines() if l.strip() != "Not set yet."]
    return "\n".join(lines).strip()


def main():
    if (Path(__file__).parent / "reply-style.OFF").exists():
        return
    section = reply_section()
    if not section:
        return
    block = (
        "How to reply on this message, from Brain/VOICE.md. This governs the words you write "
        "back, never the depth of the work. Do every check the job needs, then report it this way.\n\n"
        + section
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": block,
        }
    }))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
