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
<!-- course: cell_based_architecture -->
# Cell-Based Architecture

## Description
Cell-based architecture is the pattern that gives a large system a hard upper bound on blast `radius`. Instead
of running one large service that, when something goes wrong, takes down every customer at once, the system
is partitioned into independent `cells`. Each cell is a complete, self-contained unit. Customers are routed
to a cell, and a failure in one cell affects only the customers in that cell. The catalog has
`Multi-Region Architecture`, `Microservices Architecture`, `Multi-tenant SaaS Architecture`, and
`Disaster Recovery in Practice`. None of those is the same conversation as cell-based design — cells are
the alternative to "`make` the whole system reliable enough" that `AWS`, Slack, `Salesforce`, and the major
cloud providers have converged on for systems where blast `radius` is the primary risk.

This three day course covers cell-based architecture as practiced today. It covers the motivation (blast
`radius` bounded by design), the cell as the unit of isolation, the routing layer that sits in front of the
cells, the placement decision (which customer goes in which cell), the deployment model (each cell deploys
independently), the operational model (each cell is observed and operated separately), the cell-migration
problem (moving a customer between cells), the cost shape (more cells means more overhead), and the
patterns that `make` cells work or fail. Examples are drawn from `AWS`'s public talks on `EC2`, `S3`, and
`DynamoDB` cell architectures, Slack's cell migration, and `Salesforce`'s pod model. Participants leave
able to design a cell-based system, decide on the cell size, and operate a fleet of cells.

## Duration
24 hours / 3 days

## Intended Audience
* architects designing systems whose failure mode is "everyone is down"
* senior developers building services that need bounded blast `radius`
* `DevOps` engineers operating large multi-tenant systems
* team leads accountable for availability across a customer base

## Prerequisites
* `solid` distributed systems background
* exposure to the Distributed Systems Tradeoffs course
* familiarity with the Multi-Region Architecture course is helpful
* working experience with at least one cloud provider

## Objectives
* explain what a cell is and what it is not
* size cells correctly for the workload
* design the routing layer that places traffic on cells
* migrate customers between cells safely
* operate a fleet of cells with the right observability
* recognize when cell-based is overkill
* compare cell-based to multi-region and to `microservices`

## Outline
<!-- chapter: what-a-cell-actually-is, duration: 1h -->
* What a cell actually is
    * a complete, self-contained vertical slice
    * the difference from a microservice
    * the difference from a region
    * the difference from a tenant
    * cross-reference to the Multi-tenant `SaaS` Architecture course
    * the canonical examples: `EC2`, `S3`, `DynamoDB`, Slack pods
<!-- chapter: blast-radius-as-a-first-class-concern, duration: 2h -->
* Blast `radius` as a first-class concern
    * the "everyone is down" failure mode
    * the percentage-of-customers-affected metric
    * the cell as the bound on impact
    * the trade-off vs operational complexity
    * the "we never thought about blast `radius`" reality
<!-- chapter: cell-sizing, duration: 2h -->
* Cell sizing
    * customers per cell
    * the cost-vs-blast-`radius` trade-off
    * the operational-overhead-per-cell cost
    * the cell-saturation metric
    * worked example
<!-- chapter: the-routing-layer, duration: 2h -->
* The routing layer
    * the cell router as the only shared component
    * the customer-to-cell mapping
    * the static map vs dynamic placement
    * the routing layer's own availability
    * the "the router became the single point of failure" trap
<!-- chapter: placement-strategies, duration: 2h -->
* Placement strategies
    * round-robin placement
    * load-balanced placement
    * tiered placement (premium customers in their own cells)
    * geographic placement
    * the "hot cell" failure
<!-- chapter: cell-deployment, duration: 2h -->
* Cell deployment
    * one deploy per cell
    * the wave-based rollout
    * the canary cell
    * cross-reference to the Release Engineering course
    * the "we deployed all cells at once and it broke" failure
<!-- chapter: cell-observability, duration: 2h -->
* Cell observability
    * per-cell dashboards
    * cell-level `SLOs`
    * the aggregated view across cells
    * cross-reference to the `SLOs` and Error Budgets course
    * the "we have a thousand cells and a thousand dashboards" problem
<!-- chapter: cell-migration, duration: 3h -->
* Cell migration
    * the moving-a-customer problem
    * the live-migration approach
    * the export-and-import approach
    * the cutover and the rollback
    * the "migration broke the customer" failure
    * worked example: Slack's pod migration
<!-- chapter: data-and-state-in-cells, duration: 2h -->
* Data and state in cells
    * the database per cell
    * the cross-cell-query problem
    * the data-sharing-across-cells anti-pattern
    * the analytics warehouse outside the cells
    * the cell as the data-residency boundary
<!-- chapter: shared-services-and-the-control-plane, duration: 2h -->
* Shared services and the control plane
    * the control plane vs the data plane
    * the shared identity service
    * the shared billing service
    * the "the shared service took down all cells" incident
    * the design rule: only stateless shared services
<!-- chapter: cell-failure-modes, duration: 1h -->
* Cell failure modes
    * a cell goes down
    * a cell becomes a hot cell
    * a cell becomes a slow cell
    * the "the router routed around the dead cell" win
    * the per-cell circuit breaker
<!-- chapter: cells-vs-multi-region-vs-microservices, duration: 2h -->
* Cells vs multi-region vs `microservices`
    * cells are isolation, regions are geography, `microservices` are decomposition
    * combining them: cells in regions
    * the "we did all three" complexity tax
    * picking the right one for the problem
    * cross-reference to the `Microservices` Architecture course
<!-- chapter: when-not-to-go-cell-based, duration: 1h -->
* `When` not to `go` cell-based
    * the system that does not have enough customers to justify it
    * the team that cannot operate a fleet of cells
    * the "we made everything worse to gain isolation" failure
    * the cheaper alternative: a single well-tested system
    * the staged path to cells

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
