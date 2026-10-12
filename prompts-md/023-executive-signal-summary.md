# 023 — Executive Signal Summary

**Category:** documents · **Difficulty:** Intermediate

**Usage:** Use this to compress a long report into decisions, evidence, and implications.

**Expected output:** A one-page executive summary with findings, implications, and source locations.

**Tip:** Tell the model which decision the summary must support; relevance changes with audience.

## Best tools
- **Claude**: Maintains coherence and detail across very long documents.
- **NotebookLM**: Grounds report summaries in uploaded source passages and citations.

## Prompt

```text
You are my Executive Signal Summary partner. Compress a long report into decisions, evidence, and implications. Do not invent metrics.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Report or text to summarise: [SOURCE_REPORT]
Decision maker audience: [AUDIENCE]
Decision they must make: [DECISION]
Time they have to read: [READ_TIME]
Signals that matter most: [PRIORITY_SIGNALS]
Known constraints: [CONSTRAINTS]
What to ignore if pressed for time: [CAN_DEFER]
Tone preference: [TONE]

If the report is partial, label gaps. Never invent KPIs, quotes, or recommendations not grounded in the text.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Extract signals
Pull decisions pending, evidence offered, risks, and open questions.

STEP 2 — Rank for the reader
Prioritise what [AUDIENCE] needs for [DECISION] within [READ_TIME].

STEP 3 — Implication notes
State what follows if the evidence is right, and what breaks if a key assumption fails.

STEP 4 — Ask / act list
End with questions to ask and immediate actions that fit [CONSTRAINTS].

========================================
OUTPUT FORMAT
========================================
A. One-sentence bottom line
B. Decisions pending
C. Evidence that matters
D. Risks and uncertainties
E. Implications
F. Questions to ask
G. Deferred detail
H. Suggested next action

Rules: short; evidence-tied; honour [PRIORITY_SIGNALS] and [TONE].
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
