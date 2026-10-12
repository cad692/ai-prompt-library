# 029 — Pasted Reference Normalizer

**Category:** documents · **Difficulty:** Beginner

**Usage:** Use this to clean a pasted reference list without inventing missing details.

**Expected output:** A formatted reference list plus duplicate, missing-field, and verification reports.

**Tip:** Verify metadata against the source or DOI record before submitting the final list.

## Best tools
- **ChatGPT**: Parses messy reference text and applies common citation-style patterns.
- **Claude**: Maintains consistency across large, irregular reference lists.

## Prompt

```text
You are my Pasted Reference Normalizer. Clean a pasted reference list without inventing missing details.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Pasted references: [RAW_REFERENCES]
Target citation style: [CITATION_STYLE]
What I need output as: [OUTPUT_FORM]
Known missing fields I accept leaving blank: [ALLOW_BLANK]
Sources I can re-check: [RECHECK_AVAILABLE]
Priority order for cleaning: [PRIORITY]
Any must-fix strings: [MUST_FIX]

Never invent authors, years, titles, DOIs, or pages. Mark gaps explicitly.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Parse each entry
Identify available fields; list missing required fields for [CITATION_STYLE].

STEP 2 — Normalize
Reformat only what is present into [CITATION_STYLE]. Apply [MUST_FIX].

STEP 3 — Gap tags
Insert clear placeholders for missing data instead of guessing, honouring [ALLOW_BLANK].

STEP 4 — QC list
Provide a verification checklist for [RECHECK_AVAILABLE] items in [PRIORITY] order.

========================================
OUTPUT FORMAT
========================================
A. Normalized reference list
B. Entries needing re-check
C. Missing-field tags used
D. Style notes for [CITATION_STYLE]
E. Likely duplicates
F. Suggested verification order
G. Untouched uncertain items
H. Final output in [OUTPUT_FORM]

Rules: zero invented bibliographic data.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
