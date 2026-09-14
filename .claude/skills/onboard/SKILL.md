---
name: onboard
description: Set up this AI operating system for its owner, or refresh it later. Runs a deep conversational interview about the assistant they want, who they are, the business, where it is going, how they work and the tools they use, then writes every brain, context, project and system file from the answers. Use on first open, or when the owner says "onboard me", "set me up", "set up my AI", "refresh my onboarding", "update who I am", or the manual still shows names in double curly brackets.
---

# Onboard

Turn this empty system into the owner's own AI operating system. The interview is the product. A thin interview builds a bot that knows a few facts. A deep one builds an assistant that feels like it has worked with them for months.

Plan for 30 to 40 minutes of conversation. Never rush it to save time.

## Before the first question

1. Read `CLAUDE.md` or `AGENTS.md`, then `System/Intake.md`.
2. If the intake status is "finished", this is a refresh. Go to "Refreshing later" at the bottom.
3. If the status is "in progress", say which section you are resuming from, then continue. Never re-ask a saved answer.
4. Look at what is in the folder by name only. If there are files that did not ship with the system, say you will keep them exactly as they are.
5. Say what is about to happen in three short lines: a conversation in ten parts, the answers are saved as you go so nothing is lost, and nothing gets built until they have checked a summary and said yes.
6. One line on privacy: anything they tell the assistant is processed by the AI provider running it, Anthropic for Claude or OpenAI for Codex, and they should never paste passwords or bank details. Record in `System/Intake.md` that this was said.

## How to run the interview

- One section at a time. Ask all the questions in a section together, in one message, then wait.
- Talk like a sharp consultant having a real conversation, not a form. Short questions. One plain example only where it genuinely helps.
- Never explain things any business owner already knows. Never use numbered menus unless the choice really is fixed.
- They can answer in any order, ramble, or use voice dictation. Pull the answers out of whatever they say.
- If an answer is thin, vague or contradicts an earlier one, ask one sharp follow-up before moving on. For a goal, push for a number, a date or a deliverable. "Grow the business" is not a goal.
- If they are stuck, offer a suggestion based on what they have already said, labelled as a suggestion. Never save a suggestion as their answer unless they agree to it.
- "I don't know yet" is a real answer. Save it as unknown. Unknowns become the first things worth finding out.
- After each section, write the answers into `System/Intake.md` under that section, in their words where the wording matters. Update the status line and "Next part". Then say one line reflecting back what you heard, so they feel understood, and ask the next section.
- Show progress as "Part 3 of 10".
- If they have no business, they are employed, or they are starting something, adapt section 3 and 4 to their actual work: what they do, who it is for, what they are building. Never force business questions on someone without a business.

## The ten parts

### Part 1. Your assistant

1. What do you want to call your assistant? Pick a name you would actually say out loud every day. If nothing comes to mind, say so and we will come back to it at the end.
2. What role should it play for you? A business partner who pushes back, a chief of staff who keeps everything organised, an operator who just gets things done, a coach who holds you to account, or your own mix.
3. Whose thinking do you want in your corner? Name one to three people, real or fictional, whose way of thinking you would want in the room. It borrows how they think. It never does an impression.
4. How should it address you? Your first name, a nickname, or something else.

### Part 2. You

1. Give me the short story. What do you do, and how did you end up doing it?
2. What are you genuinely great at? And what do you know you are not great at, or put off?
3. What makes you lose trust in a person or a tool you work with?

### Part 3. The business

1. What is the business called, where does it operate, and what does it do? Say it the way you would to a customer in thirty seconds.
2. What do you sell, and roughly what does each thing cost?
3. Who buys from you, why do they buy, how do they find you, and what stops the ones who do not buy?
4. Who else is involved, and who does what? Staff, partners, contractors, family.

### Part 4. Where it stands

1. What is the one number that tells you whether a week was good? Where is it right now?
2. What does a normal month look like: revenue, enquiries, sales? Rough is fine. Not knowing is useful to know.
3. Where does the money land, and where is it tracked?

### Part 5. Where it is going

1. Where do you want this to be in twelve months? Give me one number or one outcome.
   Then: why does that matter to you? What is the goal behind the goal?
2. What two or three things have to happen in the next 90 days for that to be on track?
3. What is the single biggest thing holding you back right now?
4. If you could hand one job to someone else tomorrow and never do it again, what would it be?

### Part 6. Your week

1. Walk me through a real week. Where does the time actually go?
2. What do you do over and over that you are sick of doing?
3. What falls through the cracks?

### Part 7. How it works with you

1. How should it talk to you? Describe it, or name someone who talks the way you like.
2. When you hand it a job, should it ask before starting, tell you the plan and then go, or just do it and report back? It can differ by the type of work.
3. When it thinks you are wrong, what should it do?
4. What do you never want to see in a reply? Long paragraphs, jargon, hedging, cheerleading, anything else.

### Part 8. The guardrails

1. It will always check with you before it spends money, messages a real person, publishes or changes anything live, deletes anything, or gives a tool more access. What else should it never do without asking?
2. What kinds of information must never be sent to an AI provider or uploaded anywhere? Name the kinds only, like "client contracts" or "customer phone numbers". Never the details themselves.
3. Will anyone else use this system? How should it treat them?

### Part 9. How you write

Ask them to paste two real things they wrote recently, unedited. An email, a caption, a DM, a proposal, a text to a client. Tell them why in one line: anything typed now, inside a chat with an AI, already sounds like the chat.

This is the one rule you do not bend. If they start typing something fresh, stop them politely and ask them to open their sent emails or their last post and paste the real thing. If they truly have nothing written, save "no sample yet" and move on.

### Part 10. Tools and existing work

1. What do you use for each of these: email, calendar, files and documents, customers and sales, money and accounting, marketing and social, messaging? Anything else you live in every day?
2. Which two would make the biggest difference if your assistant could reach them?
3. Where does your existing work live? Folders on your computer, project files, documents, notes apps. List them. We bring them in properly after setup.
4. At the start of each session, what should your assistant check or remind you about?

If they skipped the assistant's name in Part 1, ask it now, and offer three suggestions that fit everything you have heard.

## The summary

When all ten parts are saved, read back one tight summary with these headings: your assistant, you, the business, where it stands, where it is going, your week, how it works with you, the guardrails, how you write, tools and existing work, what it watches.

Plain lines, no padding. Flag every unknown in one list at the end.

Ask: "Is this right, and should I build it?" Wait for a clear yes. If they correct anything, fix the summary and ask again. Save the approved summary and the date of the yes in `System/Intake.md`.

## The build

Build everything in one pass after the yes. Use the owner's words wherever the wording carries meaning. Write unknowns as "Unknown as of" and the date. Never invent a fact to fill a gap.

1. Git. If the folder still points at the Elsewise repository, run `git remote remove origin` so nothing of theirs can ever be pushed there. If the folder is not a git repository, run `git init`. If git has no name set, ask "What name should appear on the save history? Your own name is fine," and set it for this folder only with `git config user.name`. Set the email to `owner@local` unless they give one. Never change their global settings.
2. `Brain/SOUL.md`. From Part 1, plus the personality that fits the role and the minds they chose. Write it as the assistant speaking about itself.
3. `Brain/USER.md`. From Parts 2 and 6, and anything revealing from the rest. This file should read like the assistant truly knows them.
4. `Brain/STANDARD.md`. Keep the house rules. Fill "The owner's own rules" from Parts 7 and 8.
5. `Brain/VOICE.md`. Under "How I reply to you", adjust the defaults to their choices in Part 7 and fill "Their tone choices" and "How to address them". Under "How you write to other people", describe the patterns in their samples in a few plain lines, then paste both samples exactly as given.
6. `Brain/HEARTBEAT.md`. Fill "What the owner wants watched" from Part 10 question 4, and add any number from Part 4 that should be watched, with where it would be read from.
7. `Context/Business.md`, `Offer.md`, `Customers.md`, `Team.md`. From Parts 3 and 4. Set "Last confirmed" to today.
8. Area files. For every part of the business they described in real detail across Parts 3, 4 and 6, such as marketing, the website, staff or cash flow, create `Context/<Area>.md` from `Templates/Area.md` with what they said, and list each in `Context/_index.md`. Do not create an area for a passing mention.
9. `Context/Priorities.md`. From Part 5. The goal, the measure from Part 4 question 1, the 90 day priorities, the constraint and the first thing to hand over.
10. `System/Connections.md`. One row per tool from Part 10, status "not connected". Name the first two to connect.
11. `System/Platforms.md`. Fill "Which AI providers may see what" from the privacy answer and Part 8 question 2.
12. Projects. Create `Projects/<Name>/_index.md` from `Templates/Project.md` for the first thing to hand over, status live, next step "scope it with the level-up skill". For each existing work location from Part 10 question 3, create a project folder with status live, the location written under "Where it is up to", and next step "bring it in with the new-project skill" dated within the next seven days. List every project in `Projects/_index.md`.
13. `Decisions/Log.md`. One entry dated today: the system was set up, the assistant's name and role, the first thing to hand over and the first two connections, and why.
14. The manual. In `CLAUDE.md` and every file in `Brain/`, replace `{{AI_NAME}}`, `{{OWNER_NAME}}`, `{{OWNER_ADDRESS}}`, `{{BUSINESS_NAME}}`, `{{ONE_LINE_BUSINESS}}`, `{{NORTH_STAR}}` and `{{MEASURE}}`. The one line business is one plain sentence about what the business does and for whom. Delete the paragraph in `CLAUDE.md` that begins "If this file still shows a name in double curly brackets". Then copy `CLAUDE.md` over `AGENTS.md` so they match exactly.
15. `System/Intake.md`. Set the status to finished, with today's date.
16. Run `python3 Tools/check.py`. Fix every failure it reports and run it again until it passes.
17. Save point. Run `git status`. Make sure nothing secret and no large media is about to be committed. Commit with the message "Set up" and the assistant's name. Local only. The private GitHub backup is offered in the close and set up with the backup skill, never before their yes.

## The close

This is the other half of onboarding. The owner has just given you forty minutes of their life. They leave knowing exactly what they now own and what to do first. Print this, filled in from their answers, and nothing else:

```
{Assistant name} is set up, {how to address them}.

What you now own:
- A brain that loads itself. Every session starts knowing who you are, {business name}, your goal of {goal}, and what is open.
- Rules you set: {their tone in three words}, {their autonomy choice in a few words}, and it {calls you out / stays quiet} when it thinks you are wrong.
- Your guardrails: it always asks before money, messaging people, publishing, deleting or widening access{, plus their extra rules in a few words}.
- A filing system that runs itself. Business facts, projects, decisions, memory and tools each have one home.
- {n} projects already set up: {list the names}.

Skills that came with it. Say the words or type the slash:
- brief: the one thing to focus on today or this week.
- grill-me: gets a plan or an idea out of your head and into a file, and finds the holes in it.
- new-project: starts a piece of work properly, or brings in a folder you already have.
- remember: saves something worth knowing next time.
- save: wraps up a session so nothing is lost, and pushes to your backup.
- backup: sets up and keeps a private copy of this folder on your GitHub.
- link: makes a file or source findable.
- audit: checks the whole system is working.
- level-up: the weekly habit, one job off your plate at a time.
- make-skill: locks in a process you have proven so it runs the same way every time.

Your first three moves:
1. Say "back this up". {Assistant name} puts a private copy of this folder on your own GitHub account, so a dead laptop never takes it with it. Every save goes there from then on.
2. Close this chat and open a new one, so {assistant name} wakes up with its brain loaded. Ask: "{Assistant name}, what's the one thing I should focus on this week?"
3. {The most useful next step from their answers: usually bring in their existing work with new-project, or connect the first tool from System/Connections.md.}

Or tell {assistant name} what is on your mind. It knows where everything goes now.
```

Make lines 2 and 3 genuinely theirs. Name the real folders, the real tool, the real job. A generic close means the build failed.

In the new session, the brief skill answers the first question from the files. It must name their real priorities and constraint. If it cannot, open the files and fix them.

## Refreshing later

When onboarding has already finished:

1. Ask what has changed: the assistant, them, the business, the numbers, the goals, how they want to work, the guardrails, their writing, or their tools.
2. Ask only that part again, showing the saved answers so they can correct rather than restart.
3. Copy the files about to change into `Archive/Onboarding <date>/` first.
4. Rebuild only the affected files, update `System/Intake.md`, run the check and commit.

## Never

- Build anything before the yes.
- Ask for passwords, API keys, bank details or private contents.
- Save a guess or a suggestion as a fact.
- Overwrite or move files that were already in the folder.
- Push to GitHub or any remote during onboarding. The backup comes after, through the backup skill, with their yes.
- Connect a tool. Connecting comes after onboarding, one tool at a time, with the owner signing in themselves.
