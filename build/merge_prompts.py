import yaml, re, json
from collections import Counter
from pathlib import Path

ROOT = Path(r"C:\Users\DELL\Downloads\100+ AI prompt\ai-prompt-library")


def load(p):
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f)["prompts"]


def make_preview(text, limit=200):
    text = re.sub(r"\s+", " ", text.strip())
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "..."


a = load(ROOT / "data/_batch_a.yaml")
b = load(ROOT / "data/_batch_b.yaml")
c = load(ROOT / "data/_batch_c.yaml")
prompts = a + b + c
print("raw counts", len(a), len(b), len(c), "total", len(prompts))

required = [
    "id",
    "slug",
    "title",
    "category",
    "difficulty",
    "usage",
    "best_tools",
    "tip",
    "expected_output",
    "tags",
    "prompt",
]
issues = []

for p in prompts:
    for k in required:
        if k not in p or p[k] in (None, "", []):
            issues.append(f"{p.get('id')}: missing {k}")
    if p.get("difficulty") not in ("Beginner", "Intermediate", "Advanced"):
        issues.append(f"{p['id']}: bad difficulty {p.get('difficulty')}")
    words = len(str(p.get("usage", "")).split())
    if words > 22:
        issues.append(f"{p['id']}: usage too long ({words} words)")
    if str(p.get("usage", "")).endswith((" a.", " and", " the", " to", " of", " for", " with", " a")):
        issues.append(f"{p['id']}: truncated usage")
    if p["prompt"].lstrip().startswith("["):
        issues.append(f"{p['id']}: prompt starts with placeholder")
    if len(p.get("tags", [])) < 3 or len(p.get("tags", [])) > 6:
        issues.append(f"{p['id']}: tags count {len(p.get('tags', []))}")
    for t in p["best_tools"]:
        if "tool" not in t and "name" in t:
            t["tool"] = t.pop("name")
        if "reason" not in t:
            issues.append(f"{p['id']}: tool missing reason")
        # strip any price-like strings
        if re.search(r"\$|\bPKR\b|\bprice\b|\b/\$", str(t.get("reason", "")), re.I):
            issues.append(f"{p['id']}: price language in tool reason")

for p in prompts:
    override = p.pop("preview_override", None)
    # keep use_case for full pages if present; else synthesize from usage
    if not p.get("use_case"):
        p["use_case"] = p["usage"]
    # map tip from pro_tip if needed
    if "tip" not in p and "pro_tip" in p:
        p["tip"] = p.pop("pro_tip")
    p.pop("pro_tip", None)
    p.pop("customize_hint", None)
    p.pop("chain_id", None)
    p.pop("chain_step", None)
    if "chain_next" in p and "next_id" not in p:
        p["next_id"] = p.pop("chain_next")
    else:
        p.pop("chain_next", None)
    if override:
        p["preview"] = override
    else:
        p["preview"] = make_preview(p["prompt"])
    if "next_id" not in p or p["next_id"] in ("", "null", "None"):
        p["next_id"] = None
    elif p["next_id"] is not None:
        p["next_id"] = str(p["next_id"]).zfill(3) if str(p["next_id"]).isdigit() else str(p["next_id"])

ids = [p["id"] for p in prompts]
titles = [p["title"].lower() for p in prompts]
opens = [p["prompt"][:120] for p in prompts]
print("id unique", len(ids) == len(set(ids)), "range", ids[0], ids[-1])
print("title unique", len(titles) == len(set(titles)))
print("open unique", len(opens) == len(set(opens)))
print("categories", dict(Counter(p["category"] for p in prompts)))

# expected id sequence
expected = [f"{i:03d}" for i in range(1, 116)]
if ids != expected:
    issues.append(f"id sequence mismatch: got {ids[:3]}...{ids[-3:]}")


def wordset(s):
    return set(re.findall(r"[a-z0-9]+", s.lower()))


near = []
for i in range(len(prompts)):
    wi = wordset(prompts[i]["prompt"])
    for j in range(i + 1, len(prompts)):
        wj = wordset(prompts[j]["prompt"])
        jac = len(wi & wj) / len(wi | wj)
        if jac > 0.72:
            near.append((prompts[i]["id"], prompts[j]["id"], round(jac, 2)))
print("near-duplicate pairs jac>0.72", len(near), near[:8])

phrase = "self-review against accuracy, relevance, clarity"
share = sum(1 for p in prompts if phrase in p["prompt"])
print("share old template phrase", share)

chains = [p for p in prompts if p["category"] == "chains"]
print("chains", [(p["id"], p.get("next_id")) for p in chains])

# Final field order for readability
ordered = []
for p in prompts:
    ordered.append(
        {
            "id": p["id"],
            "slug": p["slug"],
            "title": p["title"],
            "category": p["category"],
            "difficulty": p["difficulty"],
            "usage": p["usage"],
            "use_case": p.get("use_case", p["usage"]),
            "preview": p["preview"],
            "best_tools": p["best_tools"],
            "tip": p["tip"],
            "expected_output": p["expected_output"],
            "tags": p["tags"],
            "next_id": p.get("next_id"),
            "prompt": p["prompt"],
        }
    )

with open(ROOT / "data/prompts.yaml", "w", encoding="utf-8") as f:
    yaml.dump({"prompts": ordered}, f, allow_unicode=True, sort_keys=False, width=100)

index = [
    {k: p[k] for k in ("id", "slug", "title", "category", "difficulty", "usage", "preview", "tags")}
    for p in ordered
]
raw = json.dumps(index, ensure_ascii=False).encode("utf-8")
print("index json bytes", len(raw))

lines = [
    "# Prompts review summary",
    f"Total: {len(ordered)}",
    f"Search-index estimate: {len(raw)} bytes",
    f"Near-duplicate pairs (jac>0.72): {len(near)}",
    f"Old template phrase hits: {share}",
    "",
    "## By category",
]
for cat, n in Counter(p["category"] for p in ordered).items():
    lines.append(f"- {cat}: {n}")
lines += ["", "## Sample (every 12th)", ""]
for p in ordered[::12]:
    lines.append(f"- **{p['id']}** {p['title']} [{p['difficulty']}]")
    lines.append(f"  - usage: {p['usage']}")
    lines.append(f"  - preview: {p['preview'][:120]}...")
    lines.append(f"  - tools: {', '.join(t['tool'] for t in p['best_tools'])}")
lines += ["", "## Issues"] + (issues[:80] or ["None"])
(ROOT / "data/PROMPTS_REVIEW.md").write_text("\n".join(lines), encoding="utf-8")
print("issues", len(issues))
for i in issues[:25]:
    print(" ", i)
print("done")
