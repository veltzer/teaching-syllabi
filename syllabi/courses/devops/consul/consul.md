---
tags:
  - tools:consul
  - infrastructure:service-mesh
  - infrastructure:service-discovery
  - practices:devops
level: intermediate
category: devops
duration_hours: 24
audience:
  - audiences:devops
  - audiences:developers
  - audiences:architects
---
<!-- course: consul -->
# `Consul`

## Description
`Consul` by `HashiCorp` is a multi-networking tool that provides service discovery, health
checking, a distributed key-value store, and a full-featured service mesh in a single,
unified platform. This course covers `Consul` from first principles, beginning with its
gossip-based architecture and progressing through service registration, `Consul Connect`
mTLS service mesh, and multi-datacenter federation. Participants will learn how to secure
service-to-service communication with intentions, enforce fine-grained access policies with
`ACLs`, and gain full observability into their service mesh with integrated metrics and
distributed tracing. The course closes with practical guidance on deploying and operating
`Consul` on `Kubernetes` using the official `Helm` chart and the `Consul` on `Kubernetes` `CLI`.

## Duration
24 hours / 3 days

## Intended Audience
* `DevOps` and platform engineers responsible for service networking and infrastructure.
* Developers building distributed `microservices` who need to understand service discovery.
* Solution architects evaluating service mesh and service discovery technologies.

## Prerequisites
* `Solid` understanding of networking fundamentals (`TCP`/`IP`, `DNS`, `TLS` certificates).
* Experience with `Linux` system administration and the command line.
* Basic familiarity with distributed systems concepts.
* Exposure to `Kubernetes` is beneficial for the final chapter.

## Objectives
* Understand `Consul`'s architecture including the gossip protocol, Raft consensus, and agent roles.
* Register services and perform health-based service discovery.
* Use the `Consul` KV store for dynamic configuration and leader election.
* Implement a zero-trust service mesh with `Consul Connect` and mutual `TLS`.
* Control traffic with intentions and enforce security policies using `ACLs`.
* Federate `Consul` across multiple datacenters and operate `Consul` on `Kubernetes`.

## Outline
<!-- chapter: introduction-to-service-mesh-and-service-discovery, duration: 2h -->
* Introduction to Service Mesh and Service Discovery
    * Challenges of service-to-service communication in distributed systems
    * `DNS`-based vs. registry-based service discovery patterns
    * What is a service mesh and what problems does it solve
    * Overview of `Consul` capabilities and positioning vs. `etcd`, `Zookeeper`, and `Istio`

<!-- chapter: consul-architecture, duration: 2h -->
* `Consul` Architecture
    * Agents: server nodes and client nodes
    * The `Serf` gossip protocol for cluster membership and failure detection
    * Raft consensus for strongly consistent data
    * Datacenter topology and the catalog, KV, and ACL subsystems

<!-- chapter: installation-and-cluster-setup, duration: 2h -->
* Installation and Cluster Setup
    * Installing `Consul` as a system service or container
    * Bootstrapping a server cluster with auto-join
    * Configuring `TLS` encryption for agent-to-agent communication
    * `consul` `CLI` basics: members, info, monitor, and validate

<!-- chapter: service-registration-and-discovery, duration: 3h -->
* Service Registration and Discovery
    * Registering services via configuration files and the `HTTP` `API`
    * Service tags, metadata, and structured `service.checks`
    * Querying the catalog with the `DNS` interface and the `HTTP` `API`
    * Service mesh sidecar proxies and transparent proxy mode
    * Prepared queries and failover across datacenters

<!-- chapter: health-checks, duration: 2h -->
* Health Checks
    * `Check` types: `HTTP`, `TCP`, `gRPC`, script, and `TTL`
    * Deregistration of unhealthy services and critical status timeouts
    * Distributing checks across agents and aggregating health state
    * Monitoring `check` results with the `Consul` UI and `API`

<!-- chapter: key-value-store, duration: 2h -->
* Key-Value Store
    * KV store data model: keys, values, flags, and modify index
    * Reading and writing values with the `CLI` and `HTTP` `API`
    * Sessions, locks, and leader election patterns
    * Watching for KV changes with blocking queries and `consul watch`

<!-- chapter: consul-connect-service-mesh, duration: 3h -->
* `Consul Connect` — Service Mesh
    * `Consul Connect` architecture: sidecar proxies and the xDS `API`
    * Automatic mTLS between services with managed certificates
    * The built-in proxy vs. `Envoy` as the data plane
    * Traffic management: `ServiceRouter`, `ServiceSplitter`, and `ServiceResolver`
    * Configuring `Envoy` via `ProxyDefaults` and `ServiceDefaults`

<!-- chapter: intentions-and-security-policies, duration: 2h -->
* Intentions and Security Policies
    * Intention-based authorization: allow and deny rules
    * Layer 4 (identity) vs. Layer 7 (`HTTP` path, method) intentions
    * `Consul` ACL system: tokens, policies, roles, and auth methods
    * Bootstrapping `ACLs` and managing least-privilege access

<!-- chapter: multi-datacenter-federation, duration: 2h -->
* Multi-Datacenter Federation
    * WAN gossip pool and datacenter peering models
    * Primary and secondary datacenter relationships
    * Cluster peering vs. WAN federation: tradeoffs and use cases
    * Cross-datacenter service discovery and failover configuration

<!-- chapter: observability-and-monitoring, duration: 2h -->
* Observability and Monitoring
    * `Consul` telemetry: `statsd`, `dogstatsd`, and `Prometheus` integration
    * L7 observability with `Envoy` metrics and access logs
    * Distributed tracing with `Zipkin` and `Jaeger` via `Envoy`
    * `Consul` UI: navigating nodes, services, intentions, and KV

<!-- chapter: consul-on-kubernetes, duration: 2h -->
* `Consul` on `Kubernetes`
    * Deploying `Consul` with the official `Helm` chart
    * `consul-k8s` `CLI` for installation and upgrade management
    * Transparent proxy and pod annotation-based service registration
    * Integrating `Consul` with `Vault` for certificate management on `Kubernetes`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
