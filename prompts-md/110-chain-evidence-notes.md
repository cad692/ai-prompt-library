# 110 — Chain Step 2 - Evidence Notes

**Category:** chains · **Difficulty:** Advanced

**Usage:** Convert the approved research brief into traceable, source-level evidence notes.

**Expected output:** An evidence ledger mapped to the brief's research questions.

**Tip:** Save quotations with page numbers or section locations at capture time.

## Best tools
- **Perplexity**: Supports source discovery with links that can be checked against originals.

## Prompt

```text
You are my Chain Evidence Notes maker. Turn sources into evidence notes for the research chain. No invented quotes.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Research brief: [BRIEF]
Sources to note: [SOURCES]
Questions to answer: [QUESTION_SET]
Note style: [NOTE_STYLE]
Quote rule: [QUOTE_RULE]
Gaps to watch: [GAPS]
Project name: [PROJECT]
Handoff to synthesis: [HANDOFF]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Notes
Create source-by-source notes from [SOURCES] against [QUESTION_SET] and [BRIEF].

STEP 2 — Quotes
Follow [QUOTE_RULE]; never invent.

STEP 3 — Gaps
Flag [GAPS].

STEP 4 — Handoff
Format for [HANDOFF] synthesis in [NOTE_STYLE] for [PROJECT].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Source note cards
B. Question coverage matrix
C. Quote bank
D. Gap list
E. Credibility flags
F. Synthesis handoff pack
G. Unused sources
H. Next retrieval needs

Rules: notes only from provided sources; chain-compatible structure.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
