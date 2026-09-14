---
name: grill-me
description: Interview the owner hard on a plan, an idea or a part of their business, saving every answer the moment it is given so nothing is lost. Use when they say "grill me", "stress test this plan", "poke holes in this", "interview me about", "get this out of my head", "help me think this through", "let's go deep on", or when a project needs context that only lives in their head.
---

# Grill me

Pull what is in the owner's head into a saved file, and find the holes in a plan before reality does. The file is the point. A long interview outgrows the chat, so every answer is saved before the next question.

## Set up

1. Read the manual, then only the context and project files that relate to the topic. Never ask something the files already answer. Confirm it instead.
2. Get today's date from the system clock.
3. Create `Context/Interviews/<YYYY-MM-DD> <Topic>.md` from `Templates/Interview.md`. Never overwrite an existing file. Add a number if the name is taken. To resume an earlier interview, open it and continue its numbering.
4. Add a line for it in `Context/Interviews/_index.md`.
5. Tell them in one line where it is saving. Then ask the first question.

## The method

- One question at a time. This skill goes deep, so each answer shapes the next question.
- Settle the big decision first, then the ones that depend on it.
- Push on the soft spots: the assumption with no evidence, the number that is a guess, the step nobody owns, the thing that happens if it goes wrong.
- For a decision, you may offer your recommendation with one reason, clearly labelled as yours. For a fact about their business or life, ask neutrally and never put words in their mouth.
- If a file or tool can answer it, check that instead of asking.
- When they cannot answer, write it as an open item with who could answer it, and move on.

## After every answer

Before asking the next question:

1. Add the question and answer to the file: what was asked, what they said in their words where it matters, confirmed facts, ideas and guesses labelled as such, and anything open.
2. Update "What we now know". If an answer changes an earlier one, mark the earlier one superseded. Do not delete it.
3. Read the saved entry back from the file to prove it saved. If saving fails, say so and keep the answer in the chat. Do not keep going as if it saved.

## Finishing

Stop when they say stop, or when every useful branch is covered. Ask once near the end: "Anything we haven't touched?"

1. Read the whole file for contradictions and gaps. List them. Never pick a side on a fact for them.
2. Set the status to finished or paused, with where to resume.
3. If the interview was about their business or their assistant, copy confirmed facts into the right `Context/` or `Brain/` file with a link back to the interview. Confirmed decisions go in `Decisions/Log.md`. Ideas stay in the interview.
4. If it was about a project, update that project's `_index.md`.
5. Reply with: where it is saved, what files were updated, the open items, and the one next step.
