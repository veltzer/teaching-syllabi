---
tags:
  - concepts:networking
  - concepts:performance
  - concepts:web-development
  - concepts:best-practices
level: advanced
category: networking
duration_hours: 16
audience:
  - audiences:senior-developers
  - audiences:network-engineers
  - audiences:architects
  - audiences:devops
---
<!-- course: quic_in_practice -->
# `QUIC` in Practice

## Description
The catalog has an `HTTP/2 and HTTP/3` course and a `TCP/IP Deep Dive` course. `QUIC` is the transport
that `HTTP/3` runs on, and it is now the dominant transport for Google, Meta, `Cloudflare`, and a
growing share of mobile and `CDN` traffic. It deserves its own course because the `HTTP/3` material does
not cover `QUIC`'s engineering reality: the multiplexing model that fixes head-of-line blocking, the
connection migration story, the `0-RTT` security trade-off, the operational implications of `UDP` as
the substrate, the middlebox problem, the load balancer problem, and the things that actually `go` wrong
when you turn `QUIC` on.

This two day course covers `QUIC` from the wire up to the operations team. It covers `RFC 9000` and the
related `RFCs`, the connection establishment dance, the cryptography integration, the loss recovery
algorithm, the congestion control choices, the streams model, connection migration, `0-RTT`, the
unreliable-datagram extension, the implementations (`quiche`, msquic, lsquic, `quic-go`, `Quinn`),
the operational gotchas (`UDP` rate limits, packet inspection middleboxes, `MTU` issues, load
balancing), and the cases where `QUIC` is the wrong choice. Participants leave able to deploy `QUIC` in
production and debug it when it misbehaves.

## Duration
16 hours / 2 days

## Intended Audience
* senior developers shipping `HTTP/3` to clients
* network engineers operating `QUIC` traffic
* architects deciding whether to adopt `QUIC`
* platform engineers running `CDN` or proxy infrastructure

## Prerequisites
* `solid` understanding of `TCP` and `TLS`
* exposure to the `HTTP/2 and HTTP/3` course or equivalent knowledge
* familiarity with at least one packet-capture tool

## Objectives
* explain `QUIC`'s structure relative to `TCP` plus `TLS` plus `HTTP/2`
* read a `QUIC` handshake on the wire
* operate `QUIC` traffic in production
* debug `QUIC` performance and connectivity issues
* reason about the `0-RTT` security trade-off
* recognize when to use `QUIC` and when not to

## Outline
<!-- chapter: why-quic-exists, duration: 1h -->
* Why `QUIC` exists
    * `TCP`'s head-of-line blocking
    * `TLS` and `TCP` as separate handshakes
    * the mobile-network reality
    * cross-reference to the `HTTP/2 and HTTP/3` course
    * the `Google` deployment as the proof
<!-- chapter: the-quic-handshake, duration: 2h -->
* The `QUIC` handshake
    * the cryptography is part of the transport
    * `1-RTT` vs `0-RTT`
    * the `Initial` packet and the version negotiation
    * `RTT` improvements vs `TCP` plus `TLS`
    * what the wire looks like
<!-- chapter: streams-and-multiplexing, duration: 2h -->
* Streams and multiplexing
    * unidirectional and bidirectional streams
    * stream `IDs` and the client/server allocation
    * the head-of-line blocking fix
    * the per-stream flow control
    * the connection-level flow control
<!-- chapter: loss-recovery-and-congestion-control, duration: 2h -->
* Loss recovery and congestion control
    * `QUIC`'s ack-based loss detection
    * `Reno`, CUBIC, BBR over `QUIC`
    * the no-ambiguous-retransmit advantage over `TCP`
    * tail-loss probes
    * the "congestion control kicked in too aggressively" failure
<!-- chapter: connection-migration, duration: 1h -->
* Connection migration
    * the connection `ID` as the primary identifier
    * `Wi-Fi` to `LTE` migration
    * `NAT` rebinding handled
    * the load balancer's view
    * the "connection migration broke our load balancer" failure
<!-- chapter: 0-rtt-and-the-replay-trade-off, duration: 1h -->
* `0-RTT` and the replay trade-off
    * the resumption flow
    * the replay attack model
    * which requests are safe over `0-RTT`
    * application-layer enforcement
    * the "we replayed a `POST` and double-charged the customer" failure
<!-- chapter: quic-implementations, duration: 2h -->
* `QUIC` implementations
    * `quiche` (`Cloudflare`)
    * `msquic` (`Microsoft`)
    * `lsquic` (`LiteSpeed`)
    * `quic-go`, `Quinn` (Rust)
    * `ngtcp2`
    * picking an implementation
<!-- chapter: operating-quic, duration: 2h -->
* Operating `QUIC`
    * the load balancer that does not understand `UDP`
    * the `firewall` that drops `UDP`
    * the `MTU` problem and `PMTU` discovery
    * the `UDP` rate limit at the edge
    * cross-reference to the Load Balancing in Depth course
<!-- chapter: middleboxes-and-the-deployment-reality, duration: 1h -->
* Middleboxes and the deployment reality
    * the encrypted-transport headers
    * the inspection-impossible reality
    * the network-operator pushback
    * the "enterprise blocked `UDP/443`" reality
    * the fallback path to `HTTP/2`
<!-- chapter: debugging-quic, duration: 1h -->
* Debugging `QUIC`
    * `qlog` and the standard event log
    * `qvis` and visualizing a connection
    * `Wireshark` with `QUIC` decryption
    * `tcpdump` of `UDP/443` traffic
    * the "we have no idea why it slowed down" failure
<!-- chapter: when-not-to-use-quic, duration: 1h -->
* `When` not to use `QUIC`
    * inside the data center where `TCP` is fine
    * environments with strict middleboxes
    * cases where `WebSocket` is sufficient
    * cross-reference to the `WebSocket` Programming course
    * the "we adopted `QUIC` because it was new" failure

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
