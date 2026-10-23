# Mail routing

The executive assistant may apply labels. It may not file the owner's mail out of the inbox, hide it, or answer it. Filters are a constrained form of that rule.

This guide is a template. It uses placeholder domains. It is not a copy of a live filter set, and it does not list real senders.

## What a filter is allowed to do

A filter has one action: **apply a label**.

Every filter must also refuse to do all of the following:

- skip the inbox
- mark the message read
- archive the message
- delete the message
- forward the message

If a mail provider bundles any of those with "label," that filter is not imported.

## Security exclusion

Every filter, including phrase filters, excludes 2FA and security mail. The exclusion is part of the query, not a separate filter that runs later:

```text
-subject:(code OR verification OR "security alert" OR "sign-in" OR password)
```

Messages that match the exclusion are left for the owner. The assistant does not label them, summarize them, or copy them into notes. A code or a sign-in alert in the body is the same rule even when the subject was vague: if the assistant notices it, the assistant stops and leaves the message alone.

The mail connector cannot create filters. The owner imports a reviewed filter by hand. An agent may draft the text of a filter from the template below and then stop.

## Label shape

Use one parent label and five children, so routing stays shallow. These names are illustrative, not a dump of a live account:

| Label | What it is for |
|---|---|
| `Agents` | Parent. Unused on its own |
| `Agents/Finance` | Bills and statements the finance agent should see |
| `Agents/Scheduling` | Calendar traffic for the executive assistant |
| `Agents/Home-sale` | Household-transaction mail for the home-sale checklist |
| `Agents/Career` | Applications and recruiting mail |
| `Agents/Noise` | Newsletters and other bulk mail the owner still wants left in the inbox, only labeled |

Other roles receive work by handoff from the chief, not by their own hidden filter.

## Template

One filter, one label, one placeholder domain. Repeat the shape for each child label. Do not paste a live export into the repo.

```text
Name: agents-finance-utility-example
Match: sender domain is utility.example
       AND -subject:(code OR verification OR "security alert" OR "sign-in" OR password)
Action: apply label "Agents/Finance"
Do not: skip inbox, mark as read, archive, delete, forward
Imported by: the owner, by hand
```

Swap the placeholder domain and the label. Keep the exclusion and the "do not" list on every filter. `utility.example`, `career.example`, and `notices.example` are placeholders. They are not the owner's mail.

A phrase filter has the same shape. The phrase is an extra match, and the security exclusion stays in the query:

```text
Name: agents-home-sale-phrase-example
Match: subject or body contains "household transaction"
       AND -subject:(code OR verification OR "security alert" OR "sign-in" OR password)
Action: apply label "Agents/Home-sale"
Do not: skip inbox, mark as read, archive, delete, forward
Imported by: the owner, by hand
```

The phrase in that template is made up for the example.

## Known gap: phrase match versus the exclusion

A phrase rule can still label a message the exclusion was meant to keep out, when the phrase appears in mail from an e-signature service whose subject looks like a security alert. That happens when the phrase rule and the exclusion are combined so the phrase wins, or when they live in two filters and the label is applied before the exclusion.

Until those filters are rebuilt and checked, the home-sale agent treats security-looking mail as out of scope even if the home-sale label is present. It does not open it and it does not copy it into notes. The owner handles it.

This gap is also a lesson in the operating model (section 10) and a residual risk in the threat model (R13).

## What the assistant does with a labeled message

1. If the subject or the visible body is 2FA or security mail, stop. Leave it unlabeled in spirit: do not summarize it, even if a label is already there.
2. Otherwise, route one owner and draft if a reply is useful.
3. Do not mark it read and do not archive it.
