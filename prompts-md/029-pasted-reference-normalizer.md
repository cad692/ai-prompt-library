# 029 — Pasted Reference Normalizer

**Category:** documents · **Difficulty:** Beginner

**Usage:** Use this to clean a pasted reference list without inventing missing details.

**Expected output:** A formatted reference list plus duplicate, missing-field, and verification reports.

**Tip:** Verify metadata against the source or DOI record before submitting the final list.

## Best tools
- **ChatGPT**: Parses messy reference text and applies common citation-style patterns.
- **Claude**: Maintains consistency across large, irregular reference lists.

## Prompt

```text
Normalize my pasted references into [CITATION_STYLE_AND_EDITION] without fabricating any bibliographic information.

References: [PASTE_REFERENCES]
Required ordering: [ALPHABETICAL_NUMERICAL_OR_CUSTOM]
Source language rules: [LANGUAGE_RULES]

First parse each entry into available fields: author, year, title, container, volume, issue, pages, publisher, DOI, URL, and access date. Preserve original text in a numbered source column so every output can be traced back.

Format entries only from supplied fields. Insert visible markers such as [MISSING YEAR], [VERIFY AUTHOR ORDER], or [INCOMPLETE URL] where necessary. Do not search for or infer missing metadata unless I explicitly request a separate verification phase.

Detect likely duplicates, including DOI matches and small title variations. Present them for confirmation rather than deleting them. Separate records by source type—journal article, book, chapter, webpage, report, thesis, or unknown—and flag any type whose formatting is uncertain.

Return three blocks: Clean Reference List, Verification Queue, and Duplicate Candidates. Then run a consistency pass for capitalization, italics indicators, punctuation, date form, and DOI format. Count input entries and output entries; explain any mismatch. End with a reminder that citation software and original source records should be checked before academic submission.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
