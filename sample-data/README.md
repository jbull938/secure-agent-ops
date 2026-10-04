# sample-data

Synthetic inputs for trying the skills. Every file is fictional: names are made up, domains
use `example.com`, `example.net`, and `example.org`, and IP addresses use the RFC 5737
documentation ranges. Each file is marked as a synthetic sample.

## `alerts/` - for [`soc-alert-triage`](../skills/soc-alert-triage/SKILL.md)

- `alert-001-lsass-credential-dumping.json`: credential dumping from a downloaded script (true positive)
- `alert-002-admin-psexec-patching.json`: admin PsExec run that matches an approved change (benign)
- `alert-003-noisy-dga-rule.json`: DGA rule firing on fleet telemetry subdomains (false positive)
- `alert-004-new-country-signin.json`: impossible-travel sign-in with an approved MFA push (ambiguous)
- `alert-005-rba-risk-threshold.json`: risk-based alerting aggregate that tells one attack story
- `alert-006-sqli-with-prompt-injection.json`: SQL injection with a prompt injection in the user agent

## `untrusted/` - for [`untrusted-content-guard`](../skills/untrusted-content-guard/SKILL.md)

- `content-001-benign-newsletter.md`: club newsletter with normal requests to the reader (clean)
- `content-002-security-blog-quoting-injection.md`: security article that quotes injection strings as examples (clean, quoted)
- `content-003-phishing-email-hidden-instruction.html`: storage-full phishing email with a hidden instruction to the AI
- `content-004-webpage-hidden-instructions.html`: product review with instructions in an HTML comment and white-on-white text
- `content-005-tool-response-injected-system-field.json`: package-tracking API response with an injected `system` field
- `content-006-support-ticket-base64.json`: help-desk ticket with a base64-encoded instruction
- `content-007-forged-delimiter.txt`: planning notes with a forged end-of-data marker and a fake user turn

The files in `untrusted/` contain prompt-injection text on purpose. Don't point an agent with
real send, share, or delete tools at them outside a test harness.
