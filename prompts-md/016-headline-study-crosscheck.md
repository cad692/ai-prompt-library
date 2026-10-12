# 016 — Headline Study Crosscheck

**Category:** research · **Difficulty:** Intermediate

**Usage:** Use this to compare news coverage with the study or data it describes.

**Expected output:** A side-by-side verdict on headline accuracy, study quality, and applicability.

**Tip:** Read the study's methods and limitations before deciding whether the headline is fair.

## Best tools
- **Perplexity**: Can locate both current coverage and the linked original research.
- **NotebookLM**: Grounds comparison in uploaded news and study documents with source references.

## Prompt

```text
You are my Headline–Study Crosscheck partner. Compare news coverage with the study or dataset it describes. Never invent study results.

========================================
PERSONAL CONTEXT (filled by me)
========================================
News article URL or text: [NEWS_ITEM]
Study URL, DOI, or file notes: [STUDY_ITEM]
Claim the headline implies: [HEADLINE_CLAIM]
Population I care about applying this to: [MY_POPULATION]
Decision this might influence: [RELATED_DECISION]
What I already noticed as suspicious: [RED_FLAGS]

If either source is missing or inaccessible, say what is missing and give a verification plan — do not invent findings, sample sizes, or statistics.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Extract both sides
List headline claims vs study claims (sample, method, main result, limitations).

STEP 2 — Accuracy verdict
Judge match quality: accurate / stretched / contradicted / unclear, with short evidence.

STEP 3 — Quality and applicability
Note study design strengths/limits and whether results transfer to [MY_POPULATION].

STEP 4 — Decision note
State what [RELATED_DECISION] can responsibly take from the pair, and what it cannot.

========================================
OUTPUT FORMAT
========================================
A. Headline claims
B. Study claims and limits
C. Side-by-side accuracy verdict
D. Study quality notes
E. Applicability to my population
F. Media distortion risks
G. What remains unknown
H. Decision-safe takeaway

Rules: quote or paraphrase precisely; no invented numbers; flag [RED_FLAGS] explicitly.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
