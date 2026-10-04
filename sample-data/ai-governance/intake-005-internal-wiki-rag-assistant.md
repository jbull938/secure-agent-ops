> SYNTHETIC SAMPLE for secure-agent-ops. Not real data. The company, people, vendor, and domains (example.com) are fictional.

# AI use case intake form

**Company:** Fernhill Freight (fictional)
**Submitted:** 2026-10-01 by Dana Whitcombe (fictional), Operations Excellence
**System name:** Ask Ops
**Inventory ID:** none yet
**New or expansion:** New

## 1. Owners
- Business owner: Dana Whitcombe (fictional), Director of Operations Excellence
- Technical owner: Felix Amadi (fictional), Internal Tools
- Risk approver: Dana Whitcombe (fictional). "As the business owner I'll sign off so we can move fast."

## 2. Purpose and users
Chat assistant that answers employee questions ("what's the process for a damaged-freight
claim?", "who approves overtime in the Leeds depot?") from internal content. About 1,400
employees in the United Kingdom and Ireland. Answers include links and inline images from the
source pages.

Out of scope: taking actions, editing content, answering customers.

## 3. Self-assessed risk
"Low. Read-only, internal, no tools."

## 4. Model and vendor
Hosted model and embedding model from ModelCo (fictional) via our enterprise account, using
the provider's "latest" model alias. DPA signed 2026-05-02 (attached): no training on our
data, 30-day retention for abuse monitoring. No commitment on notice before model changes.

## 5. Data
- Retrieval index built from:
  - the company wiki (any employee can create or edit pages; edits publish immediately)
  - the shared drive folders "Ops", "HR Policies", and "Finance Shared", crawled by the
    service account `svc-askops`, which has read access to all three folders, including
    subfolders that hold individual performance reviews and salary bands
- Index rebuilt nightly by a scheduled job. Changes to the crawl list are made by the Internal
  Tools team without review.
- Questions and answers logged for 60 days. Retrieved document IDs are not logged.

## 6. Tools and permissions
None beyond retrieval. The assistant runs as `svc-askops` for every user. It doesn't check
whether the asking employee could open the source document.

## 7. Testing
- Answer quality: 200 sample questions, 88% rated helpful by the Ops team (sheet attached).
- Security: direct prompt-injection tests typed into the chat (12 prompts, all refused).
  No tests through wiki or drive content.

## 8. Human oversight
Employees read the answer and decide what to do. A feedback button flags bad answers to
the Internal Tools team.

## 9. Transparency and training
The chat window says "Ask Ops is an AI assistant and can be wrong." No user training planned.

## 10. Policy fit
AI Acceptable Use Standard v1.0, section 3: internal assistants are allowed with risk approval.

## 11. Monitoring and incidents
Usage dashboard and the feedback queue. Disable by turning off the chat widget. No AI
incident definition.

## 12. Legal and privacy
Not reviewed yet. "It only reads what we already have."

## 13. Change management
Not addressed.

## 14. Decommissioning
Delete the index and turn off the widget.

## Notes
Several teams already paste wiki pages into a free consumer chatbot. Ask Ops is meant to
replace that.
