# evals

Test cases, expected outputs, and notes on where the model gets it wrong. Each file lists
global criteria, per-case pass and fail criteria, and a results log.

- [`soc-alert-triage.md`](soc-alert-triage.md): six alerts covering a true positive, benign admin activity, a false positive, an ambiguous sign-in, an RBA aggregate, and a prompt injection in an alert field
- [`untrusted-content-guard.md`](untrusted-content-guard.md): seven content samples covering two false-positive traps (a newsletter and a security article) and five injection techniques (hidden email text, hidden web text, a tool-output `system` field, base64, and a forged delimiter)
