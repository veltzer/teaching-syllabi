---
tags:
  - networking:tcp-ip
  - networking:protocols
  - networking:networking
level: intermediate
category: networking
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
  - audiences:security-professionals
---
<!-- course: tcp_ip_deep_dive -->
# `TCP`/`IP` Deep Dive

## Description
This course provides an in-depth exploration of the `TCP`/`IP` protocol suite and the underlying networking fundamentals that power modern communications. Participants will study each layer of the network stack, from physical framing through transport protocols, and gain hands-on experience analyzing real network traffic with Wireshark and `tcpdump`. The course is designed for professionals who already have basic networking knowledge and want to deepen their understanding of how packets traverse networks, how protocols negotiate connections, and how to diagnose network issues effectively.

## Duration
24 hours / 3 days

## Intended Audience
* Software developers who build networked applications.
* System administrators and `DevOps` engineers responsible for network infrastructure.
* Security professionals who need to understand network-level attack surfaces.

## Prerequisites
* Basic familiarity with networking concepts (`IP` addresses, ports, client-server model).
* Comfort working with the `Linux` or `Windows` command line.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Describe the layers of the OSI and `TCP`/`IP` reference models and map protocols to each layer.
* Explain `Ethernet` framing, MAC addressing, and link-layer operations.
* Calculate subnets, apply `CIDR` notation, and design addressing schemes.
* Analyze the `ARP` and `ICMP` protocols and their role in network operations.
* Explain the `TCP` three-way handshake, flow control, and congestion control mechanisms.
* Compare `TCP` and `UDP` and choose the appropriate transport protocol for a given scenario.
* Describe how `DNS` resolution works internally, including recursive and iterative queries.
* Understand `DHCP` lease negotiation and `NAT` translation types.
* Identify common routing protocols and their use cases.
* Capture and interpret network traffic using `Wireshark` and `tcpdump`.
* Apply systematic troubleshooting methodologies to diagnose network problems.

## Outline
<!-- chapter: the-osi-and-tcp-ip-models, duration: 2h -->
* The OSI and `TCP`/`IP` Models
    * The seven layers of the OSI model
    * The four layers of the `TCP`/`IP` model
    * Mapping protocols to layers
    * Encapsulation and de-encapsulation
<!-- chapter: ethernet-and-the-data-link-layer, duration: 2h -->
* `Ethernet` and the Data Link Layer
    * `Ethernet` frame structure
    * MAC addressing
    * Switches and collision domains
    * VLANs
<!-- chapter: ip-addressing-and-subnetting, duration: 2h -->
* `IP` Addressing and Subnetting
    * `IPv4` address classes and `CIDR` notation
    * Subnet mask calculation
    * Public vs. private address ranges
    * Introduction to `IPv6`
<!-- chapter: arp-and-icmp, duration: 2h -->
* `ARP` and `ICMP`
    * `ARP` request and reply process
    * `ARP` cache and `ARP` spoofing
    * `ICMP` message types
    * ping and `traceroute` internals
<!-- chapter: tcp-in-depth, duration: 2h -->
* `TCP` in Depth
    * The three-way handshake and connection teardown
    * Sequence numbers and acknowledgments
    * Sliding window and flow control
    * Congestion control algorithms (slow start, congestion avoidance)
    * `TCP` options and tuning
<!-- chapter: udp, duration: 2h -->
* `UDP`
    * `UDP` datagram structure
    * Use cases for `UDP`
    * `UDP` vs. `TCP` trade-offs
<!-- chapter: dns-internals, duration: 2h -->
* `DNS` Internals
    * `DNS` hierarchy and zone delegation
    * Recursive vs. iterative queries
    * Record types (A, AAAA, CNAME, MX, NS, `SOA`, TXT)
    * `DNS` caching and `TTL`
    * `DNSSEC` overview
<!-- chapter: dhcp, duration: 2h -->
* `DHCP`
    * `DHCP` discover, offer, request, acknowledge sequence
    * Lease management and renewal
    * `DHCP` relay agents
<!-- chapter: nat, duration: 2h -->
* `NAT`
    * Static, dynamic, and PAT (port address translation)
    * `NAT` traversal challenges
    * `NAT` and peer-to-peer applications
<!-- chapter: routing-protocols, duration: 2h -->
* Routing Protocols
    * Static vs. dynamic routing
    * Distance-vector protocols (RIP)
    * Link-state protocols (`OSPF`)
    * Path-vector protocols (`BGP`)
    * Routing tables and longest prefix match
<!-- chapter: packet-analysis-with-wireshark-and-tcpdump, duration: 2h -->
* Packet Analysis with `Wireshark` and `tcpdump`
    * Capturing traffic with `tcpdump`
    * `Wireshark` interface and display filters
    * Following `TCP` streams
    * Identifying anomalies and retransmissions
<!-- chapter: network-troubleshooting, duration: 2h -->
* Network Troubleshooting
    * Systematic troubleshooting methodology
    * Common tools (ping, `traceroute`, `netstat`, ss, `nslookup`, dig)
    * Diagnosing connectivity, performance, and `DNS` issues
    * Reading and interpreting logs

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
