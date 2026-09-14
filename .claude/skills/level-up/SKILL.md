---
name: level-up
description: The weekly habit that makes the system more useful. Finds the one repeated job or gap worth fixing, decides whether to cut it, automate it or hand it to a person, scopes it, and ships one working improvement. Use when the owner says "level up", "what should I automate", "what's next for my AI", "take this off my plate", "how do I stop doing this", after an audit, or once a week.
---

# Level up

One run, one shipped improvement. Not a list of ideas. A small thing that works beats a big thing that is planned.

## Read first

`Context/Priorities.md`, `Brain/USER.md`, `Projects/_index.md`, `System/Connections.md`, the newest report in `System/Audits/`, the last ten entries in `Decisions/Log.md`, and the list of skills in `.claude/skills/`.

If an audit named a gap, or the owner named a job, start with that. Ask only for what the files do not say.

## 1. Find the candidate

If nothing is named yet, ask these together:
1. What did you do three or more times this week?
2. What felt boring, copy and paste, or beneath you?
3. What slipped through the cracks?
4. If twice the customers turned up tomorrow, what would break first?

Name up to three candidates. Rank them by how much each attacks the constraint in `Context/Priorities.md`, with one line of reason each. Recommend one and start on it unless they redirect.

## 2. Cut, automate or hand over

In this order:
1. Cut it. What happens if this just stops? If nothing important breaks, stop doing it. That is a win. Log it and finish.
2. Automate it. If it follows the same steps most of the time, the system can do some or all of it.
3. Hand it to a person. If it needs judgement, relationships or hands, it belongs to a human. Write a short brief for who should own it, log it and finish.

## 3. Map it

Five things, in plain words:
- What starts it.
- What information it needs, and where that lives.
- The steps.
- The decisions along the way.
- Where the result goes, and who sees it.

If the owner cannot describe the steps, it is not ready to automate. Have them do it once by hand with you watching, write down what happened, and come back.

## 4. How much the assistant does

Choose the lowest level that solves the problem:
1. Suggests. The owner decides and does everything.
2. Drafts. The owner reviews and sends or saves.
3. Does it and reports. The owner checks the results regularly.
4. Does it alone.

Start at 1 or 2 for anything that touches customers, money or anything public. Level 4 only after the lower levels have run cleanly for a while, and never for the five things in "Always confirm first".

## 5. Tie it to a number

Which does it move: more customers, more value from each customer, or less time and cost? Name the number and how it will be measured. If nothing measurable moves, question whether it is worth building.

## 6. Build the smallest version

Pick the simplest thing that works, in this order:
1. A saved prompt the owner runs by hand.
2. A skill that follows fixed steps, built with the make-skill skill.
3. A skill that uses a script in `Tools/` for the fixed parts.
4. A helper agent, only when the job genuinely needs its own research and judgement.

Anything on a schedule waits until it has worked by hand more than once, then goes through `System/Automations.md`.

Build it. Run it once on a real example with the owner. Fix what they correct.

## 7. Record it

1. One entry in `Decisions/Log.md`: what was chosen, the map, the level, the number, and why.
2. If it belongs to a project, update that project's `_index.md`. If it is new work, create the project.
3. Run `python3 Tools/check.py` and commit.

## Reply

What was built, how to use it in one line, the number it should move, and when to check that it worked. Then suggest running the audit again after it has been used for a week.
