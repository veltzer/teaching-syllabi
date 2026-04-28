---
tags:
  - concepts:version-control
  - concepts:best-practices
  - concepts:developer-experience
  - concepts:agile
  - concepts:testing
  - concepts:gitops
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
<!-- course: trunk_based_development_and_ci -->
# Trunk-Based Development and `CI`

## Description
Most teams that say they do continuous integration do not. Long-lived feature branches, manual gating,
end-of-sprint integration crunches and week-long merge battles are still the norm in many places. Trunk-based
development (`TBD`) is the workflow that the highest-performing teams in the `DORA` and `Accelerate` research
actually use, and it is fundamentally a discipline, not a tool.

This five day course covers `TBD` end to end. It covers the idea (small, frequent integrations to a single
shared trunk), the practices that `make` it work (feature flags, branch by abstraction, expand-and-contract,
automated tests at every change), the `CI` pipeline architecture that supports it, the migration story from
`GitFlow` or release-branch workflows, and the cultural and organizational implications. Examples are drawn
from `Google`, `Facebook`, `Etsy`, `Stripe` and `LinkedIn`. Participants leave able to introduce or stabilize
trunk-based development on their own teams and to design the `CI` discipline that backs it.

## Duration
40 hours / 5 days

## Intended Audience
* developers and tech leads adopting or stabilizing trunk-based development
* `DevOps` engineers building the `CI` pipeline that `TBD` requires
* engineering managers driving a workflow change
* architects whose system design enables or blocks `TBD`
* engineers stuck in `GitFlow` and wondering why everything is hard

## Prerequisites
* working knowledge of `Git`
* basic familiarity with at least one `CI` system (`GitHub Actions`, `GitLab CI`, `Jenkins`, etc.)
* some experience working on a team with a shared codebase

## Objectives
* describe trunk-based development precisely and the variants that count
* design a `CI` pipeline that makes `TBD` viable
* apply the techniques (feature flags, branch by abstraction, expand-and-contract) that hide work in progress
* migrate a team from `GitFlow` or release-branch workflow without breakage
* keep the trunk green continuously
* measure the practices that matter: lead time, change failure rate, deployment frequency
* recognize the organizational changes `TBD` requires

## Outline
<!-- chapter: what-trunk-based-development-is, duration: 2h -->
* What trunk-based development is
    * the original definition (Paul Hammant)
    * the spectrum: scaled `TBD`, short-lived branches, direct-to-trunk
    * the `DORA`/`Accelerate` evidence
    * what `TBD` is not: chaos, no review, no testing
    * `TBD` and continuous integration as one practice
<!-- chapter: why-not-gitflow, duration: 2h -->
* Why not `GitFlow`
    * `GitFlow` and the long-lived branch tax
    * the integration debt that builds up
    * release branches and the merge nightmare
    * code review delay and stale review
    * `GitHub Flow`, `GitLab Flow`, `OneFlow` as middle grounds
    * recognizing `when` `GitFlow` is actually right
<!-- chapter: short-lived-branches-and-direct-to-trunk, duration: 3h -->
* Short-lived branches and direct-to-trunk
    * the under-a-day branch lifetime
    * direct commits to trunk: `Google` and `Facebook`'s model
    * pull requests as a soft form of `TBD`
    * the cost-of-delay argument for short branches
    * how to structure work into one-day chunks
    * negotiating "but my change is too big" with reality
<!-- chapter: feature-flags-as-a-tbd-enabler, duration: 3h -->
* Feature flags as a `TBD` enabler
    * the role of flags in keeping unfinished work in trunk
    * flag scope: dev-only, internal, beta, GA
    * cross-reference to the Feature Flags and Progressive Delivery course
    * flag lifetime discipline
    * the "merged dark" pattern
    * flags vs `if-disabled` checks
<!-- chapter: branch-by-abstraction, duration: 3h -->
* Branch by abstraction
    * the pattern in detail
    * the abstraction step
    * the parallel implementation step
    * the cutover step
    * the cleanup step
    * branch by abstraction for cross-cutting changes
    * combining with feature flags
<!-- chapter: expand-and-contract-for-data-and-apis, duration: 3h -->
* Expand and contract for data and `APIs`
    * the expand-and-contract pattern (also called parallel-change)
    * applying it to database migrations
    * applying it to `API` contracts
    * applying it to message schemas
    * keeping the system shippable at every step
    * cross-reference to the `API` Evolution course
<!-- chapter: continuous-integration-the-discipline, duration: 3h -->
* Continuous integration: the discipline
    * the original `XP` definition (`Beck`, `Fowler`)
    * commit at least daily
    * green trunk as a non-negotiable
    * fixing the build before anything else
    * the "stop the line" cultural rule
    * `CI` vs `CD` vs continuous deployment
<!-- chapter: ci-pipeline-architecture, duration: 3h -->
* `CI` pipeline architecture
    * the test pyramid for `CI`
    * fast feedback: under 10 minutes for the first signal
    * parallelization, sharding, test selection
    * pre-merge vs post-merge testing
    * `merge` queues and `merge` trains
    * caching, build avoidance and remote build execution
<!-- chapter: keeping-the-build-fast, duration: 3h -->
* Keeping the build fast
    * recognizing build-time creep
    * test selection and impact analysis
    * flaky tests as a build-speed problem
    * `bazel`, `nx`, `turborepo` for incremental builds
    * test parallelization at scale
    * caching artifacts across `CI` runs
<!-- chapter: handling-flaky-tests, duration: 2h -->
* Handling flaky tests
    * the cost of a single flaky test on a `TBD` team
    * detection and quarantine
    * root-causing flakes
    * flake budgets and policy
    * automated retries and their dangers
    * the "fix it or delete it" rule
<!-- chapter: code-review-in-tbd, duration: 2h -->
* Code review in `TBD`
    * pre-merge vs post-merge review
    * post-commit review at `Google`
    * stacked diffs and stacked `PRs`
    * keeping reviews under an hour
    * cross-reference to the Code Review course
<!-- chapter: deploying-from-trunk, duration: 3h -->
* Deploying from trunk
    * continuous deployment vs `continuous delivery`
    * the deploy-on-green pipeline
    * canary, blue-green, rolling deploys
    * automatic rollback on regression
    * the bakery model: every commit is releasable
    * progressive delivery as the default
<!-- chapter: scaling-tbd-across-many-teams, duration: 2h -->
* Scaling `TBD` across many teams
    * monorepo vs polyrepo `TBD`
    * `Google`-scale `TBD`: large repository, single trunk
    * release trains for shared products
    * the role of `CODEOWNERS` and review automation
    * cross-team breaking changes
<!-- chapter: migrating-to-tbd, duration: 3h -->
* Migrating to `TBD`
    * the realistic stepwise migration
    * starting with shorter feature branches
    * the green-trunk hackathon
    * preserving release stability during the migration
    * organizational pre-conditions
    * common reasons migrations fail
<!-- chapter: case-studies-and-anti-patterns, duration: 2h -->
* Case studies and anti-patterns
    * `Google`, `Facebook` and `Etsy` `TBD` rollouts
    * "trunk-based development" by name only
    * the perpetually red trunk
    * the team that flagged everything but never cleaned up
    * the team that adopted `TBD` and then stopped reviewing code
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * design walkthrough of a `TBD` `CI` pipeline for a sample team
    * `DORA` self-assessment
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
