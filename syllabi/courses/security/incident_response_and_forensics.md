---
tags:
  - concepts:security
  - concepts:operations
  - concepts:cryptography
  - concepts:network-security
  - concepts:observability
  - concepts:best-practices
level: advanced
category: security
duration_hours: 40
audience:
  - audiences:security-engineers
  - audiences:security-professionals
  - audiences:forensics-investigators
  - audiences:sres
  - audiences:devops
---
<!-- course: incident_response_and_forensics -->
# Security Incident Response and Forensics

## Description
A security incident is not the same as a production outage. The clock is different, the stakeholders are
different, and the wrong move in the first hour (rebooting a host, deleting a suspicious file, locking out an
attacker who is being watched) can destroy the evidence you need to understand what happened. This five day
course covers the discipline of responding to a security incident from detection through containment,
eradication, recovery and lessons-learned, with a parallel focus on the forensic skills that `make` any of it
possible.

The course covers the `IR` lifecycle (`NIST` and `SANS` frameworks), the legal and regulatory dimension,
evidence preservation across `Linux`, `Windows`, cloud and `Kubernetes`, malware triage, network and host
forensics, identity-attack investigation, breach timeline reconstruction, communications with executives,
customers and regulators, and the program-level practices that `make` a security `IR` capability actually work.
Participants leave able to lead a security incident, preserve evidence, and reconstruct what happened with
defensible rigor.

## Duration
40 hours / 5 days

## Intended Audience
* security engineers responding to incidents
* `SOC` analysts moving up into incident response
* forensics investigators expanding from one platform to multi-platform
* `SRE`s and `DevOps` engineers cross-training into security `IR`
* engineers establishing or rebuilding their organization's `IR` capability

## Prerequisites
* working knowledge of `Linux`, `Windows` and at least one cloud platform
* basic familiarity with `TCP`/`IP` networking and `HTTP`
* exposure to at least one `SIEM` or `EDR` platform
* basic scripting in `Python` or `PowerShell`

## Objectives
* describe the security `IR` lifecycle and operate within each phase
* preserve evidence on `Linux`, `Windows`, cloud and `Kubernetes` hosts
* triage malware safely
* reconstruct a breach timeline from logs and host artifacts
* lead an incident as the security `IC`
* communicate to executives, customers and regulators with care
* build the program-level `IR` capability for an organization

## Outline
<!-- chapter: a-security-incident-is-different, duration: 2h -->
* A security incident is different
    * outage vs security incident: clock, scope, evidence
    * confidentiality, integrity, availability and which is at stake
    * the cost of "let's just reboot"
    * the cost of "let's wait and watch"
    * how `IR` connects to threat hunting and detection engineering
<!-- chapter: the-ir-lifecycle, duration: 3h -->
* The `IR` lifecycle
    * `NIST 800-61` four-phase model
    * `SANS` six-phase model
    * preparation, identification, containment, eradication, recovery, lessons-learned
    * the difference between detection and identification
    * eradication done badly: persistence missed
    * recovery done badly: trust restored too soon
<!-- chapter: roles-and-the-ir-team, duration: 2h -->
* Roles and the `IR` team
    * the security `IC`
    * forensics, malware analysis, threat intel, comms, legal
    * relationship with the `SRE` `IC`
    * tabletop exercises and on-call rotation
    * outsourced `IR` retainers
<!-- chapter: legal-and-regulatory-context, duration: 2h -->
* Legal and regulatory context
    * chain of custody and evidence admissibility
    * `GDPR`, `HIPAA`, `PCI-DSS`, SOX, `SEC` disclosure
    * regulator notification timelines
    * working with law enforcement
    * the role of outside counsel
    * privilege and the "investigation memo"
<!-- chapter: detection-and-identification, duration: 2h -->
* Detection and identification
    * sources of detection: detections, hunts, third-party, victim
    * triage of an alert into an incident
    * scope estimation under uncertainty
    * the "is this an incident" decision
    * declaring early
<!-- chapter: containment-strategies, duration: 3h -->
* Containment strategies
    * short-term, long-term, full containment
    * network segmentation as a containment lever
    * disabling credentials without warning the attacker
    * cloud-account isolation
    * `Kubernetes` namespace and node containment
    * the silent containment vs the loud containment trade-off
<!-- chapter: evidence-preservation-fundamentals, duration: 3h -->
* Evidence preservation fundamentals
    * the order of volatility
    * imaging vs live triage
    * write blockers and their cloud equivalents
    * hashing and integrity proofs
    * timestamping and `NTP` reliability
    * documenting collection
    * preserving across reboots and snapshot deletions
<!-- chapter: linux-host-forensics, duration: 2h -->
* `Linux` host forensics
    * triage scripts: `Velociraptor`, GRR, `osquery`
    * `auditd` and `eBPF` artifacts
    * shell history and `.bash_history` caveats
    * `systemd` journal
    * persistence: `cron`, `systemd` units, `LD_PRELOAD`, kernel modules
    * memory acquisition with `LiME`/`AVML`
    * `Volatility` for memory analysis
<!-- chapter: windows-host-forensics, duration: 2h -->
* `Windows` host forensics
    * `Sysmon` and event logs
    * registry hives and `RegRipper`
    * `MFT`, `USN journal`, Prefetch, ShimCache, `AmCache`
    * `KAPE` for triage collection
    * `Velociraptor` on `Windows`
    * memory analysis with `Volatility`
    * persistence: `Run` keys, services, scheduled tasks, `WMI`
<!-- chapter: cloud-and-saas-forensics, duration: 2h -->
* Cloud and `SaaS` forensics
    * `CloudTrail`, `Cloud Audit Logs`, `Azure Activity Log`
    * `IAM` abuse and credential investigation
    * cloud snapshot-based forensics
    * `O365`/`Google Workspace` mailbox audit
    * `Okta` and `Entra ID` audit logs
    * the limits of cloud forensics: gaps in vendor logging
<!-- chapter: kubernetes-and-container-forensics, duration: 2h -->
* `Kubernetes` and container forensics
    * audit logs and what they capture
    * runtime logs from `Falco`, `Tetragon`
    * preserving an ephemeral pod
    * container image forensic analysis
    * node-level investigation
    * cluster takeover scenarios
<!-- chapter: network-forensics, duration: 2h -->
* Network forensics
    * `pcap` capture in incident-time
    * `Zeek`/`Bro` artifacts
    * `NetFlow` and traffic analysis
    * encrypted traffic and what you can still learn
    * lateral movement detection from network data
    * data exfiltration patterns
<!-- chapter: malware-triage, duration: 2h -->
* Malware triage
    * static analysis basics: strings, hashes, signatures
    * sandboxes: `Cuckoo`, `Joe Sandbox`, `Hatching Triage`
    * dynamic analysis safety
    * `YARA` rules for hunting
    * unpacking and obfuscation overview
    * deciding when to escalate to a malware analyst
<!-- chapter: identity-attack-investigation, duration: 2h -->
* Identity attack investigation
    * credential theft and reuse
    * `OAuth` consent phishing
    * session-token theft and replay
    * privilege escalation in cloud `IAM`
    * service-account abuse
    * `MFA` bypass techniques and how to spot them
<!-- chapter: timeline-reconstruction, duration: 3h -->
* Timeline reconstruction
    * the unified timeline as a deliverable
    * `log2timeline`/`plaso`
    * normalizing timestamps across timezones and sources
    * filling gaps with hypotheses, marked as such
    * the storyboard from initial access to objective
    * presenting the timeline to non-technical audiences
<!-- chapter: communications-during-and-after, duration: 2h -->
* Communications during and after
    * exec briefings: what to say and what to defer
    * customer notifications under regulation
    * regulator and law-enforcement comms
    * the public statement and the `PR` involvement
    * internal company-wide messaging
    * comms tone in a sensitive incident
<!-- chapter: post-incident-and-lessons-learned, duration: 2h -->
* Post-incident and lessons-learned
    * the security postmortem and the blamelessness question
    * tracking findings across teams
    * detection improvements driven by `IR`
    * controls improvements driven by `IR`
    * customer-facing reports
    * the long-term hardening project
<!-- chapter: program-and-tooling, duration: 1h -->
* Program and tooling
    * `IR` platforms: `IBM Resilient`, Demisto/`Cortex XSOAR`, custom
    * runbooks and playbooks for common incident types
    * tabletop exercises and red-team-driven drills
    * retainers, retainers, retainers
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * tabletop exercise: simulated breach end-to-end
    * group review of a published breach disclosure
    * recommended reading: `SANS` papers, `Mandiant` reports

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
