# Worked example: output

This is the expected output for [`example-input.json`](example-input.json), written in the
skill's output template. All data is synthetic.

---

## Triage: SYN-2026-0100 - Endpoint - Scheduled Task Created Pointing to User-Writable Path - Rule

**Recommended disposition:** Investigate
**Priority:** P3   **Confidence:** Medium - the behavior fits both a per-user software updater and a common persistence method, and the provided context can't tell them apart.
**Decision owner:** Analyst. This is a recommendation; no actions have been taken.

### Summary
A signed installer that the user ran from their Downloads folder created a daily scheduled task
that runs `update.exe` from the user's AppData folder. Per-user apps often install updaters this
way, but the publisher is not on the provided approved-publisher list, and the same pattern is a
common persistence technique. Nothing in the input shows malicious follow-on activity, but nothing
rules it out either.

### Key fields (normalized)
| Field | Value |
|---|---|
| Time | 2026-09-30T15:22:10Z (UTC; 10:22 local per the asset's America/Chicago time zone, business hours) |
| Host | ws-hr-019.corp.example.com (198.51.100.19) |
| User | CORP\lgarcia-example (not privileged) |
| Process | `schtasks.exe /create /tn "ExampleNotesUpdater" /tr "C:\Users\lgarcia-example\AppData\Local\ExampleNotes\update.exe" /sc daily /st 09:00` |
| Parent | `C:\Users\lgarcia-example\Downloads\ExampleNotesSetup.exe` |
| Parent signature | signed: ExampleNotes Software Ltd (fictional) |
| Rule ATT&CK annotation | T1053.005 |
| Missing | Hash and signature of `update.exe`, network activity, download source of the installer |

### Context used
- Provided: asset (HR workstation, medium priority), identity (HR, not privileged), approved software publisher list.
- Not provided: software request or ticket for ExampleNotes, where the installer was downloaded from, any network or process activity after task creation.

### MITRE ATT&CK mapping
| Tactic | Technique | Evidence (field) | Confidence |
|---|---|---|---|
| Persistence, Execution | T1053.005 Scheduled Task/Job: Scheduled Task | `process` creates a daily task with `/tr` pointing to AppData | High that the technique occurred; Low that it is malicious |
| Execution | T1204.002 User Execution: Malicious File | `parent_process_path` in Downloads | Low (inferred; only applies if the installer is malicious) |

### Risk assessment
- Impact: Medium. HR workstation likely has access to personnel data (inferred from business unit). User is not privileged.
- Likelihood: Low to medium. Observed: signed parent, descriptive task name matching the parent app, business-hours timing. Observed: publisher not on the approved list, target binary in a user-writable path.
- Observed vs inferred: the signature, paths, and approved list are observed. "Looks like a normal updater" is inferred.

### Known-benign check
- Matches the general shape of a per-user app updater (task name matches app, signed installer, daily schedule).
- Does **not** match the provided approved-publisher list.
- No change record or software request was provided.
- The installer's signature says nothing about `update.exe`, which could be a different file.
- To support closing as benign: confirm the software request, check that `update.exe` is signed by the same publisher, and check that it makes no unexpected network connections.

### Untrusted-content flags
None found. Free-text fields (`process`, `parent_process_path`, `description`) contain no instructions.

### Recommended next steps
1. Check `update.exe` signature and hash against the installer's publisher (pivot 1).
2. Review process and network activity on the host for 24 hours after 15:22Z (pivots 1 and 2).
3. Find where the installer came from (proxy logs for the download, pivot 3).
4. Ask the user or their manager whether ExampleNotes was requested. If it is wanted but unapproved, route it to the software approval process, not the SOC.
5. If any pivot shows unexpected network beacons or child processes, re-triage as Escalate.

### Example pivot searches (examples only; adjust to your environment)

What did `update.exe` and its children do on this host?
```spl
| tstats summariesonly=true count min(_time) as first_seen max(_time) as last_seen
  from datamodel=Endpoint.Processes
  where Processes.dest="ws-hr-019.corp.example.com"
    (Processes.process_name="update.exe" OR Processes.parent_process_name="update.exe")
  by Processes.process_name Processes.parent_process_name Processes.process Processes.process_hash
```

Did the host make new outbound connections after the task was created?
```spl
| tstats summariesonly=true count values(All_Traffic.dest_port) as ports
  from datamodel=Network_Traffic.All_Traffic
  where All_Traffic.src="ws-hr-019.corp.example.com" earliest="09/30/2026:15:00:00"
  by All_Traffic.dest
| sort - count
```

Where was the installer downloaded from?
```spl
index=proxy src="ws-hr-019.corp.example.com" url="*ExampleNotesSetup*"
| table _time src user url status bytes_in
```

### Open questions
- Was ExampleNotes requested or approved through any channel?
- Is `update.exe` signed by the same publisher as the installer?
- Has this task or binary appeared on other hosts?
