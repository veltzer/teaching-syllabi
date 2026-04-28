---
tags:
  - concepts:best-practices
  - concepts:developer-experience
  - concepts:operations
  - concepts:agile
  - concepts:observability
level: intermediate
category: practices
duration_hours: 40
audience:
  - audiences:team-leads
  - audiences:managers
  - audiences:senior-developers
  - audiences:devops
  - audiences:architects
---
<!-- course: engineering_metrics_and_dora -->
# Engineering Metrics and `DORA`

## Description
"You can't manage what you don't measure" gets used to justify a lot of bad engineering metrics. The honest
version is harder: most things that matter in software engineering are difficult to measure, and most things
that are easy to measure mislead you. The `DORA`, `SPACE` and `DX` frameworks are the best public
frameworks we have for cutting through that mess.

This five day course is a practical treatment of engineering metrics. It covers the four key `DORA` metrics and
how to compute them honestly, the `SPACE` framework's expansion of "developer productivity", the `DX` core-4
research, the anti-metrics that destroy teams, the tooling landscape (`LinearB`, `Jellyfish`, `Swarmia`,
`Code Climate Velocity`, `DX`), and the practices that `make` metrics useful for the people being measured rather
than just for the people doing the measuring. Participants leave able to introduce engineering metrics on a
team without making it worse, to read someone else's metrics critically, and to push back on metrics that
deserve pushing back on.

## Duration
40 hours / 5 days

## Intended Audience
* engineering managers and tech leads introducing metrics
* `DevOps` engineers building the data pipelines behind metrics
* senior engineers whose teams are about to be measured
* architects driving engineering-effectiveness initiatives

## Prerequisites
* several years of professional software development or management experience
* basic familiarity with `CI`/`CD`, ticketing systems and source control
* exposure to at least one metrics framework (`DORA`, `SPACE`, `DX`) is helpful

## Objectives
* define and compute the four `DORA` metrics honestly
* apply the `SPACE` framework to broader productivity questions
* use the `DX` core-4 research where it fits
* recognize and avoid the major anti-metric traps
* select tooling appropriate to team size and maturity
* introduce metrics on a team without making the team worse
* read public engineering benchmarks critically

## Outline
<!-- chapter: why-engineering-metrics-are-hard, duration: 2h -->
* Why engineering metrics are hard
    * the productivity-as-output trap
    * `Goodhart`'s law in engineering
    * individual metrics vs team metrics vs system metrics
    * what gets measured gets gamed
    * the political dimension of metrics
    * a defensible position on what is measurable
<!-- chapter: dora-the-four-metrics, duration: 4h -->
* `DORA`: the four metrics
    * deployment frequency
    * lead time for changes
    * change failure rate
    * mean time to recover
    * the `Accelerate` and `State of DevOps` research
    * the elite/high/medium/low buckets
    * what `DORA` is not
<!-- chapter: computing-dora-honestly, duration: 3h -->
* Computing `DORA` honestly
    * what counts as a deployment
    * what counts as a change failure
    * lead time start point: first commit, `PR` open, `PR` merged
    * `MTTR` start point: page, declared incident, customer impact
    * common ways teams accidentally inflate `DORA`
    * publishing the methodology alongside the numbers
<!-- chapter: the-fifth-dora-metric-and-reliability, duration: 2h -->
* The fifth `DORA` metric and reliability
    * the fifth metric debate
    * reliability as the missing dimension
    * `SLO` adherence as a fifth metric
    * cross-reference to the Incident Response course's `SLO` chapter
    * the relationship between speed and reliability in `DORA` data
<!-- chapter: space-framework, duration: 3h -->
* `SPACE` framework
    * the five `SPACE` dimensions: satisfaction, performance, activity, communication, efficiency
    * why `SPACE` exists as a critique of single-metric approaches
    * picking metrics across multiple `SPACE` dimensions
    * the qualitative dimension: developer surveys
    * `SPACE` for individual engineers vs teams vs organizations
<!-- chapter: dx-core-4-and-developer-experience, duration: 3h -->
* `DX` core-4 and developer experience
    * the `DX` research and core-4 metrics
    * `DX` vs `SPACE` vs `DORA`
    * developer experience as a leading indicator
    * the `DX` survey methodology
    * acting on `DX` data without overreacting
    * cross-reference to the Platform Engineering course
<!-- chapter: developer-surveys-done-well, duration: 3h -->
* Developer surveys done well
    * the survey as a primary instrument
    * question design: what to ask and how
    * frequency: continuous, quarterly, annual
    * sample size and statistical power for small teams
    * survey fatigue and how to avoid it
    * publishing results and acting on them
    * the survey that became performative
<!-- chapter: anti-metrics-and-traps, duration: 3h -->
* Anti-metrics and traps
    * lines of code, commits, story points
    * `PR` count without context
    * "developer activity" dashboards
    * stack-ranking engineers
    * comparing teams that do different work
    * the metrics-driven micro-management trap
    * how to recognize each
<!-- chapter: introducing-metrics-on-a-team, duration: 3h -->
* Introducing metrics on a team
    * the consent-and-context conversation
    * starting with team-level not individual-level
    * making the methodology public
    * promising to revise the metrics that `go` wrong
    * the metric-of-the-month rotation
    * the inertia problem and recovering from it
<!-- chapter: tooling-landscape, duration: 3h -->
* Tooling landscape
    * `LinearB`, `Jellyfish`, `Swarmia`, `Code Climate Velocity`
    * `DX` (the company) and `SleuthQA`
    * `Athenian` and others
    * build vs buy for metric collection
    * tool-driven vs framework-driven approaches
    * choosing tooling appropriate to team size
<!-- chapter: building-metrics-yourself, duration: 3h -->
* Building metrics yourself
    * source data: `Git`, ticket system, `CI`, deployment, paging
    * normalizing across systems
    * handling missing data without lying about it
    * dashboards engineers actually look at
    * cross-reference to the Data Quality course
    * the cost of a homemade metrics pipeline
<!-- chapter: metrics-and-incentives, duration: 2h -->
* Metrics and incentives
    * separating measurement from compensation
    * the metric-as-target trap
    * promotion criteria and engineering metrics
    * team-level metrics in performance reviews
    * the engineer who asks "is this in my review"
<!-- chapter: metrics-for-platform-and-data-teams, duration: 2h -->
* Metrics for platform and data teams
    * `DORA` for platform teams: how it differs
    * platform success metrics: adoption, time-to-onboard, `NPS`
    * data team metrics: pipeline freshness, quality, cost
    * cross-reference to the Platform Engineering course
    * cross-reference to the Data Quality course
<!-- chapter: benchmarking-against-the-industry, duration: 2h -->
* Benchmarking against the industry
    * the public `DORA` benchmarks
    * `DX` benchmarks
    * `Stack Overflow` developer survey usage
    * comparing fairly across companies
    * the survivorship bias in public engineering blog posts
<!-- chapter: case-studies-and-failure-modes, duration: 1h -->
* Case studies and failure modes
    * the team that hit elite `DORA` and burned out
    * the metrics dashboard nobody used
    * the engineering manager who weaponized metrics
    * a public `DORA` retrospective from a real organization
    * recovering from a metrics rollout that went badly
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * design a metrics program for a sample team
    * group review of a draft engineering scorecard
    * recommended reading: `Forsgren`/`Humble`/`Kim`, `DX` papers, `Reinertsen`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
