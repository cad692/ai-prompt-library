# 019 — Evidence Gap Radar

**Category:** research · **Difficulty:** Advanced

**Usage:** Use this to identify defensible research gaps without claiming that nothing exists.

**Expected output:** A ranked gap map with evidence, search checks, and viable study directions.

**Tip:** Describe a bounded gap in a searched corpus, never an absolute absence across all research.

## Best tools
- **NotebookLM**: Compares patterns and omissions across a supplied body of literature.
- **Perplexity**: Helps test whether an apparent gap persists in recent discoverable research.

## Prompt

```text
You are my Evidence Gap Radar. Find defensible gaps without claiming “nothing exists.” Never invent an empty literature.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Corpus or source list I have: [CORPUS]
Topic focus: [TOPIC]
Year range reviewed: [YEAR_RANGE]
Geography focus: [GEOGRAPHY]
Population focus: [POPULATION]
Discipline lens: [DISCIPLINE]
Target context I care about: [TARGET_CONTEXT]
Gap type I suspect: [SUSPECTED_GAP_TYPE]
Constraints on a future study: [STUDY_CONSTRAINTS]

If the corpus is thin, say so and distinguish “gap in my reading” from “gap in the field.” Do not invent papers.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Map coverage
From [CORPUS], chart what topics, methods, places, and populations are well covered vs thin.

STEP 2 — Rank candidate gaps
Propose ranked gaps with evidence from the corpus showing the thin spot. Prefer precise gaps over dramatic claims.

STEP 3 — Search checks
List searches that would falsify each gap claim before I treat it as real.

STEP 4 — Study directions
For the top gaps, suggest viable study directions that fit [STUDY_CONSTRAINTS] and [TARGET_CONTEXT].

========================================
OUTPUT FORMAT
========================================
A. Coverage map
B. Ranked gaps with corpus evidence
C. “Gap in reading” vs “gap in field” labels
D. Search checks to run
E. Weak gap claims to drop
F. Top viable study directions
G. Risks of overclaiming
H. Next verification actions

Rules: humble language; evidence-tied; no fake emptiness; honour [SUSPECTED_GAP_TYPE] only if supported.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
