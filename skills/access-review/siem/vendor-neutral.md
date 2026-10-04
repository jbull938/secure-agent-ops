# Other SIEMs: OCSF and generic webhooks

The events in [`example-events.json`](example-events.json) are plain JSON, so any SIEM or
data pipeline that accepts JSON can take them. Two common routes:

## Map to OCSF

The Open Cybersecurity Schema Framework (OCSF) has a class that fits access-review findings:
**IAM Analysis Finding** (`class_uid` 2008, Findings category). The OCSF schema was at version
1.9.0 when checked on 2026-10-04. A rough mapping (verify attribute names against the schema
version your platform uses):

| Access-review field | OCSF attribute (approximate) |
|---|---|
| `finding_id`, `signature`, `risk_message` | `finding_info.uid`, `finding_info.title`, `finding_info.desc` |
| `severity` | `severity_id` (2 Low, 3 Medium, 4 High) |
| `time` | `time` (epoch milliseconds) |
| `user`, `user_id`, `user_type` | user or identity object (`name`, `uid`, `type`) |
| `entitlements` | permission or policy details |
| `recommendation`, `recommendation_detail` | remediation description |
| `vendor_product`, `run_id` | `metadata.product.name`, `metadata.correlation_uid` |
| Everything else | `unmapped` |

If your platform doesn't support that class yet, Detection Finding (`class_uid` 2004) is a
common fallback.

## Generic webhook

Most SIEMs and SOAR tools accept an HTTPS webhook. Same rules as the Splunk example:

```bash
# Placeholders. The token comes from a secrets manager or environment variable, never the repo.
curl -sS "https://siem-ingest.example.com/webhook/access-review" \
  -H "Authorization: Bearer ${SIEM_WEBHOOK_TOKEN}" \
  -H "Content-Type: application/json" \
  --data-binary @example-events.json
```

- Send to a destination the SIEM owner approved, over TLS, with a token scoped to ingest only.
- Keep the events as notifications. The certification worksheet stays the audit evidence,
  and no automation downstream should revoke access without a human.
