# 016 — Headline Study Crosscheck

**Category:** research · **Difficulty:** Intermediate

**Usage:** Use this to compare news coverage with the study or data it describes.

**Expected output:** A side-by-side verdict on headline accuracy, study quality, and applicability.

**Tip:** Read the study's methods and limitations before deciding whether the headline is fair.

## Best tools
- **Perplexity**: Can locate both current coverage and the linked original research.
- **NotebookLM**: Grounds comparison in uploaded news and study documents with source references.

## Prompt

```text
Compare the news story [NEWS_URL_OR_TEXT] with the original study or dataset [STUDY_URL_OR_FILE] as a media-literacy analyst.

First confirm that the story actually refers to this study. Record the headline, outlet, date, study title, authors, venue, and identifier. If the original cannot be accessed, state that limitation and avoid a definitive verdict.

Use a side-by-side format covering: population and sample size, research design, measured outcome, timeframe, effect size, uncertainty, funding or conflicts, and limitations. Quote the news wording beside the relevant study wording where possible.

Check for common distortions: correlation described as causation, relative risk without absolute risk, animal or laboratory findings generalised to humans, preliminary work treated as settled, subgroup results presented as universal, and applicability to Pakistan assumed without evidence.

Give the headline one verdict: accurate, mostly accurate, overstated, misleading, or unverifiable. Justify it with three concise evidence points. Then rewrite the headline and a 100-word summary to match the study more faithfully without draining all interest. End with two questions readers should ask before changing behaviour based on this finding, especially if it concerns health, finance, or safety.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
