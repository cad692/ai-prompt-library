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
You are my Notion Database System designer. Design a Notion database system that fits a real workflow. No feature fantasy.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Workflow to support: [WORKFLOW]
Who will use it: [USERS]
Main objects to track: [OBJECTS]
Views needed: [VIEWS_NEEDED]
Must-have fields: [FIELDS_MUST]
Automations desired: [AUTOMATIONS]
Constraints: [CONSTRAINTS]
Success looks like: [SUCCESS]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Model
Propose databases/objects from [OBJECTS] for [WORKFLOW] and [USERS].

STEP 2 — Fields
Define [FIELDS_MUST] and relations.

STEP 3 — Views
Design [VIEWS_NEEDED] and light [AUTOMATIONS] within [CONSTRAINTS].

STEP 4 — Build order
Give an implementation sequence aimed at [SUCCESS].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. System overview
B. Database schemas
C. Relations
D. Views
E. Automations
F. Permissions notes
G. Build order
H. Maintenance rules

Rules: simple enough to maintain; no unused complexity.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
