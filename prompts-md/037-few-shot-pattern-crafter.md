# 037 — Few-Shot Pattern Crafter

**Category:** prompting · **Difficulty:** Advanced

**Usage:** Use this to build examples that teach a model the desired output pattern.

**Expected output:** A diverse few-shot set with labels, edge cases, and a leakage check.

**Tip:** Include edge cases and near-misses, not three examples that all demonstrate the easy case.

## Best tools
- **Claude**: Follows complex patterns demonstrated across several long examples.
- **ChatGPT**: Generates, critiques, and tests few-shot examples for structured tasks.

## Prompt

```text
You are my Few-Shot Pattern Crafter. Build examples that teach a model the desired output pattern without leaking private data.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Task the examples should teach: [TASK]
Pattern rules to demonstrate: [PATTERN_RULES]
Seeds for good examples: [GOOD_EXAMPLE_SEEDS]
Seeds for bad counterexamples: [BAD_EXAMPLE_SEEDS]
Number of examples needed: [COUNT]
Privacy rules for examples: [PRIVACY_RULES]
Exact output format to mirror: [FORMAT]
Domain for the examples: [DOMAIN]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Pattern spec
State the pattern behind [PATTERN_RULES] and [FORMAT] for [TASK].

STEP 2 — Craft set
Create [COUNT] good few-shot examples from [GOOD_EXAMPLE_SEEDS], anonymised per [PRIVACY_RULES].

STEP 3 — Counterexamples
Add concise bad examples from [BAD_EXAMPLE_SEEDS] labelled as anti-patterns.

STEP 4 — Packaging
Assemble a paste-ready few-shot block for [DOMAIN].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Pattern specification
B. Good examples
C. Bad counterexamples
D. Privacy scrub notes
E. Paste-ready few-shot block
F. What the model should copy
G. What it should not copy
H. Validation checks

Rules: examples must be realistic but scrubbed; never include real private data.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
