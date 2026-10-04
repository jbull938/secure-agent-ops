# Worked example: input

SYNTHETIC SAMPLE for secure-agent-ops. Not real data. The company, people, vendor, product
names, and domains (example.com) are fictional.

**User's request:** "Run the AI governance checklist on this intake form. The decision owner
is the AI Risk Committee."

---

## AI use case intake form

**Company:** Northbridge Logistics (fictional)
**Submitted:** 2026-09-28 by Owen Achterberg (fictional), Security Engineering
**System name:** SOC Triage Assistant
**Inventory ID:** AI-INV-0042
**New or expansion:** New (phase 1). Phase 2 is described at the end for context only.

### 1. Owners
- Business owner: Mira Castellanos (fictional), SOC Manager
- Technical owner: Owen Achterberg (fictional), Security Engineering
- Risk approver: AI Risk Committee, chaired by Helena Brandt (fictional), CISO

### 2. Purpose and users
Help SOC analysts with first-pass triage of SIEM alerts. For each new alert, the assistant
reads the alert, runs read-only searches for context, and writes a draft triage note as a
comment on the case. The analyst reads the note and decides the disposition. The assistant
cannot close, escalate, or contain anything.

Users: 9 SOC analysts. People affected: employees whose usernames, hosts, and IPs appear in
alerts. No customers.

Out of scope: closing alerts, containment, contacting users, any action outside the case tool.

### 3. Self-assessed risk
"Low. Internal tool, draft-only."

### 4. Model and vendor
Hosted model from ModelCo (fictional vendor) through our enterprise API account. "DPA signed
2026-06-12; zero data retention enabled." (DPA not attached.)

### 5. Data
- Inputs: alert JSON from the SIEM; results of read-only searches on security indexes.
- Alerts contain usernames, hostnames, internal IPs, command lines, URLs, and user agents.
- No training or fine-tuning. No retrieval index.
- Prompts, outputs, and tool calls logged to the `ai_audit` index, kept 90 days.

### 6. Tools and permissions
- `siem.search`: read-only, limited to security indexes.
- `case.comment.write`: add comments to existing cases only.
- No containment, ticket-close, email, or chat tools.
- Identity: service account `svc-ai-triage` with a token that expires every 7 days, issued
  from the secrets manager. "Will be added to the quarterly access review."

### 7. Testing
Ran the `soc-alert-triage` eval set on 2026-09-18. Results attached below.

| Case | Result |
|---|---|
| TC-01 to TC-06 | 6 of 6 passed |

Prompt injection: TC-06 (injection in the HTTP user agent) passed. No other injection tests yet.

### 8. Human oversight
Analyst decides every disposition. Comments are labeled "AI-drafted - analyst review required".
The SOC manager can disable the assistant by revoking its token.

### 9. Transparency and training
- Every comment carries the "AI-drafted" label.
- 30-minute analyst training delivered 2026-09-25. Attendance: 9 of 9 (list attached).

### 10. Policy fit
AI Acceptable Use Standard v1.2, section 4.1: "Permitted: security alert triage assistance,
draft-only, with analyst decision."

### 11. Monitoring and incidents
- Tool calls and outputs go to `ai_audit`; a weekly report shows volume, errors, and how often
  analysts change the AI's suggested disposition.
- Incident handling: "Revoke the token." No AI incident definition yet.

### 12. Legal and privacy
Privacy review "scheduled for 2026-10-20". No impact assessment ("not needed, internal tool").
Operating regions: United States only.

### 13. Change management
Any new tool, model change, or phase 2 work requires a new assessment.

### 14. Decommissioning
Not addressed.

### Phase 2 (context only, not requested now)
Auto-close low-severity alerts the assistant judges to be false positives.
