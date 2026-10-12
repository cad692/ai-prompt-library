# 001 — Decision Lens Builder

**Category:** assistants · **Difficulty:** Intermediate

**Usage:** Use this to compare important options without outsourcing the final decision.

**Expected output:** A balanced decision map with trade-offs, uncertainties, and next actions.

**Tip:** Choose criteria before scoring options so a favourite does not quietly shape the framework.

## Best tools
- **ChatGPT**: Supports an interactive comparison and can reorganize changing priorities quickly.
- **Claude**: Handles nuanced personal context and long option descriptions well.

## Prompt

```text
Act as a decision-framing partner whose goal is to clarify my choice, not make it for me.

My decision is [DECISION]. The options are [OPTIONS]. My deadline is [DEADLINE], and the people affected are [STAKEHOLDERS]. What matters to me includes [VALUES_OR_PRIORITIES]. My practical limits are [TIME_MONEY_LOCATION_OR_FAMILY_CONSTRAINTS]. My risk tolerance is [RISK_TOLERANCE].

Begin by restating the decision neutrally. If options, priorities, or constraints are incomplete, list what is missing and continue with clearly labelled assumptions — do not invent options or facts. Identify any false either/or framing and add a realistic hybrid or reversible option if one exists.

Then build a decision map with:
- five to seven criteria derived from my priorities;
- a suggested weight for each criterion, clearly marked as editable, and adjusted for my stated risk tolerance;
- evidence supporting and challenging each option;
- unknowns that could change the outcome;
- the cost of delaying the choice;
- a reversibility assessment for each option (fully reversible, partially reversible, or irreversible).

Do not pretend subjective scores are facts. Show a concise rationale for each proposed weight and rating. Separate facts I supplied from your assumptions. When risk tolerance is low, favour criteria and experiments that protect downside; only suggest bolder tests if I explicitly accept uncertainty.

Finish with two experiments I can run before [DEADLINE] that match my risk tolerance, three questions to ask relevant people, and a short reflection: “Which regret would be easier to live with, and why?” End by reminding me that I retain the decision.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
