---
tags:
  - concepts:networking
  - concepts:observability
  - concepts:operations
  - concepts:performance
  - concepts:best-practices
level: advanced
category: networking
duration_hours: 24
audience:
  - audiences:network-engineers
  - audiences:devops
  - audiences:sres
  - audiences:senior-developers
---
<!-- course: network_observability_engineering -->
# Network Observability Engineering

## Description
The catalog has `Network Troubleshooting`, `Networking Basics`, the per-cloud networking courses, and
`OpenTelemetry Deep Dive` for general observability. None of them is the focused course on the
discipline of making a network observable: instrumenting the data path, capturing flows, tracing
across hops, debugging tail latency, finding the slow link, finding the dropped packet, and
attributing a slow request to a specific point in the network.

This three day course covers network observability as a focused engineering practice. It covers the
canonical signals (`flows`, packet capture, latency-from-each-hop, retransmits, queue depth, switch
metrics), the legacy tools (`SNMP`, `NetFlow`/`sFlow`/`IPFIX`, `tcpdump`/`Wireshark`, `mtr`, `traceroute`),
the modern tools (`eBPF`-based observability with `Cilium Hubble`, `Pixie`, `Inspektor Gadget`,
`bpftrace`, `Pyroscope` for kernel profiling), the `RUM`-style end-user network observability
(`OpenTelemetry`, `Sentry`, real user monitoring tools), the cloud network observability (```VPC`` Flow
Logs`, ``Azure` NSG Flow Logs`, ``GCP` `VPC` Flow Logs`), the service-mesh observability (``Istio``, ``Linkerd``,
`Cilium`), the per-tenant or per-service segmentation, the alerting and `SLO` story, the cost shape,
and the patterns that distinguish a network you can debug from one you cannot. Examples include real
production debugging walkthroughs. Participants leave able to instrument and operate network
observability across cloud, on-prem, and edge.

## Duration
24 hours / 3 days

## Intended Audience
* network engineers extending observability
* `DevOps` and `SREs` debugging cross-service network issues
* senior developers operating distributed systems
* engineers responsible for tail-latency `SLOs`

## Prerequisites
* `solid` `TCP/IP` knowledge
* exposure to the Network Troubleshooting course
* familiarity with at least one observability stack
* basic understanding of `Linux` networking

## Objectives
* identify the canonical network observability signals
* deploy and use `eBPF`-based network observability tools
* capture and analyze flows in cloud environments
* trace requests across network hops
* debug tail latency to a specific network event
* set network-related `SLOs` and alerts
* operate the observability stack itself

## Outline
<!-- chapter: what-network-observability-actually-covers, duration: 1h -->
* What network observability actually covers
    * the boundary with system observability
    * the boundary with `APM`
    * cross-reference to the `OpenTelemetry` Deep Dive course
    * the canonical incident: the slow request
    * what we want to know and why we cannot
<!-- chapter: the-canonical-signals, duration: 2h -->
* The canonical signals
    * flows: who talks to whom
    * packet capture: what was on the wire
    * latency: round-trip and one-way
    * retransmits and loss
    * queue depth at the switch
    * the per-link bandwidth
<!-- chapter: legacy-tools-still-essential, duration: 2h -->
* Legacy tools still essential
    * `tcpdump` and `Wireshark`
    * `traceroute`, `mtr`, `tracepath`
    * `ping` and the layer it actually tests
    * `iperf3`
    * `ethtool` and `ip`
    * the "we forgot the basics and chased a fancy tool" failure
<!-- chapter: snmp-netflow-sflow-ipfix, duration: 2h -->
* `SNMP`, `NetFlow`, `sFlow`, `IPFIX`
    * `SNMP` for switch metrics
    * `NetFlow` and the variants
    * the sampling-rate question
    * the storage-cost reality
    * still the foundation of enterprise networks
<!-- chapter: ebpf-network-observability, duration: 3h -->
* `eBPF` network observability
    * `Cilium Hubble`
    * `Pixie` for `Kubernetes`
    * `Inspektor Gadget`
    * `bpftrace` for ad-hoc
    * cross-reference to the `eBPF` in Production course
    * the "we found the issue in five minutes with `Hubble`" experience
<!-- chapter: cloud-flow-logs, duration: 2h -->
* Cloud flow logs
    * `VPC Flow Logs` (`AWS`)
    * `NSG Flow Logs` (`Azure`)
    * `VPC Flow Logs` (`GCP`)
    * the cost shape
    * the analytics-on-flow-logs story
    * the "we did not enable them and could not investigate" reality
<!-- chapter: service-mesh-network-observability, duration: 2h -->
* Service-mesh network observability
    * `Istio`'s `envoy`-based observability
    * `Linkerd`'s tap and tap-injector
    * `Cilium`'s `eBPF`-based mesh
    * cross-reference to the Service Mesh Comparison course
    * the per-call observability versus per-flow
<!-- chapter: real-user-monitoring, duration: 2h -->
* Real user monitoring
    * `RUM`'s view from the client
    * `Web Vitals` and the network components
    * `OpenTelemetry` browser instrumentation
    * the "we cannot see what the user sees" reality
    * the cost-and-privacy trade-off
<!-- chapter: tracing-across-hops, duration: 2h -->
* Tracing across hops
    * trace propagation through proxies
    * the "the trace stopped at the load balancer" failure
    * the `B3` and `W3C` propagation
    * cross-reference to the Distributed Tracing in Practice course
    * the network-aware trace
<!-- chapter: tail-latency-investigation, duration: 2h -->
* Tail latency investigation
    * the "p99 is bad and p50 is fine" pattern
    * the network-side root cause vs the app-side root cause
    * the `TCP` retransmit signature
    * the "the load balancer was the issue" frequent finding
    * worked example
<!-- chapter: slos-and-alerting, duration: 1h -->
* `SLOs` and alerting
    * latency `SLOs` that include the network
    * the per-region network `SLO`
    * cross-reference to the `SLOs` and Error Budgets course
    * the alert that pages
    * the alert that should not page
<!-- chapter: cost-of-network-observability, duration: 1h -->
* Cost of network observability
    * `VPC Flow Logs` storage cost
    * `eBPF` overhead
    * the cardinality cost in metrics
    * cross-reference to the Cardinality Engineering course
    * the budget for the observability bill
<!-- chapter: putting-it-together, duration: 2h -->
* Putting it together
    * design walkthrough of a network observability stack
    * the integration with the broader observability stack
    * the on-call workflow `when` latency spikes
    * the postmortem of a network-rooted incident
    * recommended reading: `Cilium`, `Pixie`, and `Brendan Gregg`'s materials

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
