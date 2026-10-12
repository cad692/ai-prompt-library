# Prompt Quality Improvement Progress

**Task:** Deep improvement of prompt templates and unambiguous personalization questions  
**Repository:** cad692/ai-prompt-library  
**Total active prompts:** 115  
**Total question sets:** 115  

## Canonical sources
- `data/prompts.yaml` — prompt templates and metadata
- `data/questions.yaml` — personalization `q` / `ex` / `optional` per placeholder
- `assets/js/copy.js` — inserts answers into `[PLACEHOLDER]` tokens; empty optional fields leave brackets
- `build/generate.py` — regenerates HTML, MD, CSV, ZIP, search index, PDF
- `scripts/check_questions.py` — `q` ≤ 12 words; every prompt token needs `q`+`ex`

## Batch plan
| Batch | IDs | Status |
|------:|-----|--------|
| 1 | 001–010 | **complete** |
| 2 | 011–020 | pending |
| 3 | 021–030 | pending |
| 4 | 031–040 | pending |
| 5 | 041–050 | pending |
| 6 | 051–060 | pending |
| 7 | 061–070 | pending |
| 8 | 071–080 | pending |
| 9 | 081–090 | pending |
| 10 | 091–100 | pending |
| 11 | 101–110 | pending |
| 12 | 111–115 | pending |

## Note on prior checkpoint
An earlier session marked 115/115 reviewed with **0 prompt template improvements**. This run re-reviews every active prompt. Do not push until the full library is done.

## Progress counters
- Prompts reviewed: 10/115
- Prompt templates substantively improved: 10
- Prompt templates reviewed, left unchanged: 0
- Question sets reviewed: 10
- Question fields improved / added / removed / made optional: ~70 improved / 0 added / 0 removed / 0 newly optional (existing optionality preserved)

## Batch 1 (001–010) outcomes

### Templates improved
| ID | Reason |
|----|--------|
| 001 | Risk tolerance now drives weights/experiments; missing-input handling; no invented options |
| 002 | Uses focus hours + energy together; blank city/setting fallback; protects recovery blocks |
| 003 | Stops re-asking known fields; defines success-threshold scoring; clearer practice ladder |
| 004 | Blank optional considerations ignored; tone/privacy clarity preserved |
| 005 | Role inferred from participants; blank sensitive/materials omitted instead of invented |
| 006 | Blank OTHER_FIELD/LOCAL_CONTEXT handled so Wave 2 does not break |
| 007 | Thin JD clarification; never invent credentials/tools/employers |
| 008 | Blank local context → neutral examples; uncertainty marked, no fake citations |
| 009 | Blank time/money → smallest free habit; health disclaimer retained |
| 010 | CONCERNS aligned to safety/power; blank support/language handled safely |

### Questions improved (all 10 sets)
Representative clarity fixes:
- 002 AVAILABLE_TIME: “How much time do you have?” → “How much focus time can you dedicate?”
- 004 tone: examples moved into `ex`; q is “What tone should the email use?”
- 010 CONCERNS: “What worries you most?” → “What safety or power concerns exist?” (matches prompt)
- 005 PARTICIPANTS: now asks for attendee list **and** the user’s role
- Examples made concrete (amounts, dates, channel, measurable success)

### Validation
- Local placeholder/`q`≤12/`ex` coverage check: PASS (115 prompts)
- `python build/generate.py`: PASS (115 prompts; search index 56,479 bytes; ZIP/CSV/PDF regenerated)
- HTML spot checks for 001/004/010: PASS
- `scripts/check_questions.py HEAD`: blocked on Windows `git show` encoding (not a data defect)

### Commits
- Local only — **do not push until full library complete**

## Remaining
011–115 (batches 2–12)

## Next action
Review and improve prompts **011–020** (templates first, then questions), validate, commit locally, continue.
