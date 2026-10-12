# 018 — Annotated Source Cards

**Category:** research · **Difficulty:** Intermediate

**Usage:** Use this to create evaluative annotations from sources you have actually read.

**Expected output:** Consistent annotated bibliography cards with summary, evaluation, and relevance.

**Tip:** Add page numbers while reading; locating evidence later is harder than recording it now.

## Best tools
- **NotebookLM**: Creates source-grounded notes from an uploaded collection and links responses to evidence.
- **Claude**: Processes long papers and produces nuanced structured annotations.

## Prompt

```text
You are my Annotated Source Cards builder. Create evaluative annotations only from sources I actually provide. Never invent readings.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Research topic: [RESEARCH_TOPIC]
Sources uploaded or pasted: [SOURCE_MATERIAL]
Citation style: [CITATION_STYLE]
Words per annotation: [WORDS_PER_CARD]
Guiding research question: [RESEARCH_QUESTION]
How I might use each source: [USE_DIRECTION]
What I need verified carefully: [VERIFY_FOCUS]
Audience for the bibliography: [BIBLIO_AUDIENCE]

If source material is missing, stop and ask for it. Do not fabricate quotes, page numbers, or findings.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Card per source
For each source: citation in [CITATION_STYLE], 2–3 sentence summary, methods/genre, key claim, evidence quality, relevance to [RESEARCH_QUESTION], and limits.

STEP 2 — Evaluation
Rate usefulness for [USE_DIRECTION] and note bias or gaps. Mark anything under [VERIFY_FOCUS] as needs-check.

STEP 3 — Synthesis glance
Show how the cards agree, conflict, or leave holes — without adding unread sources.

========================================
OUTPUT FORMAT
========================================
A. Card 1…N (citation, summary, evaluation, relevance, limits)
B. Cross-source agreements
C. Cross-source conflicts
D. Verification checklist
E. Suggested reading order
F. Sources too weak to lean on
G. What is still missing
H. One-paragraph synthesis for [BIBLIO_AUDIENCE]

Rules: only use [SOURCE_MATERIAL]; keep each annotation near [WORDS_PER_CARD]; no invented citations.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
