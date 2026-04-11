---
tags:
  - security:security
  - practices:monitoring
level: intermediate
category: security
duration_hours: 40
audience:
  - audiences:security-professionals
---
<!-- course: soc_analyst_training -->
# `SOC` Analyst Training

## Description
This course prepares security professionals for roles in a Security Operations Center (`SOC`). It covers the full spectrum of `SOC` analyst responsibilities including security monitoring, log analysis, threat detection, incident triage, and response procedures. Participants will gain hands-on experience with industry-standard `SIEM` tools, learn to apply the `MITRE ATT&CK` framework, and develop the analytical skills needed to identify and respond to security incidents effectively.

## Duration
40 hours / 5 days

## Intended Audience
* Aspiring `SOC` analysts and junior security professionals
* IT administrators transitioning to security operations roles
* Network engineers moving into security monitoring
* Incident response team members seeking structured `SOC` methodology
* Security engineers responsible for detection and monitoring

## Prerequisites
* Basic understanding of networking concepts (`TCP`/`IP`, `DNS`, `HTTP`, firewalls)
* Familiarity with `Linux` and `Windows` operating systems administration
* Basic knowledge of information security principles
* Understanding of common network protocols and services
* Command-line proficiency on both `Linux` and `Windows`

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand the structure, roles, and workflows of a modern `SOC`
* Configure and operate `SIEM` platforms including `Splunk`, `Elastic SIEM`, and `Microsoft Sentinel`
* Analyze logs from multiple sources including `Windows` event logs, `Linux` `syslog`, and network devices
* Identify indicators of compromise and map them to the `MITRE ATT&CK` framework
* Triage and classify security incidents according to severity and impact
* Perform phishing analysis and malware triage
* Execute threat hunting activities using structured methodologies
* Write clear and actionable incident reports

## Outline
<!-- chapter: soc-operations-fundamentals, duration: 5h -->
* `SOC` Operations Fundamentals
    * `SOC` mission, structure, and operating models
    * `SOC` roles: tier 1, tier 2, tier 3 analyst responsibilities
    * Security monitoring fundamentals and alert lifecycle
    * `SOC` tools and technology stack overview
    * Standard operating procedures and playbooks
    * Shift handoff and communication protocols
    * Legal and compliance considerations in `SOC` operations
<!-- chapter: siem-platforms-and-log-management, duration: 5h -->
* `SIEM` Platforms and Log Management
    * `SIEM` architecture and core capabilities
    * Working with `Splunk`: data ingestion, search processing language (SPL), and dashboards
    * Working with `Elastic SIEM`: index management, KQL queries, and detection rules
    * Working with `Microsoft Sentinel`: data connectors, analytics rules, and workbooks
    * Log source onboarding and normalization
    * Creating correlation rules and alerts
    * `SIEM` tuning and reducing false positives
<!-- chapter: log-analysis-and-network-traffic-analysis, duration: 6h -->
* Log Analysis and Network Traffic Analysis
    * `Windows` event log analysis: authentication events, process creation, and `PowerShell` logging
    * `Linux` `syslog` analysis: auth logs, cron jobs, and system events
    * `Firewall` and proxy log analysis
    * `DNS` log analysis and detecting `DNS`-based threats
    * Network traffic analysis fundamentals using `Wireshark` and Zeek
    * NetFlow analysis and baseline establishment
    * Identifying anomalous patterns in network communications
    * Email header analysis and mail flow investigation
<!-- chapter: threat-intelligence-and-ioc-identification, duration: 6h -->
* Threat Intelligence and `IOC` Identification
    * Threat intelligence sources and feeds
    * Indicator of compromise (`IOC`) types: hashes, `IP` addresses, domains, and behavioral indicators
    * Threat intelligence platforms and enrichment tools
    * `MITRE ATT&CK` framework: tactics, techniques, and procedures
    * Mapping observed activity to ATT&CK techniques
    * Using `ATT&CK Navigator` for coverage analysis
    * Building and maintaining `IOC` databases
    * Intelligence sharing standards: STIX and `TAXII`
<!-- chapter: incident-triage-and-analysis, duration: 6h -->
* Incident Triage and Analysis
    * Incident triage methodology and prioritization
    * Incident classification frameworks and severity levels
    * Phishing email analysis: header inspection, URL analysis, and attachment sandboxing
    * Malware triage: static indicators, sandbox detonation, and behavioral analysis
    * Account compromise investigation workflows
    * Lateral movement detection and analysis
    * Data exfiltration detection techniques
    * Escalation procedures and criteria
<!-- chapter: threat-hunting-and-vulnerability-management, duration: 6h -->
* Threat Hunting and Vulnerability Management
    * Threat hunting fundamentals and `hypothesis`-driven approach
    * Proactive hunting techniques using `SIEM` queries
    * Hunting for persistence mechanisms
    * Hunting for credential access and privilege escalation
    * Vulnerability management lifecycle
    * Vulnerability scanning tools and prioritization
    * Correlating vulnerabilities with threat intelligence
    * Risk-based vulnerability remediation strategies
<!-- chapter: incident-response-and-reporting, duration: 6h -->
* Incident Response and Reporting
    * Incident response procedures and lifecycle
    * Containment strategies: isolation, blocking, and account disabling
    * Evidence collection and chain of custody basics
    * Incident documentation best practices
    * Writing effective incident reports
    * Post-incident review and lessons learned
    * `SOC` metrics and KPIs: mean time to detect, mean time to respond, and alert volume
    * Continuous improvement and process refinement

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
