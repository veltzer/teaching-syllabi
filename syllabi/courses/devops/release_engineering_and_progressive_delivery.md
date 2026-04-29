---
tags:
  - concepts:gitops
  - concepts:operations
  - concepts:best-practices
  - concepts:testing
level: intermediate
category: devops
duration_hours: 24
audience:
  - audiences:devops
  - audiences:sres
  - audiences:senior-developers
  - audiences:team-leads
---
<!-- course: release_engineering_and_progressive_delivery -->
# Release Engineering and Progressive Delivery

## Description
Release engineering is the discipline of getting code from a merged pull request to a happy customer.
The catalog has a `Feature Flags and Progressive Delivery` course that covers feature flags as a tool;
this course covers the broader release engineering picture into which flags fit. It is the difference
between "how do I use a flag" and "how does my organization release software safely, repeatably, and
without burning out the on-call rotation."

This three day course covers release strategy as an end-to-end concern. It covers release trains versus
trunk-based versus feature-branch, the canary as both a deployment strategy and a verification strategy,
blue-green and rolling deploys and the cases for each, the rollback story, the database migration
problem (the deploy that cannot be rolled back), the release-on-Friday question, the release-readiness
checklist, the metrics that decide whether a release succeeded, and the relationship between release
engineering and incident response. Examples are drawn from the public engineering writing of `LinkedIn`,
`Facebook`, `Google`, `Netflix`, and the `Accelerate` book's claims about release frequency and
reliability. Participants leave able to design a release process that the team will actually follow.

## Duration
24 hours / 3 days

## Intended Audience
* `DevOps` engineers owning the deployment pipeline
* platform engineers building the paved release road
* senior developers introducing progressive delivery to a team
* tech leads accountable for change-failure rate

## Prerequisites
* working experience with at least one `CI/CD` system
* exposure to either `Kubernetes` or a comparable deploy target
* familiarity with the Trunk Based Development course is helpful

## Objectives
* design a release strategy appropriate for the team and the product
* choose between blue-green, rolling, canary, and shadow
* solve the database migration rollback problem
* define what a release-readiness checklist contains
* measure the success of a release with the right metrics
* recognize the patterns that lead to release pain
* connect release engineering to incident response

## Outline
<!-- chapter: what-release-engineering-actually-covers, duration: 1h -->
* What release engineering actually covers
    * the path from `merge` to user
    * release engineering vs `CI/CD`
    * cross-reference to the Trunk Based Development and `CI` course
    * cross-reference to the Feature Flags and Progressive Delivery course
    * what happens before the deploy and what happens after
<!-- chapter: release-strategies-overview, duration: 2h -->
* Release strategies overview
    * release train, trunk-based, feature branch
    * the cadence question: weekly, daily, on-demand
    * the per-team-cadence vs whole-org cadence
    * `Accelerate`'s findings on release frequency and reliability
    * picking a strategy for the team
<!-- chapter: deployment-patterns, duration: 3h -->
* Deployment patterns
    * recreate, rolling, blue-green, canary, shadow
    * the rollback semantics of each
    * the cost shape of each
    * the "we picked blue-green and the database broke it" failure
    * worked examples
<!-- chapter: canary-deployment, duration: 2h -->
* Canary deployment
    * the canary as a verification mechanism
    * automatic vs manual canary analysis
    * `Argo Rollouts`, `Flagger`, `Spinnaker`
    * cross-reference to the `ArgoCD` and `GitOps` course
    * the "we always promoted the canary regardless" failure
<!-- chapter: feature-flags-and-decoupling-deploy-from-release, duration: 2h -->
* Feature flags and decoupling deploy from release
    * deploy is mechanical, release is a business decision
    * the dark launch
    * the gradual rollout
    * cross-reference to the Feature Flags course
    * the flag-graveyard problem
<!-- chapter: database-migrations-and-irreversibility, duration: 3h -->
* Database migrations and irreversibility
    * the deploy you cannot roll back
    * expand-contract migrations
    * the dual-read and dual-write phase
    * cross-reference to the Database Migration Strategies course
    * the "we shipped the schema and the rollback bricked us" failure
<!-- chapter: release-readiness-and-checklists, duration: 2h -->
* Release readiness and checklists
    * the release-readiness review
    * the runbook and the on-call handoff
    * the load-test gate
    * the security review gate
    * the "we have a process and nobody follows it" failure
<!-- chapter: rollback-and-recovery, duration: 2h -->
* Rollback and recovery
    * rollback as a first-class operation
    * the rollback budget
    * the time-to-rollback metric
    * forward-fix vs rollback
    * the "we lost data on rollback" failure
<!-- chapter: release-metrics, duration: 2h -->
* Release metrics
    * `DORA` metrics: deployment frequency, lead time, change failure rate, `MTTR`
    * cross-reference to the Engineering Metrics and `DORA` course
    * the metric you should not chase
    * `SLO`-based release decisions
    * the canary-success metric
<!-- chapter: release-and-incident-response, duration: 1h -->
* Release and incident response
    * the deploy that started the incident
    * the rollback as the first action
    * cross-reference to the Incident Response and Postmortems course
    * the deploy-freeze question
<!-- chapter: organizational-patterns, duration: 2h -->
* Organizational patterns
    * the central release team vs federated
    * release manager vs everyone-deploys
    * the release notes pipeline
    * the change advisory board and `when` it helps
    * the release-on-Friday debate
<!-- chapter: tooling-survey, duration: 1h -->
* Tooling survey
    * `ArgoCD`, `Flux`, `Spinnaker`, `Harness`, `Octopus Deploy`
    * `Argo Rollouts` and `Flagger`
    * `LaunchDarkly`, `Unleash`, `Statsig`, `GrowthBook` for flags
    * picking the toolchain for the team
<!-- chapter: a-release-engineering-walkthrough, duration: 1h -->
* A release engineering walkthrough
    * design walkthrough of a release pipeline
    * walkthrough of a real bad deploy
    * walkthrough of the postmortem that followed
    * recommended reading: `Google SRE` book release chapters, `Accelerate`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
