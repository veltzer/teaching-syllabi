---
tags:
  - practices:sre
  - practices:monitoring
  - practices:observability
  - concepts:scalability
level: intermediate
category: architecture
duration_hours: 16
audience:
  - audiences:sres
  - audiences:devops
  - audiences:developers
  - audiences:team-leads
---
<!-- course: sre_practices -->
# SRE Practices

## Description
This two day course covers the core practices of Site Reliability Engineering as pioneered by Google. Participants will learn to define and measure service reliability through SLIs, SLOs, and SLAs, manage error budgets, reduce toil, plan capacity, handle incidents, conduct postmortems, and build reliable release engineering and on-call practices.

## Duration
16 hours / 2 days

## Intended Audience
* Site reliability engineers and platform engineers
* `DevOps` engineers adopting SRE principles
* Development team leads responsible for service reliability

## Prerequisites
* Experience operating production systems
* Basic understanding of monitoring and alerting
* Familiarity with `Linux` system administration

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Define meaningful SLIs, SLOs, and SLAs for services.
* Implement and manage error budget policies.
* Identify and systematically reduce toil.
* Plan capacity based on growth projections and performance data.
* Run effective incident management and blameless postmortems.
* Design release engineering processes that balance velocity and reliability.

## Outline
<!-- chapter: introduction-to-sre, duration: 1h -->
* Introduction to SRE
    * SRE principles and philosophy
    * SRE vs traditional operations
    * Organizational models for SRE teams
    * The role of software engineering in operations
<!-- chapter: slis-slos-and-slas, duration: 1h -->
* SLIs, SLOs, and SLAs
    * Choosing meaningful service level indicators
    * Setting achievable service level objectives
    * Relationship between SLOs and SLAs
    * Measuring and reporting on SLIs
<!-- chapter: error-budgets, duration: 1h -->
* Error Budgets
    * Error budget calculation and tracking
    * Error budget policies and decision making
    * Balancing feature velocity with reliability
    * Stakeholder alignment on error budgets
<!-- chapter: toil-reduction, duration: 1h -->
* Toil Reduction
    * Defining and measuring toil
    * Identifying automation opportunities
    * Prioritizing toil reduction projects
    * Tracking toil reduction over time
<!-- chapter: capacity-planning, duration: 2h -->
* Capacity Planning
    * Demand forecasting and growth modeling
    * Load testing for capacity estimation
    * Resource provisioning strategies
    * Cost-aware capacity decisions
<!-- chapter: incident-management, duration: 2h -->
* Incident Management
    * Incident response roles and responsibilities
    * Incident command structure
    * Communication during incidents
    * Incident severity classification and escalation
<!-- chapter: postmortems, duration: 2h -->
* Postmortems
    * Blameless postmortem culture
    * Writing effective postmortem documents
    * Identifying root causes and contributing factors
    * Tracking and following up on action items
<!-- chapter: release-engineering, duration: 2h -->
* Release Engineering
    * Release strategies: canary, blue-green, rolling
    * Feature flags and progressive rollouts
    * Rollback procedures and safety mechanisms
    * Release velocity and reliability tradeoffs
<!-- chapter: on-call-practices, duration: 2h -->
* On-Call Practices
    * Designing sustainable on-call rotations
    * Runbooks and operational documentation
    * Alert quality and actionability
    * On-call compensation and burnout prevention
<!-- chapter: automation, duration: 2h -->
* Automation
    * Automation hierarchy and decision framework
    * Self-healing systems and auto-remediation
    * Infrastructure as code for reliability
    * Measuring automation effectiveness

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
