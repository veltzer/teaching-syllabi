---
tags:
  - networking:dns
  - protocols:dns
  - infrastructure:networking
  - concepts:internet-infrastructure
level: intermediate
category: networking
duration_hours: 16
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:network-engineers
  - audiences:developers
---
<!-- course: dns_deep_dive -->
# `DNS` Deep Dive

## Description
The Domain Name System (`DNS`) is one of the most critical and yet least understood components of internet and enterprise infrastructure, translating human-readable names into addresses that power every networked application. Despite its ubiquity, `DNS` misconfigurations and vulnerabilities are responsible for a significant share of outages, security incidents, and performance problems in production environments. This course goes far beyond the basics, covering `DNS` resolution internals, all major record types, zone management, `DNSSEC`, modern privacy-preserving protocols (`DoH` and `DoT`), split-horizon architectures, and the full spectrum of `DNS`-based attacks and mitigations. Participants will emerge with the deep knowledge necessary to design, operate, secure, and troubleshoot `DNS` infrastructure at any scale.

## Duration
16 hours / 2 days

## Intended Audience
* System administrators and `DevOps` engineers managing internal and external `DNS` for organizations of any size.
* Network engineers responsible for naming infrastructure, zone delegation, and network service reliability.
* Developers who build applications that depend on `DNS` and need to understand resolution behavior, caching, and failure modes.

## Prerequisites
* `Solid` understanding of `TCP/IP` networking: `IP` addressing, routing, and `UDP`/`TCP`.
* Familiarity with `Linux` command-line tools: `dig`, `nslookup`, `ping`, `netstat`.
* Basic knowledge of networking services and how internet infrastructure is organized.

## Required Knowledge
* `TCP/IP` networking fundamentals
* `Linux` command-line proficiency

## Objectives
* Trace the full `DNS` resolution process from recursive query to authoritative answer
* Understand every major `DNS` record type and `when` to use each
* Configure and operate authoritative `DNS` servers and manage zones
* Explain how recursive resolvers work and how caching affects resolution
* Implement `DNSSEC` to cryptographically authenticate `DNS` responses
* Configure `DNS` over `HTTPS` and `DNS` over `TLS` for privacy and security
* Design split-horizon `DNS` for internal/external name separation
* Optimize `DNS` performance through caching tuning and resolver selection
* Identify and mitigate common `DNS` attacks including cache poisoning and `DDoS`
* Use standard tools to diagnose and resolve `DNS` incidents effectively

## Outline
<!-- chapter: dns-fundamentals-and-resolution, duration: 2h -->
* `DNS` Fundamentals and Resolution Process
    * The purpose of `DNS` and the namespace hierarchy
    * Domain name structure: TLD, second-level domain, subdomain, FQDN
    * `DNS` resolution: recursive queries, iterative queries, and referrals
    * The role of the root servers, TLD nameservers, and authoritative nameservers
    * Resolvers: stub resolvers, recursive resolvers, and forwarders
    * `UDP` vs `TCP` in `DNS` and `when` `TCP` is used
    * The `DNS` wire format: message structure, flags, and sections
    * `TTL` and how caching affects resolution behavior
<!-- chapter: dns-record-types, duration: 2h -->
* `DNS` Record Types
    * `A` and `AAAA` records for `IPv4` and `IPv6` address mapping
    * `CNAME` records: canonical names, limitations, and `ALIAS`/`ANAME` alternatives
    * `MX` records and email routing priorities
    * `NS` records and zone delegation
    * `TXT` records: `SPF`, `DKIM`, `DMARC`, and domain verification
    * `SRV` records for service discovery
    * `PTR` records and reverse `DNS` lookups
    * `SOA` record: zone authority, serial numbers, and refresh parameters
    * `CAA` records for certificate authority authorization
    * Newer record types: `HTTPS`, `SVCB`, `TLSA`
<!-- chapter: authoritative-dns-and-zones, duration: 2h -->
* Authoritative `DNS` and Zones
    * Zone files: structure, syntax, and best practices
    * Primary and secondary nameserver synchronization with `AXFR`/`IXFR`
    * Zone delegation and `glue` records
    * Setting up authoritative `DNS` with `BIND` and `NSD`
    * `NOTIFY` and `TSIG`-secured zone transfers
    * `Dynamic DNS` (`RFC 2136`) for programmatic record updates
    * Hosting zones in cloud providers: `Route 53`, `Cloud DNS`, `Azure DNS`
    * Zone `file` management and change control practices
<!-- chapter: recursive-resolvers, duration: 2h -->
* Recursive Resolvers
    * How resolvers navigate the `DNS` hierarchy
    * Caching behavior: positive caching, negative caching (`NXDOMAIN`)
    * Cache poisoning and the importance of random source ports
    * Configuring `Unbound` as a validating, caching resolver
    * `BIND` as a recursive resolver with forwarding and views
    * Public resolvers: `8.8.8.8`, `1.1.1.1`, `9.9.9.9` — differences and trade-offs
    * Resolver selection strategies for latency optimization
    * `EDNS(0)` extensions and the `EDNS` client subnet option
<!-- chapter: dnssec, duration: 2h -->
* `DNSSEC`
    * Why `DNSSEC` is needed: the Kaminsky attack and its lessons
    * `DNSSEC` records: `RRSIG`, `DNSKEY`, `DS`, `NSEC`, `NSEC3`
    * Zone signing and key types: KSK and ZSK
    * The chain of trust from root to authoritative zone
    * Enabling `DNSSEC` validation on resolvers
    * Signing zones with `BIND` and `ldns-signzone`
    * Key rollover procedures: ZSK and KSK rollovers
    * `DNSSEC` operational challenges and failure modes
<!-- chapter: doh-and-dot, duration: 2h -->
* `DNS` over `HTTPS` and `DNS` over `TLS`
    * Privacy problems with traditional `DNS`: eavesdropping and manipulation
    * `DNS` over `TLS` (`DoT`): protocol mechanics and port 853
    * `DNS` over `HTTPS` (`DoH`): embedding `DNS` in `HTTPS` traffic
    * Configuring `DoT` and `DoH` in `Unbound` and `BIND`
    * Client-side `DoH`/`DoT` configuration in browsers and operating systems
    * `Oblivious DoH` (`ODoH`) for enhanced privacy
    * Deployment trade-offs: security, privacy, and enterprise inspection
<!-- chapter: split-horizon-and-internal-dns, duration: 1h -->
* Split-Horizon and Internal `DNS`
    * Split-horizon `DNS`: different answers for internal vs external queries
    * Configuring views in `BIND` for split-horizon
    * Internal `DNS` zones for private infrastructure naming
    * Service discovery with `DNS` in `Kubernetes` and `Docker`
    * `CoreDNS` for cloud-native and `Kubernetes` environments
    * Avoiding split-horizon pitfalls with `DNSSEC` and `DoH`
<!-- chapter: dns-performance-and-caching, duration: 1h -->
* `DNS` Performance and Caching
    * Impact of `TTL` values on cache hit rates and propagation speed
    * Pre-fetching and zero-`TTL` implications
    * `DNS` prefetching in browsers
    * Resolver performance benchmarking: `dnsperf` and `resperf`
    * Anycast `DNS` for geographic load distribution
    * Negative `TTL` and `NXDOMAIN` caching
<!-- chapter: dns-security-threats, duration: 1h -->
* `DNS` Security Threats and Mitigations
    * Cache poisoning attacks and Kaminsky-style exploits
    * `DNS` amplification and reflection `DDoS` attacks
    * `DNS` tunneling for command-and-control and data exfiltration
    * Domain Generation Algorithms (`DGA`) and botnet evasion
    * `NXDOMAIN` hijacking and monetization threats
    * `RPZ` (Response Policy Zones) for `DNS` filtering and blocking
    * Monitoring `DNS` traffic for anomalies with query logging
<!-- chapter: troubleshooting-dns, duration: 1h -->
* Troubleshooting `DNS`
    * `dig` in depth: query types, trace mode, and output interpretation
    * `nslookup` and `host` for quick lookups
    * `drill` for `DNSSEC`-aware queries
    * Checking delegation and zone propagation
    * Diagnosing `DNSSEC` validation failures
    * Common `DNS` failure patterns: stale cache, missing `glue`, lame delegation
    * Using `Wireshark` to capture and analyze `DNS` packets

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
