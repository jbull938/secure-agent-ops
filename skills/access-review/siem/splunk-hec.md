# Sending access-review findings to Splunk with HEC

How to send the skill's JSON events to Splunk through the HTTP Event Collector (HEC). This is
an example, not a tested integration. Host, token, index, and port are placeholders.

[`example-events.json`](example-events.json) holds five finding events and the run summary,
built from the synthetic sample data. A full run of the sample data produces one event per
finding (18 identities have findings, some with more than one check) plus the summary.

## Before you start

- A HEC token created for this purpose only, allowed to write to one index (for example, an
  `access_review` index), with a default sourcetype of `secure_agent_ops:access_review`.
- TLS on the HEC endpoint. Don't turn off certificate checks (`-k`) outside a lab.
- Approval from the person who owns the SIEM to send data there. Sending findings is a write
  to an external system, so it follows the approval rules in
  [`docs/operating-model.md`](../../../docs/operating-model.md).

## Token hygiene

- **Never commit a token.** Not in scripts, notebooks, `.env` files, or sample commands. This
  repo's secret scan will fail the push, and that's the point.
- Read the token from an environment variable or a secrets manager at run time:
  `export SPLUNK_HEC_TOKEN="$(your-secrets-cli get hec/access-review)"`.
- Scope it to one index and one sourcetype, and rotate it on a schedule.
- Keep the token out of logs. Don't run the curl command with `-v` in a shared terminal.

## Send the events

HEC's `/services/collector/event` endpoint takes one or more JSON objects, each with an
`event` payload and optional metadata. For a batch, send the objects one after another (not
as a JSON array). This converts the example file and sets `time` from each event:

```bash
# Placeholders. Set these in your shell or CI secrets, never in the repo.
export SPLUNK_HEC_HOST="splunk-hec.example.com"
export SPLUNK_HEC_TOKEN="<token-from-your-secrets-manager>"
export SPLUNK_INDEX="<your_access_review_index>"

jq -c --arg idx "$SPLUNK_INDEX" '.[] | {
    time: (.time | fromdateiso8601),
    host: "access-review-agent",
    source: "secure-agent-ops:access-review",
    sourcetype: "secure_agent_ops:access_review",
    index: $idx,
    event: .
  }' example-events.json > hec-batch.json

curl -sS "https://${SPLUNK_HEC_HOST}:8088/services/collector/event" \
  -H "Authorization: Splunk ${SPLUNK_HEC_TOKEN}" \
  -H "Content-Type: application/json" \
  --data-binary @hec-batch.json
```

A successful send returns `{"text":"Success","code":0}`. Delete `hec-batch.json` afterward
if it holds real data.

## Check that it landed (example SPL, untested)

```spl
index=<your_access_review_index> sourcetype="secure_agent_ops:access_review"
| stats count by event_type severity
```

The events are JSON, so search-time field extraction usually works with `KV_MODE = json` on
the sourcetype. Adjust to your environment.

## Human in the loop

Sending findings to a SIEM is fine. It is notification, not action. The agent still never
revokes, disables, rotates, or changes access, and it doesn't triage or close the SIEM
findings it created. A named reviewer certifies the worksheet, and changes happen in the
system of record.
