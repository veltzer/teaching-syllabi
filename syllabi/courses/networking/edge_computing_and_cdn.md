---
tags:
  - concepts:networking
  - concepts:scalability
  - concepts:performance
  - concepts:distributed-systems
  - concepts:serverless
  - concepts:operations
level: intermediate
category: networking
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:devops
  - audiences:network-engineers
  - audiences:architects
---
<!-- course: edge_computing_and_cdn -->
# Edge Computing and `CDN`

## Description
The edge has changed. What used to be a static-asset cache in front of an origin server is now a programmable
runtime where a meaningful share of application logic lives: authentication, A/B testing, redirect rules,
personalization, image transformation, even full request handlers. Engineers who learned `CDN` as "set a long
`TTL` on `/static/`" are now responsible for code that runs in 300 cities and is hard to debug.

This five day course covers edge computing and content delivery as one continuous topic. It covers the
classical `CDN` architecture, modern edge runtimes (`Cloudflare Workers`, `Fastly Compute`, `AWS Lambda@Edge`
and `CloudFront Functions`, `Vercel Edge Functions`, `Deno Deploy`), cache architecture and invalidation,
edge auth and personalization, image and media transformation, observability and debugging at the edge, and
the architectural patterns that `make` the edge work or fail. Participants leave able to design edge-aware
systems, write and operate edge functions, and reason about the cache hierarchy with discipline.

## Duration
40 hours / 5 days

## Intended Audience
* developers building or operating web and `API` workloads at scale
* `DevOps` engineers operating `CDN` and edge infrastructure
* network engineers handling global traffic
* architects designing systems with the edge as a first-class layer
* engineers diagnosing latency or correctness issues that touch the edge

## Prerequisites
* working knowledge of `HTTP`, `TLS` and `DNS`
* exposure to at least one `CDN` (Cloudflare, Fastly, Akamai, `CloudFront`)
* basic familiarity with at least one programming language with edge support
* some experience operating production `web services`

## Objectives
* describe the modern `CDN` and edge architecture
* design cache strategies at the edge that are correct and performant
* write and operate edge functions across the major platforms
* implement edge auth, personalization and A/B testing correctly
* invalidate the cache deliberately, not by accident
* observe and debug edge workloads
* avoid the common edge architecture mistakes

## Outline
<!-- chapter: the-modern-edge, duration: 2h -->
* The modern edge
    * the classical `CDN`: caching, `TLS`, `DDoS`
    * the programmable edge: code at points of presence
    * `PoP` (point of presence) topology and anycast
    * the spectrum: `CDN`, edge functions, edge containers, full edge runtime
    * the difference between edge and serverless
    * what the edge is good for and what it is not
<!-- chapter: cdn-architecture-fundamentals, duration: 3h -->
* `CDN` architecture fundamentals
    * the request path: client, `DNS`, edge `PoP`, cache, origin shield, origin
    * cache hierarchy: edge, regional, origin shield
    * the role of `BGP` anycast in steering
    * `TLS` termination at the edge
    * `HTTP/2` and `HTTP/3` at the edge
    * cross-reference to the Load Balancing course
<!-- chapter: caching-the-actually-hard-part, duration: 4h -->
* Caching: the actually hard part
    * cache keys, `Vary`, query parameters
    * `Cache-Control` directives in detail
    * `s-maxage`, `stale-while-revalidate`, `stale-if-error`
    * surrogate keys and tag-based invalidation
    * range requests and partial responses
    * negative caching and the `5xx` cache
    * the public/private/no-store decision
<!-- chapter: cache-invalidation, duration: 3h -->
* Cache invalidation
    * the second-hardest problem
    * purge by `URL`, by surrogate key, by tag
    * soft purge vs hard purge
    * `stale-while-revalidate` as an invalidation strategy
    * propagation time and consistency
    * monitoring purge effectiveness
    * the test plan for an invalidation change
<!-- chapter: cloudflare-workers-deep-dive, duration: 3h -->
* `Cloudflare Workers` deep dive
    * the `V8` isolate model
    * `Workers` runtime `APIs` and limits
    * `Workers KV`, `Durable Objects`, D1, R2, `Queues`
    * `Workers Sites` and `Pages Functions`
    * `Cloudflare`-specific routing and rules
    * deploying and versioning workers
<!-- chapter: fastly-compute-and-vcl, duration: 2h -->
* `Fastly Compute` and `VCL`
    * `VCL` for cache logic
    * `Compute@Edge` and `WASM`-based runtime
    * `Fastly`-specific patterns
    * `Fastly` real-time logging and observability
    * comparing `Fastly` to `Cloudflare`
<!-- chapter: aws-cloudfront-and-lambda-edge, duration: 3h -->
* `AWS` `CloudFront` and `Lambda@Edge`
    * `CloudFront` distributions and behaviors
    * `Lambda@Edge` vs `CloudFront Functions`
    * the four `Lambda@Edge` triggers: viewer-request, origin-request, origin-response, viewer-response
    * `CloudFront` cache key policies
    * integration with `S3` and origin shield
    * `AWS Global Accelerator` adjacent topic
<!-- chapter: vercel-deno-deploy-and-the-framework-edges, duration: 2h -->
* `Vercel`, `Deno Deploy` and the framework edges
    * `Vercel` edge functions and middleware
    * `Next.js` edge runtime and the Node/`Edge` split
    * `Deno Deploy`
    * `Netlify Edge Functions`
    * the framework-driven edge model
<!-- chapter: edge-auth-and-personalization, duration: 3h -->
* Edge auth and personalization
    * `JWT` verification at the edge
    * session validation patterns
    * geo-based personalization and consent
    * A/B testing and experiment-bucketing at the edge
    * cross-reference to the Feature Flags course
    * "do not break the cache" patterns for personalization
<!-- chapter: image-and-media-transformation, duration: 2h -->
* Image and media transformation
    * on-the-fly resize and format conversion (`WebP`, `AVIF`)
    * `Cloudflare Images`, Fastly IO, imgix, `Thumbor`
    * video transcoding at the edge: when it is and is not viable
    * cache-key design for transformed media
    * cost models for image transformation
<!-- chapter: edge-storage-and-state, duration: 3h -->
* Edge storage and state
    * `Cloudflare KV`, `Durable Objects`, R2, `D1`
    * `Fastly Object Store` and `KV Store`
    * `Vercel Edge Config`
    * the consistency models of edge storage
    * the regional-but-not-edge alternative
    * keeping the edge stateless when possible
<!-- chapter: observability-at-the-edge, duration: 3h -->
* Observability at the edge
    * the cache-hit-ratio dashboard
    * `RUM` (real user monitoring) at the edge
    * structured logging from edge functions
    * tracing across edge and origin
    * cardinality and the `PoP` dimension
    * synthetic monitoring of edge behavior
<!-- chapter: security-at-the-edge, duration: 3h -->
* Security at the edge
    * `WAF` rules at the edge
    * `DDoS` mitigation tiers
    * bot management and challenge pages
    * `mTLS` from the edge to origin
    * cross-reference to the Zero Trust Networking course
    * preventing cache poisoning attacks
    * preventing host-header injection
<!-- chapter: cost-engineering-at-the-edge, duration: 2h -->
* Cost engineering at the edge
    * cost dimensions: requests, bandwidth, compute time, storage
    * pricing differences across edge providers
    * cache-hit ratio as the main cost lever
    * cross-reference to the Cloud Cost Optimization course
    * the egress-cost-vs-`CDN`-cost tradeoff
<!-- chapter: anti-patterns-and-incidents, duration: 1h -->
* Anti-patterns and incidents
    * the dynamic-content-with-no-cache origin `storm`
    * the cache key that included the session cookie
    * the personalization function that broke shared cache
    * the purge that nobody knew was needed
    * a real production cache-poisoning incident
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * design walkthrough of an edge architecture for a sample product
    * group review of an edge-function deployment
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
