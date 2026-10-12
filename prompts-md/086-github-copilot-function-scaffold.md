# 086 — GitHub Copilot Function Scaffold

**Category:** addins · **Difficulty:** Intermediate

**Usage:** Generate a function stub with explicit contracts, edge cases, and test placeholders.

**Expected output:** A typed function skeleton, documentation, validation, and test cases.

**Tip:** Keep the TODOs until each assumption has a matching test or documented decision.

## Best tools
- **GitHub Copilot**: Uses nearby code, types, and conventions to propose an in-editor scaffold.

## Prompt

```text
You are my GitHub Copilot Function Scaffold coach. Write a Copilot-friendly function scaffold with clear intent comments and tests. No unsafe secrets.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Function goal: [FUNCTION_GOAL]
Language: [LANGUAGE]
Inputs: [INPUTS]
Outputs: [OUTPUTS]
Constraints: [CONSTRAINTS]
Edge cases: [EDGE_CASES]
Code style notes: [STYLE]
Test ideas: [TEST_IDEAS]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Spec
Specify behaviour from [FUNCTION_GOAL], [INPUTS], [OUTPUTS], and [CONSTRAINTS].

STEP 2 — Scaffold
Produce a [LANGUAGE] scaffold with intent comments Copilot can follow, matching [STYLE].

STEP 3 — Edges
Encode [EDGE_CASES] and [TEST_IDEAS].

STEP 4 — Safety
Ban secrets/credentials and note validation needs.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Behaviour spec
B. Function scaffold
C. Intent comments
D. Edge cases
E. Starter tests
F. Copilot prompt tips
G. Safety notes
H. Done criteria

Rules: clear contracts; no secrets; tests first mindset.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
