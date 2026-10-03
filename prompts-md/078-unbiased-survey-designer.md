# 078 — Unbiased Survey Designer

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to design a short survey that measures one clear research objective.

**Expected output:** A field-ready survey instrument with rationale and pilot checks.

**Tip:** Pilot with five people and ask what they thought each question meant.

## Best tools
- **Google Forms**: Builds accessible surveys with common question types and branching.
- **Microsoft Forms**: Supports straightforward organizational survey collection and export.

## Prompt

```text
Act as a survey methodologist designing the shortest instrument that can answer [RESEARCH_OBJECTIVE].

Target population: [POPULATION]
Sampling and distribution plan: [SAMPLING]
Decisions based on results: [DECISIONS]
Required topics: [TOPICS]
Languages and accessibility needs: [LANGUAGES_ACCESS]
Maximum completion time: [TIME]
Sensitive questions: [SENSITIVE]

Begin with a construct map: what must be measured, what is merely interesting, and what should be excluded. Then draft the survey in respondent order: brief consent and purpose, screening if necessary, easy behavioral questions, core measures, optional open text, demographics only when analytically justified, and close.

Use one idea per question. Avoid leading, loaded, double-barrelled, absolute, and hypothetical wording. For every closed question, provide balanced response options, an appropriate recall period, and “not applicable/prefer not to answer” where needed. Do not use agreement scales when a direct frequency or quality measure is clearer.

Annotate each question privately with purpose, variable type, and planned analysis. Add branch logic and randomization only when justified. Estimate completion time, then design a five-person cognitive pilot with probes for comprehension and response fit. End with privacy, translation/back-translation, mobile display, missing-data, and reporting checks. Do not promise anonymity if collection settings cannot guarantee it.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
