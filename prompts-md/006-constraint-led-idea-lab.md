# 006 — Constraint-Led Idea Lab

**Category:** assistants · **Difficulty:** Intermediate

**Usage:** Use this to generate feasible ideas within real limits instead of generic brainstorming.

**Expected output:** A diverse shortlist of feasible concepts with tests and rejection reasons.

**Tip:** Include one unusual constraint; it often produces more distinctive ideas than asking for creativity.

## Best tools
- **Gemini**: Generates and reorganizes diverse concepts from detailed contextual constraints.
- **DeepSeek**: Offers capable text brainstorming and structured option comparison.

## Prompt

```text
Run a constraint-led idea lab for the goal [GOAL], prioritising usefulness over sheer quantity.

The audience is [AUDIENCE]. We have [BUDGET], [TIME], [TEAM_SIZE], and access to [RESOURCES]. We must respect [NON_NEGOTIABLES], avoid [EXCLUSIONS], and account for [LOCAL_CONTEXT]. Success means [MEASURE_OF_SUCCESS].

Generate ideas in three deliberately different waves:
Wave 1 — five dependable ideas using familiar methods.
Wave 2 — five combinations that borrow a mechanism from [OTHER_FIELD].
Wave 3 — three “reverse assumption” ideas that challenge how this is normally done.

Each idea must fit on three lines: concept, why it fits the constraints, and its weakest point. Do not repeat the same core mechanism under new names.

Next, apply a hard filter: eliminate anything that exceeds a non-negotiable limit and explain each rejection in one sentence. Score the survivors from 1–5 for impact, effort, inclusion, and testability. Select a portfolio of three: one safe, one balanced, and one bold.

For each finalist, design a [DAYS]-day pilot requiring no more than [PILOT_BUDGET]. End with the single piece of evidence that would make us stop, adapt, or scale each pilot.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
