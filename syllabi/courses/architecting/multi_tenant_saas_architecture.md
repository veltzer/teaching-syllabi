---
tags:
  - concepts:architecture
  - concepts:scalability
  - concepts:distributed-systems
  - concepts:microservices
  - concepts:security
  - concepts:identity
  - concepts:cloud-economics
level: intermediate
category: architecture
duration_hours: 40
audience:
  - audiences:architects
  - audiences:developers
  - audiences:senior-developers
  - audiences:team-leads
---
<!-- course: multi_tenant_saas_architecture -->
# Multi-Tenant `SaaS` Architecture

## Description
Building a `SaaS` product is not the same as building a regular web application running once per customer. Multi-tenant
`SaaS` introduces concerns that single-tenant systems never have to face: how to share infrastructure between thousands
of customers without leaking data, how to scale per-tenant load that varies by orders of magnitude, how to bill tenants
proportionally to their usage, and how to onboard, upgrade, isolate and offboard tenants without manual intervention.

This five day course is dedicated to those concerns. It covers tenancy models (silo, pool, bridge and hybrid), identity
and access at tenant boundaries, data isolation strategies, per-tenant scaling and noisy-neighbor mitigation, tenant
lifecycle automation, configurability, billing and metering, and operational concerns including observability, support
and per-tenant `SLOs`. Participants leave able to design a new `SaaS` from scratch with a coherent tenancy story or to
refactor an existing single-tenant system into a viable multi-tenant product.

## Duration
40 hours / 5 days

## Intended Audience
* architects designing or evolving multi-tenant `SaaS` products
* senior developers responsible for tenancy-sensitive parts of the platform
* engineering managers and tech leads on `SaaS` teams
* engineers extracting a multi-tenant product out of a single-tenant codebase

## Prerequisites
* `solid` web application development experience
* familiarity with at least one cloud provider (`AWS`, `GCP`, `Azure`)
* basic understanding of databases, identity, and `HTTP`
* ideally some experience operating a production system

## Objectives
* compare tenancy models and pick the right one for a given product and customer profile
* design tenant identification and isolation at every layer of the stack
* implement data isolation strategies and reason about their trade-offs
* address noisy-neighbor problems and per-tenant scaling
* automate tenant lifecycle: onboarding, upgrades, suspension, offboarding
* design metering and billing systems that align with the cost model
* run a multi-tenant system with appropriate observability and support tooling
* migrate an existing single-tenant system to multi-tenant safely

## Outline
<!-- chapter: what-makes-saas-different, duration: 2h -->
* What makes `SaaS` different
    * single-tenant, multi-instance, multi-tenant
    * the economic case for multi-tenancy
    * customer expectations: isolation, customization, compliance
    * the engineering cost of multi-tenancy
    * `B2B` `SaaS` vs `B2C` `SaaS` vs platform-as-a-service
<!-- chapter: tenancy-models, duration: 3h -->
* Tenancy models
    * silo: dedicated stack per tenant
    * pool: shared everything, tenant identifier in every request
    * bridge: shared compute, dedicated data
    * hybrid models for premium tiers
    * choosing a model from product and customer constraints
    * mixing models within a single product
<!-- chapter: tenant-identification-and-routing, duration: 2h -->
* Tenant identification and routing
    * subdomain, path, header and `JWT`-claim based identification
    * resolving the tenant at the edge
    * tenant context propagation across services
    * the tenant context object and its discipline
    * dealing with cross-tenant operations safely
<!-- chapter: identity-and-access-for-multi-tenant-systems, duration: 3h -->
* Identity and access for multi-tenant systems
    * tenant `IDs`, user `IDs` and the relationship between them
    * `SSO` per tenant: `SAML`, `OIDC`, `SCIM`
    * per-tenant identity providers
    * `B2B` user invites and cross-tenant users
    * delegated administration
    * audit logs scoped per tenant
<!-- chapter: authorization-models-rbac-and-beyond, duration: 3h -->
* Authorization models: `RBAC` and beyond
    * tenant-scoped `RBAC`
    * `ABAC` for tenant-aware policies
    * relationship-based access control (`Zanzibar`/`OpenFGA`)
    * choosing between policy engines: `OPA`, `Cerbos`, in-app
    * the cost of getting authorization wrong in a multi-tenant system
<!-- chapter: data-isolation-at-the-database-layer, duration: 4h -->
* Data isolation at the database layer
    * separate database per tenant
    * separate schema per tenant
    * shared schema with tenant `ID` column
    * row-level security (`PostgreSQL` `RLS`)
    * implications for migrations, backups and connection pooling
    * comparing options on cost, isolation and operational pain
    * data residency and per-tenant database placement
<!-- chapter: data-isolation-at-other-layers, duration: 2h -->
* Data isolation at other layers
    * `file` storage isolation: bucket per tenant vs prefix per tenant
    * cache isolation and per-tenant cache keys
    * search index isolation
    * message bus and queue isolation
    * `LLM` and embedding isolation
<!-- chapter: noisy-neighbors-and-per-tenant-resource-management, duration: 3h -->
* Noisy neighbors and per-tenant resource management
    * what a noisy neighbor actually looks like in production
    * per-tenant rate limiting and quota
    * fair queueing and token bucket strategies
    * per-tenant background job isolation
    * resource pools per tenant tier
    * detecting and mitigating live noisy-neighbor incidents
<!-- chapter: per-tenant-scaling-and-sharding, duration: 3h -->
* Per-tenant scaling and sharding
    * sharding by tenant
    * tenant migration between shards
    * scaling out very large tenants
    * scaling down dormant tenants to near-zero cost
    * mixing big and small tenants on shared infrastructure
    * cell-based architectures
<!-- chapter: tenant-lifecycle-automation, duration: 3h -->
* Tenant lifecycle automation
    * self-service tenant signup
    * onboarding flows and time-to-first-value
    * tenant configuration and feature flags per tenant
    * suspending and reactivating tenants
    * `GDPR`-compliant offboarding and data deletion
    * exporting tenant data for portability
<!-- chapter: configurability-and-customization, duration: 2h -->
* Configurability and customization
    * the configurability axis: nothing, settings, plug-ins, custom code
    * per-tenant feature flags
    * white-labeling and branding
    * per-tenant workflows and rules
    * the limits of safe customization in a `SaaS`
<!-- chapter: metering-and-billing, duration: 3h -->
* Metering and billing
    * billing models: per-seat, per-usage, tiered, hybrid
    * the metering pipeline: emit, aggregate, bill
    * accuracy, idempotency and replay in metering
    * tying technical metrics to invoiceable units
    * `Stripe` `Billing`, `Orb`, `Lago`, `Metronome`
    * showing usage and cost back to the customer
<!-- chapter: deployment-topologies-and-cells, duration: 2h -->
* Deployment topologies and cells
    * single regional deployment
    * multi-region deployment
    * cell-based architecture (`AWS`-style cells)
    * blast-`radius` reduction through cells
    * tenant placement and rebalancing
<!-- chapter: observability-for-multi-tenant-systems, duration: 2h -->
* Observability for multi-tenant systems
    * tenant `ID` in every log line, span and metric
    * per-tenant dashboards
    * per-tenant `SLOs` and `SLAs`
    * cardinality cost of tenant-tagged metrics
    * tenant-aware alerting
<!-- chapter: support-and-operations, duration: 1h -->
* Support and operations
    * support staff impersonation safely
    * tenant-scoped feature flags for incident mitigation
    * runbooks for tenant-specific issues
    * the "`prod` access" model for engineers
<!-- chapter: migrating-from-single-tenant-to-multi-tenant, duration: 1h -->
* Migrating from single-tenant to multi-tenant
    * patterns for retrofitting tenancy into an existing codebase
    * the strangler approach for tenancy
    * data migration from per-customer instances into a shared system
    * organizational implications of the migration
<!-- chapter: case-studies-and-wrap-up, duration: 1h -->
* Case studies and wrap up
    * walkthrough of a `B2B` `SaaS` design
    * walkthrough of a `B2C` `SaaS` design
    * common failure modes
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
