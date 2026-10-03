# 073 — Assumptions First Analysis

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use before quantitative analysis to expose definitions, assumptions, and decision thresholds.

**Expected output:** An analysis contract with assumptions, tests, and stop conditions.

**Tip:** Ask the decision owner to approve definitions before calculating results.

## Best tools
- **Claude**: Handles complex analytical context and tracks assumptions across a long brief.
- **ChatGPT**: Structures decision questions, sensitivity tests, and evidence gaps.

## Prompt

```text
Act as an analytical reviewer who pauses calculation until the question and assumptions are explicit.

Decision to be made: [DECISION]
Available data: [DATA]
Proposed method: [METHOD]
Stakeholders: [STAKEHOLDERS]
Constraints: [CONSTRAINTS]
Deadline: [DEADLINE]

Produce an “analysis contract.” Define the outcome variable, unit of analysis, population, comparison, time window, success threshold, and decision rule. Then create an assumption ledger grouped into data quality, measurement, sampling, method, external conditions, and stakeholder values. For each assumption, state why it matters, current evidence, confidence, and how failure would bias the result.

Identify the five assumptions with the highest combination of uncertainty and decision impact. Design a sensitivity test or validation check for each. Draw a boundary between questions the data can answer, questions it can only indicate, and questions it cannot address.

Propose the smallest defensible analysis sequence, including baseline, segmentation, robustness checks, and uncertainty reporting. Add stop conditions for data that is too incomplete or definitions that remain unresolved. End with a pre-analysis sign-off containing choices the decision owner must confirm. Do not perform calculations or invent missing values unless explicitly asked after this framing is approved.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
