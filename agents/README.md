# Agents

One role card per agent. A card is the public least-privilege boundary for that role: what it is for, which tools it may use without asking, what it must ask about first, and what it never does. A private permission review can be stricter than a card. It cannot be looser.

The assistant roster is ten roles. A coding agent on the owner's workstation is separate: it does not read mail and it is not in the routing diagram as an inbox owner. See [How work is handed to the coding agent](../docs/operating-model.md#handoff-to-the-coding-agent).

| Role | Card | One job |
|---|---|---|
| Chief (router) | [`chief.md`](chief.md) | Classify the request, name one owner, track open work |
| Executive assistant | [`executive-assistant.md`](executive-assistant.md) | Triage mail and calendar, label, draft |
| Finance | [`finance.md`](finance.md) | Track spending and bills; propose, never write the books |
| Music admin | [`music-admin.md`](music-admin.md) | Keep the music library organized |
| Career | [`career.md`](career.md) | Resumes, applications, and drafts |
| Tax | [`tax.md`](tax.md) | Deadlines and checklists; the owner files |
| LLC books | [`llc-books.md`](llc-books.md) | Side-business records; the owner files and pays |
| Engineering | [`engineering.md`](engineering.md) | Notes on the home network and servers; the owner changes them |
| Home sale | [`home-sale.md`](home-sale.md) | Transaction checklists and drafts; the owner signs |
| Fitness | [`fitness.md`](fitness.md) | Schedule and habit reminders, with no health details in memory |
| Coding agent | [`coding-agent.md`](coding-agent.md) | Implement an approved brief on the workstation |

Shared rules live in [`guardrails/`](../guardrails/) and in the [operating model](../docs/operating-model.md).
