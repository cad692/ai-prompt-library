# 040 — Output Rubric Designer

**Category:** prompting · **Difficulty:** Advanced

**Usage:** Use this to define measurable criteria for evaluating an AI-generated output.

**Expected output:** A weighted rubric with anchors, failure gates, and a calibration exercise.

**Tip:** Weight factuality and safety separately from style so polished errors cannot score highly.

## Best tools
- **ChatGPT**: Builds task-specific rubrics and applies them iteratively to sample outputs.
- **Claude**: Provides nuanced criterion definitions and evidence-based evaluations of long outputs.

## Prompt

```text
You are my Output Rubric Designer. Define measurable criteria for evaluating an AI-generated deliverable.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Deliverable to evaluate: [DELIVERABLE]
Audience judging quality: [AUDIENCE]
Must-pass criteria: [MUST_PASS]
Nice-to-have criteria: [NICE_TO_HAVE]
Scoring scale to use: [SCALE]
Examples of failure: [FAILURE_EXAMPLES]
Weighting preferences: [WEIGHTS_HINT]
How the rubric will be used: [USE_CASE]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Criteria
Turn [MUST_PASS] and [NICE_TO_HAVE] into observable rubric rows for [DELIVERABLE].

STEP 2 — Scale
Define [SCALE] descriptors with concrete anchors, including [FAILURE_EXAMPLES].

STEP 3 — Weights
Propose weights from [WEIGHTS_HINT] that total 100.

STEP 4 — Usage
Explain how to apply the rubric in [USE_CASE] for [AUDIENCE], including AI-assisted pre-score caveats.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Rubric table
B. Scale descriptors
C. Weights
D. Fail-fast gates
E. Worked scoring example
F. Common scoring mistakes
G. AI pre-score caution
H. Revision priorities

Rules: measurable over vague; no personality scoring; keep criteria observable.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
