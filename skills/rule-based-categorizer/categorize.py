#!/usr/bin/env python3
"""Propose transaction categories from local rules.

Dry run by default. This program reads a rules file and a transactions
file, then prints a proposal. Pass --write to save that same proposal to
a local file. It does not contact a bank, a bank-data aggregator, or a
spreadsheet, and it has no credentials and no apply mode.

The data owner reviews the proposal and applies any accepted rows.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


def load_rules(path: Path) -> list[dict]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"could not read rules file: {exc}") from exc
    if not isinstance(data, list) or not data:
        raise SystemExit("rules file must be a non-empty JSON list")
    rules = []
    for index, rule in enumerate(data, start=1):
        if not isinstance(rule, dict):
            raise SystemExit(f"rule {index} must be an object")
        cleaned = {}
        for key in ("id", "field", "match", "pattern", "category"):
            value = rule.get(key)
            if not isinstance(value, str) or not value.strip():
                raise SystemExit(f"rule {index} missing {key}")
            cleaned[key] = value.strip()
        if cleaned["match"] not in ("contains", "equals"):
            raise SystemExit(
                f"rule {cleaned['id']} has unsupported match {cleaned['match']}"
            )
        rules.append(cleaned)
    return rules


def load_transactions(path: Path) -> list[dict]:
    try:
        handle = path.open(newline="", encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"could not read transactions file: {exc}") from exc
    with handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        if "row_id" not in fields or "description" not in fields:
            raise SystemExit("transactions need row_id and description columns")
        rows = []
        for row in reader:
            rows.append({key: (value or "").strip() for key, value in row.items()})
        return rows


def classify(row: dict, rules: list[dict]) -> dict:
    for rule in rules:
        haystack = row.get(rule["field"], "")
        needle = rule["pattern"]
        if rule["match"] == "contains":
            matched = needle.casefold() in haystack.casefold()
        else:
            matched = needle.casefold() == haystack.casefold()
        if matched:
            return {
                "row_id": row.get("row_id", ""),
                "rule_id": rule["id"],
                "category": rule["category"],
                "matched_on": rule["field"],
                "status": "proposed",
            }
    return {
        "row_id": row.get("row_id", ""),
        "rule_id": None,
        "category": "Uncategorized",
        "matched_on": None,
        "status": "needs_owner",
    }


def build_payload(rows: list[dict], rules: list[dict], wrote_file: bool) -> dict:
    proposals = [classify(row, rules) for row in rows]
    return {
        "mode": "proposal_file" if wrote_file else "dry_run",
        "applied_to_records": False,
        "proposal_count": len(proposals),
        "needs_owner_count": sum(item["status"] == "needs_owner" for item in proposals),
        "proposals": proposals,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Propose categories. Does not write to a spreadsheet or a bank."
    )
    parser.add_argument("--rules", required=True, type=Path)
    parser.add_argument("--transactions", required=True, type=Path)
    parser.add_argument(
        "--write",
        type=Path,
        help="Save the proposal JSON to this local file. This does not apply categories.",
    )
    args = parser.parse_args(argv)

    rules = load_rules(args.rules)
    rows = load_transactions(args.transactions)
    payload = build_payload(rows, rules, wrote_file=args.write is not None)
    text = json.dumps(payload, indent=2) + "\n"
    if args.write is not None:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(text, encoding="utf-8")
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
