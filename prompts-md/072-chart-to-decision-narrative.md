# 072 — Chart to Decision Narrative

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to explain a chart in plain language without overstating it.

**Expected output:** A chart narrative with takeaway, caveats, and decision implications.

**Tip:** Read the narrative beside the chart and verify every directional claim.

## Best tools
- **ChatGPT**: Synthesizes supplied chart details into an audience-aware narrative.
- **Excel/Sheets**: Allows direct verification of values, labels, and chart construction.

## Prompt

```text
You are a data interpreter writing the honest story of a chart for a non-specialist decision-maker.

Chart or data: [CHART_DATA]
Metric definition: [METRIC]
Audience and decision: [AUDIENCE_DECISION]
Comparison period: [PERIOD]
Source and caveats: [SOURCE_CAVEATS]

Inspect the evidence in four passes. First describe only what is visible: level, direction, variation, and notable comparisons. Second identify the strongest decision-relevant pattern with exact values and units. Third test that pattern against base effects, seasonality, denominators, target changes, missing periods, small samples, and category redefinitions. Fourth consider at least one plausible alternative explanation.

Write three narrative layers: a 12-word chart headline, a 60-word executive explanation, and a 150-word analytical note. Each must distinguish observation from interpretation and implication. If the data does not support a firm conclusion, use appropriately cautious language rather than manufacturing certainty.

Add two annotations that should appear on the chart, one question the audience is likely to ask, and the precise additional data needed to answer it. Conclude with a decision statement formatted as “This evidence supports [ACTION] within [BOUNDARY], while we monitor [UNCERTAINTY].” Do not infer causation from timing alone.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
