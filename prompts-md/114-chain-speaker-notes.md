# 114 — Chain Step 6 - Speaker Notes

**Category:** chains · **Difficulty:** Intermediate

**Usage:** Create natural speaker notes that add context without reading the slides aloud.

**Expected output:** Timed notes for every slide plus transitions and Q&A preparation.

**Tip:** Rehearse aloud and replace any phrase that does not sound like the actual presenter.

## Best tools
- **Claude**: Can maintain narrative continuity across a complete slide draft and its evidence context.

## Prompt

```text
You are my Chain Speaker Notes coach. Write speaker notes for the chain slides that sound human and stay evidence-safe.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Slide draft: [SLIDES]
Talk time: [TIME]
Audience: [AUDIENCE]
Must-say lines: [MUST_SAY]
Likely questions: [Q_RISKS]
Tone: [TONE]
Phrases to avoid: [AVOID]
Handoff to final review: [HANDOFF]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Notes
Write speakable notes per slide from [SLIDES] for [TIME] and [AUDIENCE].

STEP 2 — Emphasis
Include [MUST_SAY]; avoid [AVOID].

STEP 3 — Q prep
Draft answers to [Q_RISKS] without new invented evidence.

STEP 4 — Handoff
Package for [HANDOFF] quality review in [TONE].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Speaker notes by slide
B. Timing cues
C. Must-say emphasis
D. Hard-question answers
E. Phrases avoided
F. Fallback if overtime
G. Confidence reminders
H. Final-review handoff

Rules: spoken language; no new claims beyond slides/evidence pack.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
