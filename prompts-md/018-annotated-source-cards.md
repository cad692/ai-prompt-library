# 018 — Annotated Source Cards

**Category:** research · **Difficulty:** Intermediate

**Usage:** Use this to create evaluative annotations from sources you have actually read.

**Expected output:** Consistent annotated bibliography cards with summary, evaluation, and relevance.

**Tip:** Add page numbers while reading; locating evidence later is harder than recording it now.

## Best tools
- **NotebookLM**: Creates source-grounded notes from an uploaded collection and links responses to evidence.
- **Claude**: Processes long papers and produces nuanced structured annotations.

## Prompt

```text
Create rigorous annotated source cards for [RESEARCH_TOPIC] using only [UPLOADED_SOURCES_OR_PASTED_TEXT].

Citation style: [APA_MLA_CHICAGO_OR_OTHER]. Target annotation length: [WORDS] words. My research question is [QUESTION], and my intended argument or inquiry is [DIRECTION]. Never fabricate missing bibliographic fields, page numbers, quotations, DOIs, or findings; mark missing data as [VERIFY].

For each source, produce a card containing:
- a formatted citation;
- the source’s purpose and central claim;
- method, sample, or evidence base;
- two major findings with page locations when available;
- one strength and one limitation;
- relevance to my question;
- relationship to another source in the set.

Keep summary and evaluation in separate labelled paragraphs. If the source is commentary rather than research, adapt the method field honestly. Add three keywords not already obvious from the title.

After all cards, group sources into conversation clusters: agreement, tension, extension, and context. Identify duplicated evidence where several sources rely on the same dataset. Finish with a verification queue of incomplete citations and claims I must inspect in the originals. The annotations must support my own reading and writing, not replace them.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
