# Splunk Enterprise Security: detections, risk, and a dashboard

Example ways to turn access-review findings into Splunk Enterprise Security (ES) content.
**All SPL here is an untested example.** Index names, field names, thresholds, and
scheduling must be adjusted to your environment and checked before use.

## Terminology (ES 8.x, with older names)

ES 8.0 renamed much of the content model. This repo uses the 8.x names.

| ES 8.x | Before 8.0 |
|---|---|
| Event-based detection | Correlation search (also "risk rule" when it only writes risk) |
| Finding-based detection | Risk incident rule |
| Finding | Notable event (and "risk notable") |
| Intermediate finding (stored in the risk index; not shown in the analyst queue) | Roughly, a risk event |
| Finding group | Notable created from aggregated risk |
| Entity (in a finding) | Risk object |
| Analyst queue in Mission Control | Incident Review |
| Investigation | ES investigation or Mission Control incident |

Field names such as `risk_object`, `risk_object_type`, and `risk_score` are still used in
the risk index. Checked against Splunk's ES 8.x documentation on 2026-10-04 (8.6 is the
latest documented release); recheck for your version.

## Approach

Two patterns. Pick one; don't run both on the same events, or you'll double-count.

1. **Direct findings for High items.** An event-based detection creates a finding for each
   new High access-review event. Simple, and good for a short list of urgent items such as
   "leaver still active, login after end date".
2. **Risk-based alerting (recommended).** An event-based detection writes every
   access-review finding as an intermediate finding (risk) on the identity. A finding-based
   detection raises a finding group when an identity's risk crosses a threshold, or when
   access-review risk joins other risk on the same identity (for example, a leaver account
   that also shows up in an authentication detection). This is where an access review
   becomes useful to the SOC.

In both, `risk_object` is the user or agent identity (`user` in the events), and
`risk_object_type` is `user`. Add AI agents and service accounts to the ES identity lookup
(for example, with a category of `ai_agent` or `service_account`) so they get owners,
priority, and correlation like people do.

## Event-based detection: High findings (untested example)

Schedule after each review run. Set the action to create a finding (pattern 1), or to create
intermediate findings with the risk analysis action using `risk_object`, `risk_object_type`,
and `risk_score` from the results (pattern 2; in that case remove the `severity` filter).

```spl
index=<your_access_review_index> sourcetype="secure_agent_ops:access_review"
    event_type=access_review_finding severity=high
| dedup finding_id
| eval risk_object=coalesce(risk_object, user),
       risk_object_type=coalesce(risk_object_type, "user"),
       finding_title="Access review: ".signature." - ".user
| table _time run_id finding_id app user user_type owner signature signature_id
        severity risk_score risk_object risk_object_type risk_message recommendation
        refer_to_security control_refs{} row_ids{}
```

Suggested settings: throttle on `finding_id` so a rerun doesn't duplicate findings; map
`annotations.mitre_attack` to the detection's MITRE annotations where present (for example,
T1078 for leaver and orphaned access).

## Finding-based detection: risk threshold per identity (untested example)

Most teams build this in the finding-based detection editor. The equivalent search, for
reading or testing:

```spl
index=risk risk_object_type=user earliest=-30d
| stats sum(risk_score) as total_risk
        dc(source) as detection_count
        values(source) as detections
        values(signature) as signatures
        by risk_object
| where total_risk >= 100 OR (detection_count >= 2 AND match(mvjoin(detections, "|"), "(?i)access review"))
```

The second condition catches an identity with access-review risk plus risk from any other
detection, which is often the more interesting case.

## Investigating in Mission Control

- Findings and finding groups land in the **analyst queue** in Mission Control. Start an
  **investigation** for anything marked `refer_to_security=true`.
- Pivot from the entity to the authentication and change data for the same identity. For
  example, did `hana.yoshida` sign in anywhere else after 2026-09-12?
- Add the review's `run_id` and the worksheet location as a **note** on the investigation, so
  the access decision and the security investigation point at the same evidence.
- Access changes still go through the access owner and the system of record. Any response
  plan or automation that would disable an account needs human approval; the agent that
  produced the finding doesn't run it.

## Dashboard panel: latest run (untested example)

```spl
index=<your_access_review_index> sourcetype="secure_agent_ops:access_review"
    event_type=access_review_finding
| eventstats latest(run_id) as latest_run
| where run_id=latest_run
| eval sev_rank=case(severity="high",1, severity="medium",2, severity="low",3)
| stats count as findings dc(user) as identities by sev_rank severity signature recommendation
| sort sev_rank - findings
| fields - sev_rank
```

A second panel for the run summary:

```spl
index=<your_access_review_index> sourcetype="secure_agent_ops:access_review"
    event_type=access_review_summary
| head 1
| table run_id review_as_of rows_reviewed identities_with_findings high_risk_identities
        recommendations.keep recommendations.revoke recommendations.modify
        recommendations.needs_owner_decision certification_status
```
