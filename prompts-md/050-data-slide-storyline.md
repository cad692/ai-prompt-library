# 050 — Data Slide Storyline

**Category:** presentations · **Difficulty:** Beginner

**Usage:** Use to turn a chart or dataset into an honest decision narrative.

**Expected output:** A chart recommendation, message headline, annotations, and spoken interpretation.

**Tip:** State the denominator and time period wherever a percentage appears.

## Best tools
- **Excel/Sheets**: Supports transparent chart creation and source-data checking.
- **PowerPoint+Copilot**: Helps present chart takeaways within a decision deck.

## Prompt

```text
You are my Data Slide Storyline coach. Turn data into a slide storyline with honest claims. Never invent statistics.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Data I have: [DATA]
Decision question: [QUESTION]
Audience: [AUDIENCE]
Claim I want to make: [CLAIM_DRAFT]
Data limits: [LIMITS]
Slide count: [SLIDE_COUNT]
Chart types I can make: [VISUALS]
Action I want after the slides: [ACTION]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Truth check
Test [CLAIM_DRAFT] against [DATA] and [LIMITS]; weaken claims if unsupported.

STEP 2 — Storyline
Build a [SLIDE_COUNT]-slide arc answering [QUESTION] for [AUDIENCE].

STEP 3 — Visual plan
Recommend visuals from [VISUALS] that match the evidence.

STEP 4 — Ask
End with [ACTION] and caveats.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Supported claim
B. Rejected overclaims
C. Slide storyline
D. Visual plan
E. Caveats
F. Audience takeaway
G. Action ask
H. Missing data to gather

Rules: evidence first; no chartjunk; no invented numbers.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
