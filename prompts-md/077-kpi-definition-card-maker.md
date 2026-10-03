# 077 — KPI Definition Card Maker

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to define KPIs consistently before building a dashboard.

**Expected output:** Standard KPI cards and a metric governance checklist.

**Tip:** Calculate one example by hand with the metric owner before publishing.

## Best tools
- **Excel/Sheets**: Documents metric formulas and validates sample calculations transparently.
- **Notion**: Maintains a shared KPI dictionary with owners and revision history.

## Prompt

```text
You are a measurement lead defining KPIs so two analysts calculate the same answer from the same data.

Business objective: [OBJECTIVE]
Proposed KPI names: [KPIS]
Available systems: [SYSTEMS]
Reporting audience: [AUDIENCE]
Review frequency: [FREQUENCY]
Known disputes: [DISPUTES]

For each KPI, create a definition card containing: decision it informs, plain-language meaning, exact formula, numerator, denominator, unit, inclusion rules, exclusion rules, time window, segment dimensions, source system, refresh timing, data owner, business owner, target source, and known limitations. Clarify whether the metric is leading, lagging, diagnostic, or guardrail.

Include a worked example using clearly labelled sample numbers, then test edge cases such as zero denominator, late-arriving records, cancellations, duplicates, and timezone boundaries. If a term like “active,” “customer,” or “completed” appears, demand an operational definition.

Compare any KPIs that may conflict or encourage harmful gaming. Recommend one balancing metric where needed. Finish with a compact KPI dictionary, a change-control rule for revised definitions, and five dashboard footnotes users may need. Do not choose targets without evidence or present an attractive number as useful if it does not inform action.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
