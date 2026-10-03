# 062 — Proposal Scope Boundary Builder

**Category:** work-business · **Difficulty:** Beginner

**Usage:** Use to define project deliverables, exclusions, acceptance, and change handling.

**Expected output:** A proposal scope with deliverables, boundaries, assumptions, and acceptance criteria.

**Tip:** Write acceptance criteria so both sides can observe whether the work is complete.

## Best tools
- **Claude**: Structures detailed scope language across long project notes.
- **Notion**: Keeps scope, deliverables, and decisions in a collaborative workspace.

## Prompt

```text
Act as a project scoping facilitator converting messy discovery notes into a shared definition of done.

Client goal: [GOAL]
Discovery notes: [NOTES]
Deliverables discussed: [DELIVERABLES]
Timeline constraints: [TIMELINE]
Client responsibilities: [CLIENT_INPUTS]
Budget model if relevant: [BUDGET_MODEL]

Write a proposal scope draft with these functional sections: outcome, deliverable cards, project phases, client inputs, explicit exclusions, assumptions, acceptance method, change-request path, and handover. Each deliverable card must state what will be produced, format, quantity or boundary, review rounds, dependencies, and observable acceptance criteria.

Create a “scope edge” section using examples of nearby work that is not included, so ambiguity is reduced without sounding defensive. Identify contradictions or unanswered questions in the notes and list them before the draft as decisions required. Do not invent dates, fees, legal protections, intellectual-property terms, or service guarantees.

Add a lightweight change process: request, impact assessment, written approval, and revised schedule or cost. Finish with a plain-language summary the client can read in one minute and a kickoff checklist. Label the document as a commercial working draft requiring appropriate business or legal review where needed.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
