---
tags:
  - concepts:architecture
  - concepts:cloud-economics
  - concepts:best-practices
  - concepts:operations
level: advanced
category: cloud
duration_hours: 24
audience:
  - audiences:architects
  - audiences:senior-developers
  - audiences:team-leads
  - audiences:devops
---
<!-- course: cost_aware_architecture -->
# Cost-Aware Architecture

## Description
The catalog already has a `Cloud Cost Optimization` course and a `FinOps` course. Both treat cost as
something to be measured and reduced after a system exists. This course is the architectural complement.
It treats cost as an input to design, not a thing to optimize after the fact. It is the difference between
"how do we lower the bill" and "what should the bill be, and why."

This three day course walks through the design decisions that compound into the cost of a system: data
gravity and egress, the choice of storage class, the choice of database, the choice of compute primitive,
serverless versus container versus `VM`, the cost shape of caching, the cost shape of fan-out, the cost
shape of multi-region, the cost shape of observability, the way single-tenant vs multi-tenant affects unit
economics. Examples are drawn from the public engineering blogs of `Netflix`, `Honeycomb`, `Discord`,
`Notion`, `Cloudflare` and `Basecamp`'s public exit-from-cloud write-ups. Participants leave able to `make`
the cost case for an architectural decision before they ship it, not after the bill arrives.

## Duration
24 hours / 3 days

## Intended Audience
* architects responsible for cost as a non-functional requirement
* senior developers leading service design decisions
* tech leads whose `P&L` includes the cloud bill
* platform engineers building paved roads that others will spend money on

## Prerequisites
* working experience with at least one major cloud provider
* exposure to the `Cloud Cost Optimization` course is helpful but not required
* familiarity with the basic primitives: object storage, managed databases, container platforms

## Objectives
* recognize the cost-shape of common architectural primitives
* compute the unit economics of a feature before it ships
* design data flow with egress and storage class in mind
* pick the right compute primitive for the workload's cost shape
* anticipate the cost-failure modes of multi-tenant systems
* push back on architectural patterns that cannot be afforded
* communicate cost trade-offs to non-engineering stakeholders

## Outline
<!-- chapter: why-cost-is-an-architectural-concern, duration: 1h -->
* Why cost is an architectural concern
    * the bill as a leading indicator of bad architecture
    * the difference between optimization and design
    * cross-reference to the `Cloud Cost Optimization` course
    * cross-reference to the `FinOps` course
    * who owns the bill in your organization
<!-- chapter: unit-economics-as-a-design-input, duration: 2h -->
* Unit economics as a design input
    * cost-per-request, cost-per-tenant, cost-per-feature
    * the back-of-envelope before the design doc
    * gross margin and the engineering decision
    * the "we cannot afford to support that customer" failure
    * worked example: a cost model on one page
<!-- chapter: the-cost-shape-of-storage, duration: 2h -->
* The cost shape of storage
    * object storage classes and the access pattern
    * the lifecycle policy as part of the schema
    * the "we have a petabyte of logs nobody reads" failure
    * block, `file`, object: `when` each is the wrong choice
    * the snapshot multiplier
<!-- chapter: the-cost-shape-of-data-movement, duration: 2h -->
* The cost shape of data movement
    * egress as the largest unmodelled cost
    * cross-region and cross-`AZ` traffic
    * the data-gravity argument
    * the "every microservice talks to every other" cost
    * `CDN` and the offload argument
<!-- chapter: the-cost-shape-of-databases, duration: 2h -->
* The cost shape of databases
    * `IOPS` and the storage tier
    * the read replica and the write amplifier
    * managed vs self-hosted: total cost not unit cost
    * the "we picked a serverless database for a steady workload" failure
    * cross-reference to the Database Internals course
<!-- chapter: the-cost-shape-of-compute, duration: 3h -->
* The cost shape of compute
    * spot, reserved, savings plan, on-demand
    * `Lambda` vs `Fargate` vs `EC2` vs `Kubernetes`
    * the cold start tax
    * the always-on tax
    * the right-sizing problem
    * `ARM` and the architecture choice
<!-- chapter: the-cost-shape-of-serverless, duration: 2h -->
* The cost shape of serverless
    * the per-invocation model
    * the "fan-out blew up the bill" failure
    * the duration-and-memory product
    * idle cost vs busy cost
    * `when` serverless wins and `when` it loses
<!-- chapter: the-cost-shape-of-caching, duration: 2h -->
* The cost shape of caching
    * the cache as a cost-shifter
    * memory cost vs compute cost vs egress cost
    * the cache miss as a tail latency amplifier
    * `CDN` caching, application caching, database caching
    * cache invalidation as a cost driver
<!-- chapter: the-cost-shape-of-multi-tenant-systems, duration: 2h -->
* The cost shape of multi-tenant systems
    * shared vs siloed vs pooled
    * the noisy-neighbor cost
    * cross-reference to the Multi-tenant `SaaS` Architecture course
    * the "one customer is using 90 percent of capacity" failure
    * unit cost by tenant cohort
<!-- chapter: the-cost-shape-of-multi-region, duration: 2h -->
* The cost shape of multi-region
    * the replication tax
    * the conflict-resolution tax
    * the "we went multi-region for marketing" failure
    * which workloads actually need it
    * cross-reference to the Multi-region Architecture course
<!-- chapter: the-cost-shape-of-observability, duration: 2h -->
* The cost shape of observability
    * cardinality as a cost driver
    * sampling as a design decision
    * log volume vs log value
    * the "our observability bill exceeds our infra bill" failure
    * tiered retention
<!-- chapter: cost-as-a-non-functional-requirement, duration: 2h -->
* Cost as a non-functional requirement
    * cost budgets in the design doc
    * the cost `SLO`
    * cost regression testing
    * the cost-architecture review meeting
    * how to push back on a request that is too expensive

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
