# 034 — Clarification Gate Designer

**Category:** prompting · **Difficulty:** Intermediate

**Usage:** Use this to make an AI ask important questions before attempting the task.

**Expected output:** A two-stage prompt with a strict clarification gate and fallback assumptions.

**Tip:** Tell the model to ask only decision-changing questions, or the intake can become tedious.

## Best tools
- **ChatGPT**: Handles multi-turn clarification and adapts later output to user responses.
- **Claude**: Maintains detailed answers from an intake phase through final delivery.

## Prompt

```text
You are my Clarification Gate designer. Make an AI ask the important questions before attempting the task.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Task the AI will eventually do: [TASK]
Facts it must know first: [MUST_KNOW]
Optional helpful facts: [NICE_TO_KNOW]
Maximum clarifying questions: [MAX_QUESTIONS]
User patience level: [USER_PATIENCE]
Defaults allowed if user skips: [DEFAULTS_OK]
What breaks if the AI guesses: [FAILURE_IF_GUESS]
AI tool this gate is for: [TOOL]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Gate logic
Define what must be asked, what can default, and when to proceed for [TASK].

STEP 2 — Question set
Write at most [MAX_QUESTIONS] high-value questions covering [MUST_KNOW], suited to [USER_PATIENCE].

STEP 3 — Proceed rules
State proceed / ask-more / refuse-to-guess rules tied to [FAILURE_IF_GUESS].

STEP 4 — Prompt pack
Deliver the clarification-gate prompt ready for [TOOL].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Must-know list
B. Question gate
C. Defaults policy
D. Proceed / stop rules
E. Ready-to-paste prompt
F. Example dialogue
G. Guessing risks blocked
H. Tuning notes

Rules: ask less but better; never silently invent [MUST_KNOW] details.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
