# Guardrails

Policy for the personal multi-agent assistant. The [operating model](../docs/operating-model.md) explains why these rules exist. These files are the copy an agent can follow, and the approval matrix is the machine-readable one the operating model points to.

| File | What it is |
|---|---|
| [`approval-matrix.yaml`](approval-matrix.yaml) | Every action class, and whether it is autonomous, needs approval, or is never allowed |
| [`stop-conditions.md`](stop-conditions.md) | When to stop: three failed tries, two failed logins, a usage limit, and what the report must contain |
| [`tool-allowlist.md`](tool-allowlist.md) | Which tools exist, in which order to try them. Connectors first. The browser last |
| [`mail-routing.md`](mail-routing.md) | Label-only mail filters. Nothing skips the inbox, marks mail read, or touches 2FA or security mail |
| [`propose-then-apply.md`](propose-then-apply.md) | Separation of duties for the transaction categorizer: code proposes, the data owner applies |

Role cards in [`agents/`](../agents/) can be stricter than this folder. They cannot be looser.

If a role card and the approval matrix disagree, stop and ask the owner. Do not pick the looser one.
