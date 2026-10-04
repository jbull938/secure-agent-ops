# Worked example: output

This is the expected output for [`example-input.md`](example-input.md), written in the
skill's output template. All data is synthetic.

---

## Access review: ExpenseApp and AI agents as of 2026-10-01

**Prepared for:** Riley Moss (reviewer); alternate reviewer needed for row X03
**Status:** Recommendation only. No access has been changed. A named human certifies each row.
**Thresholds used:** Defaults. Inactive after 90 days without login (before 2026-07-03); agent tokens flagged with no expiry or 30 days unused.

### Summary
Seven rows reviewed (six account entitlements and one AI agent token). Five need attention.
Sasha Grant left on 2026-09-05 and still has an enabled account. Quinn Harper can both
approve and pay expenses, which is a separation-of-duties conflict involving money. The
finance agent's token includes `expense.approve`, which its role card does not allow. The
service account's entitlement is missing from the role definitions. The reviewer holds one
of the rows under review.

| Recommended decision | Rows |
|---|---|
| Keep | 2 (X01, X05) |
| Revoke | 2 (X02, X04) |
| Modify | 1 (G01) |
| Needs owner decision | 2 (X03, X06) |

X01 is a conditional Keep: it holds only once X02 is revoked. X03 is clean but needs an
alternate reviewer.

### Data profile and quality gaps
- Files and row counts: access export 6 rows, HR roster 4 rows, role definitions 5 rows, agent identities 1 row. All as of 2026-10-01 per the request; the files carry no dates of their own.
- Join results: 5 of 5 human rows matched on `employee_id`. One service account (X06) has owner E2002, who is active.
- Gaps:
  - `expense.import` (X06) is not in the role definitions, so its privilege level and eligibility can't be checked.
  - Manager E2099 is not in the roster, so the alternate reviewer for Riley Moss can't be named from the data.

### Findings
| # | Check | Account (app) | Rows | Evidence (field values) | Risk | Recommended decision | Control refs |
|---|---|---|---|---|---|---|---|
| 1 | F1 Leaver still active | sasha.grant (ExpenseApp) | X04 | HR `status=terminated`, `end_date=2026-09-05`; account `enabled`; `last_login=2026-09-03` (before end date) | High | Revoke | AC-2(3); PCI 8.2.5 |
| 2 | F6 Toxic combination; F4 Excessive privilege | quinn.harper (ExpenseApp) | X01, X02 | Holds `expense.pay` and `expense.approve`, listed as conflicting; `expense.approve` is eligible only for Finance Manager and Sales Manager, and Quinn is Expense Analyst | High | Revoke X02 | AC-5; AC-6; PCI 7.2.2 |
| 3 | F10 Agent scope beyond role card | agent-finance (ai-agents) | G01 | Scope `expense.approve` is `eligible_for=none (approvals need a human)`; the finance role card allows read-only views | High | Modify: remove `expense.approve` | AC-6; PCI 7.2.5 |
| 4 | DQ Undefined entitlement | svc-expense-import (ExpenseApp) | X06 | `expense.import` not in role definitions | Medium | Needs owner decision | AC-2; PCI 7.2.5.1 |
| 5 | Reviewer independence | riley.moss (ExpenseApp) | X03 | The assigned reviewer holds this row | Medium | Needs owner decision (alternate reviewer) | AC-5; SOX ITGC reviewer independence |

The MFA status on X04 (`N`) is noted but moot once the account is revoked.

### Certification worksheet
| Row | App | Account | Type | Person / owner | Entitlement | Findings | Recommended | Reason | Reviewer | Reviewer decision | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X01 | ExpenseApp | quinn.harper | human | Quinn Harper (E2001) | expense.pay | 2 | Keep (if X02 is revoked) | Eligible for Expense Analyst; used 2026-09-29 | Riley Moss | | |
| X02 | ExpenseApp | quinn.harper | human | Quinn Harper (E2001) | expense.approve | 2 | Revoke | Conflicts with expense.pay; not eligible for title. The "backup approver for summer" note is a claim with no end date or approval record. | Riley Moss | | |
| X03 | ExpenseApp | riley.moss | human | Riley Moss (E2002) | expense.approve | 5 | Needs owner decision | Eligible and used; reviewer can't certify own access | Alternate needed | | |
| X04 | ExpenseApp | sasha.grant | human | Sasha Grant (E2003) | expense.submit | 1 | Revoke | Terminated 2026-09-05; still enabled | Riley Moss | | |
| X05 | ExpenseApp | toby.reyes | human | Toby Reyes (E2004) | expense.approve | None | Keep | Eligible for Sales Manager; used 2026-09-28; MFA on | Riley Moss | | |
| X06 | ExpenseApp | svc-expense-import | service | Owner Riley Moss (E2002) | expense.import | 4 | Needs owner decision | Owner active; entitlement undefined; used 2026-10-01 | Alternate needed (owner is the reviewer) | | |
| G01 | ai-agents | agent-finance | ai_agent | Owner Riley Moss (E2002) | finance.transactions.read; expense.approve | 3 | Modify | Remove expense.approve; keep read scope | Alternate needed (owner is the reviewer) | | |

### AI agent identities
| Agent | Role card | Owner | Scopes granted | Scopes beyond role card | Token expiry / last used | Recommended |
|---|---|---|---|---|---|---|
| agent-finance | finance (read-only account and transaction views) | E2002 | finance.transactions.read; expense.approve | expense.approve | 2026-10-20 / 2026-09-30 | Modify |

### Untrusted-content flags
None found. The `notes` values on X02 and X06 contain no instructions. The X02 note is a
claim and is treated as an open question, not evidence.

### Audit-evidence notes
- Population: four files supplied in the request, all as of 2026-10-01. 6 account rows and 1 agent token reviewed; none excluded.
- Method: joined on `employee_id`; eligibility and conflicts from `role-definitions.csv`; default thresholds as stated above.
- Reviewer independence: Riley Moss holds X03 and owns X06 and G01. Recommend Riley's manager (E2099, not in the roster) or another independent reviewer certify those three rows.
- Pending: reviewer decisions and dates for all 7 rows. Each Revoke or Modify should get a ticket, and the closed ticket should be attached as remediation evidence.
- Not covered: activity performed with the access (for example, whether Quinn approved and paid the same report), other apps, and MFA enforcement beyond the export's `mfa_enabled` field.

### Open questions
- Was Quinn's backup-approver access approved, and did it have an end date?
- Did Quinn approve and pay any of the same expense reports between 2026-07-01 and now? That is a transaction review, not part of this access review.
- What does `expense.import` grant, and is it privileged?
- Who is E2099, and can they act as the alternate reviewer?
