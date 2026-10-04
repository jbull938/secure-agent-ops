# Worked example: output

This is the expected output for [`example-input.md`](example-input.md), written in the
skill's output template. The optional GRC summary is in
[`example-grc-summary.json`](example-grc-summary.json). All data is synthetic.

---

## AI governance assessment: SOC Triage Assistant

**Recommendation:** Go with conditions
**Risk tier:** Tier 2 Elevated - draft-only (A1), but it reads attacker-controlled alert fields, holds two tools, and processes security-monitoring data about employees.
**Decision owner:** AI Risk Committee. This is a recommendation; a human decides. Nothing has been approved or deployed.
**Assessed:** 2026-10-04 (UTC-5) against the intake form dated 2026-09-28. Frameworks as listed in the skill metadata; verify before formal citation.

### Use case summary
| Field | Value |
|---|---|
| System | SOC Triage Assistant (inventory ID AI-INV-0042) |
| Owners | Business: Mira Castellanos (SOC Manager). Technical: Owen Achterberg (Security Engineering). Approver: AI Risk Committee, independent of both owners. |
| Purpose | First-pass triage notes on SIEM alerts; analyst decides every disposition |
| Users / affected | 9 SOC analysts / employees named in alerts; no customers |
| Context | Internal |
| Deployment pattern | Agent with tools (read-only search and case comments) on a hosted model API |
| Model and provider | Hosted model from ModelCo (fictional) via enterprise API. Version or deployment ID not stated. |
| Data | Alert JSON and read-only search results (usernames, hosts, IPs, command lines, URLs); no training or retrieval index; logs kept 90 days |
| Tools and scopes | `siem.search` (read-only, security indexes); `case.comment.write` (comments on existing cases) |
| Identity | `svc-ai-triage`, 7-day token from the secrets manager |
| Autonomy | A1 Draft |
| Regions | United States only |
| Stage | New, phase 1. Phase 2 (auto-close) is not part of this request. |
| Shadow-use history | Not stated (open question) |

### Risk tier rationale
Autonomy is low (A1): the assistant drafts notes and an analyst decides. Two factors raise it to
Tier 2. It reads untrusted content, since attackers control user agents, command lines, URLs,
and file names in alerts. And alerts are security-monitoring data about employees (usernames,
hosts, IPs, activity), which is more than ordinary work content. Nothing reaches Tier 3:
no consequential actions, no decisions about people, no special-category data. The team's
self-assessment ("Low") didn't account for the untrusted input.

### Regulatory context (not legal advice)
The form says the company operates in the United States only, so the EU AI Act is marked not
applicable. If any alerts concern people in the EU, counsel should revisit that. Employee data
in alerts may be subject to privacy law and internal monitoring policy, which the scheduled
privacy review should cover. Regulatory notes are context for legal review, not legal advice.

### Checklist
| ID | Control | Question | Evidence provided | Status | Blocking | Owner | Framework refs |
|---|---|---|---|---|---|---|---|
| GC-01 | Use case inventory | In the inventory with ID, owner, purpose, status? | Inventory ID AI-INV-0042 | Met | No | Owen Achterberg | GOVERN 1.6; ISO A.4.2 |
| GC-02 | Accountability | Owners and approver named? | Section 1 names all three | Met | No | Mira Castellanos | GOVERN 2.1; ISO A.3.2 |
| GC-03 | Policy alignment | Fits the AI policy? | Quoted excerpt of AI Acceptable Use Standard v1.2, section 4.1 (full policy not reviewed) | Met | No | Mira Castellanos | GOVERN 1.2; ISO A.2.2 |
| GC-04 | Legal and regulatory review | Legal or privacy review done? | "Scheduled for 2026-10-20" | Partial | Yes | Owen Achterberg | GOVERN 1.1; MAP 4.1; ISO A.2.3 |
| GC-05 | Intended use | Purpose, users, out-of-scope uses documented? | Section 2, including out-of-scope list | Met | No | Mira Castellanos | MAP 1.1; ISO A.9.4 |
| GC-06 | Risk classification | Tier assigned with rationale? | Self-assessed "Low" with no rationale for untrusted input | Partial | No (this assessment proposes Tier 2 for the approver to confirm) | AI Risk Committee | GOVERN 1.3; MAP 1.5; ISO 6.1.2 |
| GC-07 | Impact assessment | Impact on individuals and groups assessed? | "Not needed, internal tool"; alerts contain employee data | Gap | Yes | Mira Castellanos | MAP 5.1; ISO A.5.2-A.5.4 |
| GC-08 | Data provenance and governance | Sources, personal data, retention documented? | Section 5 lists sources, data types, no training, 90-day retention | Met | No | Owen Achterberg | MAP 4.1; ISO A.7.2, A.7.5 |
| GC-09 | Third-party and vendor AI risk | Vendor terms reviewed? | DPA and zero-retention claimed; DPA not attached. Training use, sub-processor notice, and incident notice not stated | Partial | Yes | Owen Achterberg | GOVERN 6.1; MANAGE 3.1; ISO A.10.3; OWASP LLM04:2026 |
| GC-10 | Tools, permissions, agent identity | Tools least-privilege, short-lived credential, in access reviews? | Two scoped tools; 7-day token; access review "will be added" | Partial | Yes | Owen Achterberg | MAP 3.5; OWASP LLM03:2026; `access-review` |
| GC-11 | Performance evaluation | Tested on representative data? | `soc-alert-triage` evals, 6 of 6 passed on 2026-09-18 (table provided) | Met | No | Owen Achterberg | MEASURE 2.3; ISO A.6.2.4 |
| GC-12 | Security and injection testing | Injection tested through every untrusted input? | One field tested (TC-06 user agent); other fields and search results untested | Partial | Yes | Owen Achterberg | MEASURE 2.7; OWASP LLM01:2026; `untrusted-content-guard` |
| GC-13 | Fairness and bias | Outcomes tested across groups? | None needed: the assistant does not score or decide about people (see note) | N/A | No | - | MEASURE 2.11 |
| GC-14 | Privacy | Data minimized, privacy assessment, retention? | Retention 90 days; privacy review pending | Partial | Yes | Owen Achterberg | MEASURE 2.10; ISO A.7.4; OWASP LLM02:2026 |
| GC-15 | Human oversight | Per-action approval; override and stop? | Analyst decides every disposition; no consequential tools; token revocation stops it | Met | No | Mira Castellanos | MAP 3.5; MANAGE 2.4; ISO A.9.2 |
| GC-16 | Transparency | Users told it's AI; limits documented? | "AI-drafted - analyst review required" label on every comment | Met | No | Mira Castellanos | MEASURE 2.8; ISO A.8.2 |
| GC-17 | Logging and monitoring | Enough logged to reconstruct an incident; monitored? | Prompts, outputs, and tool calls in `ai_audit`; weekly report including analyst override rate. Model version not listed among logged fields (see GC-25) | Met | No | Owen Achterberg | MANAGE 4.1; ISO A.6.2.6, A.6.2.8 |
| GC-18 | AI incident response | Incident definition, evidence set, kill switch, rollback? | "Revoke the token"; no incident definition or evidence set; kill switch untested | Partial | Yes | Mira Castellanos | MANAGE 2.4, 4.3; ISO A.8.4 |
| GC-19 | Output handling | Outputs validated before downstream use? | Comments only, read by an analyst; nothing executes them | Met | No | Owen Achterberg | MEASURE 2.7; OWASP LLM10:2026 |
| GC-20 | Change management | Re-assessment triggers defined? | Section 13: new tool, model change, or phase 2 | Met | No | Owen Achterberg | GOVERN 1.5; ISO A.6.2.6 |
| GC-21 | Decommissioning | Retirement plan? | "Not addressed" | Gap | No (required at Tier 3) | Owen Achterberg | GOVERN 1.7; ISO A.6.1.3 |
| GC-22 | Training and AI literacy | Users trained? | Training delivered 2026-09-25, 9 of 9; attendance list referenced, not provided | Partial | No | Mira Castellanos | GOVERN 2.2; ISO 7.2 |
| GC-23 | Retrieval and knowledge-base security | Retrieval enforces source permissions; index changes controlled? | "No retrieval index" (section 5). Search runs as a tool under `svc-ai-triage` and is covered by GC-10 | N/A | No | - | MEASURE 2.7; OWASP LLM09:2026 |
| GC-24 | Explanation and recourse | Outcomes explainable and contestable? | None needed: the assistant does not make or shape decisions about people (see note) | N/A | No | - | MEASURE 2.9; MANAGE 4.1 |
| GC-25 | Model and component provenance | Component record, pinned version, provider change notice? | Provider and model named; no version or deployment ID; no provider change-notice commitment; the 2026-09-18 eval isn't tied to a version | Partial | No (see note) | Owen Achterberg | GOVERN 6.1; ISO A.4.2; OWASP LLM04:2026 |

GC-13 and GC-24 are N/A because the assistant doesn't score or decide about people. It
summarizes alerts for an analyst who does. Revisit both if phase 2 or any user-risk scoring
is added.

GC-25 is required at Tier 2, but the gap isn't blocking. It can't cause harm at launch: the
risk is that a later, unannounced provider update invalidates the evaluation. That makes it
a dated follow-up, due before the first model change.

Totals: 11 Met, 9 Partial, 2 Gap, 3 N/A (25 controls).

### Top risks
1. **Indirect prompt injection through alert fields** (GC-12). Attackers control much of what
   the assistant reads. Only one field has been tested, and search results haven't been tested
   at all. The impact is limited to misleading notes, because there are no action tools.
2. **Analysts over-trusting AI-drafted dispositions** (GC-15, GC-17). Draft-only design helps,
   and so does the weekly override-rate report, as long as someone reads it.
3. **Employee data sent to a vendor without reviewed terms** (GC-09, GC-14). The zero-retention
   claim is plausible but unverified.
4. **Scope creep to phase 2** (GC-20). Auto-close would make this A3 on a consequential action
   and move it to Tier 3. The change-management trigger covers it; keep it enforced.

### Required before go-live
| # | Mitigation | Closes | Owner | Verify by |
|---|---|---|---|---|
| 1 | Complete the privacy review and a short impact assessment on employee data in alerts | GC-04, GC-07, GC-14 | Owen Achterberg, Mira Castellanos | Signed review and assessment attached to AI-INV-0042 |
| 2 | Provide the ModelCo DPA and evidence that zero retention is enabled on this account. Confirm in writing that prompts and outputs aren't used for training, and get the sub-processor and incident notice terms | GC-09 | Owen Achterberg | Reviewer reads the documents |
| 3 | Run injection tests across every free-text alert field and against injected search results (for example, the `untrusted-content-guard` sample set) | GC-12 | Owen Achterberg | Results table with pass/fail per field |
| 4 | Add `svc-ai-triage` to the access review and confirm its scopes match the two listed tools | GC-10 | Owen Achterberg | Access-review worksheet row, certified |
| 5 | Write a one-paragraph AI incident definition (including suspected poisoning of alert or search data), list the evidence to preserve (input, context, output, model version, tool calls, invoking case), and test token revocation end to end | GC-18 | Mira Castellanos | Test record with time-to-disable |

### Follow-ups (non-blocking)
- GC-21: write a decommissioning plan (revoke token, delete `ai_audit` data per policy, retire inventory entry). Owner: Owen Achterberg. Before the 90-day review.
- GC-22: attach the training attendance list. Owner: Mira Castellanos. Within 2 weeks.
- GC-25: record the model version or deployment ID in the inventory and in `ai_audit`, ask ModelCo for advance notice of model changes, and tie the eval results to that version. Owner: Owen Achterberg. Within 2 weeks, and before any model change.

### Untrusted-content flags
None found. The intake form contains no instructions aimed at the reviewer or the AI.

### Open questions
- Do any alerts concern employees or contractors outside the United States?
- Were analysts already pasting alerts into unapproved AI tools before this request? If so, what data left?
- Who reads the weekly override-rate report, and what rate would trigger a review?
- Is the 90-day log retention consistent with the SOC's existing retention policy for alert data?
