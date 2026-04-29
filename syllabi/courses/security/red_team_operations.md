---
tags:
  - concepts:security
  - concepts:network-security
  - concepts:operations
  - concepts:best-practices
level: advanced
category: security
duration_hours: 40
audience:
  - audiences:security-engineers
  - audiences:penetration-testers
  - audiences:management
  - audiences:senior-developers
---
<!-- course: red_team_operations -->
# Red Team Operations

## Description
Red team operations are end-to-end adversary emulation engagements: instead of finding a vulnerability and
reporting it, a red team simulates a real attacker over a sustained period to test the organization's
ability to detect and respond. The catalog has `Network Penetration Testing`, `Web Application Penetration
Testing`, and `Threat Hunting and Detection Engineering` courses. None of those is the same as a red team
engagement. A pen test answers "is this thing exploitable" — a red team answers "if a real attacker gets
in, would we know."

This five day course covers red team operations as practiced today. It covers the engagement lifecycle
(rules of engagement, scope, objectives, communication plan), threat-actor emulation and the `MITRE ATT&CK`
mapping, the operational security of the red team itself, infrastructure setup (`C2` `redirectors`,
phishing infrastructure, payload hosting), the kill chain from initial access through actions on
objectives, the relationship to purple-team exercises, the deliverable that actually changes blue-team
behavior, and the legal and ethical perimeter. Tools covered include `Cobalt Strike`, `Sliver`,
`Mythic`, `Havoc`, `BloodHound`, `Impacket`, and the modern open-source `C2` ecosystem. Participants
leave able to plan, execute, and report on a red team engagement against an authorized target.

> This course assumes authorized engagements only. Lab work is performed in dedicated lab environments
> against systems the participant owns or is contractually authorized to test. Discussion of techniques
> is for defensive understanding and authorized offensive use only.

## Duration
40 hours / 5 days

## Intended Audience
* security engineers moving from pen testing into red team work
* internal red teams scaling up their practice
* security managers commissioning red team engagements
* senior developers who want to understand how attackers actually operate

## Prerequisites
* completion of `Network Penetration Testing` and `Web Application Penetration Testing` or equivalent
* working familiarity with `Linux`, `Windows`, `Active Directory`
* exposure to the `Cyber Threats and Attack Vectors` course
* employer authorization to use these techniques

## Objectives
* plan a red team engagement end-to-end
* map techniques to the `MITRE ATT&CK` matrix
* set up red team infrastructure that survives an engagement
* execute the kill chain against an authorized target
* operate with `OPSEC` discipline
* deliver a report that changes blue-team behavior
* understand the legal and ethical perimeter

## Outline
<!-- chapter: red-team-versus-pen-test, duration: 2h -->
* Red team versus pen test
    * the question each answers
    * scope, time, stealth, objectives
    * the cost difference and the value difference
    * cross-reference to the `Network Penetration Testing` course
    * cross-reference to the `Web Application Penetration Testing` course
    * `when` an organization is ready for a red team
<!-- chapter: the-engagement-lifecycle, duration: 3h -->
* The engagement lifecycle
    * rules of engagement
    * scope and target lists
    * out-of-scope and the no-`go` list
    * the communication plan and the trusted agent
    * the white card and the get-out-of-jail letter
    * the engagement debrief
<!-- chapter: threat-actor-emulation-and-mitre-attack, duration: 3h -->
* Threat-actor emulation and `MITRE ATT&CK`
    * the `ATT&CK` matrix as the common language
    * choosing the threat actor to emulate
    * tactics, techniques, procedures
    * the `ATT&CK Navigator`
    * cross-reference to the Threat Hunting course
    * the deliverable as `ATT&CK` coverage
<!-- chapter: red-team-infrastructure, duration: 4h -->
* Red team infrastructure
    * the team server, the redirector, the payload host
    * domain fronting and category-aged domains
    * the burnable infrastructure principle
    * `OPSEC` of the infrastructure
    * `Cobalt Strike` infrastructure as the canonical example
    * the cost shape of running this infrastructure
<!-- chapter: c2-frameworks, duration: 3h -->
* `C2` frameworks
    * `Cobalt Strike`
    * `Sliver`
    * `Mythic`
    * `Havoc`
    * `Brute Ratel` (commercial)
    * picking a framework
<!-- chapter: initial-access, duration: 3h -->
* Initial access
    * phishing as the dominant vector
    * social engineering with explicit authorization
    * the public-facing exploit case
    * the supply-chain case
    * the assumed-breach starting point
<!-- chapter: payload-development-and-evasion, duration: 4h -->
* Payload development and evasion
    * the modern endpoint-detection landscape
    * the "off-the-shelf payload was caught" reality
    * loaders, droppers, and the chain
    * the in-memory execution argument
    * `BYOVD` and signed-driver abuse
    * the ethics of evasion in an authorized engagement
<!-- chapter: post-exploitation-and-active-directory, duration: 4h -->
* Post-exploitation and `Active Directory`
    * `BloodHound` and the path to domain admin
    * `Kerberoasting`, `AS-REP roasting`
    * `NTLM` relaying
    * `Impacket` and the `Python` toolkit
    * the "we got domain admin in 30 minutes" engagement
    * cross-reference to the Identity and Access Management course
<!-- chapter: lateral-movement, duration: 3h -->
* Lateral movement
    * legitimate-looking lateral movement
    * `WMI`, `PsExec`, `WinRM`, `SSH`
    * the noisy vs the quiet method
    * pivoting through bastions
    * the cloud-pivot from on-prem credentials
<!-- chapter: actions-on-objectives, duration: 2h -->
* Actions on objectives
    * the agreed objective
    * data exfiltration in a controlled way
    * the "we proved we could exfiltrate" deliverable
    * the destructive-test exclusion
    * the "we accidentally took down production" failure
<!-- chapter: opsec-for-the-red-team, duration: 3h -->
* `OPSEC` for the red team
    * the red team as the target of the blue team
    * artefact hygiene
    * the timestamp problem
    * the "we burned the engagement on day one" failure
    * the "blue team owned our team server" failure
<!-- chapter: purple-team-exercises, duration: 2h -->
* Purple team exercises
    * the collaborative variant
    * the value to the blue team
    * the value to the red team
    * structuring a purple team day
    * cross-reference to the Detection Engineering course
<!-- chapter: reporting-that-changes-behavior, duration: 2h -->
* Reporting that changes behavior
    * the executive summary
    * the timeline of compromise
    * the detection-gap analysis
    * the prioritized remediation list
    * the report that gets shelved vs the one that drives change
<!-- chapter: legal-and-ethical-perimeter, duration: 2h -->
* Legal and ethical perimeter
    * authorization in writing
    * scope creep and the discovered-asset
    * personal data and the `GDPR` constraint
    * cross-reference to the `GDPR` and Compliance course
    * what to do `when` the engagement uncovers a real intrusion

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
