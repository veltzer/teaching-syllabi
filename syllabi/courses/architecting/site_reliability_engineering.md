---
tags:
  - practices:sre
  - concepts:architecture
  - practices:devops
level: intermediate
category: architecture
duration_hours: 24
audience:
  - audiences:developers
  - audiences:devops
  - audiences:managers
  - audiences:sres
---
<!-- course: site_reliability_engineering -->
# Site Reliability Engineering

## Description
This course provides a comprehensive introduction to Site Reliability Engineering (SRE) as pioneered by Google. Participants will learn the core principles, practices, and cultural aspects of SRE, including defining and implementing SLOs, managing error budgets, reducing toil, and building a healthy on-call and incident management culture. The course bridges the gap between development and operations, equipping teams to balance reliability with the pace of innovation.

## Duration
24 hours / 3 days

## Intended Audience
* Software developers responsible for production reliability
* `DevOps` engineers transitioning to or adopting SRE practices
* Engineering managers building or leading SRE teams
* Operations engineers seeking a more engineering-driven approach
* Technical leads balancing feature velocity with system reliability

## Prerequisites
* Experience developing or operating production software systems
* Basic understanding of distributed systems concepts
* Familiarity with monitoring and logging tools
* General knowledge of `Linux` systems administration
* Awareness of `CI/CD` and deployment practices

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand the core principles and philosophy of SRE
* Define and implement SLIs, SLOs, and SLAs for services
* Use error budgets to `make` data-driven decisions about reliability vs velocity
* Identify and reduce toil through automation and engineering
* Establish effective incident management and blameless postmortem processes
* Design monitoring and alerting systems based on symptoms rather than causes
* Implement SRE practices and team structures within an organization

## Outline
<!-- chapter: sre-principles, duration: 1h -->
* SRE Principles
    * What is Site Reliability Engineering
    * Google's approach to SRE
    * SRE as a practice and a role
    * Core tenets: embracing risk, service level objectives, eliminating toil, automation
    * The relationship between SRE and software engineering
<!-- chapter: slos-slis-and-slas, duration: 2h -->
* SLOs, SLIs, and SLAs
    * Defining Service Level Indicators (SLIs)
    * Choosing the right SLIs for your services
    * Setting Service Level Objectives (SLOs)
    * SLO target selection and negotiation
    * Service Level Agreements (SLAs) and their relationship to SLOs
    * Measuring and tracking SLO compliance
    * SLO documentation and communication
<!-- chapter: error-budgets, duration: 2h -->
* Error Budgets
    * The error budget concept
    * Calculating and tracking error budgets
    * Error budget policies
    * Using error budgets to balance reliability and velocity
    * Handling error budget exhaustion
    * Error budget-driven decision making
<!-- chapter: toil, duration: 2h -->
* Toil
    * Defining and identifying toil
    * Measuring toil across teams
    * Strategies for toil reduction
    * Automation vs elimination
    * Setting toil budgets
    * Tracking toil reduction over time
<!-- chapter: monitoring-and-alerting, duration: 2h -->
* Monitoring and Alerting
    * Monitoring philosophy: symptoms vs causes
    * The four golden signals (latency, traffic, errors, saturation)
    * Designing effective dashboards
    * Alerting on SLOs and burn rates
    * Reducing alert noise and fatigue
    * Monitoring distributed systems
    * Tools and platforms for SRE monitoring
<!-- chapter: incident-management, duration: 2h -->
* Incident Management
    * Incident response framework
    * Roles during incidents (incident commander, communications lead, operations lead)
    * Incident severity classification
    * Communication during incidents
    * Incident coordination tools and practices
    * Managing customer communication during outages
<!-- chapter: postmortem-culture, duration: 2h -->
* Postmortem Culture
    * Blameless postmortems
    * Writing effective postmortem reports
    * Root cause analysis techniques
    * Action item tracking and follow-through
    * Learning from incidents at an organizational level
    * Building a culture of psychological safety
<!-- chapter: capacity-planning, duration: 1h -->
* Capacity Planning
    * Demand forecasting
    * Load testing and performance modeling
    * Resource provisioning strategies
    * Capacity planning for growth
    * Cost optimization and efficiency
<!-- chapter: release-engineering, duration: 1h -->
* Release Engineering
    * Release processes and best practices
    * Progressive rollouts and canary deployments
    * Feature flags for risk reduction
    * Rollback strategies
    * Release velocity vs reliability trade-offs
<!-- chapter: on-call-best-practices, duration: 2h -->
* On-Call Best Practices
    * Designing sustainable on-call rotations
    * On-call compensation and work-life balance
    * Runbooks and playbooks
    * Escalation policies
    * On-call load balancing and burnout prevention
    * Training new on-call engineers
<!-- chapter: automation-hierarchy, duration: 2h -->
* Automation Hierarchy
    * Levels of automation maturity
    * From manual to fully autonomous systems
    * Deciding what to automate
    * Self-healing systems
    * Automation safety and guardrails
<!-- chapter: reliability-vs-velocity-trade-offs, duration: 1h -->
* Reliability vs Velocity Trade-Offs
    * The tension between moving fast and keeping things stable
    * Risk tolerance and its impact on development practices
    * Feature freezes and reliability sprints
    * Embedding reliability into the development lifecycle
<!-- chapter: sre-team-structure, duration: 1h -->
* SRE Team Structure
    * SRE team models (embedded, centralized, consulting)
    * Staffing and hiring for SRE
    * Career development for SRE engineers
    * Collaboration between SRE and product development teams
<!-- chapter: implementing-sre-in-your-organization, duration: 2h -->
* Implementing SRE in Your Organization
    * Starting small: where to begin
    * Building executive support
    * Measuring SRE maturity
    * Common pitfalls and anti-patterns
    * Scaling SRE practices across the organization
<!-- chapter: sre-vs-devops, duration: 1h -->
* SRE vs `DevOps`
    * Philosophical similarities and differences
    * SRE as a specific implementation of `DevOps` principles
    * `When` to adopt SRE vs `DevOps` practices
    * Complementary aspects of both approaches

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
