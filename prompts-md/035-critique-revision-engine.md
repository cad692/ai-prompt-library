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
Build a critique-then-revise loop for improving [DRAFT_TYPE] against [GOAL].

The draft will be supplied as [DRAFT]. The audience is [AUDIENCE], constraints are [CONSTRAINTS], and non-negotiable content is [MUST_PRESERVE]. Create a rubric with four to six criteria tailored to this task, each having a concrete pass condition. Avoid vague labels such as “good” without observable evidence.

The loop must run in distinct passes:
Pass A — Diagnose: quote or locate each issue and score the rubric.
Pass B — Plan: rank no more than five changes by impact.
Pass C — Revise: edit only what the plan justifies.
Pass D — Verify: rescore and check facts, constraints, and preserved meaning.

Instruct the model to show concise rationale and checkable evidence, not private hidden chain-of-thought. Require a change log that maps every major edit to one diagnosed issue. If revision would need missing facts, insert [NEEDS INPUT] instead of inventing them.

Set a stop rule: finish when all critical criteria pass or after [MAX_ROUNDS] rounds, whichever comes first. If the score does not improve, preserve the strongest version and explain the blockage. Return the complete reusable prompt, followed by one miniature demonstration using [SHORT_SAMPLE] and a note on when human review remains essential.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
