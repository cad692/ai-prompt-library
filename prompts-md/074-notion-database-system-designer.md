# 074 — Notion Database System Designer

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to design a practical Notion database before building views and automations.

**Expected output:** A build-ready Notion schema with views, templates, and governance.

**Tip:** Start with one source-of-truth database and add relations only for repeated entities.

## Best tools
- **Notion**: Supports linked databases, templates, filtered views, and team workflows.
- **ChatGPT**: Translates workflow requirements into a clear database specification.

## Prompt

```text
Take the role of a Notion systems designer building the smallest database structure that supports the real workflow.

What is being tracked: [ITEMS]
Users and roles: [USERS]
Workflow stages: [STAGES]
Questions users need answered: [QUESTIONS]
Existing databases: [EXISTING]
Reporting or automation needs: [NEEDS]

Start by identifying the primary record and its unique naming rule. Decide whether the solution needs one database or related databases; justify every relation. Specify each property with name, type, purpose, required/optional status, allowed values, example, and owner. Avoid redundant properties that can be derived or rolled up.

Design views around user decisions: personal queue, team board, calendar, review list, and archive only where relevant. For each view, provide filter, sort, grouping, visible properties, and intended user. Create two database templates with default fields, prompts, and checklists. Add formulas only as plain-language logic unless [FORMULA_SYNTAX] is requested.

Define lifecycle rules for creation, status changes, stale records, permissions, archive, and deletion. Include one migration plan for current data and a five-record pilot test. Finish with a build order and identify nice-to-have features to postpone. Do not suggest automations that Notion cannot perform without a confirmed integration.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
