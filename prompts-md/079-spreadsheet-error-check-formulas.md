# 079 — Spreadsheet Error Check Formulas

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to design formula-based checks that flag likely spreadsheet errors.

**Expected output:** A formula check library with test cases and review guidance.

**Tip:** Keep every flag column visible during testing and investigate false positives.

## Best tools
- **Excel/Sheets**: Supports transparent formulas, validation rules, and conditional formatting.
- **ChatGPT**: Drafts formula patterns from a supplied schema and business rules.

## Prompt

```text
Work as a spreadsheet quality reviewer proposing checks that flag anomalies without silently changing data.

Tool and version: [EXCEL_OR_SHEETS]
Column letters/names: [SCHEMA]
Sample rows: [SAMPLES]
Business rules: [RULES]
Known errors: [KNOWN_ERRORS]
Locale separators: [LOCALE]

Design a set of helper-column checks for required blanks, duplicate keys, invalid categories, text where numbers are expected, impossible date order, out-of-range values, inconsistent units, cross-column mismatch, formula errors, and broken totals. Include only checks relevant to the supplied schema.

For each check, give a plain-language rule, formula using the exact supplied columns, expected TRUE/FALSE or message output, one passing example, one failing example, and what a reviewer should do. Prefer readable formulas and explain compatibility differences between Excel and Google Sheets. Where a formula depends on modern functions, offer a simpler fallback.

Add a summary section that counts each error type and highlights rows through conditional formatting without hiding source values. Distinguish hard errors from warnings. Recommend testing formulas on a copy, locking reference ranges where needed, and manually verifying a sample. If schema details are missing, provide formula pseudocode with [COLUMN] placeholders instead of guessing.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
