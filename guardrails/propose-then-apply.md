# Propose, then the owner applies

Some jobs look like a write and are safer as a proposal. Categorizing transactions is the worked example. The same shape covers any bulk edit to records the owner keeps.

## The split

| Who | Does | Does not |
|---|---|---|
| Local categorizer script | Reads a rules file and a transactions file the owner pointed at. Prints a proposal. With `--write`, saves that same proposal to a local file | Talk to a bank, a bank-data aggregator, a spreadsheet, or the network. Hold a credential. Apply a category |
| Finance agent | Asks for a dry run, reads the proposal, points out rows that need a person | Write the spreadsheet, reorder rules, or treat a proposal as already applied |
| Coding agent | Changes the script on the workstation after an approved brief | Run it against live records, or receive bank or aggregator credentials |
| Data owner | Previews the proposal and applies the rows they accept, in the spreadsheet, themselves | Hand the script a credential so it can "just update the sheet" |

Dry run is the default. There is no apply flag. Adding one is a design change, not a convenience flag, and it would violate the approval matrix entry `records.apply`.

## Rules

- The script uses the language runtime's standard library only. No third-party packages, so a run does not fetch code.
- First matching rule wins. Rule order is part of the policy. The owner reviews order when they review results.
- Rows that match nothing are `Uncategorized` and `needs_owner`. The script does not guess a category.
- The sample inputs are made up. They contain no account numbers and no amounts. Live exports stay off this repo and out of agent memory.
- The finance spreadsheet's tabs and columns are schema the budget dashboard reads. The proposal does not rename them, and neither does the finance agent.

## Where the example lives

The skill, the script, and the synthetic files:

- [`skills/rule-based-categorizer/`](../skills/rule-based-categorizer/SKILL.md)
- [`sample-data/categorizer/`](../sample-data/categorizer/)

Run a dry run from the repo root:

```text
python3 skills/rule-based-categorizer/categorize.py \
  --rules sample-data/categorizer/rules.json \
  --transactions sample-data/categorizer/transactions.csv
```

Add `--write /tmp/category-proposal.json` only when you want a local copy of the same proposal. That file is still a proposal. The data owner applies it, if they accept it, outside this program.
