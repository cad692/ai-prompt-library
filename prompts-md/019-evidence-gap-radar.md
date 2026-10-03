# 019 — Evidence Gap Radar

**Category:** research · **Difficulty:** Advanced

**Usage:** Use this to identify defensible research gaps without claiming that nothing exists.

**Expected output:** A ranked gap map with evidence, search checks, and viable study directions.

**Tip:** Describe a bounded gap in a searched corpus, never an absolute absence across all research.

## Best tools
- **NotebookLM**: Compares patterns and omissions across a supplied body of literature.
- **Perplexity**: Helps test whether an apparent gap persists in recent discoverable research.

## Prompt

```text
Act as an evidence-gap analyst for the literature collection [CORPUS_OR_SOURCE_LIST] on [TOPIC].

My scope is [YEARS], [GEOGRAPHY], [POPULATION], and [DISCIPLINE]. Begin by defining what would count as a gap: missing context, neglected population, methodological weakness, inconsistent result, untested mechanism, outdated evidence, or implementation problem. Do not equate “few papers I saw” with “no research exists.”

Build a coverage grid crossing major themes with populations, locations, methods, and time periods. Populate it only from traceable sources and include citations or source IDs. Mark cells as well covered, partly covered, apparently sparse, or not assessed.

For each apparent gap, perform an adversarial check: propose two search strings, likely databases, alternate terminology, and neighbouring disciplines where overlooked work may exist. If browsing is available, report what that check found; otherwise label it pending.

Rank the surviving gaps by significance, originality within scope, feasibility, ethical access, and value for Pakistan or [TARGET_CONTEXT]. For the top three, draft a cautious gap statement, a possible research question, suitable evidence, and a reason the study matters. End with wording to avoid—such as “no one has studied”—and a defensible replacement tied to the reviewed corpus.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
