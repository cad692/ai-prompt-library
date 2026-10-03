# 085 — Browser Sidebar Research Capture Card

**Category:** addins · **Difficulty:** Intermediate

**Usage:** Capture a web source into reusable evidence notes without confusing claims with conclusions.

**Expected output:** A source card with claims, quotes, limitations, and follow-up questions.

**Tip:** Open the original source and verify quotations instead of trusting the sidebar summary.

## Best tools
- **Browser AI sidebar**: Can summarise the open page while keeping its URL and visible context nearby.

## Prompt

```text
Role: You are an evidence-capture librarian working from the currently open webpage; create a source card, not a generic summary.

Record the page title, publisher, author if visible, publication or update date, URL [PAGE_URL], and access date [ACCESS_DATE]. Identify the source type—report, news article, company page, opinion, dataset, or other—and note who appears responsible for the content.

Extract three to seven claims relevant to [RESEARCH_QUESTION]. For every claim, include a short supporting quotation or precise page location, plus a label: direct evidence, author interpretation, or promotional assertion. Preserve numbers with their units, geography, sample, and time period. If these details are absent, write “not stated.”

Add:
- a two-sentence relevance note;
- likely limitations or conflicts of interest;
- terms worth searching independently;
- one claim that needs corroboration;
- a suggested filename using [PROJECT_NAME].

Do not infer facts hidden behind links or paywalls. Never fabricate a quotation. End with a reliability note based on transparent criteria, not a definitive truth score.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
