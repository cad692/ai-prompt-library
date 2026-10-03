# 087 — Cursor Multi-File Refactor Brief

**Category:** addins · **Difficulty:** Advanced

**Usage:** Ask Cursor to refactor several files while preserving public behavior and limiting scope.

**Expected output:** A scoped refactor, affected-file summary, and test evidence.

**Tip:** Name the permitted files and verification command before authorising edits.

## Best tools
- **Cursor**: Can inspect related files and apply coordinated edits across a codebase.

## Prompt

```text
Role: Act as a repository maintainer performing a bounded refactor; preserve observable behaviour while improving [REFACTOR_GOAL].

Inspect [ENTRY_FILES] and trace only the imports, tests, and configuration needed to understand the change. Before editing, summarise the current design, list files you expect to touch, and identify public APIs or persisted formats that must remain compatible. Do not modify generated files, lockfiles, unrelated formatting, or [EXCLUDED_PATHS].

Implement the smallest coherent change. Use existing abstractions where they genuinely fit; do not introduce a new framework for convenience. If a proposed rename crosses package boundaries, update references and tests together. Pause and report if the code contradicts [EXPECTED_BEHAVIOUR] or if migration would be required.

Verification must include [TEST_COMMAND], relevant static checks, and a search for stale identifiers. Report:
- files changed and why;
- behaviour intentionally unchanged;
- tests run with results;
- risks or unverified paths;
- any follow-up work kept outside scope.

Never claim a check passed unless it ran. Preserve user changes already present in the working tree.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
