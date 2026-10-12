# 072 — Chart to Decision Narrative

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to explain a chart in plain language without overstating it.

**Expected output:** A chart narrative with takeaway, caveats, and decision implications.

**Tip:** Read the narrative beside the chart and verify every directional claim.

## Best tools
- **ChatGPT**: Synthesizes supplied chart details into an audience-aware narrative.
- **Excel/Sheets**: Allows direct verification of values, labels, and chart construction.

## Prompt

```text
You are my Chart-to-Decision Narrative coach. Turn a chart into a decision narrative without inventing trends not in the data.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Chart description or data: [CHART_DESCRIPTION]
Decision to support: [DECISION]
Audience: [AUDIENCE]
Claim I want to make: [CLAIM_DRAFT]
Data limits: [LIMITS]
Comparison that matters: [CONTRAST]
Action options: [ACTION]
Tone: [TONE]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Read
Describe what [CHART_DESCRIPTION] actually shows, including [LIMITS].

STEP 2 — Test claim
Accept, weaken, or reject [CLAIM_DRAFT] using visible evidence and [CONTRAST].

STEP 3 — Narrative
Write a decision narrative for [AUDIENCE] tied to [DECISION].

STEP 4 — Options
Frame [ACTION] with uncertainties in [TONE].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. What the chart shows
B. What it does not show
C. Claim verdict
D. Decision narrative
E. Options & trade-offs
F. Caveats
G. Questions still open
H. One-slide takeaway

Rules: no imagined data points; decisions over decoration.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
