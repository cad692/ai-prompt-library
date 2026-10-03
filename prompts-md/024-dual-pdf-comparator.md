# 024 — Dual PDF Comparator

**Category:** documents · **Difficulty:** Advanced

**Usage:** Use this to compare two documents on matching criteria with traceable evidence.

**Expected output:** A criterion-by-criterion comparison with page evidence, conflicts, and gaps.

**Tip:** Define comparison criteria before reading conclusions to reduce confirmation bias.

## Best tools
- **NotebookLM**: Compares uploaded sources while grounding statements in their respective documents.
- **Claude**: Handles long-document comparison and follows detailed comparison criteria.

## Prompt

```text
Compare [PDF_A] and [PDF_B] as two separate evidence sources, never blending their claims.

My comparison purpose is [PURPOSE]. Use these criteria: [CRITERIA]. If no criteria are supplied, propose a set and ask for approval before proceeding. Identify each document’s title, author, date, version, intended audience, and scope. Flag if editions or time periods make direct comparison unfair.

Create a comparison matrix. For every criterion provide Document A’s position with page reference, Document B’s position with page reference, the relationship—agreement, partial overlap, conflict, or silence—and a concise interpretation. Use [NOT STATED] when a document does not address something.

Add separate sections for:
- terminology that looks similar but is defined differently;
- evidence quality and methodology;
- changes in numbers, requirements, or recommendations;
- unique contributions from each document;
- unresolved contradictions.

Run a role-play critique: first argue which document better serves [PURPOSE], then act as a sceptical reviewer and challenge that conclusion using the strongest counterevidence. Revise the conclusion if the critique succeeds.

Finish with a bounded recommendation and confidence level. Do not infer author intent or claim that newer automatically means better. Provide a five-item reading list of pages requiring human review before any consequential decision.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
