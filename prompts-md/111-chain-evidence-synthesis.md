# 111 — Chain Step 3 - Evidence Synthesis

**Category:** chains · **Difficulty:** Advanced

**Usage:** Turn verified evidence notes into findings, tensions, and calibrated implications.

**Expected output:** Thematic findings with confidence, caveats, and traceable evidence IDs.

**Tip:** A synthesis should explain relationships, not merely shorten every source.

## Best tools
- **Claude**: Can compare a long evidence ledger and preserve nuanced disagreements.

## Prompt

```text
You are my Chain Evidence Synthesiser. Synthesise evidence notes into findings for the chain. Separate fact, inference, and unknown.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Evidence notes: [NOTES]
Questions: [QUESTIONS]
Decision: [DECISION]
Known conflicts: [CONFLICTS]
Confidence rule: [CONFIDENCE_RULE]
Audience: [AUDIENCE]
Handoff to outline: [HANDOFF]
Limits: [LIMITS]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Synthesize
Answer [QUESTIONS] from [NOTES] only; label fact vs inference.

STEP 2 — Conflicts
Resolve or surface [CONFLICTS] using [CONFIDENCE_RULE] and [LIMITS].

STEP 3 — Decision link
State implications for [DECISION] for [AUDIENCE].

STEP 4 — Handoff
Package findings for [HANDOFF] presentation outline.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Findings by question
B. Fact vs inference table
C. Conflict handling
D. Confidence ratings
E. Decision implications
F. Unknowns
G. Outline handoff pack
H. Claims to avoid on slides

Rules: synthesis not spin; no new sources invented mid-chain.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
