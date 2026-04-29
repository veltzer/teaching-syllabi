---
tags:
  - concepts:networking
  - concepts:scalability
  - concepts:performance
  - concepts:best-practices
level: advanced
category: networking
duration_hours: 16
audience:
  - audiences:network-engineers
  - audiences:senior-developers
  - audiences:architects
  - audiences:devops
---
<!-- course: anycast_and_global_load_balancing -->
# Anycast and Global Load Balancing

## Description
The catalog has `Load Balancing in Depth`, `TCP/IP Deep Dive`, `Edge Computing and CDN`, and
`Multi-Cloud Networking`. None of those covers the specific subject of routing user traffic to the
right server across the world: anycast as the routing primitive, `BGP` as the substrate, the load
balancer at the edge, the global health `check`, the failover from one region to another, and the
patterns that distinguish "we have a region in three countries" from "users actually get the closest
region every time."

This two day course covers anycast and global load balancing as a focused engineering topic. It covers
the difference between unicast, multicast, and anycast, how `BGP` makes anycast work in practice, the
design of an anycast service (a `DNS` resolver, a `DDoS`-protected `HTTP` endpoint, an edge cache),
the global load balancers offered by the major clouds (`AWS Global Accelerator`, `Cloudflare`,
`GCP Global Load Balancer`, `Azure Front Door`, `Fastly`), the `DNS`-based alternatives
(`Route 53`, `NS1`), the health-`check`-and-failover model, the latency vs availability trade-off, the
`DDoS`-mitigation story, the operational realities (the day a `BGP` route was leaked), and the
patterns that work versus the ones that look right but are not. Participants leave able to design and
operate global routing for a service that serves users in more than one region.

## Duration
16 hours / 2 days

## Intended Audience
* network engineers operating global services
* senior developers shipping a service to multiple regions
* architects designing edge-routing
* `DevOps` engineers running `CDN` and global load balancers

## Prerequisites
* `solid` `TCP/IP` knowledge
* exposure to the Load Balancing in Depth course
* familiarity with `DNS`
* basic understanding of `BGP`

## Objectives
* explain anycast and the role of `BGP`
* design an anycast service deployment
* compare global load balancers across major clouds
* design the health-`check`-and-failover model
* operate global routing in production
* recognize the failure modes of anycast
* compare `DNS`-based and `IP`-based global routing

## Outline
<!-- chapter: unicast-multicast-anycast, duration: 1h -->
* Unicast, multicast, anycast
    * the three routing models
    * what anycast actually does at the network layer
    * the "same `IP` everywhere" property
    * cross-reference to the `TCP/IP` Deep Dive course
    * the canonical use cases
<!-- chapter: bgp-as-the-substrate, duration: 2h -->
* `BGP` as the substrate
    * `BGP` advertises the prefix
    * the as-path and the routing decision
    * peering and transit
    * the "anycast just works because of `BGP`" simplification
    * the "we leaked a `BGP` route and broke the internet" reality
<!-- chapter: dns-based-global-routing, duration: 2h -->
* `DNS`-based global routing
    * `Route 53`, `NS1`, `Cloud DNS`, `Azure Traffic Manager`
    * latency-based routing
    * geo-based routing
    * health-checks and failover
    * the `TTL` problem
    * the "`DNS` cache held an old answer for an hour" failure
<!-- chapter: ip-anycast-vs-dns, duration: 1h -->
* `IP` anycast vs `DNS`
    * the trade-offs
    * `DNS` is application-layer, anycast is network-layer
    * convergence time
    * the connection-stickiness problem
    * picking
<!-- chapter: cloudflare-and-the-anycast-cdn-model, duration: 2h -->
* `Cloudflare` and the anycast `CDN` model
    * `Cloudflare`'s anycast everywhere
    * the `Workers` placement story
    * the `DDoS` story
    * cross-reference to the Edge Computing and `CDN` course
    * the operational simplification
<!-- chapter: aws-global-accelerator, duration: 1h -->
* `AWS Global Accelerator`
    * the model
    * pricing
    * the failover behavior
    * `Global Accelerator` vs `CloudFront`
    * picking
<!-- chapter: gcp-global-load-balancer, duration: 1h -->
* `GCP` global load balancer
    * the global anycast `IP`
    * the cross-region backend service
    * the `Cloud Armor` integration
    * the no-region-pinning property
    * the cost shape
<!-- chapter: azure-front-door, duration: 1h -->
* `Azure Front Door`
    * the model
    * comparison with `Application Gateway`
    * the `WAF` integration
    * the cost shape
    * picking
<!-- chapter: health-checks-and-failover, duration: 2h -->
* Health checks and failover
    * the active health `check`
    * the passive health `check`
    * the failover threshold
    * the "we failed over to a region that was also broken" failure
    * the failover-`storm` risk
<!-- chapter: stateful-connections-and-anycast, duration: 1h -->
* Stateful connections and anycast
    * `TCP` and connection migration
    * the `BGP`-route-flap-during-connection problem
    * `QUIC`'s connection-migration property
    * cross-reference to the `QUIC` in Practice course
    * the "long-lived connections rebalanced badly" failure
<!-- chapter: ddos-mitigation, duration: 1h -->
* `DDoS` mitigation
    * the absorb-with-anycast strategy
    * `Cloudflare`, `Akamai`, `AWS Shield`
    * the rate-limit-at-edge layer
    * cross-reference to the `API` Rate Limiting and Quota Systems course
    * the "the attack was distributed and our origin was not anycast" failure
<!-- chapter: operational-realities, duration: 1h -->
* Operational realities
    * the `BGP` route leak
    * the `RPKI` story
    * the dependency on the upstream provider
    * the "the cloud's global LB had an outage" reality
    * the runbook
    * recommended reading: `Cloudflare` engineering blog, `BGP` `RFC` 4271

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
