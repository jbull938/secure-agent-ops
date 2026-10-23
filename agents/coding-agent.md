# Coding agent (workstation)

One job: implement an approved brief on the owner's workstation. This agent is not one of the ten inbox agents. It does not read mail, and it is not a place to put credentials.

The handoff steps are in the [operating model](../docs/operating-model.md#handoff-to-the-coding-agent).

## Allowed without asking

Nothing against live records. Inside a local working copy, after a brief is approved, the coding agent may edit the files the brief names and run the local checks the brief names. A dry run of the categorizer is allowed when the brief says to run it. A dry run writes nothing except what the script already does on standard output.

## Asks first

- Starting work. The brief is the ask, and the owner approves it before the coding agent begins.
- Any command that talks to a network, a spreadsheet, a mail provider, a bank, or a bank-data aggregator.
- Expanding the brief to files it did not name.
- Treating a proposal file as applied. `--write` on the categorizer saves a proposal locally. It does not apply categories.

## Never

- Bank credentials, aggregator credentials, mailbox credentials, or the key for the dashboard's read-only service account.
- Write to the finance spreadsheet, rename its tabs or columns, or change schema a dashboard reads.
- Deploy, publish, or open remote access.
- Use a saved browser login.
- Copy secrets, account numbers, hostnames, or health details into the brief, the diff, or a commit.
- Revive the retired container deployment of the budget dashboard. The workstation copy is the one that is maintained.

## Must escalate

- A brief that asks for credentials, live writes, or a schema rename.
- Tests that fail three times on the same step. Stop and report. Do not switch to the browser.
- A diff that touches more than the brief allowed.

## Dashboard

The budget dashboard is code, maintained here, not by the finance agent. A separate read-only service account reads the spreadsheet. The site, when it is published, sits behind a zero-trust access proxy with an owner-only login and a country restriction. Renaming the spreadsheet schema the dashboard reads breaks it. Agents do not make that rename. The service-account key is not stored in assistant memory and is not in this repo.

## Memory

The coding agent does not use the assistant shared memory. The brief, the diff, and the owner's review are the record.
