---
name: audit
description: Check whether this AI operating system actually works, on evidence, and name the one gap worth fixing next. Saves a dated report and tracks every finding across runs. Use when the owner says "audit my system", "check my AI OS", "is this set up right", "what's broken", "health check", "how good is my setup", after a big change, or about a week after onboarding.
---

# Audit

A folder, an installed skill or a saved key is not proof anything works. This audit only gives credit for what it can see working. It reads and reports. It changes nothing except saving its own report.

## Before checking

1. Get today's date. Read the manual.
2. Read the newest report in `System/Audits/` if there is one. Carry every finding forward with its ID. Recheck each one. Never assume an old result is still true.
3. Run `python3 Tools/check.py` and keep its output as evidence.

## The six areas

Grade each area Working, Needs work, or Not started. Give the evidence behind every grade: the file, the result, or the date of a real run. When something could not be checked, say "not checked" and why. Unchecked is never the same as broken, and never the same as working.

### 1. Identity

Could a brand new session understand the owner and the goal without this chat?
- The brain files, context and priorities are filled with real content, not "Not set yet".
- The facts agree with each other across `Brain/`, `Context/` and the manual.
- The priorities have numbers, dates or deliverables, and were confirmed in the last 90 days.

### 2. Finding things

Ask five real questions, adapted to the owner's actual work, and follow the routes the manual declares:
1. What does the business do, for whom, and what matters most right now?
2. Where is the current state and next step of the most important live project?
3. Why was a recent decision made?
4. Where is a file or document the owner uses often?
5. How would you reach the data behind the number the owner watches?

For each: the route tried, where it led, and whether it was found directly, found only by searching, or not found. Finding it by searching means the route is broken.

### 3. Wiring

- The check script passes.
- The two manuals match and the manual is under 200 lines.
- Every skill has its Codex pointer. Every agent exists for both engines.
- `System/Platforms.md` shows which checks have really been tested in each engine.

### 4. Connections

For each tool in `System/Connections.md`: is there a dated, real test result? Configured is not signed in. Signed in is not tested. Where a safe read-only check exists, you may run it. Never send, post, spend or change anything to test a connection.

### 5. Workflows

Pick up to three workflows tied to the current priorities. For each: is there a skill or written process, has it produced a real output that someone used, and has it been used more than once? A skill that has never run is a draft.

### 6. Upkeep

- Live projects have a next step with a date that has not quietly passed.
- Decisions and lessons were written in the last 30 days, if work happened.
- `Scratch/` has nothing older than 14 days.
- Automations in `System/Automations.md` have a recent successful run, or are marked as manual.

## Findings

Every problem gets a stable ID, like A1, A2. Keep the same ID for the same problem in later audits. For each finding record: ID, area, what is wrong, the evidence, the effect on the owner, the fix, what would prove it fixed, and a status: new, still open, fixed, came back, or not rechecked. Only mark it fixed when the proof check passes.

## Report

Save `System/Audits/<YYYY-MM-DD> Audit.md` and add a line to `System/Audits/_index.md`. Never overwrite an earlier report. The report holds:

1. The date, and what was and was not checked.
2. The six areas with grades and evidence.
3. The five questions and their results.
4. Every finding, carried and new.
5. What changed since the last audit: real fixes, new problems, and anything only now checked.
6. The one gap to fix next, and a ready-to-use line to start it with the level-up skill.

Read the saved report back.

## Reply to the owner

Keep it short: the overall state in one sentence, the grade for each area in one line each, and the one gap to fix next with why. Point to the saved report for the rest.
