The Claude file lives at `.claude/skills/{name}/SKILL.md`:

---
name: {name}
description: {What it does and exactly when to use it. Include the phrases the owner actually says, in their words. This line decides whether the skill fires.}
---

# {Name}

{One paragraph: the job, and why it must run the same way every time.}

## Before you start

{What to read first. What must be true, or stop and say so.}

## Steps

1. {Step}
2. {Step}

## Finished looks like

{What the output is, where it is saved, and how it is checked.}

## Never

{The mistakes that already happened once, and anything that needs the owner's yes.}

The Codex pointer lives at `.agents/skills/{name}/SKILL.md`:

---
name: {name}
description: {the same description}
---

Read `.claude/skills/{name}/SKILL.md` from the root of this folder and follow it exactly. It is the one source for this skill in both Claude and Codex. If that file is missing, stop and tell the owner. Do not rebuild the procedure from memory.

Where the Claude file says to type /{name}, in Codex it is ${name}.
