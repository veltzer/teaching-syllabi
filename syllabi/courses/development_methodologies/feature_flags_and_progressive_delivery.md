---
tags:
  - concepts:best-practices
  - concepts:developer-experience
  - concepts:operations
  - concepts:testing
  - concepts:migration
  - concepts:architecture
level: intermediate
category: methodology
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:devops
  - audiences:team-leads
  - audiences:architects
---
<!-- course: feature_flags_and_progressive_delivery -->
# Feature Flags and Progressive Delivery

## Description
Feature flags decouple deployment from release. Done well, they `let` teams ship code continuously, roll out features
gradually to subsets of users, run experiments in production, and recover from incidents in seconds rather than hours.
Done poorly, they accumulate as a tangle of dead conditionals that nobody dares to delete.

This five day course covers feature flags as an engineering discipline. It covers the spectrum of flag types
(release, ops, experiment, permission), flag-platform architecture, integration patterns at the application level,
gradual rollout strategies, A/B and multivariate testing, kill switches, flag debt and disciplined cleanup. The
course is platform-aware (`LaunchDarkly`, `Unleash`, `Flagsmith`, `Split`, `Statsig`, `OpenFeature`) but vendor-neutral.
Participants leave able to introduce feature flags into a codebase, run a progressive delivery program, and avoid
the operational and code-quality traps that have ended other teams' attempts.

## Duration
40 hours / 5 days

## Intended Audience
* developers introducing feature flags into their codebases
* tech leads and architects designing a flag strategy across teams
* `DevOps` engineers running rollout and experimentation infrastructure
* product engineers running A/B and feature experiments
* engineers responsible for incident-time mitigation tooling

## Prerequisites
* working knowledge of at least one mainstream programming language
* basic familiarity with `CI`/`CD` and deployment workflows
* some experience with web or service development

## Objectives
* describe the spectrum of feature flag types and use cases
* introduce feature flags into a codebase without making it harder to read
* design rollout strategies appropriate to the risk profile of a change
* run A/B experiments with statistical rigor
* operate flags safely as incident-mitigation tools
* manage flag lifecycle and avoid flag debt
* choose between flag platforms or build a small one in-house

## Outline
<!-- chapter: why-feature-flags, duration: 2h -->
* Why feature flags
    * decoupling deployment from release
    * the trunk-based development connection
    * incident mitigation in seconds
    * experimentation without code changes
    * permission and entitlement management
    * what feature flags are not a substitute for
<!-- chapter: types-of-feature-flags, duration: 2h -->
* Types of feature flags
    * release flags
    * operational and circuit-breaker flags
    * experiment flags
    * permission and entitlement flags
    * long-lived vs short-lived flags
    * matching flag type to lifecycle expectations
<!-- chapter: flag-platform-architecture, duration: 3h -->
* Flag platform architecture
    * the evaluation engine
    * configuration storage
    * client `SDKs` and bootstrapping
    * streaming vs polling vs hybrid update models
    * client-side vs server-side evaluation
    * fallback values and offline behavior
    * latency, availability and consistency requirements
<!-- chapter: integrating-flags-into-application-code, duration: 3h -->
* Integrating flags into application code
    * the flag-`check` call site
    * keeping conditionals readable
    * branching at the right level: function, request, page, feature
    * dependency injection of flag clients
    * server-side rendering and front-end frameworks
    * mobile and offline-capable clients
    * `OpenFeature` as a portability layer
<!-- chapter: targeting-segments-and-context, duration: 3h -->
* Targeting, segments and context
    * the evaluation context: user, account, device, request
    * percentage rollouts and bucketing stability
    * targeting rules and segments
    * dependent and prerequisite flags
    * dynamic segments
    * data minimization and `PII` in evaluation context
<!-- chapter: progressive-rollout-strategies, duration: 3h -->
* Progressive rollout strategies
    * dark launch
    * percentage-based rollout
    * ring deployment: canary, internal, beta, general availability
    * geo-bucketed rollout
    * tenant-based rollout in `B2B` `SaaS`
    * monitoring during rollout
    * rollback as the default response
<!-- chapter: experimentation-and-a-b-testing, duration: 4h -->
* Experimentation and A/B testing
    * what an experiment actually answers
    * experiment design: `hypothesis`, primary metric, guardrails
    * sample size and statistical power
    * frequentist vs Bayesian frameworks
    * multivariate testing
    * stratification and blocking
    * sequential testing and peeking
    * common analysis pitfalls
<!-- chapter: kill-switches-and-incident-tooling, duration: 2h -->
* Kill switches and incident tooling
    * operational flags as a runbook tool
    * making flags discoverable during an incident
    * audit trail of flag changes
    * permissions and approval for production toggles
    * "break glass" workflows
<!-- chapter: testing-and-flagged-code, duration: 3h -->
* Testing and flagged code
    * test matrix explosion
    * mocking the flag client
    * testing both branches without `n^2` complexity
    * end-to-end tests with controlled flag states
    * property-based and randomized flag tests
    * keeping `CI` cost under control
<!-- chapter: flag-debt-and-cleanup, duration: 3h -->
* Flag debt and cleanup
    * the lifecycle of a release flag
    * flag expiry policies
    * detecting stale flags from telemetry
    * codemods for flag removal
    * the "flag of the month" cleanup ritual
    * cultural enforcement: ownership and review
<!-- chapter: governance-permissions-and-audit, duration: 2h -->
* Governance, permissions and audit
    * environments and promotion of flag config
    * `RBAC` for flag changes
    * change approval and four-eyes principle
    * audit logs and compliance
    * separating production toggles from experiment flags
<!-- chapter: flag-platform-comparison, duration: 2h -->
* Flag platform comparison
    * `LaunchDarkly`, `Split`, `Unleash`, `Flagsmith`, `Statsig`, `ConfigCat`
    * managed vs self-hosted vs build-it-yourself
    * `OpenFeature` and the portability story
    * cost models and quotas
    * choosing a platform from team requirements
<!-- chapter: building-a-minimal-flag-system, duration: 2h -->
* Building a minimal flag system
    * what a minimum-viable flag service looks like
    * config-store, evaluator, `SDK`
    * scaling the small system as you grow
    * `when` to migrate to a vendor
<!-- chapter: progressive-delivery-beyond-flags, duration: 2h -->
* Progressive delivery beyond flags
    * traffic mirroring and shadowing
    * service mesh-driven canary
    * `Argo Rollouts` and `Flagger`
    * combining infra-level and code-level rollout
    * automated rollback on `SLO` regression
<!-- chapter: case-studies-and-anti-patterns, duration: 2h -->
* Case studies and anti-patterns
    * the flag that stayed forever
    * the experiment that drew the wrong conclusion
    * the kill switch that did not switch
    * the team that flagged everything
    * lessons from real-world rollout incidents
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * end-to-end design of a flag program for a sample team
    * group review of flag-using code
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
