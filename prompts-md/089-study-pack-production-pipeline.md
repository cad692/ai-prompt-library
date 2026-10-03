# 089 — Study Pack Production Pipeline

**Category:** workflows · **Difficulty:** Intermediate

**Usage:** Design a multi-tool pipeline that turns learning material into an ethical study pack.

**Expected output:** A sequenced workflow with tools, handoffs, quality gates, and file names.

**Tip:** Keep source citations attached to notes throughout every transformation.

## Best tools
- **ChatGPT**: Coordinates staged transformations and produces clear reusable instructions.

## Prompt

```text
Role: You are a learning-workflow designer; map a responsible study-pack pipeline for [SUBJECT] and [LEARNER_LEVEL].

The available inputs are [SOURCE_MATERIALS], the deadline is [DEADLINE], and permitted tools are [AVAILABLE_TOOLS]. Design a sequence that may use document extraction, an AI assistant, flashcard software, and a word processor, but assign each tool only work it performs well. Describe what moves between tools and in which format.

Include stages for source inventory, concept mapping, plain-language notes, worked examples, retrieval questions, flashcards, a timed revision plan, and final fact-checking against original material. Insert a human approval gate before generated content becomes a study aid. Do not create answer keys for live tests or suggest bypassing academic rules.

For every stage specify: input, action, tool choice, output filename, and quality check. Show how to preserve page numbers or links so claims remain traceable. Offer a low-tech alternative where a proposed integration is unavailable.

Finish with a folder structure and a 30-minute maintenance routine. Optimise for understanding and recall, not volume of generated notes.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
