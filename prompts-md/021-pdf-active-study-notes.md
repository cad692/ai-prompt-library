# 021 — PDF Active Study Notes

**Category:** documents · **Difficulty:** Beginner

**Usage:** Use this to transform an uploaded reading into notes that support active recall.

**Expected output:** Page-linked study notes, recall questions, misconceptions, and a review plan.

**Tip:** Try the recall questions before reopening the PDF or reading the answer key.

## Best tools
- **NotebookLM**: Answers from uploaded sources with grounding and source-location support.
- **Claude**: Handles long PDFs and produces well-structured learning materials.

## Prompt

```text
Turn the uploaded [PDF_TITLE] into active study notes for [COURSE_OR_EXAM], grounded only in the document.

My current level is [LEVEL], the assessed topics are [TOPICS], and I have [STUDY_TIME]. Read the document’s headings, figures, tables, and conclusion. If pages are missing, scanned illegibly, or inaccessible, identify them rather than guessing.

Build the notes in learning order, which may differ from page order. For each concept include: a plain-language explanation, essential terminology, one concrete example from the PDF, and page references. Mark definitions exactly quoted from the document with quotation marks; paraphrase everything else.

Then create an Active Recall Pack:
- eight short-answer questions;
- three application questions;
- two “spot the misconception” items;
- a compact answer key with page pointers.

Add a visual text map connecting the chapter’s main ideas with arrows and relationship labels. Identify any formula, framework, or process that requires memorisation, and devise one mnemonic without distorting the meaning.

Close with a [NUMBER_OF_DAYS]-day review schedule using spaced practice. Include a “return to the PDF” list for claims, diagrams, or examples that need closer reading. Do not write assignment answers or conceal AI assistance; these notes must help me learn the source.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
