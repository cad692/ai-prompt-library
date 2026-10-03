# 111 — Chain Step 3 - Evidence Synthesis

**Category:** chains · **Difficulty:** Advanced

**Usage:** Turn verified evidence notes into findings, tensions, and calibrated implications.

**Expected output:** Thematic findings with confidence, caveats, and traceable evidence IDs.

**Tip:** A synthesis should explain relationships, not merely shorten every source.

## Best tools
- **Claude**: Can compare a long evidence ledger and preserve nuanced disagreements.

## Prompt

```text
Role: You are the synthesis editor at step three; transform [PREVIOUS_OUTPUT] from evidence notes into defensible findings.

First check whether claims have source identifiers, dates, quotations or locations, and limitations. If not, flag the deficiency and avoid upgrading uncertain material. Group evidence by meaningful themes or causal relationships rather than by source. Within each theme, show convergence, contradiction, contextual differences, and missing voices.

Produce four to seven findings. For each, write the finding in one sentence, list supporting evidence IDs, note counterevidence, assign a confidence level with a short justification, and explain why it matters to [AUDIENCE]. Keep observed facts separate from interpretation and recommendation. Do not turn correlation into causation or majority repetition into quality.

Add a section for surprises, unresolved tensions, and claims excluded from use. Then formulate a coherent synthesis narrative of no more than [WORD_LIMIT], preserving important numbers and conditions.

Conclude with “HANDOFF TO STEP 4”: ranked findings, evidence references, audience implications, and non-negotiable caveats. It must be understandable independently when inserted as [PREVIOUS_OUTPUT].
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
