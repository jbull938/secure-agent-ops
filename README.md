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

## How to use these skills

Each skill is a folder with a `SKILL.md` file: plain-language instructions an AI assistant follows. There are three ways to use one, from simplest to most integrated:

1. **Paste it into any AI chat.** Copy the contents of a skill's `SKILL.md` into the chat assistant of your choice, then give it an input (for example, one of the sample alerts) and ask it to run the skill. No setup is needed, but you'll paste it again in each new chat.
2. **Install it in a tool that supports Agent Skills.** Many agent tools can load skill folders directly. Download the skill's folder (or the whole repo) and add it to your tool's skills location, following that tool's documentation. The assistant then uses the skill automatically when a request matches the `description` at the top of `SKILL.md`.
3. **Wire it into a workflow.** Teams can run a skill inside an automated pipeline, such as drafting a triage note for each new SIEM alert for an analyst to review. Keep a human in the loop: every skill here recommends, and none acts on its own.

**Try it on sample data first.** Run a skill against the files in `sample-data/`, then compare the results to the test cases in `evals/` before trusting it with anything real. Never paste real customer, employer, or personal data into a tool your organization hasn't approved.

## Roadmap

- [ ] Operating model and threat model
- [x] Skill: SOC alert triage (Splunk ES-style, sample data)
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
