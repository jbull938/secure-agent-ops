# Worked example: input

SYNTHETIC SAMPLE for secure-agent-ops. Not real data. All names, IDs, apps, and domains
(example.com) are fictional.

**User's request:** "Run the access review for ExpenseApp and its AI agent as of 2026-10-01.
Riley Moss is the reviewer. Use default thresholds."

## access-export.csv

```csv
row_id,app,account_id,account_type,employee_id,entitlement,status,mfa_enabled,last_login,created,owner_id,notes
X01,ExpenseApp,quinn.harper,human,E2001,expense.pay,enabled,Y,2026-09-29,2024-05-06,,
X02,ExpenseApp,quinn.harper,human,E2001,expense.approve,enabled,Y,2026-09-02,2026-07-01,,Backup approver for summer.
X03,ExpenseApp,riley.moss,human,E2002,expense.approve,enabled,Y,2026-09-30,2022-02-14,,
X04,ExpenseApp,sasha.grant,human,E2003,expense.submit,enabled,N,2026-09-03,2023-08-21,,
X05,ExpenseApp,toby.reyes,human,E2004,expense.approve,enabled,Y,2026-09-28,2021-11-01,,
X06,ExpenseApp,svc-expense-import,service,,expense.import,enabled,n/a,2026-10-01,2025-03-10,E2002,Imports card transactions nightly.
```

## hr-roster.csv

```csv
employee_id,name,email,department,title,manager_id,employment_type,status,hire_date,end_date,last_transfer_date,prior_department
E2001,Quinn Harper,quinn.harper@corp.example.com,Finance,Expense Analyst,E2002,employee,active,2024-05-01,,,
E2002,Riley Moss,riley.moss@corp.example.com,Finance,Finance Manager,E2099,employee,active,2022-02-01,,,
E2003,Sasha Grant,sasha.grant@corp.example.com,Sales,Sales Representative,E2004,employee,terminated,2023-08-14,2026-09-05,,
E2004,Toby Reyes,toby.reyes@corp.example.com,Sales,Sales Manager,E2099,employee,active,2021-10-25,,,
```

## role-definitions.csv

```csv
app,entitlement,description,privileged,eligible_for,sod_conflicts_with
ExpenseApp,expense.submit,Submit expense reports,N,All employees,
ExpenseApp,expense.approve,Approve expense reports,Y,Finance:Finance Manager;Sales:Sales Manager,expense.pay
ExpenseApp,expense.pay,Release reimbursement payments,Y,Finance:Expense Analyst,expense.approve
ai-agents,finance.transactions.read,Read-only transaction views,N,finance,
ai-agents,expense.approve,Approve expense reports,Y,none (approvals need a human),
```

## ai-agent-identities.csv

```csv
row_id,agent_id,agent_role,owner_employee_id,token_id,scopes,token_created,token_expires,token_last_used,status,notes
G01,agent-finance,finance,E2002,tok-fin-11,finance.transactions.read;expense.approve,2026-09-20,2026-10-20,2026-09-30,active,
```
