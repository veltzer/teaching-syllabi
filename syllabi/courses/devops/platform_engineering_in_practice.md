---
tags:
  - concepts:developer-experience
  - concepts:operations
  - concepts:gitops
  - concepts:best-practices
  - concepts:architecture
  - concepts:scalability
level: intermediate
category: devops
duration_hours: 40
audience:
  - audiences:devops
  - audiences:sres
  - audiences:senior-developers
  - audiences:architects
  - audiences:team-leads
---
<!-- course: platform_engineering_in_practice -->
# Platform Engineering In Practice

## Description
Most organizations that build internal platforms rebuild them every two years. The pattern is familiar: a
platform team gets formed, a year of building goes by, the platform ships, half the engineers ignore it, the
other half complain about the parts they actually use, and eventually a reorg dissolves the team and the next
generation starts over. The teams that break this cycle treat their platform as a product with internal users
and operate accordingly.

This five day course is the implementation-and-operation complement to the philosophical platform engineering
material already in the catalog. It covers the platform-as-product mindset, golden paths and paved roads,
internal developer platforms (`Backstage`, Port, Cortex, `OpsLevel`), self-service infrastructure,
templating and scaffolding, internal `APIs` and abstractions, the operational story for platforms, and the
organizational shape that makes platform teams successful. Participants leave able to design, ship and
operate a platform that engineers actually want to use.

## Duration
40 hours / 5 days

## Intended Audience
* `DevOps` and `SRE` engineers transitioning into platform roles
* platform team members building or operating an internal platform
* tech leads designing the platform their organization needs
* architects working with or shaping a platform program
* engineers tasked with adopting a platform that already exists

## Prerequisites
* `solid` `DevOps` or `SRE` experience
* working knowledge of `Kubernetes`, at least one cloud, IaC, CI/`CD`
* experience operating production services
* basic familiarity with `Backstage` or another `IDP` is helpful but not required

## Objectives
* describe the platform-as-product mindset and apply it
* design golden paths that match real developer workflows
* build and operate an internal developer platform
* implement self-service infrastructure with appropriate guardrails
* run a platform team like a product team
* measure platform success with appropriate metrics
* avoid the failure modes that kill most platform programs

## Outline
<!-- chapter: what-platform-engineering-actually-is, duration: 2h -->
* What platform engineering actually is
    * platform engineering vs `DevOps` vs `SRE`
    * the cognitive-load argument
    * the `Team Topologies` framing
    * the `CNCF` platforms whitepaper
    * what platform engineering is not (just `Kubernetes`, just `IaC`)
    * the cases where you do not need a platform
<!-- chapter: platform-as-product, duration: 3h -->
* Platform as product
    * internal users as customers
    * the platform product manager role
    * roadmaps and the platform backlog
    * deprecation as a product decision
    * marketing the platform internally
    * resisting the "we know best" trap
<!-- chapter: golden-paths-and-paved-roads, duration: 3h -->
* Golden paths and paved roads
    * the difference between a guideline and a paved road
    * `Spotify`'s golden path model
    * the golden-path-per-language pattern
    * paved-road-vs-dirt-road tradeoff
    * deviations and the request-to-leave-the-road
    * the cost of having too many golden paths
<!-- chapter: internal-developer-platforms, duration: 4h -->
* Internal developer platforms
    * the `IDP` concept and what it covers
    * `Backstage`, Port, Cortex, OpsLevel, `Humanitec`
    * the service catalog as the entry point
    * scorecards and maturity models
    * `TechDocs` and developer documentation in the `IDP`
    * the `IDP` as the front door for everything else
    * choosing build vs buy for the `IDP`
<!-- chapter: scaffolding-and-templates, duration: 3h -->
* Scaffolding and templates
    * the new-service experience
    * `Backstage` software templates
    * `Cookiecutter`, copier, `yeoman`
    * the "five-minute new service" goal
    * versioning and updating templates after the fact
    * keeping templates from becoming dependencies
<!-- chapter: self-service-infrastructure, duration: 3h -->
* Self-service infrastructure
    * the self-service goal
    * `Crossplane`, `Terraform Cloud`, `Pulumi automation API`
    * `Kubernetes` operators as self-service primitives
    * resource budgets and cost guardrails
    * the request-and-approval flow for non-self-service
    * detecting drift and over-provisioning
<!-- chapter: api-design-for-platforms, duration: 3h -->
* `API` design for platforms
    * the platform's `API` is its `UX`
    * declarative vs imperative interfaces
    * `Kubernetes` `CRDs` as platform interfaces
    * `gRPC` and `REST` for platform services
    * versioning platform interfaces
    * cross-reference to the `API` Evolution course
<!-- chapter: gitops-and-the-platform, duration: 2h -->
* `GitOps` and the platform
    * `GitOps` as a platform interface
    * `ArgoCD`, `Flux`, `Kargo` in the platform context
    * the application-of-applications pattern
    * `GitOps` repository structure for many teams
    * the relationship between `GitOps` and the `IDP`
<!-- chapter: developer-experience-as-a-metric, duration: 3h -->
* Developer experience as a metric
    * `DX` as a measurable outcome
    * developer surveys and what to ask
    * lead time, deploy frequency, time-to-onboard
    * cross-reference to the Engineering Metrics and `DORA` course
    * the `SPACE` and `DX` frameworks
    * acting on `DX` data without overreacting
<!-- chapter: observability-for-platforms, duration: 2h -->
* Observability for platforms
    * the platform's own metrics
    * the platform's effect on consumer service metrics
    * blast-`radius` monitoring during platform changes
    * `SLI`/`SLO` for the platform
    * platform incident response
<!-- chapter: security-and-policy-as-code, duration: 3h -->
* Security and policy as code
    * `OPA`, `Kyverno`, `Conftest`
    * the platform as the place to enforce policy
    * cost guardrails as policy
    * security guardrails as policy
    * the appeals process for blocked policy
    * cross-reference to the Secrets Management and Zero Trust courses
<!-- chapter: paved-road-for-data-and-ai, duration: 2h -->
* Paved road for data and `AI`
    * data platform as a sub-platform
    * `feature store` as a platform component
    * `LLM` gateways as platform infrastructure
    * `MLOps` as a platform concern
    * the cross-reference between platform engineering and data platforms
<!-- chapter: organizational-shape-of-platform-teams, duration: 3h -->
* Organizational shape of platform teams
    * the platform team and the stream-aligned team
    * `Team Topologies` for platforms
    * size and seniority of the platform team
    * the platform-engineering-manager role
    * the embed and the rotation patterns
    * platform team budget conversations
<!-- chapter: migration-and-deprecation, duration: 2h -->
* Migration and deprecation
    * driving a platform-wide migration
    * deprecation telemetry
    * forced retirement and brownouts
    * cross-reference to the `API` Evolution course's deprecation chapter
    * the long tail and what to do with it
<!-- chapter: anti-patterns-failure-modes-and-wrap-up, duration: 2h -->
* Anti-patterns, failure modes and wrap up
    * the gold-plated platform nobody uses
    * the platform team that became the bottleneck
    * the platform that diverged from real workflows
    * the second platform built around the first
    * the reorg that dissolved the platform team
    * how to recognize each early
    * design walkthrough of a platform program for a sample organization
    * recommended reading: `Skelton`/Pais, `CNCF` whitepaper, `Bottcher`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
