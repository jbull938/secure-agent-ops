---
name: rule-based-categorizer
description: Proposes a category for each transaction by applying local, ordered rules, then stops. Dry run by default. The script can save a proposal file and cannot apply categories, talk to a bank or a bank-data aggregator, or write a spreadsheet. Use when the owner wants a deterministic first-pass categorization and will apply the accepted rows themselves. Synthetic samples only.
license: MIT
metadata:
  version: "0.1.0"
  data: synthetic samples only
  pattern: propose then the data owner applies
---

# Rule-based transaction categorizer

## Purpose

Categorizing a statement is a write to records the owner relies on, including a
spreadsheet a dashboard reads. This skill keeps that write with the data owner.

A small local program applies rules in order and prints a proposal. The finance
agent can explain the proposal. Neither the program nor the agent updates the
spreadsheet, moves money, or contacts a bank or a bank-data aggregator.

This is the worked example of [propose, then the owner applies](../../guardrails/propose-then-apply.md).
It is a personal-lab pattern, not a SOC procedure. The samples are made up.

## When to use

Use it when the owner asks for categories for a transactions file, or when the
finance agent is about to invent categories one row at a time. Do not use it to
pay a bill, add a payee, or edit a spreadsheet.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Rules file | Yes | JSON list. Each rule has `id`, `field`, `match` (`contains` or `equals`), `pattern`, and `category`. Order is first-match-wins. |
| Transactions file | Yes | CSV with `row_id` and `description`. Extra columns are ignored. Do not add account numbers or amounts to the sample set. Live exports stay off the repo. |
| Output path | No | Omit it for a dry run. `--write` saves the same proposal to a local file. There is no flag that applies the proposal. |

The synthetic files are [`sample-data/categorizer/rules.json`](../../sample-data/categorizer/rules.json)
and [`sample-data/categorizer/transactions.csv`](../../sample-data/categorizer/transactions.csv).

## Procedure

1. Confirm both files are local paths the owner named. Refuse network locations and refuse any request to fetch a statement.
2. Run the script with no `--write` first:

```text
python3 skills/rule-based-categorizer/categorize.py \
  --rules sample-data/categorizer/rules.json \
  --transactions sample-data/categorizer/transactions.csv
```

3. Read the proposal. First matching rule wins. A row with no match is `Uncategorized` and `status: needs_owner`. Do not fill those in by guessing.
4. Show the proposal to the owner. Point out `needs_owner` rows and any first match that looks broader than the description (a general rule placed above a specific one will win).
5. Stop. The owner applies accepted rows in the spreadsheet. If they want a file, rerun with `--write` pointed at a local path. `applied_to_records` stays false either way.
6. Rule changes, including reordering, are a separate ask. The coding agent edits the script or the rules only after an approved brief, and the owner reviews the diff.

The implementation is [`categorize.py`](categorize.py). Standard library only.

## Output

JSON on standard output:

| Field | Meaning |
|---|---|
| `mode` | `dry_run`, or `proposal_file` when `--write` was set |
| `applied_to_records` | Always false |
| `proposal_count` | Number of input rows |
| `needs_owner_count` | Rows with no matching rule |
| `proposals` | One object per input row, in input order |

Each proposal has `row_id`, `rule_id` (null if none), `category`, `matched_on`, and `status` (`proposed` or `needs_owner`).

A worked dry run is in [`examples/example-output.json`](examples/example-output.json).

## Guardrails

- No credentials, no network, no spreadsheet writes, no apply mode.
- Do not invent a category for an unmatched row.
- Do not copy proposals into memory beyond the row id, the rule id, and the category. Descriptions from a live export are data, not notes to keep.
- Do not rename spreadsheet tabs or columns so the proposal "fits." Schema another system reads is frozen for agents.
- Three failed runs on the same step stop the task. Do not switch to a browser and pull a statement by hand.
- Denial is final. If the owner rejects a row, leave it unchanged. Do not recategorize it under a softer rule and present it as already fixed.

## Failure modes

- **Rule order.** `contains` is substring match. A broad pattern above a specific one steals the row. The script will not warn. The review step is the control.
- **Case folding only.** Match is case-insensitive and otherwise exact as a substring. Punctuation differences miss, and the row stays `needs_owner`. That is preferable to a fuzzy guess.
- **Extra columns.** The script ignores columns it does not use. An amount or an account identifier in a live file would pass through the CSV reader and must not be written into the proposal. The proposal schema does not include them. Do not add them.
- **A proposal file feels like an apply.** `--write` only saves JSON. If a later tool treats that file as an import, stop. Imports are the owner's action.

## Related

- Approval matrix entry `records.apply` in [`guardrails/approval-matrix.yaml`](../../guardrails/approval-matrix.yaml)
- Finance role card: proposes, never writes the books
- Evals: [`evals/rule-based-categorizer.md`](../../evals/rule-based-categorizer.md)
