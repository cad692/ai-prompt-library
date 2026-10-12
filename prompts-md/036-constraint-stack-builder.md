# 036 — Constraint Stack Builder

**Category:** prompting · **Difficulty:** Intermediate

**Usage:** Use this to organise multiple prompt constraints without creating contradictions.

**Expected output:** A prioritized constraint stack, conflict analysis, and executable prompt.

**Tip:** Rank hard constraints above preferences so the model knows what may flex.

## Best tools
- **ChatGPT**: Organises detailed constraints and detects conflicts through interactive refinement.
- **Gemini**: Handles structured instruction design and offers alternative constraint resolutions.

## Prompt

```text
You are my Constraint Stack Builder. Organise many prompt constraints without creating contradictions.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Task the constraints apply to: [TASK]
Raw constraints to organise: [CONSTRAINT_LIST]
Priority order if conflicts arise: [PRIORITIES]
Non-negotiable constraints: [NON_NEGOTIABLES]
Flexible preferences: [FLEXIBLE_ITEMS]
Required output form: [OUTPUT_FORM]
Conflicts already noticed: [CONFLICT_EXAMPLES]
Target AI tool: [TOOL]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Cluster
Group [CONSTRAINT_LIST] into safety, format, style, scope, and domain stacks.

STEP 2 — Resolve
Detect contradictions using [PRIORITIES], [NON_NEGOTIABLES], and [FLEXIBLE_ITEMS]; resolve or flag.

STEP 3 — Stack prompt
Write a clean constraint block for [TASK] and [OUTPUT_FORM] usable in [TOOL].

STEP 4 — Stress test
Show how the stack handles [CONFLICT_EXAMPLES].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Constraint clusters
B. Conflicts found
C. Resolutions
D. Final constraint stack
E. Ready prompt snippet
F. Override order
G. Test cases
H. Open conflicts still needing me

Rules: non-negotiables win; no hidden contradictions; keep language enforceable.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
