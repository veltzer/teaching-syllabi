---
tags:
  - concepts:gitops
  - concepts:security
  - concepts:operations
  - concepts:best-practices
  - concepts:scalability
level: advanced
category: containers
duration_hours: 24
audience:
  - audiences:devops
  - audiences:security-engineers
  - audiences:architects
  - audiences:senior-developers
---
<!-- course: kubernetes_multi_tenancy -->
# `Kubernetes` Multi-Tenancy

## Description
Once a `Kubernetes` cluster is shared by more than one team, multi-tenancy becomes the dominant
operational concern. The catalog has `Kubernetes`, `Kubernetes for Developers`, ```Kubernetes``
Troubleshooting`, ``Kubernetes` Security`, and the `Container and `Kubernetes` Security` course. None of
those is the focused course on operating a multi-tenant cluster: how to isolate tenants from each
other, how to give them autonomy without giving them everything, how to charge them, how to keep one
tenant from starving another, and how to know when single-cluster multi-tenancy is the wrong answer
and you should give each tenant their own cluster.

This three day course covers `Kubernetes` multi-tenancy as a focused engineering topic. It covers the
canonical tenancy models (soft, hard, virtual cluster), the namespace-as-tenant pattern and its
limits, the network-policy story, the pod-security-standards story, the resource-quota and
limit-range story, the noisy-neighbor problem, the per-tenant observability and cost-allocation, the
`vCluster` and Kamaji-style virtual clusters, the Capsule and `kiosk` operator approaches, the
deciding-when-to-give-each-tenant-a-cluster question, and the operational reality of running
multi-tenant clusters at scale. Examples are drawn from public engineering writing of Slack,
`Spotify`, Datadog, and the `CNCF` multi-tenancy `WG`. Participants leave able to design and operate
a `Kubernetes` multi-tenancy strategy.

## Duration
24 hours / 3 days

## Intended Audience
* `DevOps` engineers running shared `Kubernetes` clusters
* security engineers reviewing tenant isolation
* architects designing internal `PaaS`
* senior developers building multi-tenant `SaaS` on `Kubernetes`

## Prerequisites
* `solid` `Kubernetes` knowledge
* exposure to `Kubernetes Security` and the Container and `Kubernetes` Security course
* familiarity with at least one cluster operator
* basic understanding of `Linux` namespaces and `cgroups`

## Objectives
* explain the multi-tenancy models and pick one
* design namespace-as-tenant correctly
* enforce network and pod-security boundaries
* manage resource quotas and noisy neighbors
* run virtual clusters when the soft model is not enough
* allocate cost per tenant
* recognize when multi-cluster is the right answer

## Outline
<!-- chapter: tenancy-models, duration: 2h -->
* Tenancy models
    * soft multi-tenancy: trusted users, shared cluster
    * hard multi-tenancy: untrusted users, shared cluster
    * virtual cluster: each tenant gets a `Kubernetes API`-shaped slice
    * cluster-per-tenant
    * cross-reference to the Multi-tenant `SaaS` Architecture course
    * picking
<!-- chapter: namespace-as-tenant, duration: 2h -->
* Namespace as tenant
    * the canonical pattern
    * what namespaces give you
    * what namespaces do not give you
    * the cluster-scoped resource problem
    * the "namespace was a soft boundary, not a hard one" failure
<!-- chapter: rbac-for-multi-tenancy, duration: 2h -->
* `RBAC` for multi-tenancy
    * per-namespace `Role` and `RoleBinding`
    * the `ClusterRole`-with-`RoleBinding` trick
    * the per-tenant service accounts
    * `OIDC` integration for tenant users
    * the "we gave a team `cluster-admin` once" disaster
<!-- chapter: network-isolation, duration: 2h -->
* Network isolation
    * `NetworkPolicy` as the default-deny baseline
    * `Calico`, Cilium, `Kuma` enforcement
    * the egress-policy story
    * service-mesh-based isolation
    * cross-reference to the Service Mesh Comparison course
    * the "all pods could talk to all pods" reality
<!-- chapter: pod-security-standards, duration: 2h -->
* Pod-security standards
    * `restricted`, baseline, `privileged`
    * the per-namespace enforcement
    * the migration from `PodSecurityPolicy`
    * `OPA` Gatekeeper and `Kyverno` for policy
    * the "we shipped privileged pods to a tenant namespace" failure
<!-- chapter: resource-quotas-and-limits, duration: 2h -->
* Resource quotas and limits
    * `ResourceQuota` per namespace
    * `LimitRange` for default requests
    * the noisy-neighbor problem
    * the "the platform team's pod was evicted by a tenant" failure
    * the priority-class strategy
<!-- chapter: storage-isolation, duration: 1h -->
* Storage isolation
    * per-tenant storage classes
    * the `PVC`-can-cross-namespace problem
    * `CSI` drivers and tenant boundary
    * the "two tenants shared an `EBS` volume by accident" reality
    * the snapshot-and-clone question
<!-- chapter: virtual-clusters, duration: 3h -->
* Virtual clusters
    * `vCluster` overview
    * `Kamaji` overview
    * `Capsule` for soft-virtual
    * each tenant gets their own `kube-apiserver`
    * the cost-and-isolation trade-off
    * the "we used virtual clusters and it was the right call" experience
<!-- chapter: per-tenant-observability, duration: 2h -->
* Per-tenant observability
    * per-namespace metrics
    * per-tenant log routing
    * the cardinality cost of per-tenant labels
    * cross-reference to the Cardinality Engineering course
    * the "we have one dashboard for everyone" failure
<!-- chapter: cost-allocation, duration: 2h -->
* Cost allocation
    * `OpenCost` and `Kubecost`
    * the namespace-as-cost-center
    * the per-tenant chargeback
    * the shared-cost allocation question
    * cross-reference to the `FinOps` course
    * the "we cannot charge tenants because we cannot measure" reality
<!-- chapter: when-to-go-multi-cluster, duration: 1h -->
* `When` to `go` multi-cluster
    * the regulatory boundary
    * the trust boundary
    * the blast-`radius` requirement
    * the cost crossover
    * cross-reference to the Cell-Based Architecture course
<!-- chapter: operating-the-multi-tenant-platform, duration: 2h -->
* Operating the multi-tenant platform
    * the platform team as the operator
    * the tenant on-boarding workflow
    * the tenant off-boarding workflow
    * the "we forgot to delete the tenant's namespace" reality
    * the platform `SLO` per tenant
<!-- chapter: case-studies, duration: 1h -->
* Case studies
    * Slack's multi-tenancy story
    * `Datadog`'s internal platform
    * `Spotify`'s `Backstage`-driven model
    * the lessons learned
    * recommended reading: `CNCF Multi-Tenancy WG`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
