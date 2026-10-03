# 033 — Grounded Answer Guardrails

**Category:** prompting · **Difficulty:** Advanced

**Usage:** Use this to design prompts that reduce unsupported claims and invented details.

**Expected output:** A hallucination-resistant prompt with evidence rules and adversarial tests.

**Tip:** Require an abstention phrase and source locations, then test the prompt with an unanswerable question.

## Best tools
- **NotebookLM**: Grounds responses in user-provided sources and exposes supporting source locations.
- **Claude**: Follows detailed evidence constraints across long source material.

## Prompt

```text
Design a grounded-answer prompt for [TASK] where unsupported claims would create [RISK].

Allowed evidence is [APPROVED_SOURCES]. The user’s question will appear as [QUESTION]. Build instructions that force a clean boundary between supplied evidence, general background knowledge if allowed, and inference. Use the exact abstention phrase “[NOT SUPPORTED BY PROVIDED SOURCES]” whenever the evidence is insufficient.

The resulting prompt must require:
- a source location beside each material claim;
- quotations only when exact wording is available;
- uncertainty labels for ambiguous passages;
- no invented citations, links, statistics, names, or dates;
- a conflict note when approved sources disagree;
- a request for missing information when it would change the answer.

Choose an output structure suited to [AUDIENCE] rather than a generic essay. Include a final evidence ledger mapping conclusions to source IDs.

Stress-test the prompt with three probes: one answerable question, one partly answerable question, and one plausible but absent claim. Predict the compliant behaviour for each without answering the domain question. Identify any instruction that could still reward confident guessing and tighten it.

Return the production prompt first, followed by the tests and a short human verification protocol. Do not claim these controls eliminate hallucinations; state their limits and recommend review proportional to the risk.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
