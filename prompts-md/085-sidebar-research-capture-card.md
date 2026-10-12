# 085 — Browser Sidebar Research Capture Card

**Category:** addins · **Difficulty:** Intermediate

**Usage:** Capture a web source into reusable evidence notes without confusing claims with conclusions.

**Expected output:** A source card with claims, quotes, limitations, and follow-up questions.

**Tip:** Open the original source and verify quotations instead of trusting the sidebar summary.

## Best tools
- **Browser AI sidebar**: Can summarise the open page while keeping its URL and visible context nearby.

## Prompt

```text
You are my Browser Sidebar Research Capture Card maker. Turn a webpage reading into a portable research capture card. No invented citations.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Page notes or paste: [PAGE_NOTES]
URL or title: [URL_OR_TITLE]
Research question: [RESEARCH_QUESTION]
Claim focus: [CLAIM_FOCUS]
What I need to capture: [NEED]
Card style: [STYLE]
Project this feeds: [PROJECT]
What to verify later: [VERIFY]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Capture
Build a card from [PAGE_NOTES] tied to [RESEARCH_QUESTION] and [PROJECT].

STEP 2 — Claims
Extract claims relevant to [CLAIM_FOCUS] with anchors from the page.

STEP 3 — Gaps
List [VERIFY] items and missing context.

STEP 4 — Format
Deliver in [STYLE] including [URL_OR_TITLE] and [NEED].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Capture card
B. Key claims + anchors
C. Methods/limits noted
D. Relevance to RQ
E. Verification list
F. Quote candidates
G. Tags for filing
H. One-line usefulness rating

Rules: page-grounded only; never invent authors/dates/quotes.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
