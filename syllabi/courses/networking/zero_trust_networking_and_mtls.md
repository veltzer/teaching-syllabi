---
tags:
  - concepts:network-security
  - concepts:identity
  - concepts:certificates
  - concepts:pki
  - concepts:cryptography
  - concepts:service-mesh
  - concepts:microservices
level: advanced
category: networking
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:devops
  - audiences:security-engineers
  - audiences:network-engineers
  - audiences:architects
---
<!-- course: zero_trust_networking_and_mtls -->
# Zero Trust Networking and `mTLS`

## Description
The classic perimeter security model is dead. Modern systems run across clouds, regions, vendors and edges, with
no meaningful "inside the network". Zero trust networking replaces the perimeter with strong workload identity,
mutual `TLS` everywhere, and explicit authorization on every request.

This five day course is the implementation-focused complement to the policy-level zero trust security material
already in the catalog. It covers workload identity (`SPIFFE`/`SPIRE`, cloud workload identity), `mTLS` at scale,
service-to-service auth patterns (`JWT`, `OAuth2`, signed requests, `SPIFFE` `JWT-SVID`), zero trust gateways
(`BeyondCorp`, IAP, `Cloudflare Access`), `service mesh`-driven mutual auth, and the operational disciplines
that `make` zero trust workable in practice. Participants leave able to design and operate zero trust networks for
their own workloads.

## Duration
40 hours / 5 days

## Intended Audience
* developers building services that need to authenticate other services
* `DevOps` and platform engineers operating zero trust infrastructure
* security engineers implementing zero trust networking
* architects designing distributed systems with strong identity boundaries
* network engineers transitioning from perimeter-based to identity-based models

## Prerequisites
* working knowledge of `TLS`, `PKI` and public-key cryptography
* familiarity with `Kubernetes` and modern cloud platforms
* basic understanding of `JWT`, `OAuth2` and `OIDC`
* experience operating at least one production service

## Objectives
* explain the zero trust model and how it differs from perimeter security
* implement workload identity using `SPIFFE`/`SPIRE` or cloud-native equivalents
* deploy and operate `mTLS` at scale, including rotation and bootstrapping
* design service-to-service authorization for diverse workload types
* integrate zero trust with `service mesh`, `API` gateway and load balancer infrastructure
* federate identity across clusters, clouds and organizations
* operate zero trust systems with appropriate observability and incident tooling

## Outline
<!-- chapter: the-zero-trust-model, duration: 2h -->
* The zero trust model
    * the failure of perimeter security
    * the zero trust principles
    * `BeyondCorp` and Google's deployment
    * the `NIST` zero trust architecture
    * misconceptions about zero trust
    * what zero trust does and does not solve
<!-- chapter: workload-identity-fundamentals, duration: 3h -->
* Workload identity fundamentals
    * the principle "every workload has an identity"
    * machine identity vs human identity
    * identity bootstrapping and the secret-zero problem
    * attestation and proof of identity
    * naming and identity hierarchies
    * comparing workload identity systems
<!-- chapter: spiffe-and-spire, duration: 4h -->
* `SPIFFE` and `SPIRE`
    * the `SPIFFE` identity model and `SPIFFE ID`
    * `X509-SVID` and `JWT-SVID`
    * `SPIRE` server and agent architecture
    * node attestation and workload attestation
    * federation across `SPIRE` deployments
    * `SPIRE` deployment topologies
    * integrating `SPIRE` with applications
<!-- chapter: cloud-workload-identity, duration: 3h -->
* Cloud workload identity
    * `AWS IAM` roles for `EC2`, `EKS` IRSA, `Pod` Identity
    * `GCP` workload identity for `GKE` and beyond
    * `Azure` managed identity and workload identity
    * cross-cloud identity federation
    * identity in serverless workloads
    * comparing cloud-native identity to `SPIFFE`
<!-- chapter: tls-fundamentals-revisited, duration: 2h -->
* `TLS` fundamentals revisited
    * the `TLS` 1.3 handshake
    * cipher suites and curves
    * certificate verification semantics
    * `OCSP`, stapling and revocation
    * `SNI`, `ALPN` and ECH
    * `TLS` performance considerations at scale
<!-- chapter: pki-for-zero-trust, duration: 3h -->
* `PKI` for zero trust
    * `CA` design for service-to-service `PKI`
    * private vs public `CAs`
    * intermediate `CAs`, cross-signing, root rotation
    * short-lived certificates as the new default
    * `cert-manager`, `step-ca`, cloud-managed `PKI`
    * certificate transparency for internal `PKI`
<!-- chapter: mtls-in-practice, duration: 4h -->
* `mTLS` in practice
    * the `mTLS` handshake step by step
    * client certificate validation
    * `SAN` and URI-`SAN` for `SPIFFE` `IDs`
    * server-side configuration in Envoy, `nginx`, `HAProxy`, application servers
    * client-side configuration in Go, `Java`, `Python`, `Node.js`
    * connection reuse and the cost of `mTLS`
    * common `mTLS` debugging scenarios
<!-- chapter: certificate-rotation-and-renewal, duration: 2h -->
* Certificate rotation and renewal
    * automated renewal pipelines
    * watching for renewal in long-lived processes
    * graceful key rotation
    * revocation, blocklists and short lifetimes
    * monitoring certificate expiry
    * outage stories from expired certificates
<!-- chapter: service-to-service-authentication-patterns, duration: 3h -->
* Service-to-service authentication patterns
    * `mTLS` as authentication
    * `JWT`-based service auth
    * `SPIFFE` `JWT-SVID`
    * signed requests (`SigV4`-style)
    * combining `mTLS` and token-based auth
    * end-user identity propagation across services
<!-- chapter: authorization-on-every-request, duration: 3h -->
* Authorization on every request
    * separating authentication from authorization
    * policy engines: `OPA`, Cerbos, `Casbin`
    * `service mesh` authorization policies
    * relationship-based access control across services
    * fine-grained vs coarse-grained policy
    * the audit trail of denied requests
<!-- chapter: zero-trust-and-service-mesh, duration: 3h -->
* Zero trust and `service mesh`
    * what a `service mesh` does and does not provide
    * `Istio`, `Linkerd`, `Consul Connect`, Cilium `Service Mesh`
    * automatic `mTLS` between meshed services
    * `SPIFFE` integration in meshes
    * `AuthorizationPolicy` and RequestAuthentication in `Istio`
    * meshes vs in-app implementations
<!-- chapter: zero-trust-gateways-and-access, duration: 2h -->
* Zero trust gateways and access
    * `BeyondCorp` for human access
    * `Google IAP`, `Cloudflare Access`, `Tailscale`, `Teleport`
    * device posture and conditional access
    * `SSO` integration
    * privileged access management for engineers
<!-- chapter: federation-across-trust-domains, duration: 2h -->
* Federation across trust domains
    * federating identity across clusters
    * federating across clouds
    * federating across organizations (`B2B`)
    * `SPIFFE` federation in detail
    * trust bundles and their distribution
    * the limits of federation
<!-- chapter: observability-for-zero-trust, duration: 2h -->
* Observability for zero trust
    * audit logs for authentication events
    * dashboards for `mTLS` health
    * detecting unauthorized identity use
    * alerting on certificate near-expiry
    * anomaly detection on service-to-service traffic
    * incident response with identity context
<!-- chapter: migration-from-perimeter-to-zero-trust, duration: 1h -->
* Migration from perimeter to zero trust
    * the realistic stepwise migration
    * coexistence of perimeter and zero trust
    * the high-value first targets
    * organizational change required
    * common migration pitfalls
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * end-to-end design walkthrough on a sample multi-cluster system
    * tabletop incident: compromised workload identity
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
