---
tags:
  - concepts:networking
  - concepts:scalability
  - concepts:distributed-systems
  - concepts:performance
  - concepts:operations
  - concepts:architecture
level: intermediate
category: networking
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:devops
  - audiences:sres
  - audiences:network-engineers
  - audiences:architects
---
<!-- course: load_balancing_in_depth -->
# Load Balancing In Depth

## Description
Load balancing is one of the most-used and least-understood pieces of infrastructure. Almost every production
system depends on it, but the choice between `L4` and `L7`, between sticky sessions and stateless requests,
between client-side and server-side balancing, between `DNS`-based global balancing and anycast, has more
operational consequences than most engineers realize.

This five day course covers load balancing end to end. It is implementation-focused but vendor-neutral, with
deep dives into Envoy, `nginx`, `HAProxy`, cloud load balancers, `Kubernetes` `ingress`, and the global
traffic-management story. The course covers algorithms (round robin, least connections, EWMA, P2C, consistent
hashing), health checking, session persistence, `TLS` termination, traffic shaping and shedding, observability,
failure modes, and the architectural patterns that `make` load balancing scale and survive incidents.

## Duration
40 hours / 5 days

## Intended Audience
* developers operating services behind load balancers
* `DevOps` and `SRE` engineers running load balancer infrastructure
* network engineers handling `L4`/`L7` traffic
* architects designing the traffic layer of a system
* engineers diagnosing latency and availability issues at the load-balancer layer

## Prerequisites
* working knowledge of `TCP`, `UDP`, `HTTP` and `TLS`
* basic familiarity with `DNS` and routing
* some experience operating production services

## Objectives
* choose between `L4` and `L7` load balancing for a workload
* select an appropriate algorithm and tune it
* configure health checks that actually catch the right failures
* operate `TLS` termination and `mTLS` correctly
* design global load balancing across regions
* observe and debug load-balancer-layer incidents
* avoid the most common load-balancing failure modes

## Outline
<!-- chapter: load-balancing-fundamentals, duration: 2h -->
* Load balancing fundamentals
    * why we load balance
    * the four jobs: distribution, health, session, security
    * `L4` vs `L7` precisely
    * client-side vs server-side balancing
    * the load-balancer as a single point of failure and how to avoid it
<!-- chapter: load-balancing-algorithms, duration: 3h -->
* Load balancing algorithms
    * round robin and weighted round robin
    * least connections
    * least response time and `EWMA`
    * power-of-two-choices (`P2C`)
    * consistent hashing
    * maglev and rendezvous hashing
    * algorithm choice under skewed workloads
<!-- chapter: l4-load-balancing, duration: 3h -->
* `L4` load balancing
    * `TCP`/`UDP` connection forwarding
    * direct server return
    * `IPVS` and `LVS`
    * `Maglev` (Google) and Katran (`Meta`)
    * cloud `NLB` (`AWS`), `TCP/UDP` LB (`GCP`), `Azure` Load Balancer
    * `XDP` and `eBPF`-based load balancing
    * connection draining at `L4`
<!-- chapter: l7-load-balancing, duration: 4h -->
* `L7` load balancing
    * `HTTP` request routing
    * path, host, header, query-based routing
    * `gRPC` load balancing peculiarities
    * `WebSockets` and long-lived connections
    * request coalescing and retry
    * Envoy, `nginx`, `HAProxy` deep dive
    * `ALB` (`AWS`), `HTTP(S)` LB (`GCP`), `Application Gateway` (`Azure`)
<!-- chapter: health-checks-that-work, duration: 3h -->
* Health checks that work
    * passive vs active health checks
    * shallow vs deep health checks
    * the `/healthz` and `/readyz` distinction
    * cascading failure from synchronized health checks
    * health check from where: panel of probes vs single point
    * partial unhealth and graceful degradation
<!-- chapter: session-persistence, duration: 2h -->
* Session persistence
    * stateless requests as the goal
    * cookie-based stickiness
    * source-`IP`-based stickiness
    * consistent hashing for caching
    * the cost of stickiness on rolling deploys
    * session affinity in `Kubernetes`
<!-- chapter: tls-and-load-balancing, duration: 3h -->
* `TLS` and load balancing
    * `TLS` termination at the `LB`
    * `TLS` passthrough vs re-encryption
    * `SNI`-based routing
    * `mTLS` at the load-balancer layer
    * certificate rotation without downtime
    * `OCSP` stapling and revocation
    * the cost of `TLS` for connection reuse
<!-- chapter: traffic-shaping-shedding-and-rate-limiting, duration: 3h -->
* Traffic shaping, shedding and rate limiting
    * rate limiting algorithms: token bucket, leaky bucket, sliding window
    * per-key rate limiting at scale
    * load shedding under overload
    * priority queueing
    * circuit breakers at the `LB`
    * the difference between throttling and queueing
<!-- chapter: kubernetes-ingress-and-gateway-api, duration: 3h -->
* `Kubernetes` Ingress and `Gateway API`
    * Ingress, `Service`, `EndpointSlice`
    * `ingress` controllers: nginx, `Traefik`, Contour, `Gloo`
    * the `Gateway API` and why it replaces Ingress
    * service mesh `ingress` (`Istio`, `Linkerd`)
    * external load balancers vs in-cluster
    * the `LoadBalancer` `Service` type and its surprises
<!-- chapter: dns-and-anycast-for-global-traffic, duration: 3h -->
* `DNS` and anycast for global traffic
    * `DNS`-based load balancing
    * `GeoDNS` and `EDNS` client subnet
    * `BGP` anycast
    * cloud global load balancers (`Cloud Load Balancing`, `Global Accelerator`, `Front Door`)
    * `CDN` as a load balancer
    * the `TTL` tradeoff for `DNS`-based balancing
<!-- chapter: client-side-and-mesh-load-balancing, duration: 2h -->
* Client-side and mesh load balancing
    * `gRPC` client-side load balancing
    * service mesh sidecar balancing
    * `xDS` and dynamic config
    * locality-aware load balancing
    * outlier detection and ejection
<!-- chapter: observability-for-the-traffic-layer, duration: 2h -->
* Observability for the traffic layer
    * `RED` metrics for load balancers
    * top-talker analysis
    * `4xx`/`5xx` cardinality
    * upstream connection metrics
    * latency histograms and `p99` analysis
    * tracing through the load balancer
<!-- chapter: failure-modes-and-incidents, duration: 3h -->
* Failure modes and incidents
    * thundering herd at deploy
    * retry amplification
    * health check storms
    * the half-open connection problem
    * stuck connections and idle timeouts
    * load-balancer-side `OOM` and how to detect
    * post-mortem walkthroughs from public outages
<!-- chapter: capacity-planning-and-tuning, duration: 2h -->
* Capacity planning and tuning
    * sizing the load balancer fleet
    * connection limits and ephemeral port exhaustion
    * keep-alive tuning
    * file descriptor and `conntrack` limits
    * autoscaling load balancers
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * end-to-end design walkthrough on a sample multi-region service
    * tabletop incident: cascading failure at the `LB` layer
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
