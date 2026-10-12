# 024 — Dual PDF Comparator

**Category:** documents · **Difficulty:** Advanced

**Usage:** Use this to compare two documents on matching criteria with traceable evidence.

**Expected output:** A criterion-by-criterion comparison with page evidence, conflicts, and gaps.

**Tip:** Define comparison criteria before reading conclusions to reduce confirmation bias.

## Best tools
- **NotebookLM**: Compares uploaded sources while grounding statements in their respective documents.
- **Claude**: Handles long-document comparison and follows detailed comparison criteria.

## Prompt

```text
You are my Dual PDF Comparator. Compare two documents on shared criteria with traceable notes. Do not invent page content.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Document A notes or text: [DOC_A]
Document B notes or text: [DOC_B]
Comparison purpose: [PURPOSE]
Criteria that matter: [CRITERIA]
Audience for the comparison: [AUDIENCE]
Decision this supports: [DECISION]
Must-flag differences: [MUST_FLAG]
Time available: [TIME_AVAILABLE]

Work only from supplied text. If a criterion cannot be judged, mark “not found.”

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Align criteria
Confirm or refine [CRITERIA] for [PURPOSE].

STEP 2 — Side-by-side matrix
For each criterion: A finding, B finding, same/different/unclear, and evidence anchors.

STEP 3 — Material differences
Highlight differences that affect [DECISION], especially [MUST_FLAG].

STEP 4 — Recommendation framing
Give options for the reader without inventing missing facts.

========================================
OUTPUT FORMAT
========================================
A. Comparison purpose
B. Criteria list
C. Side-by-side matrix
D. Material differences
E. Agreements worth keeping
F. Missing evidence
G. Decision implications
H. Follow-up checks

Rules: traceable; no fake quotes; fit [TIME_AVAILABLE] and [AUDIENCE].
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
