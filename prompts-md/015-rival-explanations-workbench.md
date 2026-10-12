# 015 — Rival Explanations Workbench

**Category:** research · **Difficulty:** Advanced

**Usage:** Use this to test multiple explanations for an observation without anchoring early.

**Expected output:** A set of competing explanations with predictions, tests, and update rules.

**Tip:** Seek evidence that distinguishes hypotheses, not more evidence compatible with all of them.

## Best tools
- **ChatGPT**: Generates competing hypotheses and structures discriminating tests interactively.
- **Claude**: Maintains nuanced causal models across substantial background material.

## Prompt

```text
You are my Rival Explanations Workbench. Generate and stress-test multiple explanations without anchoring on my first belief.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Observation or outcome to explain: [OBSERVATION]
Context around it: [CONTEXT]
Data or facts I already have: [KNOWN_DATA]
My current leading belief: [CURRENT_BELIEF]
Limits on tests (time, access, ethics, budget): [TEST_LIMITS]
Result that would surprise me: [SURPRISING_RESULT]
Hypothesis I want stress-tested: [LEAD_HYPOTHESIS]
Alternative result worth watching: [RIVAL_RESULT]

If any field is blank or still shows brackets, list the gap and continue with labelled assumptions. Do not invent measurements I did not supply.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Rival set
Produce at least four rival explanations, including one that challenges [CURRENT_BELIEF] / [LEAD_HYPOTHESIS]. Keep them mutually distinct.

STEP 2 — Predictions
For each explanation, state what else should be true and what should not be true.

STEP 3 — Discriminating tests
Design tests that fit [TEST_LIMITS]. Prefer tests that can kill explanations, not only support favourites.

STEP 4 — Update rules
Say which evidence would raise, lower, or retire each explanation, including responses to [SURPRISING_RESULT] and [RIVAL_RESULT].

========================================
OUTPUT FORMAT
========================================
A. Observation restated
B. Rival explanations (4+)
C. Predictions table
D. Discriminating tests
E. Update rules
F. What would falsify the lead belief
G. Ranked current plausibility (labelled speculative)
H. Next smallest test to run

Rules: no early anchoring; no fake data; respect ethics and [TEST_LIMITS].
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
