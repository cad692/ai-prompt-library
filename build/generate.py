#!/usr/bin/env python3
"""Generate the AI Prompt Library site, offline pack, and Index PDF from data/prompts.yaml."""

from __future__ import annotations

import csv
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "prompts.yaml"
CONFIG = ROOT / "config.yaml"


def load_config():
    with open(CONFIG, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_prompts():
    with open(DATA, encoding="utf-8") as f:
        prompts = yaml.safe_load(f)["prompts"]
    # normalize
    for p in prompts:
        p["id"] = str(p["id"]).zfill(3)
        if p.get("next_id") not in (None, "", "null"):
            p["next_id"] = str(p["next_id"]).zfill(3)
        else:
            p["next_id"] = None
        for t in p.get("best_tools", []):
            if "tool" not in t and "name" in t:
                t["tool"] = t["name"]
    return prompts


def make_preview(text: str, limit: int = 200) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "..."


def highlight_placeholders(text: str) -> str:
    esc = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return re.sub(r"(\[[A-Z0-9_]+\])", r'<span class="ph">\1</span>', esc)


def cat_map(cfg):
    return {c["id"]: c for c in cfg["categories"]}


def build_search_index(prompts, out: Path):
    index = []
    for p in prompts:
        preview = p.get("preview") or make_preview(p["prompt"])
        index.append(
            {
                "id": p["id"],
                "slug": p["slug"],
                "title": p["title"],
                "category": p["category"],
                "difficulty": p["difficulty"],
                "usage": p["usage"],
                "preview": preview,
                "tags": p.get("tags") or [],
            }
        )
    out.write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return len(out.read_bytes())


def write_markdown(prompts, cfg):
    out_dir = ROOT / "prompts-md"
    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob("*.md"):
        old.unlink()
    for p in prompts:
        tools = "\n".join(f"- **{t['tool']}**: {t['reason']}" for t in p.get("best_tools", []))
        body = f"""# {p['id']} — {p['title']}

**Category:** {p['category']} · **Difficulty:** {p['difficulty']}

**Usage:** {p['usage']}

**Expected output:** {p['expected_output']}

**Tip:** {p['tip']}

## Best tools
{tools}

## Prompt

```text
{p['prompt'].rstrip()}
```

---
{cfg['workshop']['org']} · Last updated: {cfg['meta']['last_updated']}
"""
        (out_dir / f"{p['id']}-{p['slug']}.md").write_text(body, encoding="utf-8")


def write_offline(prompts, cfg):
    dl = ROOT / "downloads"
    dl.mkdir(exist_ok=True)
    txt_dir = ROOT / "build" / "_tmp_txt"
    if txt_dir.exists():
        for f in txt_dir.glob("*"):
            f.unlink()
    txt_dir.mkdir(parents=True, exist_ok=True)

    csv_path = dl / "prompts.csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "id",
                "slug",
                "title",
                "category",
                "difficulty",
                "usage",
                "expected_output",
                "tip",
                "tags",
                "best_tools",
                "next_id",
                "prompt",
            ]
        )
        for p in prompts:
            tools = "; ".join(f"{t['tool']}: {t['reason']}" for t in p.get("best_tools", []))
            tags = ", ".join(p.get("tags") or [])
            w.writerow(
                [
                    p["id"],
                    p["slug"],
                    p["title"],
                    p["category"],
                    p["difficulty"],
                    p["usage"],
                    p["expected_output"],
                    p["tip"],
                    tags,
                    tools,
                    p.get("next_id") or "",
                    p["prompt"],
                ]
            )
            (txt_dir / f"{p['id']}-{p['slug']}.txt").write_text(p["prompt"].rstrip() + "\n", encoding="utf-8")

    zip_path = dl / "offline-prompts.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for f in sorted(txt_dir.glob("*.txt")):
            z.write(f, arcname=f"prompts/{f.name}")
        z.write(csv_path, arcname="prompts.csv")
        readme = (
            "AI Prompt Library — offline backup\n"
            f"{cfg['workshop']['org']}\n"
            f"Last updated: {cfg['meta']['last_updated']}\n\n"
            "The website and preview sheet need internet.\n"
            "This ZIP (one .txt per prompt) and prompts.csv are the offline option.\n"
        )
        z.writestr("README.txt", readme)
    return zip_path, csv_path


def adjacent(prompts):
    by_id = {p["id"]: i for i, p in enumerate(prompts)}
    for i, p in enumerate(prompts):
        p["_prev"] = prompts[i - 1] if i > 0 else None
        p["_next"] = prompts[i + 1] if i + 1 < len(prompts) else None
        # chain override next if present
        if p.get("next_id") and p["next_id"] in by_id:
            p["_chain_next"] = prompts[by_id[p["next_id"]]]
        else:
            p["_chain_next"] = None


def render_site(prompts, cfg):
    env = Environment(
        loader=FileSystemLoader(str(ROOT / "build" / "templates")),
        autoescape=select_autoescape(["html"]),
    )
    env.filters["ph"] = highlight_placeholders
    cats = cat_map(cfg)
    adjacent(prompts)

    # grouped for noscript / SSR list
    grouped = defaultdict(list)
    for p in prompts:
        grouped[p["category"]].append(p)
    cat_order = [c["id"] for c in cfg["categories"]]

    index_html = env.get_template("index.html").render(
        cfg=cfg,
        prompts=prompts,
        cats=cats,
        cat_order=cat_order,
        grouped=grouped,
        base_url=cfg["BASE_URL"].rstrip("/"),
        repo_url=cfg["GITHUB_REPO_URL"].rstrip("/"),
        cat_names_json=json.dumps({c["id"]: c["name"] for c in cfg["categories"]}),
    )
    (ROOT / "index.html").write_text(index_html, encoding="utf-8")

    prompts_dir = ROOT / "prompts"
    prompts_dir.mkdir(exist_ok=True)
    for old in prompts_dir.glob("*.html"):
        old.unlink()

    tpl = env.get_template("prompt.html")
    for p in prompts:
        html = tpl.render(
            cfg=cfg,
            p=p,
            cats=cats,
            base_url=cfg["BASE_URL"].rstrip("/"),
            repo_url=cfg["GITHUB_REPO_URL"].rstrip("/"),
            highlighted=highlight_placeholders(p["prompt"]),
        )
        (prompts_dir / f"{p['id']}-{p['slug']}.html").write_text(html, encoding="utf-8")

    pages = ROOT / "pages"
    pages.mkdir(exist_ok=True)
    for name in ("foundations", "responsible", "cheat-sheet"):
        html = env.get_template(f"{name}.html").render(cfg=cfg, base_url=cfg["BASE_URL"].rstrip("/"))
        (pages / f"{name}.html").write_text(html, encoding="utf-8")


def main():
    import sys

    sys.path.insert(0, str(ROOT / "build"))
    from build_pdf import build_index_pdf

    cfg = load_config()
    prompts = load_prompts()
    assert len(prompts) >= 100, f"Need 100+ prompts, got {len(prompts)}"

    for p in prompts:
        if not p.get("preview"):
            p["preview"] = make_preview(p["prompt"])

    (ROOT / "assets").mkdir(exist_ok=True)
    size = build_search_index(prompts, ROOT / "assets" / "prompts-index.json")
    write_markdown(prompts, cfg)
    zip_path, csv_path = write_offline(prompts, cfg)
    render_site(prompts, cfg)
    pdf_path = build_index_pdf(prompts, cfg)

    print(f"Prompts: {len(prompts)}")
    print(f"Search index: {size} bytes")
    print(f"ZIP: {zip_path}")
    print(f"CSV: {csv_path}")
    print(f"PDF: {pdf_path}")
    print("Done.")


if __name__ == "__main__":
    main()
