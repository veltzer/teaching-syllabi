---
tags:
  - practices:sre
  - practices:methodology
  - practices:devops
level: intermediate
category: methodology
duration_hours: 16
audience:
  - audiences:developers
  - audiences:managers
  - audiences:devops
  - audiences:sres
---
<!-- course: incident_management -->
# Incident Management

## Description
Effective incident management is critical for maintaining reliable systems and services.
This course covers the full incident lifecycle, from detection and response through
resolution and post-incident learning. Students will learn how to build robust on-call
processes, run effective incident responses, conduct blameless postmortems, and establish
a culture of reliability using SRE principles.

## Duration
16 hours / 2 days

## Intended Audience
* Developers responsible for operating production services.
* `DevOps` and SRE engineers building reliability practices.
* Managers overseeing on-call teams and incident processes.

## Prerequisites
* Experience working with production systems.
* Basic understanding of monitoring and logging concepts.
* Familiarity with `Linux` command line and `web services`.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* understand the core concepts and principles of incident management
* gain practical knowledge of incident response coordination
* gain practical knowledge of post-incident review and organizational learning
* gain practical knowledge of SLOs, SLIs, and error budgets

## Outline
<!-- chapter: incident-management-lifecycle, duration: 1h -->
* Incident Management Lifecycle
    * What is an incident
    * Detection, response, mitigation, resolution
    * Incident states and transitions
    * Documentation during incidents
<!-- chapter: on-call-best-practices, duration: 1h -->
* On-Call Best Practices
    * Designing on-call rotations
    * On-call compensation and sustainability
    * Reducing on-call burden
    * Handoff procedures
    * On-call tooling
<!-- chapter: incident-severity-levels, duration: 1h -->
* Incident Severity Levels
    * Defining severity tiers
    * Severity classification criteria
    * Escalation triggers
    * Response expectations per severity
<!-- chapter: incident-commander-role, duration: 1h -->
* Incident Commander Role
    * Responsibilities and authority
    * Coordinating responders
    * Decision-making under pressure
    * Communication management
    * Training incident commanders
<!-- chapter: communication-during-incidents, duration: 1h -->
* Communication During Incidents
    * Internal communication channels
    * Status page updates
    * Customer communication
    * Stakeholder management
    * Communication templates
<!-- chapter: incident-response-tools, duration: 1h -->
* Incident Response Tools
    * `PagerDuty`
    * OpsGenie
    * Slack and ChatOps for incidents
    * Incident tracking systems
    * War rooms (virtual and physical)
<!-- chapter: runbooks-and-playbooks, duration: 1h -->
* Runbooks and Playbooks
    * Writing effective runbooks
    * Playbook structure and content
    * Automation of common procedures
    * Keeping runbooks up to date
<!-- chapter: post-incident-review, duration: 1h -->
* Post-Incident Review
    * Blameless postmortems
    * Facilitating postmortem meetings
    * Writing postmortem documents
    * Action items and follow-through
    * Sharing learnings across the organization
<!-- chapter: slos-slis-and-slas, duration: 1h -->
* SLOs, SLIs, and SLAs
    * Service Level Indicators (SLIs)
    * Service Level Objectives (SLOs)
    * Service Level Agreements (SLAs)
    * Choosing the right SLIs
    * Setting meaningful SLOs
<!-- chapter: error-budgets, duration: 1h -->
* Error Budgets
    * Error budget concept
    * Error budget policies
    * Balancing reliability and velocity
    * Error budget exhaustion responses
<!-- chapter: monitoring-and-alerting-strategy, duration: 1h -->
* Monitoring and Alerting Strategy
    * Alert quality and signal-to-noise ratio
    * Actionable alerts
    * Alert fatigue and its dangers
    * Monitoring for symptoms vs causes
    * Dashboard design for incidents
<!-- chapter: escalation-procedures, duration: 1h -->
* Escalation Procedures
    * Escalation paths and policies
    * `When` and how to escalate
    * Management escalation
    * Cross-team escalation
<!-- chapter: chaos-engineering-introduction, duration: 1h -->
* Chaos Engineering Introduction
    * Principles of chaos engineering
    * Failure injection techniques
    * Tools (`Chaos Monkey`, Litmus, Gremlin)
    * Starting small and safely
<!-- chapter: game-days, duration: 1h -->
* Game Days
    * Planning game day exercises
    * Running simulated incidents
    * Evaluating team response
    * Identifying gaps and improvements
<!-- chapter: organizational-learning-from-incidents, duration: 2h -->
* Organizational Learning from Incidents
    * Building a learning culture
    * Incident databases and knowledge bases
    * Trend analysis across incidents
    * Reliability as a shared responsibility
    * Building a culture of reliability

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
