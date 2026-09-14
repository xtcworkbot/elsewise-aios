# Brain

Who the assistant is, who the owner is, and how they work together. SOUL, USER and HEARTBEAT are loaded at the start of every session by `.claude/hooks/load-brain.py`. STANDARD is read when the rules matter. The reply section of VOICE is loaded on every message. Keep each one short. Detail belongs in `Context/`, `Memory/` or a project.

- `SOUL.md`: the assistant's name, role, personality and the minds it draws on.
- `USER.md`: who the owner is, what drives them, how they work, what frustrates them.
- `STANDARD.md`: the house rules for working together, plus the owner's own rules.
- `VOICE.md`: how the assistant replies, and how the owner writes to other people.
- `HEARTBEAT.md`: what the assistant watches and when to raise it.
