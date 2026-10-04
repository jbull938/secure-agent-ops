# evals

Test cases, expected outputs, and notes on where the model gets it wrong. Each file lists
global criteria, per-case pass and fail criteria, and a results log.

- [`soc-alert-triage.md`](soc-alert-triage.md): six alerts covering a true positive, benign admin activity, a false positive, an ambiguous sign-in, an RBA aggregate, and a prompt injection in an alert field
- [`untrusted-content-guard.md`](untrusted-content-guard.md): seven content samples covering two false-positive traps (a newsletter and a security article) and five injection techniques (hidden email text, hidden web text, a tool-output `system` field, base64, and a forged delimiter)
- [`access-review.md`](access-review.md): 24 cases covering every planted issue in the access-review sample data (leavers, orphans, movers, excessive and unused privilege, SoD conflicts, shared and service accounts, stale tokens, AI agent scopes, MFA, reviewer independence, and an injection in a notes field), plus clean-row and data-gap traps and two checks that SIEM JSON events are valid and match the worksheet
- [`ai-governance-checklist.md`](ai-governance-checklist.md): five intake forms covering a low-risk summarizer (false-positive trap), an autonomous email and ticket agent with an injection in its notes, a customer-facing chatbot, a resume-screening tool, and a retrieval assistant over an editable wiki, plus the worked example and a GRC JSON check
- [`draft-before-send.md`](draft-before-send.md): six outbound scenarios covering a clean internal reply (false-positive trap), a planted injection with a lookalike domain, a recipient-list expansion after approval, a declined post with pressure to switch channels, a routine trying to use a standing permission, and an out-of-office, mass-send, and sensitive-data request, plus the worked example and an audit-event check
