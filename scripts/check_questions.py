#!/usr/bin/env python3
"""Validate question metadata against prompt placeholders and the baseline YAML."""

from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "prompts.yaml"
QUESTIONS_PATH = ROOT / "data" / "questions.yaml"
TOKEN_RE = re.compile(r"\[([A-Z0-9_]+)\]")


def load_yaml(path: Path):
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def token_counts_for_prompt(prompt_text: str) -> Counter:
    return Counter(TOKEN_RE.findall(prompt_text))


def check_questions(start_hash: str):
    errors: list[str] = []
    questions = load_yaml(QUESTIONS_PATH) or {}
    prompts = load_yaml(DATA_PATH) or {}
    prompt_entries = prompts.get("prompts", [])

    if not start_hash:
        errors.append("Missing starting commit hash.")
        return False, errors

    try:
        baseline = subprocess.run(
            ["git", "show", f"{start_hash}:data/prompts.yaml"],
            cwd=str(ROOT),
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        errors.append(f"Unable to read baseline from commit {start_hash}: {exc.stderr.strip() or exc.stdout.strip()}")
        return False, errors

    baseline_prompts = (yaml.safe_load(baseline.stdout) or {}).get("prompts", [])
    baseline_counts = {
        str(p.get("id", "")).zfill(3): token_counts_for_prompt(p.get("prompt", ""))
        for p in baseline_prompts
    }

    current_counts = {
        str(p.get("id", "")).zfill(3): token_counts_for_prompt(p.get("prompt", ""))
        for p in prompt_entries
    }

    for entry in prompt_entries:
        pid = str(entry.get("id", "")).zfill(3)
        if pid not in questions:
            continue
        meta = questions.get(pid, {})
        prompt_tokens = token_counts_for_prompt(entry.get("prompt", ""))
        prompt_token_set = set(prompt_tokens)
        question_token_set = set(meta)

        for token in sorted(prompt_token_set):
            if token not in meta:
                errors.append(f"{pid}: missing token {token} in questions.yaml")
                continue
            item = meta.get(token)
            if not isinstance(item, dict):
                errors.append(f"{pid}: token {token} metadata is not a mapping")
                continue
            if "q" not in item or not item.get("q"):
                errors.append(f"{pid}: token {token} is missing q")
            if "ex" not in item or not item.get("ex"):
                errors.append(f"{pid}: token {token} is missing ex")
            q_text = item.get("q", "")
            if q_text and len(q_text.split()) > 12:
                errors.append(f"{pid}: token {token} q exceeds 12 words: {q_text}")

        extras = sorted(question_token_set - prompt_token_set)
        if extras:
            errors.append(f"{pid}: questions.yaml has extra tokens not used in the prompt: {', '.join(extras)}")

    for pid in sorted(set(baseline_counts) | set(current_counts)):
        if baseline_counts.get(pid) != current_counts.get(pid):
            errors.append(
                f"{pid}: placeholder counts changed from {dict(baseline_counts.get(pid, Counter()))} to {dict(current_counts.get(pid, Counter()))}"
            )

    if not errors:
        print("PASS")
        return True, [f"Checked {len(prompt_entries)} prompt entries against baseline {start_hash}."]

    print("FAIL")
    for message in errors:
        print(message)
    return False, errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/check_questions.py <start-commit-hash>")
        sys.exit(2)
    ok, details = check_questions(sys.argv[1])
    if ok:
        sys.exit(0)
    sys.exit(1)
