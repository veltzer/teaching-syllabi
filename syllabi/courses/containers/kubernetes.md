---
tags:
  - infrastructure:kubernetes
  - infrastructure:containers
  - infrastructure:docker
  - practices:devops
  - practices:ci-cd
  - infrastructure:cloud
level: intermediate
category: containers
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: kubernetes -->
# `Kubernetes`

## Description
This course provides a thorough introduction to `Kubernetes`, the industry-standard
container orchestration platform. Students will learn how to deploy, manage, and scale
containerized applications on a `Kubernetes` cluster. The course covers core concepts
such as pods, services, and deployments, as well as more advanced topics including
Helm charts, `RBAC`, networking, `ingress`, configuration management, and observability.
By the end of the course, students will have the practical skills needed to operate
and manage production-grade `Kubernetes` environments.

## Duration
24 hours / 3 days

## Intended Audience
* Developers who want to deploy and manage their applications on `Kubernetes`.
* System administrators and infrastructure engineers adopting `Kubernetes`.
* `DevOps` engineers building and maintaining `Kubernetes`-based platforms.
* Anyone with basic container knowledge who wants to learn container orchestration.

## Prerequisites
* Working knowledge of `Docker` and containerization concepts.
* Familiarity with the `Linux` command line.
* Basic understanding of networking (`TCP`/`IP`, `DNS`, `HTTP`).
* Some experience with `YAML` syntax.

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand the `Kubernetes` architecture and its core components
* Deploy and manage applications using pods, deployments, and ReplicaSets
* Configure service discovery and load balancing with `Kubernetes` services
* Manage application configuration using `ConfigMaps` and Secrets
* Set up `ingress` controllers and networking policies
* Implement role-based access control (`RBAC`)
* Use Helm to package and deploy applications
* Monitor and observe `Kubernetes` workloads

## Outline
<!-- chapter: introduction-to-kubernetes, duration: 3h -->
* Introduction to `Kubernetes`
    * What is container orchestration?
    * The history and evolution of `Kubernetes`
    * `Kubernetes` architecture overview
        * Control plane components: `API server`, etcd, scheduler, controller manager
        * Worker node components: kubelet, kube-proxy, container runtime
    * Installing and configuring `kubectl`
    * Setting up a local cluster with `minikube` or kind
    * Navigating the `Kubernetes` `API`
<!-- chapter: pods, duration: 3h -->
* Pods
    * What is a pod?
    * Pod lifecycle and phases
    * Creating pods from `YAML` manifests
    * Multi-container pods: sidecar, init containers
    * Pod resource requests and limits
    * Pod health checks: liveness, readiness, and startup probes
    * Debugging and troubleshooting pods
<!-- chapter: replicasets-and-deployments, duration: 2h -->
* ReplicaSets and Deployments
    * What is a ReplicaSet?
    * Scaling applications with ReplicaSets
    * Deployments and declarative updates
    * Rolling updates and rollbacks
    * Deployment strategies: rolling update, recreate
    * Managing deployment history and revisions
<!-- chapter: services-and-service-discovery, duration: 2h -->
* Services and Service Discovery
    * The need for services in `Kubernetes`
    * Service types: ClusterIP, NodePort, LoadBalancer, ExternalName
    * Selectors and label matching
    * `DNS`-based service discovery
    * Headless services
    * Endpoints and endpoint slices
<!-- chapter: configmaps-and-secrets, duration: 2h -->
* `ConfigMaps` and Secrets
    * Separating configuration from code
    * Creating and managing `ConfigMaps`
    * Injecting configuration via environment variables and volume mounts
    * Creating and managing Secrets
    * Secret types and encoding
    * Best practices for managing sensitive data
<!-- chapter: networking, duration: 2h -->
* Networking
    * `Kubernetes` networking model
    * Pod-to-pod communication
    * The CNI (Container Network Interface) model
    * Network policies: `ingress` and egress rules
    * Restricting traffic between namespaces
    * `CoreDNS` and `DNS` in `Kubernetes`
<!-- chapter: ingress, duration: 2h -->
* Ingress
    * What is Ingress?
    * Ingress controllers: `NGINX`, `Traefik`, and others
    * Defining Ingress resources
    * Path-based and host-based routing
    * `TLS` termination with Ingress
    * Ingress annotations and customization
<!-- chapter: role-based-access-control-rbac, duration: 2h -->
* Role-Based Access Control (`RBAC`)
    * Authentication and authorization in `Kubernetes`
    * Roles and ClusterRoles
    * RoleBindings and ClusterRoleBindings
    * Service accounts
    * Least privilege principles
    * Auditing access and permissions
<!-- chapter: helm, duration: 3h -->
* Helm
    * What is Helm and why use it?
    * Helm charts: structure and components
    * Installing and managing applications with Helm
    * Chart repositories
    * Customizing deployments with values files
    * Creating your own Helm charts
    * Chart versioning and dependency management
<!-- chapter: observability, duration: 3h -->
* Observability
    * The three pillars of observability: logs, metrics, and traces
    * Collecting and viewing container logs
    * `Kubernetes` events and auditing
    * Monitoring with `Prometheus` and `Grafana`
    * Metrics server and resource monitoring
    * Introduction to distributed tracing
    * Alerting strategies and best practices

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
