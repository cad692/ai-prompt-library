# 082 — Excel Analysis Question Designer

**Category:** addins · **Difficulty:** Intermediate

**Usage:** Ask Copilot in Excel for a focused, auditable analysis of a selected table.

**Expected output:** An analysis plan, formulas or pivots, findings, and validation checks.

**Tip:** Convert the range to a named table and define each column before asking.

## Best tools
- **Microsoft Copilot**: Can analyze structured workbook tables and suggest formulas or summaries in context.

## Prompt

```text
Goal: Act as an Excel analysis partner and answer [BUSINESS_QUESTION] using only the table named [TABLE_NAME].

Begin by mapping the relevant columns: [COLUMN_DESCRIPTIONS]. State which field represents time, category, value, and any unique identifier. Inspect for blanks, duplicated records, inconsistent labels, impossible values, and mixed units before interpreting patterns. If the question cannot be answered from these columns, say exactly what is missing.

Propose the smallest useful analysis: formulas, a PivotTable, or a chart—not all three unless each adds a distinct insight. Show formulas with structured references and explain where they should be placed. Separate observed results from possible explanations; correlation is not proof of cause.

Present the response as:
1. data-quality findings;
2. recommended analysis steps;
3. key results in plain language;
4. one suitable visual with axis definitions;
5. two manual cross-checks using totals or sample rows.

Use [DATE_RANGE] and [SEGMENTS] as filters. Never overwrite source data, and label any estimated or excluded values.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
