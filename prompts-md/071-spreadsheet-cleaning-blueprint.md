# 071 — Spreadsheet Cleaning Blueprint

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to plan safe cleaning before changing a messy spreadsheet.

**Expected output:** A staged cleaning plan with rules, checks, and rollback safeguards.

**Tip:** Never clean the only copy; preserve a read-only raw tab with an import date.

## Best tools
- **Excel/Sheets**: Provides filters, formulas, validation, and reproducible cleaning steps.
- **ChatGPT**: Helps diagnose column issues and draft transformation logic.

## Prompt

```text
Work as a cautious data steward planning a spreadsheet cleanup that can be audited and reversed.

File purpose: [PURPOSE]
Columns and sample rows: [SCHEMA_SAMPLE]
Known problems: [PROBLEMS]
Intended analysis: [ANALYSIS]
Tool: [EXCEL_OR_SHEETS]
Locale, date, and number conventions: [LOCALE]

Do not clean values immediately. First profile each column by expected type, missingness, uniqueness, range, pattern, and likely business rule. Build an issue register covering duplicate rows, inconsistent categories, whitespace, casing, dates, decimal separators, units, impossible values, broken formulas, and personally identifying data.

Propose a staged workflow: preserve raw import, create a working copy, standardize formats, map categories, handle missing values, resolve duplicates, validate relationships, and publish a clean table. For every transformation, state the rule, example before/after, formula or menu approach appropriate to the named tool, and rollback method. Never recommend deleting an outlier solely because it looks unusual.

Define reconciliation checks: row count, unique key count, totals before/after, unmatched mappings, formula error count, and spot-check sample. Mark decisions that require a domain owner. Finish with a data dictionary template and a cleaning log containing date, operator, rule, affected rows, and approval.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
