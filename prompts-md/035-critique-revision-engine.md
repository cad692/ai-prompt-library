# 035 — Critique Revision Engine

**Category:** prompting · **Difficulty:** Advanced

**Usage:** Use this to build a prompt that critiques an output before revising it.

**Expected output:** A reusable critique-then-revise prompt with stop conditions and change tracking.

**Tip:** Make the critique cite exact draft locations so revision does not become a total rewrite.

## Best tools
- **Claude**: Performs nuanced long-form critique and revision while preserving intent.
- **ChatGPT**: Supports rubric-based iteration and transparent change summaries.

## Prompt

```text
You are my Critique→Revision Engine builder. Build a prompt that critiques an output against criteria before revising it.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Type of output to improve: [OUTPUT_TYPE]
Rubric or quality criteria: [RUBRIC]
Sample output to critique: [SAMPLE_OUTPUT]
What must stay unchanged: [MUST_PRESERVE]
Goal of the revision: [REVISION_GOAL]
Audience for the revised output: [AUDIENCE]
How strict the critique should be: [STRICTNESS]
Critique-revise rounds needed: [ROUNDS]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Critique
Score [SAMPLE_OUTPUT] against [RUBRIC] at [STRICTNESS]; cite concrete issues.

STEP 2 — Preserve
List what must not change from [MUST_PRESERVE].

STEP 3 — Revise
Produce a revised version aimed at [REVISION_GOAL] for [AUDIENCE].

STEP 4 — Engine prompt
Package the critique-then-revise workflow into a reusable prompt for [ROUNDS] rounds.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Critique scorecard
B. Issue list with evidence
C. Preservation constraints
D. Revised output
E. Change log
F. Reusable engine prompt
G. Stop conditions
H. Residual risks

Rules: critique before rewrite; no silent meaning changes; honour [MUST_PRESERVE].
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
