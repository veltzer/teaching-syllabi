---
tags:
  - concepts:security
  - concepts:network-security
  - concepts:observability
  - concepts:operations
  - concepts:best-practices
level: advanced
category: security
duration_hours: 40
audience:
  - audiences:security-engineers
  - audiences:security-professionals
  - audiences:developers
  - audiences:senior-developers
---
<!-- course: threat_hunting_and_detection_engineering -->
# Threat Hunting and Detection Engineering

## Description
Modern defense is not "buy a `SIEM`, hope for the best." It is the engineering discipline of building, tuning and
maintaining detections, and the investigative discipline of hunting for threats that detections did not catch.
This five day course covers both, end to end.

The course covers the threat landscape and the `MITRE ATT&CK` framework as a shared language, the data sources
defenders rely on, the engineering practice of writing and tuning detections, the economics of false positives,
threat-hunting methodology and `hypothesis`-driven investigation, the tooling ecosystem (`Splunk`, `Elastic`,
`Sigma`, `Sumo Logic`, `Sentinel`, `Chronicle`, custom data lakes), and the team practices that turn detection
engineering and threat hunting into a continuous improvement loop. Participants leave able to write good
detections, run productive hunts, and contribute to a defensive program rather than just consume alerts from one.

## Duration
40 hours / 5 days

## Intended Audience
* security engineers building or tuning detections
* `SOC` analysts moving up into detection engineering or threat hunting
* developers and `SREs` cross-training into defensive security
* security architects designing detection and hunting programs

## Prerequisites
* working knowledge of `Linux` and `Windows` system internals at the user level
* basic familiarity with networking (`TCP`/`IP`, `DNS`, `HTTP`)
* exposure to at least one `SIEM` or log aggregation platform
* basic scripting in `Python` or `PowerShell`

## Objectives
* describe the threat landscape using the `MITRE ATT&CK` framework
* enumerate and reason about the data sources defenders rely on
* write detections that are actionable, maintainable and reviewed
* manage the false-positive economics of a detection program
* run `hypothesis`-driven threat hunts and document them
* operate `SIEM` and detection tooling effectively
* build the team practices that mature a detection program over time

## Outline
<!-- chapter: the-defenders-mindset, duration: 2h -->
* The defender's mindset
    * detection vs prevention vs response
    * the kill chain and `MITRE ATT&CK`
    * the pyramid of pain
    * threat intelligence: strategic, operational, tactical
    * defender economics: time, attention, false positives
    * what "good" looks like for a defensive program
<!-- chapter: mitre-att-ck-as-a-shared-language, duration: 3h -->
* `MITRE` `ATT&CK` as a shared language
    * the structure: tactics, techniques, sub-techniques, procedures
    * `ATT&CK` matrices: enterprise, mobile, `ICS`
    * mapping detections to techniques
    * coverage analysis and heatmaps
    * `D3FEND` and the defender ontology
    * the `ATT&CK` evaluation results
<!-- chapter: data-sources-for-defenders, duration: 4h -->
* Data sources for defenders
    * endpoint telemetry: `Sysmon`, `EDR`, `osquery`, `auditd`, `eBPF`
    * network telemetry: flow data, `Zeek`, `DNS` logs, `TLS` metadata
    * cloud telemetry: `CloudTrail`, `Cloud Audit Logs`, `Azure Activity Log`
    * application and identity logs
    * `Kubernetes` audit and runtime logs
    * what makes a data source good for detection
    * data hygiene, retention and cost
<!-- chapter: introduction-to-detection-engineering, duration: 3h -->
* Introduction to detection engineering
    * detection as code
    * the detection lifecycle: ideation, build, validate, deploy, tune, retire
    * detection ownership and review
    * detection metadata: name, description, owner, references, severity
    * `Sigma` as a portable detection format
    * detection content sources: `Sigma HQ`, `Elastic Detection Rules`, vendor catalogues
<!-- chapter: writing-good-detections, duration: 4h -->
* Writing good detections
    * specificity vs generality
    * the four-quadrant model: precision and recall
    * threshold detections, anomaly detections, behavioral detections
    * indicator-based detections and their decay
    * writing detections from `ATT&CK` techniques
    * the "would this have caught real attackers" test
    * the "would this fire constantly" test
<!-- chapter: tuning-and-the-economics-of-false-positives, duration: 3h -->
* Tuning and the economics of false positives
    * the cost of a single false positive in analyst minutes
    * the false-positive budget per detection
    * tuning at the rule, environment and analyst layers
    * suppression, allow-listing and risk-based scoring
    * detection retirement criteria
    * automation as a way to absorb low-fidelity alerts
<!-- chapter: testing-and-validating-detections, duration: 3h -->
* Testing and validating detections
    * unit tests for detection logic
    * `Atomic Red Team` and `Caldera` for technique simulation
    * purple team exercises
    * `BAS` (breach and attack simulation) platforms
    * regression testing detections in `CI`
    * coverage gap analysis after a real incident
<!-- chapter: siem-and-tooling-deep-dive, duration: 3h -->
* `SIEM` and tooling deep dive
    * `Splunk`, `Elastic`, `Sentinel`, `Chronicle`, `Sumo Logic`
    * data lake-first architectures: `Snowflake`, `Databricks`
    * `SOAR` platforms and where they help
    * detection-as-code pipelines: `Panther`, `Anvilogic`, custom
    * choosing tooling for your scale and budget
<!-- chapter: threat-hunting-methodology, duration: 3h -->
* Threat hunting methodology
    * what threat hunting is and is not
    * `hypothesis`-driven hunting
    * the hunt loop: `hypothesis`, data, analyze, conclude, document
    * hunting from `ATT&CK` techniques
    * hunting from intelligence
    * hunting from observed anomaly
    * the `TaHiTI` and `PEAK` hunting frameworks
<!-- chapter: hunting-techniques-by-domain, duration: 3h -->
* Hunting techniques by domain
    * endpoint hunting: process trees, persistence, defense evasion
    * network hunting: beaconing, `DNS` tunneling, lateral movement
    * cloud hunting: identity abuse, exfiltration, persistence in `IAM`
    * `Kubernetes` hunting: workload escape, privileged containers
    * identity hunting: anomalous logins, token abuse
<!-- chapter: turning-hunts-into-detections, duration: 2h -->
* Turning hunts into detections
    * recognizing reproducible hunt patterns
    * promoting a hunt finding to a detection
    * documenting "we hunted, we found nothing" as a contribution
    * the relationship between hunting and detection engineering
<!-- chapter: detection-and-the-blue-purple-and-red-teams, duration: 2h -->
* Detection and the blue, purple and red teams
    * collaboration models with red and purple teams
    * what to ask the red team for
    * defending against your own red team's findings
    * the threat-informed defense loop
<!-- chapter: incident-response-handoff, duration: 2h -->
* Incident response handoff
    * what a good detection alert contains
    * triage SOPs and runbooks
    * preserving evidence during triage
    * the alert-to-incident transition
    * feedback loops from `IR` back into detection engineering
<!-- chapter: program-metrics-and-maturity, duration: 2h -->
* Program metrics and maturity
    * coverage metrics
    * detection precision and recall
    * mean time to detect and to triage
    * analyst burnout signals
    * detection program maturity models
    * communicating value to leadership
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * write detections from a sample `ATT&CK` technique set
    * group hunt on a synthetic dataset
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
