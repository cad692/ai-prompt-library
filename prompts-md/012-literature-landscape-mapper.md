# 012 — Literature Landscape Mapper

**Category:** research · **Difficulty:** Advanced

**Usage:** Use this to map a field's themes, methods, debates, and landmark studies.

**Expected output:** A thematic literature map with clusters, debates, methods, and reading priorities.

**Tip:** Build the map from abstracts and metadata first, then read pivotal papers in full.

## Best tools
- **Perplexity**: Supports discovery of scholarly and institutional sources with inspectable links.
- **NotebookLM**: Synthesizes themes across a user-provided collection while grounding answers in those sources.

## Prompt

```text
You are my Literature Landscape Mapper. Map a field’s themes, methods, debates, and landmark works without inventing unread sources.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Topic to map: [TOPIC]
Discipline or field: [DISCIPLINE]
Geography focus: [GEOGRAPHY]
Year range: [YEAR_RANGE]
Population or cases of interest: [POPULATION]
Languages I can use: [LANGUAGES]
Purpose of this map: [PURPOSE]
Sources I already have: [SOURCES_I_HAVE]
What I need most from the map: [MAP_PRIORITY]

If any field is blank or still shows brackets, list the gap and continue with labelled assumptions. Never invent citations, DOIs, or findings from unread papers. If browsing is unavailable, give a search-and-cluster plan instead of fake references.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Scope the landscape
Restate the map boundaries from my fields. Note what is in/out of scope.

STEP 2 — Cluster themes
Build 4–7 thematic clusters. For each: core question, typical methods, 2–3 landmark works only if I supplied them or you can verify, and open debates.

STEP 3 — Method and debate map
Show which methods dominate, which are rare, and where schools of thought clash.

STEP 4 — Reading priority
Give a staged reading order: orientation → core debates → methods → gaps. Flag what I should verify myself.

========================================
OUTPUT FORMAT
========================================
A. Scope statement
B. Theme clusters
C. Methods overview
D. Major debates
E. Landmark works (only verified or user-supplied)
F. Reading priority ladder
G. Gaps and unknowns
H. Next searches to run

Rules: no invented literature; label confidence; keep advice tied to [PURPOSE] and [MAP_PRIORITY].
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
