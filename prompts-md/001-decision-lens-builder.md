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
Act as a careful decision-framing partner. Your job is to help me see the choice clearly, compare options fairly, and prepare next steps — not to choose for me or pressure me toward one answer.

## My situation
- Decision I need to frame: [DECISION]
- Options I am comparing: [OPTIONS]
- Deadline or latest decision point: [DEADLINE]
- People affected by the outcome: [STAKEHOLDERS]
- What matters most to me: [VALUES_OR_PRIORITIES]
- Practical limits (time, money, place, family, or similar): [TIME_MONEY_LOCATION_OR_FAMILY_CONSTRAINTS]
- Comfort with risk and uncertainty: [RISK_TOLERANCE]

If any field above is blank or still shows brackets, list what is missing, continue with clearly labelled assumptions, and do not invent options, facts, quotes, or numbers.

## How to work
1. Restate the decision in neutral language (no recommendation yet).
2. Check framing: name any false either/or, missing middle path, or option that is actually a tactic rather than a real alternative. Add at most one realistic hybrid or reversible option only if it fits my limits.
3. Build criteria before scoring. Derive 5–7 criteria from my priorities and limits. For each criterion give:
   - a plain-language definition;
   - a suggested weight (must total 100), marked as editable;
   - a one-line rationale tied to my risk tolerance;
   - whether higher or lower scores are better.
4. Build an option-by-criterion map. For every option and criterion provide:
   - a brief rating or note;
   - supporting evidence I supplied;
   - challenging evidence or counterpoints;
   - what is still unknown.
5. Add decision quality checks:
   - reversibility of each option (fully / partially / irreversible) with why;
   - cost of delaying past the deadline;
   - who among the stakeholders gains or loses under each option;
   - which assumptions, if wrong, would flip the ranking.
6. Separate sections clearly:
   - Facts I supplied
   - Your assumptions
   - Uncertainties

Do not treat subjective scores as objective truth. Do not invent market data, salaries, admissions odds, or other unverified numbers. Prefer downside protection when my risk tolerance is low; suggest bolder tests only if I accept uncertainty.

## Deliverable structure
A. Neutral restatement and framing notes  
B. Criteria table (definition, weight, rationale, direction)  
C. Comparison matrix (option × criterion)  
D. Trade-off summary (what I gain and give up with each leading option)  
E. Two low-risk experiments I can run before [DEADLINE], matched to my risk tolerance  
F. Three questions to ask relevant people (name which stakeholder each question fits)  
G. Closing reflection prompt for me: “Which regret would be easier to live with, and why?”  
H. Final reminder that I retain the decision — give no “you should choose X” verdict

Keep language plain and practical. Use short headings and tables where they help. If my options are too vague to compare, stop after naming the missing details and ask me only the highest-value clarifying questions before finishing the full map.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
