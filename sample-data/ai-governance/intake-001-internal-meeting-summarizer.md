> SYNTHETIC SAMPLE for secure-agent-ops. Not real data. The company, people, vendor, and domains (example.com) are fictional.

# AI use case intake form

**Company:** Larkspur Analytics (fictional)
**Submitted:** 2026-09-30 by Tomas Reyna (fictional), IT Collaboration Services
**System name:** Meeting Notes Summarizer
**Inventory ID:** AI-INV-0107
**New or expansion:** New

## 1. Owners
- Business owner: Grace Oyelaran (fictional), Director of Operations
- Technical owner: Tomas Reyna (fictional), IT Collaboration Services
- Risk approver: AI Review Board

## 2. Purpose and users
Summarizes transcripts of internal meetings into decisions and action items. The meeting
organizer reviews and edits the summary before sharing it. Users: about 120 employees in
Operations. People affected: meeting attendees (employees only). External meetings are
excluded by a calendar rule.

Out of scope: customer calls, HR or legal meetings (blocked by meeting label), any automatic sharing.

## 3. Self-assessed risk
Low.

## 4. Model and vendor
Built-in AI feature of our existing meeting platform from ConferCo (fictional), covered by
the master agreement. Vendor AI addendum attached (`ConferCo-AI-Addendum-2026.pdf`): customer
content is not used for training; transcripts and summaries are retained per our tenant
retention setting (30 days).

## 5. Data
Internal meeting transcripts (employee names and work topics). No customer data. No
training, fine-tuning, or retrieval index. Summaries stored in the meeting record; deleted
with the transcript at 30 days.

## 6. Tools and permissions
None. The feature produces text in the meeting record. It can't send, share, or edit anything else.

## 7. Testing
Pilot with 15 users from 2026-08-01 to 2026-08-29. Organizers rated 41 of 46 summaries
"accurate, minor edits"; 5 had a wrong owner on an action item. Results sheet attached.

## 8. Human oversight
The organizer must open and approve the summary before it's visible to attendees.

## 9. Transparency and training
Summaries carry an "AI-generated summary - reviewed by <organizer>" footer. A one-page
guide was sent to all users on 2026-09-15.

## 10. Policy fit
AI Acceptable Use Standard v1.2, section 3.2: "Permitted: summarization of internal content
with human review before distribution."

## 11. Monitoring and incidents
Admins can turn the feature off tenant-wide in under 5 minutes (tested 2026-08-20). Issues
go to the IT service desk with the "AI" category. Monthly report on usage and edit rates.

## 12. Legal and privacy
Privacy team reviewed on 2026-09-10: no new processing beyond existing transcript retention;
note attached. Regions: United States and Canada.

## 13. Change management
New data sources, external meetings, or automatic sharing require a new assessment.

## 14. Decommissioning
Not yet written.
