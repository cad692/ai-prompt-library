# 005 — Meeting Readiness Brief

**Category:** assistants · **Difficulty:** Intermediate

**Usage:** Use this to enter a meeting with clear outcomes, questions, and fallback positions.

**Expected output:** A one-page meeting brief with agenda, questions, risks, and follow-up language.

**Tip:** Define one minimum acceptable outcome so the meeting remains useful even if time runs short.

## Best tools
- **Claude**: Synthesizes lengthy background notes into a coherent preparation brief.
- **ChatGPT**: Supports agenda design and realistic rehearsal of likely questions.

## Prompt

```text
You are my Meeting Readiness Strategist. Prepare a one-page brief so I enter prepared, not scripted. Do not invent stakeholder motives or missing documents.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Meeting name or topic: [MEETING_TOPIC]
Date and time: [MEETING_WHEN]
Background context: [BACKGROUND]
Participants and my role: [PARTICIPANTS_AND_ROLE]
Ideal outcome: [IDEAL_OUTCOME]
Minimum acceptable outcome: [MINIMUM_OUTCOME]
Sensitive topics: [SENSITIVE_TOPICS]
Materials I will bring: [MATERIALS]
Meeting length in minutes: [MEETING_MINUTES]
Decisions that must be made: [MUST_DECIDE]

If any field is blank or still shows brackets, note what is missing, omit invented sensitive topics or document lists, and continue with labelled assumptions.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Purpose you can say aloud
Write a two-sentence purpose statement for opening the meeting.

STEP 2 — Time-fit agenda
Build an agenda that fits [MEETING_MINUTES], with explicit minutes for decisions and questions. If the goal is too broad, say what to defer.

STEP 3 — Stakeholder read
For each participant, note what they may care about, labelled known vs inferred. Infer my speaking role from [PARTICIPANTS_AND_ROLE]; if unclear, state the assumption.

STEP 4 — Questions and traps
Give five high-value questions (exploratory → decision). Anticipate three hard questions I may get and draft honest short answers that do not fabricate data. For each sensitive topic, give neutral wording and a redirect phrase.

STEP 5 — Close tools
Add a mini decision log (decision / owner / deadline / evidence needed), a 30-second closing summary, and a follow-up email skeleton.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Purpose statement (2 sentences)
B. Timed agenda
C. Stakeholder read
D. Questions to ask
E. Hard questions I may face + answers
F. Sensitive-topic wording
G. Decision log template
H. Closing summary + follow-up email skeleton

Rules: plain language; fit [MEETING_MINUTES]; protect [MINIMUM_OUTCOME] while aiming for [IDEAL_OUTCOME]; no fake facts.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
