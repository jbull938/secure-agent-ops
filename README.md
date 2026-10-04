# secure-agent-ops

**Security-first patterns for running AI agents, built by a SOC and SIEM practitioner.**

I'm Justin Bull, a CISSP and security product architect focused on Splunk Enterprise Security and SOC delivery. Earlier in my career I spent years in identity and access management and compliance (PCI-DSS, SOX, HIPAA, GLBA), and those principles still shape how I think about security.

AI agents are a new kind of privileged identity. They read untrusted content, call tools, and act on someone's behalf. This repo applies classic security controls to them: least privilege, separation of duties, human approval for risky actions, and audit-ready evidence.

It documents how I design and run a small personal multi-agent assistant safely, and it shares reusable security skills you can try yourself.

## What's here

| Folder | What it holds |
|---|---|
| `docs/` | The operating model (roles, routing, memory, guardrails) and a threat model mapped to the OWASP Top 10 for LLM Applications and MITRE ATLAS |
| `skills/` | Reusable skills in the open Agent Skills (`SKILL.md`) format |
| `agents/` | One role card per agent: purpose, allowed tools, and when it must escalate to a human |
| `guardrails/` | Policy files: approval matrix, tool allowlist, stop conditions |
| `sample-data/` | Synthetic alerts, access exports, and emails, all clearly fake |
| `evals/` | Test cases, expected outputs, and notes on where the model gets it wrong |

## Roadmap

- [ ] Operating model and threat model
- [ ] Skill: SOC alert triage (Splunk ES-style, sample data)
- [ ] Skill: untrusted content and prompt-injection guard
- [ ] Skill: access review and least-privilege audit
- [ ] Skill: AI governance checklist (NIST AI RMF, ISO/IEC 42001)
- [ ] Skill: draft-before-send for outbound messages

## Ground rules

- **Synthetic data only.** Nothing here comes from any employer, customer, or real person.
- **Every skill documents its failure modes.** Knowing where an agent breaks matters as much as the demo.
- **No secrets in the repo.** Every push is scanned automatically.

This is a personal project built on my own time and equipment. It isn't affiliated with or endorsed by my employer.

## License

MIT
