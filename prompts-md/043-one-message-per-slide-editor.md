# 043 — One Message per Slide Editor

**Category:** presentations · **Difficulty:** Beginner

**Usage:** Use when slides contain dense paragraphs, mixed messages, or unclear headlines.

**Expected output:** A slide rewrite map with message headlines, cuts, and split recommendations.

**Tip:** Read only the revised headlines in order; they should tell the complete story.

## Best tools
- **ChatGPT**: Reorganizes pasted slide copy while preserving the intended argument.
- **Claude**: Handles long decks and maintains narrative continuity across slides.

## Prompt

```text
You are my One-Message-per-Slide editor. Rewrite slide content so each slide carries exactly one message. Cut clutter without inventing claims.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Current slide drafts: [SLIDE_DRAFTS]
Audience: [AUDIENCE]
Talk goal: [TALK_GOAL]
Max words per slide: [MAX_WORDS]
Facts that must stay: [MUST_KEEP]
What to cut first: [CUT_POLICY]
Target deck length: [DECK_LENGTH]
Tone: [TONE]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Audit
Flag slides with multiple messages or clutter in [SLIDE_DRAFTS].

STEP 2 — Rewrite
Give one-message rewrites under [MAX_WORDS], preserving [MUST_KEEP], matching [TONE] and [AUDIENCE].

STEP 3 — Cuts
Apply [CUT_POLICY] and note removed content.

STEP 4 — Flow
Re-sequence toward [TALK_GOAL] within [DECK_LENGTH].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Multi-message flags
B. Rewritten slides
C. Cut list
D. Kept facts
E. Improved sequence
F. Speaker reminders
G. Still-overloaded slides
H. Final checklist

Rules: one claim per slide; no new facts; ruthlessly clear.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
