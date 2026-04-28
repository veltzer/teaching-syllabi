---
tags:
  - concepts:networking
  - concepts:internet-infrastructure
  - concepts:operations
  - concepts:scalability
  - concepts:network-security
level: intermediate
category: networking
duration_hours: 40
audience:
  - audiences:devops
  - audiences:sres
  - audiences:network-engineers
  - audiences:senior-developers
  - audiences:architects
---
<!-- course: dns_in_production -->
# `DNS` in Production

## Description
The `DNS Deep Dive` course in the catalog covers `DNS` as a protocol. This course covers `DNS` as the
hidden dependency that takes systems down. Most engineers can name the basic record types and roughly
explain how recursion works; far fewer can debug a propagation issue at 2 AM, design a multi-region
authoritative `DNS` architecture, or know which `DNS` failure modes their incident response plan does
not cover.

This five day course is dedicated to operating `DNS` in production. It covers `DNS`-as-a-hidden-dependency
patterns, the propagation and `TTL` realities that confuse most engineers, anycast `DNS`, split-horizon
deployments, `DNSSEC` operationally, the major managed `DNS` providers (`Route 53`, `Cloud DNS`,
`Azure DNS`, `Cloudflare`, `NS1`, `DNSimple`), `DNS`-driven outages and how to debug them, the security
dimension (cache poisoning, hijacking, takeover), and the `DNS`-based traffic management story for
multi-region systems. Participants leave able to design, operate, and debug production `DNS`.

## Duration
40 hours / 5 days

## Intended Audience
* `DevOps` and `SRE` engineers operating production systems
* network engineers handling enterprise or public `DNS`
* senior developers whose systems depend on `DNS` more than they realize
* architects designing multi-region or global systems
* engineers responding to `DNS`-driven incidents

## Prerequisites
* working knowledge of `TCP`/`IP`, `HTTP`, and the `DNS` Deep Dive material
* basic familiarity with at least one cloud provider
* exposure to running at least one production service

## Objectives
* identify `DNS` as the hidden dependency in incident scenarios
* design authoritative `DNS` architecture for production scale
* operate `DNSSEC` correctly
* implement `DNS`-based traffic management at the global level
* debug `DNS` issues quickly under incident pressure
* harden the `DNS` security posture
* avoid the common `DNS`-driven outage patterns

## Outline
<!-- chapter: dns-as-the-hidden-dependency, duration: 2h -->
* `DNS` as the hidden dependency
    * `DNS` in the request path
    * the failure modes that engineers do not anticipate
    * resolver caching and its consequences
    * `DNS` outage in incident postmortems
    * `Dyn` 2016 and `Route 53` 2019: lessons learned
    * what `DNS` is not the right tool for
<!-- chapter: ttl-and-propagation-realities, duration: 3h -->
* `TTL` and propagation realities
    * `TTL` semantics: authoritative, recursive, application
    * the resolver-cache-and-mismatched-`TTL` problem
    * negative caching and `SOA` minimum
    * the ten-minute "global propagation" myth
    * planning a `DNS` change with realistic timelines
    * the rapid-rollback `TTL` strategy
<!-- chapter: authoritative-dns-architecture, duration: 3h -->
* Authoritative `DNS` architecture
    * primary, secondary, hidden primary
    * zone transfer (`AXFR`, `IXFR`) and the `NOTIFY` mechanism
    * `BIND`, `NSD`, `Knot`, `PowerDNS`, `CoreDNS`
    * managed authoritative providers
    * multi-provider authoritative for redundancy
    * the `1.1.1.1` and `8.8.8.8` reality
<!-- chapter: anycast-dns-and-global-distribution, duration: 3h -->
* Anycast `DNS` and global distribution
    * `BGP` anycast for `DNS`
    * cross-reference to the Edge Computing course
    * latency-based steering
    * the "closest server" myth
    * geographically distributed authoritative
    * `Route 53`, `Cloud DNS`, `Azure DNS`, `Cloudflare DNS` design
<!-- chapter: split-horizon-and-internal-dns, duration: 2h -->
* Split-horizon and internal `DNS`
    * the internal-vs-external view
    * `DNS` views in `BIND`
    * `Route 53 Resolver`, `Cloud DNS` private zones, `Azure Private DNS`
    * `service mesh` and internal `DNS` (e.g. `CoreDNS` in `Kubernetes`)
    * the cross-`VPC` resolution problem
    * `DNS` and zero trust networking
<!-- chapter: dnssec-operationally, duration: 3h -->
* `DNSSEC` operationally
    * what `DNSSEC` actually proves
    * `KSK` and `ZSK` rollover
    * `KSK` rollover at the `TLD` level
    * `DS` records at the parent
    * the `DNSSEC` outage hall of fame
    * managed `DNSSEC` vs self-managed
    * is `DNSSEC` worth the cost
<!-- chapter: dns-based-traffic-management, duration: 3h -->
* `DNS`-based traffic management
    * weighted routing
    * latency-based routing
    * geo-based routing
    * health-`check` based failover
    * cross-reference to the Multi-Region Active-Active course
    * cross-reference to the Disaster Recovery in Practice course
    * the `TTL` tradeoff for `DNS`-based failover
<!-- chapter: dns-and-modern-cloud, duration: 2h -->
* `DNS` and modern cloud
    * `Route 53`: zones, alias records, `health checks`
    * `Cloud DNS`: zones, policies, forwarding
    * `Azure DNS` and `Traffic Manager`
    * `Cloudflare DNS` and orange-cloud
    * `NS1`, `DNSimple` for managed advanced
    * choosing a managed provider
<!-- chapter: kubernetes-and-service-discovery-dns, duration: 2h -->
* `Kubernetes` and service-discovery `DNS`
    * `CoreDNS` in `Kubernetes`
    * `Service` and `Endpoints` resolution
    * `External-DNS` controller
    * `Headless Service` and the `StatefulSet` `DNS` pattern
    * cross-reference to the existing `Kubernetes` material
    * `DNS` failure modes inside the cluster
<!-- chapter: dns-debugging-toolbox, duration: 3h -->
* `DNS` debugging toolbox
    * `dig` deep dive
    * `kdig`, `drill`, `host`, `nslookup`
    * `+trace`, `+norecurse`, `+short`, `+nssearch`
    * resolver-cache inspection
    * `tcpdump` for `DNS`
    * `dnsperf` and stress testing
    * the "is it `DNS`" decision tree
<!-- chapter: dns-driven-outages-and-incidents, duration: 3h -->
* `DNS`-driven outages and incidents
    * registrar lapse and the expired domain
    * fat-finger zone changes
    * authoritative outage patterns
    * resolver outage patterns
    * `TTL`-induced delayed outages
    * cross-reference to the Incident Response courses
    * post-mortem walkthrough of a real `DNS` incident
<!-- chapter: dns-security, duration: 3h -->
* `DNS` security
    * cache poisoning revisited
    * `Kaminsky` and how it changed defaults
    * `DNS` hijacking at the registrar
    * subdomain takeover from dangling records
    * cross-reference to the Threat Hunting course
    * `DNSSEC`, `DoH`, `DoT` for confidentiality and integrity
    * `DNS` query monitoring as a detection signal
<!-- chapter: dns-and-email-deliverability, duration: 2h -->
* `DNS` and email deliverability
    * `MX`, `SPF`, `DKIM`, `DMARC` records
    * the email-sender-verification story
    * `BIMI` and the new layer
    * the misconfigured-record-causes-all-email-to-spam pattern
    * monitoring email-related `DNS`
<!-- chapter: dns-monitoring-and-alerting, duration: 2h -->
* `DNS` monitoring and alerting
    * authoritative-server availability
    * resolver latency and failure
    * record-change auditing
    * lame delegation detection
    * expiry monitoring
    * the dashboard that catches `DNS` issues early
<!-- chapter: dns-program-and-governance, duration: 2h -->
* `DNS` program and governance
    * domain-name inventory
    * registrar consolidation
    * change-control for production zones
    * `IaC` for `DNS` (`Terraform`, `OctoDNS`)
    * the four-eyes principle for `DNS` changes
    * the abandoned subdomain problem
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * audit a sample organization's `DNS` setup
    * tabletop incident: simulated authoritative outage
    * recommended reading: `Liu`/`Albitz` `DNS and BIND`, `RFCs`, `IANA` resources

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
