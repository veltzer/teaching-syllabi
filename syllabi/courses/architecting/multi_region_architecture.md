---
tags:
  - concepts:architecture
  - concepts:distributed-systems
  - concepts:scalability
  - concepts:best-practices
level: advanced
category: architecture
duration_hours: 24
audience:
  - audiences:architects
  - audiences:senior-developers
  - audiences:devops
  - audiences:team-leads
---
<!-- course: multi_region_architecture -->
# Multi-Region Architecture

## Description
Going multi-region is one of the most consequential architectural decisions a system can `make`. It is also
one of the most commonly made for the wrong reason. The catalog covers `Disaster Recovery`,
`Distributed Systems Tradeoffs`, and `Multi-Cloud Networking`. None of those covers the specific
discipline of designing, building, and operating a service that runs in multiple geographic regions
simultaneously.

This three day course covers multi-region architecture as practiced today. It covers the motivations
that justify multi-region (latency to users, regulatory data residency, regional disaster recovery,
business continuity) and the motivations that do not, the topology choices (active-passive,
active-active, follower-reads, regional-shards), the data layer as the hardest problem (the
single-writer model, multi-writer with last-writer-wins, multi-writer with conflict-free types,
geo-partitioning), the routing layer (`DNS`, Anycast, `GeoDNS`), the failover question, the
multi-region operations problem (rolling deploys, multi-region observability, multi-region incident
response), and the cost story. Examples are drawn from the public engineering writing of Stripe,
`Cloudflare`, Shopify, `DynamoDB Global Tables`, Spanner, and `CockroachDB`. Participants leave
able to `make` the multi-region decision deliberately, design the data layer correctly, and operate the
result.

## Duration
24 hours / 3 days

## Intended Audience
* architects deciding whether to `go` multi-region
* senior developers building multi-region services
* platform engineers operating multi-region infrastructure
* tech leads accountable for `RTO` and `RPO`

## Prerequisites
* `solid` distributed systems background
* exposure to the Distributed Systems Tradeoffs course
* working experience with at least one cloud provider
* familiarity with the Disaster Recovery course is helpful

## Objectives
* decide whether multi-region is justified for the system at hand
* choose the right topology for the workload
* design the data layer for the chosen topology
* implement region-aware routing
* operate a multi-region service safely
* recognize the cost shape of multi-region
* avoid the common multi-region failure modes

## Outline
<!-- chapter: why-go-multi-region, duration: 1h -->
* Why `go` multi-region
    * latency to users
    * regulatory data residency
    * regional disaster recovery
    * business continuity
    * the bad reason: it sounded good in the strategy deck
    * the cost of not knowing why
<!-- chapter: topology-choices, duration: 2h -->
* Topology choices
    * active-passive
    * active-active
    * follower-reads with single-region writes
    * geo-sharded
    * the cell-based architecture variant
    * picking the topology
<!-- chapter: the-data-layer-as-the-hard-part, duration: 3h -->
* The data layer as the hard part
    * the `CAP` theorem revisited in geographic terms
    * write latency vs read latency vs availability
    * the "we made the database multi-region and it got slower" failure
    * cross-reference to the Distributed Systems Tradeoffs course
    * the data-residency constraint as a forcing function
<!-- chapter: single-writer-multi-region, duration: 2h -->
* Single-writer multi-region
    * one region writes, others follow
    * the read-from-local-follower pattern
    * the read-your-writes problem
    * `Aurora Global Database`, `Cloud SQL` cross-region replicas
    * the failover-promotes-a-follower story
<!-- chapter: multi-writer-multi-region, duration: 3h -->
* Multi-writer multi-region
    * `DynamoDB Global Tables` and last-writer-wins
    * `CockroachDB`, Spanner, `YugabyteDB`
    * `Cassandra` multi-`DC`
    * the conflict-resolution strategy
    * the application-level reconciliation
<!-- chapter: geo-partitioning, duration: 2h -->
* Geo-partitioning
    * the user-pinned-to-region model
    * the row-level region tag
    * the "user moved regions and broke" edge case
    * the regional-failover question
    * the `GDPR` data-residency case
<!-- chapter: routing-and-traffic-management, duration: 2h -->
* Routing and traffic management
    * `DNS`-based geo-routing
    * `Anycast` and the `BGP` story
    * `Route 53`, `Cloud DNS`, `Azure Traffic Manager`, `Cloudflare`
    * the failover-`DNS` `TTL` story
    * the "`DNS` cached too long and we sent traffic to a dead region" failure
<!-- chapter: caches-and-multi-region, duration: 1h -->
* Caches and multi-region
    * per-region cache vs global cache
    * cache-warming after failover
    * the "the cache was empty and we melted the database" failure
    * `CDN` placement
    * cross-reference to the Edge Computing and `CDN` course
<!-- chapter: the-failover, duration: 2h -->
* The failover
    * planned failover vs unplanned
    * automated failover and the split-brain risk
    * the failover runbook
    * the failover drill cadence
    * the "we never tested the failover and it failed" reality
<!-- chapter: deployment-across-regions, duration: 2h -->
* Deployment across regions
    * region-by-region rollout
    * the bake-time per region
    * the "all regions failed because we deployed everywhere at once" outage
    * cross-reference to the Release Engineering course
    * the regional kill-switch
<!-- chapter: observability-multi-region, duration: 1h -->
* Observability multi-region
    * per-region dashboards
    * cross-region trace propagation
    * the "we did not know which region was failing" incident
    * the global aggregation question
    * cross-reference to the `OpenTelemetry` Deep Dive course
<!-- chapter: incident-response-multi-region, duration: 1h -->
* Incident response multi-region
    * the follow-the-sun on-call
    * the regional commander pattern
    * cross-reference to the Incident Response and Postmortems course
    * the time-zone handover problem
    * the "wrong region was paged" failure
<!-- chapter: cost-shape-of-multi-region, duration: 1h -->
* Cost shape of multi-region
    * the replication tax
    * the cross-region egress cost
    * the duplicated-capacity cost
    * cross-reference to the Cost-Aware Architecture course
    * the "we underestimated by 3x" reality
<!-- chapter: when-not-to-go-multi-region, duration: 1h -->
* `When` not to `go` multi-region
    * the team that cannot operate one region well
    * the system whose users are in one region
    * the system whose database cannot be multi-region
    * the cheaper alternative: cell-based single-region
    * the staged path to multi-region

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
