# Stop conditions

Every task has a stop, not only a goal. Hitting a stop is a successful control. The agent reports and waits. It does not invent a fourth approach.

These thresholds are the concrete form of the stop condition in the [operating model](../docs/operating-model.md), section 7.

## Three failed tries

On a single step, the same approach may fail twice. The third failure stops the task. Rewording the error, switching flags, or moving to a heavier tool is not a new approach. In particular, failing with a connector and then opening a browser counts as the same step, not a fresh start.

After the third failure the agent stops even if it still has ideas.

## Two failed logins

Two failed logins to the same site, connector, or portal pause the task. There is no third attempt. The agent does not try another account, a saved session, or a password reset. A saved login is a credential, not a workaround. See threat T3 in the [threat model](../docs/threat-model.md).

## Usage limit

If a tool or a model reports a usage limit or a quota, the agent pauses that work and reports once. It does not switch accounts, open a browser, or split the task to get around the limit.

## Other stops (unchanged)

Also stop, even on the first failure, when:

- the next step would need a heavier tool than the job needs, such as a browser when a connector or an export exists
- the next step would not be worth another half hour
- the next step would bypass an approval, a stop, or a role card
- the owner has denied the action. Denial is final. Do not rephrase it and try again

## What the report contains

The stop report is the blocker record. It says:

1. What is done.
2. What is blocked.
3. Why, including the error or the threshold that fired (third failure, second login failure, usage limit).
4. The cheapest alternative, which may be "the owner does this step."

The report does not include secrets, message bodies, verification codes, account numbers, health details, hostnames, or addresses. The chief tracks open stop reports. There is no second copy of this record in the repo.

## Preview before a write

Before any write the owner will have to live with, show the exact change and wait. That includes shared notes other agents read, a Decision Log row, a filter, a spreadsheet cell, and a code diff. Writes to the agent's own scratch notes may proceed when the approval matrix says so, and they still must not contain secrets or health details.

A script that proposes categories is not a write to the books. Saving its proposal to a local file is still not applying it. See [propose-then-apply](propose-then-apply.md).
