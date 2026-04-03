---
tags:
  - tools:kubernetes
  - infrastructure:containers
  - practices:devops
  - languages:go
  - concepts:service-mesh
level: advanced
category: devops
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: advanced_kubernetes -->
# Advanced `Kubernetes`

## Description
The Advanced `Kubernetes` training course is designed for students with a basic understanding of `Kubernetes` wanting to venture into customizing clusters by creating business-specific components to deliver more powerful solutions. This course focuses on advanced topics such as deploying resilient applications, extending `Kubernetes`, cluster provisioning, and traffic shifting with network policies.

The course begins with deploying resilient applications, extending `Kubernetes`, cluster provisioning, and ServiceMesh. Next, the course dives into three levels of `Kubernetes` administration. The course concludes with a lesson on roles and access control and a review of Serverless.

The course will be code heavy using GoLang to tap into the various APIs to build enhanced `Kubernetes` powered clusters. Prerequisites include a working knowledge of `Kubernetes` as well as GoLang.

## Duration
24 hours / 3 days

## Intended Audience
* Developers and developer teams needing a better way to manage containers.
* People who are already familiar with `Kubernetes` basics.

## Prerequisites
* Some knowledge of `go` is required

## Required Knowledge
* `Go` Programming (or equivalent experience)

## Objectives
* Design and deploy resilient applications.
* Apply next-level command-line tools like Kube-scheduler, cloud-controller-manager, operators, and more.
* Provision clusters with Kube-admin and cluster `API`.
* Utilize `RBAC` to regulate access to a computer or network resources based on the roles of individual users within an enterprise.

## Outline
<!-- chapter: deploying-resilient-applications, duration: 4h -->
* Deploying Resilient Applications
    * ReplicaSets
    * StatefulSets
    * Resources
    * Probes
    * HorizontalPodAutoscaler
    * Cluster Autoscaler
<!-- chapter: extending-kubernetes, duration: 3h -->
* Extending `Kubernetes`
    * Schedulers
    * Controllers
    * Operators
    * Init Containers
    * Custom Resource Definitions
<!-- chapter: cluster-provisioning, duration: 1h -->
* Cluster Provisioning
    * Kubeadm
    * Cluster `API`
<!-- chapter: observability, duration: 3h -->
* Observability
    * `Prometheus`
    * OpenTracing
<!-- chapter: servicemesh, duration: 2h -->
* ServiceMesh
    * Traffic shifting and network policies
<!-- chapter: advanced-k8s-administration-i, duration: 4h -->
* Advanced K8S Administration I
    * DaemonSets
    * Jobs
    * CronJobs
    * Advanced Volume Usage
    * `ConfigMaps`
    * Secrets
<!-- chapter: advanced-k8s-administration-ii, duration: 2h -->
* Advanced K8S Administration II
    * Controlling K8S using declarative object configuration
    * Use cases, best practices and real-life examples
<!-- chapter: advanced-k8s-administration-iii, duration: 2h -->
* Advanced K8S Administration III
    * Patterns for deployment and updates
    * Best practices in rolling upgrades, canary deploys, blue-green deploys etc
<!-- chapter: roles-and-access-control, duration: 2h -->
* Roles and Access Control
    * Role-Based Authentication
<!-- chapter: serverless, duration: 1h -->
* Serverless
    * Knative

## References
[advanced-`Kubernetes`](`https`://www.pluralsight.com/professional-services/it-ops/advanced-`Kubernetes`)

## Installations
Each student should have:
* An `Ubuntu` 24:04 machine
* 8 GB `RAM` for each machine because we are going to practice `Kubernetes` with `Minikube`. This requires some `RAM`.
* Free, wide band, access to the internet from all machines with no weird corporate firewalls that might stop us from installing software.
* Username and password of a user that has `sudo` privileges on the machine.
* [`https`://www.linuxvmimages.com/images/`ubuntu`-2204/](`https`://www.linuxvmimages.com/images/`ubuntu`-2204/)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
