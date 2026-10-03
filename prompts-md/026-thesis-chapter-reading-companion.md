# 026 — Thesis Chapter Reading Companion

**Category:** documents · **Difficulty:** Advanced

**Usage:** Use this to take analytical notes on a thesis chapter without rewriting it.

**Expected output:** An argument map, evidence audit, and ethical revision checklist for one chapter.

**Tip:** Ask for diagnosis before suggested wording so you remain the author of revisions.

## Best tools
- **Claude**: Tracks argument structure and consistency across long academic chapters.
- **NotebookLM**: Grounds analytical notes in uploaded chapter and reference materials.

## Prompt

```text
Act as a thesis reading companion for [CHAPTER_TITLE], helping me diagnose the draft while preserving my authorship.

Degree and discipline: [PROGRAMME]. Research question: [QUESTION]. Chapter purpose: [PURPOSE]. Institutional guidance: [GUIDANCE]. Read the uploaded chapter and refer to paragraph, heading, or page locations. Do not write replacement passages unless I later request limited examples, and never generate fabricated data or references.

Produce four analytical layers:
1. Argument spine: one line per major claim, showing how each supports the chapter purpose.
2. Evidence anchors: data or citations attached to each claim, including unsupported transitions.
3. Reader journey: points where definitions arrive late, logic jumps, or signposting fails.
4. Boundary check: material that belongs in another chapter or exceeds the research question.

Then act as two reviewers. Reviewer One is a supportive supervisor seeking coherence; Reviewer Two is a rigorous examiner testing contribution, method alignment, and overclaiming. Give each reviewer five comments grounded in locations.

Ask me to choose the three comments I accept. Only then create a revision sequence ordered by dependency and effort, expressed as tasks rather than ghostwritten prose. End with an academic-integrity check covering citation verification, source reading, disclosure rules, and my responsibility for every final claim.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
