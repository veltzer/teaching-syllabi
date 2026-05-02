---
tags:
  - concepts:observability
  - concepts:operations
  - concepts:best-practices
  - concepts:performance
level: intermediate
category: observability
duration_hours: 16
audience:
  - audiences:sres
  - audiences:devops
  - audiences:team-leads
  - audiences:senior-developers
---
<!-- course: slos_and_error_budgets -->
# `SLOs` and Error Budgets

## Description
Service-level objectives (`SLOs`) and error budgets are the most important reliability tool the
`SRE` movement produced and the most commonly misapplied. The catalog has Site Reliability Engineering
and `SRE Practices` courses; this course is the deep dive into the specific discipline of designing
`SLIs` (the indicators), defining `SLOs` (the objectives), and using error budgets as the operational
contract between engineering and the business. It is the difference between "we have an `SLO`" and
"the `SLO` actually shapes the team's behavior."

This two day course covers `SLOs` as a working engineering practice. It covers the `SLI` design
problem (request-driven, pipeline-driven, capacity-driven), the multi-window multi-burn-rate alerting
algorithm, the error budget as the cross-functional currency, the freeze-when-budget-exhausted policy
and its alternatives, the `SLO` review meeting, the relationship of `SLOs` to release engineering, the
shape of an `SLO` for a streaming pipeline vs a request-response service, the customer-facing `SLA` vs
the internal `SLO`, and the patterns that make `SLOs` succeed or fail in a real organization.
Examples are drawn from the `Google SRE` books and the public engineering writing of organizations
that ship `SLO` programs that actually work. Participants leave able to set up `SLOs` that the team
will respect and the business will trust.

## Duration
16 hours / 2 days

## Intended Audience
* `SRE` and platform engineers introducing or fixing `SLOs`
* tech leads owning service reliability
* senior developers operating production services
* engineering managers with reliability `KPIs`

## Prerequisites
* working experience operating a production service
* familiarity with at least one observability stack
* exposure to the Site Reliability Engineering course is helpful

## Objectives
* design good `SLIs` for request-response, batch, and streaming systems
* set `SLOs` at the right number for the right reason
* implement multi-window multi-burn-rate alerting
* manage an error budget as the engineering-product contract
* run an `SLO` review that changes behavior
* recognize the patterns that `make` `SLO` programs fail
* connect `SLOs` to release engineering and incident response

## Outline
<!-- chapter: what-an-slo-actually-is, duration: 1h -->
* What an `SLO` actually is
    * `SLI`, SLO, `SLA` — the three layers
    * the `SLO` as a contract with users
    * the error budget as the consequence
    * cross-reference to the Site Reliability Engineering course
    * the "we have a 99.9 percent `SLO` and nobody acts on it" failure
<!-- chapter: choosing-an-sli, duration: 2h -->
* Choosing an `SLI`
    * the request-driven shape: availability, latency, correctness
    * the pipeline-driven shape: freshness, completeness, throughput
    * the capacity-driven shape: utilization, headroom
    * the user-journey `SLI`
    * the "we measured what was easy, not what mattered" failure
<!-- chapter: the-99-point-9-trap, duration: 1h -->
* The 99.9 trap
    * `SLOs` should not be 99.9 by default
    * the cost-per-nine
    * the user-impact-per-nine
    * the "we set it where the marketing team wanted" failure
    * how to negotiate the right number
<!-- chapter: composite-and-journey-slos, duration: 2h -->
* Composite and journey `SLOs`
    * the per-endpoint vs per-journey question
    * composing dependent services
    * the "every dependency was 99.9 so the journey was 98" math
    * critical-user-journey identification
    * the worked example
<!-- chapter: the-error-budget, duration: 2h -->
* The error budget
    * the budget as engineering-product currency
    * the budget-exhaustion policy
    * the freeze, the slowdown, the case-by-case approach
    * the "we exhausted the budget and shipped anyway" failure
    * the budget-burn dashboard
<!-- chapter: multi-window-multi-burn-rate-alerting, duration: 2h -->
* Multi-window multi-burn-rate alerting
    * the canonical `Google` algorithm
    * the short-window vs long-window trade-off
    * the precision-recall analysis
    * the page vs ticket distinction
    * implementation in `Prometheus` recording rules
    * cross-reference to the Advanced `Prometheus` course
<!-- chapter: implementing-slos-in-prometheus, duration: 1h -->
* Implementing `SLOs` in `Prometheus`
    * `histogram_quantile` and the `bucket` story
    * the `slo-libsonnet` and `pyrra` libraries
    * `Sloth` and the `SLO`-generator pattern
    * the `Grafana SLO` panels
    * cross-reference to the `Prometheus` Deep Dive course
<!-- chapter: streaming-and-pipeline-slos, duration: 1h -->
* Streaming and pipeline `SLOs`
    * the freshness `SLI`
    * the completeness `SLI`
    * the end-to-end latency `SLI`
    * the "the dashboards were green but the data was three days old" failure
    * cross-reference to the Streaming Data Systems course
<!-- chapter: the-slo-review-meeting, duration: 1h -->
* The `SLO` review meeting
    * cadence: weekly, monthly, quarterly
    * what the meeting decides
    * who is in the room
    * the "the meeting that changes nothing" failure
    * the actions that should come out
<!-- chapter: slos-and-release-engineering, duration: 1h -->
* `SLOs` and release engineering
    * the budget-driven release decision
    * the canary success criterion as `SLO`-bound
    * the "ship-Friday-when-budget-is-healthy" rule
    * cross-reference to the Release Engineering course
    * cross-reference to the Feature Flags course
<!-- chapter: organizational-patterns, duration: 1h -->
* Organizational patterns
    * who owns the `SLO`
    * the product-engineering negotiation
    * the customer-facing `SLA` vs the internal `SLO`
    * the "we promised what we cannot measure" anti-pattern
    * the maturity ladder for `SLO` programs
<!-- chapter: when-slos-fail, duration: 1h -->
* `When` `SLOs` fail
    * the perfect-`SLO` paralysis
    * the gamed `SLI`
    * the "everyone agreed and nothing changed" outcome
    * the program-rebuild path
    * what to do in the first 90 days of fixing it

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
