# AI Prompt Library

Premium workshop perk for **Mastering Modern AI Tools** by Thrive Wellness & Development.

## What you get

1. **Index PDF** — cover + menu of all prompts (links only, no full text)
2. **Website** — search, filters, preview sheet, full copyable prompt pages
3. **Offline ZIP + CSV** — one `.txt` per prompt for weak internet

## Live links

After deploy, set these in `config.yaml` and rebuild:

```yaml
BASE_URL: "https://<username>.github.io/ai-prompt-library"
GITHUB_REPO_URL: "https://github.com/<username>/ai-prompt-library"
```

## Build

```bash
pip install pyyaml jinja2 reportlab qrcode pillow
python build/generate.py
```

Outputs:

- `index.html`, `prompts/*.html`, `pages/*.html`
- `assets/prompts-index.json` (search index, no full prompts)
- `prompts-md/*.md`
- `downloads/AI-Prompt-Library-Index.pdf`
- `downloads/offline-prompts.zip`
- `downloads/prompts.csv`

## Add a prompt

1. Edit `data/prompts.yaml` (follow the schema of existing entries).
2. Run `python build/generate.py`.
3. Commit and push.

Preview text is auto-cut from the prompt opening (~200 characters) unless you set `preview` manually.

## Notes

- The website and preview sheet need internet.
- Use the ZIP/CSV offline.
- Tool recommendations change; verify before high-stakes use.
- Academic integrity: this library coaches learning — it does not help cheat exams or bypass detectors.
