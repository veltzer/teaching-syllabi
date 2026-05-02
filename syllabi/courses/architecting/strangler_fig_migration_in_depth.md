---
tags:
  - concepts:architecture
  - concepts:migration
  - concepts:best-practices
  - concepts:design-patterns
level: advanced
category: architecture
duration_hours: 24
audience:
  - audiences:architects
  - audiences:senior-developers
  - audiences:team-leads
  - audiences:developers
---
<!-- course: strangler_fig_migration_in_depth -->
# Strangler Fig Migration in Depth

## Description
The Strangler Fig is the canonical pattern for migrating a legacy system to a new system without a big-bang
cutover. The catalog has `Legacy Modernization` and `Code Modernization and Legacy Rescue`. Both touch the
strangler pattern; neither covers it as a full engineering discipline. The strangler is more than "route
some traffic to a new service" — it is a migration approach with its own routing infrastructure, data
synchronization story, identity-and-state-sharing problem, deployment cadence, and verification model.
Most strangler migrations fail not because the pattern is wrong but because the team underestimated the
infrastructure required to support a long-running parallel-systems phase.

This three day course covers the strangler fig as a migration discipline. It covers the routing layer
(what decides whether a request goes to old or new), the migration unit (an endpoint, a feature, a
customer cohort, a tenant), the data synchronization model (the new system reads from old, writes to
both, eventually owns), the identity-and-session question, the verification approach (shadow traffic,
diff, score), the rollback story, the long-tail problem (the last 5 percent that is impossible to
migrate), the team and organizational shape that makes it work, and the metrics that tell you whether
the migration is succeeding. Examples are drawn from the public engineering writing of Stripe,
`Shopify`, `GitHub`, Etsy, and `Monzo`. Participants leave able to plan, execute, and finish a
strangler migration.

## Duration
24 hours / 3 days

## Intended Audience
* architects leading a system migration
* senior developers writing the strangler routing layer
* team leads accountable for the migration finishing
* developers working on either side of a strangler-in-progress

## Prerequisites
* working experience on a legacy system
* exposure to the Legacy Modernization course is helpful
* familiarity with at least one routing or proxy technology
* basic understanding of database replication

## Objectives
* design a strangler migration end-to-end
* build the routing layer correctly
* synchronize data between old and new systems
* verify the new system before promoting it
* finish the migration (the hardest part)
* recognize the patterns that doom strangler migrations
* connect the migration to organizational change

## Outline
<!-- chapter: what-the-strangler-fig-actually-is, duration: 1h -->
* What the Strangler Fig actually is
    * Martin Fowler's original article
    * the metaphor and what it implies
    * the difference from rewrite
    * the difference from rip-and-replace
    * cross-reference to the Legacy Modernization course
<!-- chapter: the-routing-layer, duration: 2h -->
* The routing layer
    * proxy vs in-app routing
    * `nginx`, Envoy, `HAProxy` as the strangler proxy
    * the per-endpoint routing rule
    * the per-customer routing rule
    * the dynamic-config approach
    * the "we hard-coded routes and could not change them" failure
<!-- chapter: choosing-the-migration-unit, duration: 2h -->
* Choosing the migration unit
    * endpoint by endpoint
    * feature by feature
    * customer by customer
    * tenant by tenant
    * picking for the system at hand
    * the "we picked the wrong unit and it took 4 years" reality
<!-- chapter: data-synchronization, duration: 3h -->
* Data synchronization
    * the new system reads from old
    * the new system writes to both
    * the new system owns the write
    * cross-reference to the Change Data Capture in Depth course
    * cross-reference to the Database Migration Strategies course
    * the "we got the dual-write order wrong and corrupted data" failure
<!-- chapter: identity-and-session-sharing, duration: 2h -->
* Identity and session sharing
    * cookies that work in both systems
    * the shared session store
    * the shared `JWT` and the issuer question
    * cross-reference to the `OAuth2` and `OIDC` course
    * the "users got logged out every time we routed them" failure
<!-- chapter: shadow-traffic-and-verification, duration: 3h -->
* Shadow traffic and verification
    * shadow traffic as the safety net
    * diffing responses old vs new
    * `GitHub`'s `Scientist` library
    * scoring and the false-positive
    * the "shadow traffic looked fine but production was broken" failure
<!-- chapter: rollback-and-the-rollback-budget, duration: 2h -->
* Rollback and the rollback budget
    * the per-rule rollback
    * the data-rollback question
    * the "we cannot roll back because we wrote to the new database" trap
    * the time-bounded rollback window
    * cross-reference to the Release Engineering course
<!-- chapter: the-long-tail-problem, duration: 2h -->
* The long-tail problem
    * the last 5 percent that is hardest
    * the legacy endpoint that one customer still uses
    * the rare-but-critical workflow
    * the deprecation-and-deadline approach
    * the "we never finished and lived with both systems forever" failure
<!-- chapter: the-team-shape, duration: 1h -->
* The team shape
    * the migration team vs the feature team
    * the "we asked feature teams to migrate too" failure
    * the strangler ownership question
    * the long-running migration as a project
    * the migration as a product
<!-- chapter: metrics-of-a-migration, duration: 2h -->
* Metrics of a migration
    * percent-of-traffic-on-new
    * percent-of-data-on-new
    * percent-of-features-on-new
    * the velocity-of-migration metric
    * the "the dashboard said 95 percent and we celebrated for two years" anti-pattern
<!-- chapter: organizational-pre-conditions, duration: 1h -->
* Organizational pre-conditions
    * the executive sponsor
    * the migration as a deadline
    * the "everyone agrees we should migrate but nobody is funded" failure
    * the team that can be dedicated
    * the calendar reality
<!-- chapter: case-studies, duration: 2h -->
* Case studies
    * Stripe's pre-Stripe to Stripe migration story
    * `Shopify`'s `monolith` decomposition
    * `Etsy`'s `PHP` to `multi-stack` migration
    * `Monzo`'s migration patterns
    * the abandoned migrations and what we can learn
<!-- chapter: when-not-to-strangler, duration: 1h -->
* `When` not to strangler
    * the system small enough to rewrite
    * the system on a forced deadline
    * the team that cannot maintain two systems
    * the "we strangler-ed for a year and gave up" reality
    * picking another approach instead

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
