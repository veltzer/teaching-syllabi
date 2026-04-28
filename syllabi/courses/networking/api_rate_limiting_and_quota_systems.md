---
tags:
  - concepts:api
  - concepts:scalability
  - concepts:performance
  - concepts:distributed-systems
  - concepts:operations
  - concepts:network-security
level: intermediate
category: networking
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:devops
  - audiences:sres
  - audiences:architects
---
<!-- course: api_rate_limiting_and_quota_systems -->
# `API` Rate Limiting and Quota Systems

## Description
Every production `API` ends up needing rate limiting, and most of them implement it badly. The naive
approach (in-process counters, fixed `windows`) breaks the moment traffic grows or the service horizontally
scales. The good approach (distributed limiters, fairness across tenants, separate budgets for separate
capabilities) is well-understood but rarely taught as a coherent topic.

This five day course is dedicated to rate limiting and quota systems as their own engineering discipline.
It covers the algorithms (token bucket, leaky bucket, sliding window, sliding log, GCRA), the deployment
options (in-process, edge, gateway, service-mesh, dedicated service), the distributed-state story (`Redis`,
`Memcached`, custom counter services, eventually-consistent designs), fairness and isolation across
tenants, quota accounting and billing alignment, abuse detection, and the operational realities. Examples
are drawn from `Stripe`, `GitHub`, `Cloudflare`, `Envoy`, and the public engineering blogs of organizations
that operate large public APIs. Participants leave able to design and operate rate limiting that is
correct, fair, observable and survivable.

## Duration
40 hours / 5 days

## Intended Audience
* developers and architects designing public or internal `APIs`
* `DevOps` and `SRE` engineers operating rate-limited platforms
* engineers fixing a rate-limiting incident or migrating to a better system
* engineers designing the abuse-prevention story for an `API`

## Prerequisites
* working knowledge of `HTTP`, `APIs`, and at least one cache or key-value store
* basic familiarity with at least one cloud or `Kubernetes` environment
* exposure to at least one production rate-limited `API` from either side

## Objectives
* describe the major rate-limiting algorithms and pick the right one
* design a distributed rate limiter with appropriate consistency and fairness
* implement quota systems aligned to billing
* deploy rate limiting at the right layer (edge, gateway, service, mesh)
* protect downstream services from abuse and accidental misuse
* observe and tune rate limiting in production
* avoid the most common rate-limiting failure modes

## Outline
<!-- chapter: why-rate-limiting-is-everywhere, duration: 2h -->
* Why rate limiting is everywhere
    * abuse, capacity, fairness, billing
    * the difference between rate limiting and throttling
    * the difference between rate limiting and load shedding
    * the difference between rate limiting and circuit breaking
    * the cases where rate limiting is the wrong tool
<!-- chapter: the-algorithms, duration: 4h -->
* The algorithms
    * fixed window
    * sliding window log and sliding window counter
    * token bucket
    * leaky bucket
    * `GCRA` (generic cell rate algorithm)
    * `MeshRate` and concurrency-based limits
    * choosing an algorithm from real requirements
<!-- chapter: distributed-state, duration: 4h -->
* Distributed state
    * the multi-instance counter problem
    * `Redis`-based counters: `INCR`, `Lua`, `Redis Cell`
    * `Memcached`-based counters
    * `DynamoDB` and other cloud key-value stores
    * eventually-consistent vs strongly-consistent designs
    * the burst-on-failover problem
    * `CRDTs` for distributed counters
<!-- chapter: where-to-rate-limit, duration: 3h -->
* Where to rate limit
    * edge `CDN` and `WAF`
    * `API` gateway
    * service mesh sidecar
    * application code
    * dedicated rate-limit service
    * choosing the right layer per requirement
    * the layered defense model
<!-- chapter: keying-and-identity, duration: 3h -->
* Keying and identity
    * `API`-key, `OAuth` client, user, tenant, `IP`
    * the `IP`-as-identity problem with `NAT` and proxies
    * compound keys: tenant + endpoint
    * authenticated vs unauthenticated rate limits
    * privacy considerations in keying
<!-- chapter: per-endpoint-and-per-method-limits, duration: 2h -->
* Per-endpoint and per-method limits
    * cost-weighted rate limits
    * the expensive-endpoint problem
    * limits per `HTTP` method
    * point-in-time vs sustained limits
    * the `GitHub` cost-based model
<!-- chapter: fairness-across-tenants, duration: 3h -->
* Fairness across tenants
    * the noisy-neighbor problem in shared infrastructure
    * proportional fairness
    * weighted fair queueing for `APIs`
    * tenant tiers and burstable budgets
    * cross-reference to the Multi-Tenant `SaaS` Architecture course
<!-- chapter: quotas-and-billing-alignment, duration: 3h -->
* Quotas and billing alignment
    * the difference between rate limit and quota
    * monthly quota accounting
    * idempotency and quota counting
    * cross-reference to the Idempotency course
    * tying technical metering to invoiceable units
    * cross-reference to the Multi-Tenant `SaaS` course's metering chapter
    * showing usage to the customer
<!-- chapter: client-side-behavior-and-protocol, duration: 3h -->
* Client-side behavior and protocol
    * `HTTP 429` semantics
    * `Retry-After` and the client-side backoff
    * `RateLimit-*` standard headers (`IETF` draft)
    * exponential backoff with jitter
    * client `SDK` design for rate limit awareness
    * the "polite client" pattern
<!-- chapter: dedicated-rate-limit-services, duration: 3h -->
* Dedicated rate-limit services
    * `Envoy` rate limit service
    * `Lyft` ratelimit
    * `Cloudflare`-style edge limits
    * `Stripe`'s public design
    * `Doorman` (`Google`)
    * build vs buy
<!-- chapter: tooling-and-implementations, duration: 2h -->
* Tooling and implementations
    * `Kong`, `Tyk`, `APISIX` rate-limit plugins
    * `nginx` `limit_req` and `limit_conn`
    * cloud `API` gateways: `AWS API Gateway`, `Azure API Management`, `Google Cloud Endpoints`
    * `Istio` and `Linkerd` rate-limit policies
    * `Redis Cell` and `Redis` patterns
<!-- chapter: abuse-detection-and-adaptive-limits, duration: 2h -->
* Abuse detection and adaptive limits
    * the static limit vs adaptive limit tradeoff
    * detecting credential stuffing and scraping
    * captcha and challenge integration
    * `IP` reputation feeds
    * cross-reference to the Threat Hunting course
    * shadow-banning and tarpitting
<!-- chapter: observability-and-tuning, duration: 2h -->
* Observability and tuning
    * metrics: requests admitted, requests rejected, by key, by endpoint
    * cardinality and the per-tenant dashboard
    * latency contribution of the limiter
    * detecting an under-sized limit
    * detecting a leaking limit
    * the limit-misconfiguration incident
<!-- chapter: failure-modes-and-incidents, duration: 2h -->
* Failure modes and incidents
    * the limiter outage that takes down the `API`
    * the limiter that fails open vs fails closed
    * cache stampede on limit reset
    * the bypass via different endpoint
    * the legitimate user accidentally locked out
    * recovery patterns after each
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * design a rate-limit system for a sample multi-tenant `API`
    * group review of a real `429` policy
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
