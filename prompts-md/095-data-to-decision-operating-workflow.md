# 095 — Data-to-Decision Operating Workflow

**Category:** workflows · **Difficulty:** Advanced

**Usage:** Turn operational data into a documented recommendation with validation and accountability.

**Expected output:** A controlled analytical workflow ending in a decision record.

**Tip:** Reconcile totals to the source system before discussing trends.

## Best tools
- **Microsoft Copilot**: Works across spreadsheet analysis, written summaries, and presentation preparation.

## Prompt

```text
Role: Act as an analytics process designer; map how [DATASET] should inform [DECISION] without overstating certainty.

Identify the source system, data owner, refresh date, unit of analysis, and decision deadline. Lay out a sequence using [DATA_TOOL] for cleaning, [ANALYSIS_TOOL] for calculation, [WRITING_TOOL] for the decision memo, and [PRESENTATION_TOOL] only if stakeholders need it. Every handoff must retain dataset version and filter definitions.

Insert controls for duplicates, missing values, outliers, unit mismatches, denominator changes, and reconciliation to known totals. Distinguish descriptive findings, forecasts, and causal claims. Require sensitivity checks for [KEY_ASSUMPTIONS] and segment results where averages could hide material differences.

The workflow should produce an analysis notebook or formula record, a chart pack, a finding log, and a recommendation with options. Assign a challenger to test alternative explanations before approval.

Finish with a decision register capturing owner, date, evidence used, assumptions, chosen option, rejected alternatives, review trigger, and later outcome. Include a route to say “insufficient evidence” rather than manufacturing confidence.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
