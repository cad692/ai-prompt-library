# 050 — Data Slide Storyline

**Category:** presentations · **Difficulty:** Beginner

**Usage:** Use to turn a chart or dataset into an honest decision narrative.

**Expected output:** A chart recommendation, message headline, annotations, and spoken interpretation.

**Tip:** State the denominator and time period wherever a percentage appears.

## Best tools
- **Excel/Sheets**: Supports transparent chart creation and source-data checking.
- **PowerPoint+Copilot**: Helps present chart takeaways within a decision deck.

## Prompt

```text
Take the role of a data-story editor who refuses to make the chart claim more than the evidence supports.

Data or chart description: [DATA]
Decision audience: [AUDIENCE]
Decision at stake: [DECISION]
Time period and units: [TIME_AND_UNITS]
Known caveats: [CAVEATS]

Begin by naming the single comparison that matters most for the decision. Recommend the chart form that makes that comparison easiest, and explain why two plausible alternatives would be weaker. Specify axes, sorting, baseline, labels, and any reference line. Never suggest a truncated axis without clearly disclosing its effect.

Write a message headline containing the supported takeaway, followed by a subtitle that states scope. Identify up to three chart annotations tied to exact values or periods. Then provide a spoken narrative in this order: context, pattern, exception, limitation, and decision implication. Distinguish correlation from causation and flag small samples, missing denominators, changing definitions, or cherry-picked dates.

Add a “reasonable alternative reading” of the same data and say what additional evidence would resolve the ambiguity. Close with a slide footnote template for source, refresh date, metric definition, and caveat. If raw data is incomplete, request what is missing rather than estimating it.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
