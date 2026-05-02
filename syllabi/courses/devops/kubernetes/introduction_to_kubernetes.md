---
tags:
  - tools:kubernetes
  - tools:docker
  - infrastructure:containers
  - practices:devops
  - infrastructure:orchestration
level: beginner
category: devops
duration_hours: 32
audience:
  - audiences:developers
  - audiences:architects
  - audiences:devops
---
<!-- course: introduction_to_kubernetes -->
# Introduction to `Kubernetes`

## Description
`Kubernetes` (k8s) is fast becoming the industry standard for container orchestration and this is an introductory
course to that technology. The course takes the participants from no knowledge of containers and container
orchestration to a beginner level in using `docker` and orchestrating docker containers with `Kubernetes`.

The course includes training on real live systems and orchestrating real live clusters.

The course covers `Kubernetes` from installation and configuration through resources, pods, and controllers. The course ends with a look into services, volumes, and cluster administration.

## Duration
32 hours / 4 days

## Intended Audience
* Developers who wish to deploy small applications or better understand their own production environments.
* Architects who wish to understand `Kubernetes` and container orchestration to utilize these technologies within
their respective companies and application design schemes.
* `Devops` people who are are not familiar with `Kubernetes` and `docker` and would like to add these technologies to their
tool chest.
* Cloud practitioners who wish to understand `Kubernetes` in order to better decide between `Kubernetes` and other
more cloud specific offering.

## Prerequisites
* Experience in tech environments is a must
* Understanding of web applications at a basic level is a must
* `DevOps` experience is a plus
* System administration experience is a plus
* Cloud familiarity with one of the big three cloud platforms is a plus

## Required Knowledge
* `Docker` Fundamentals (or equivalent container experience)

## Objectives
* Describe `Kubernetes`, its main uses, advantages and disadvantages.
* Deploy `Kubernetes` clusters and manage them.
* Write `Kubernetes` deployment descriptors and modify them to their needs.
* Debug `Kubernetes` run time issues.
* Have a basic understanding of the various techniques to upgrade `Kubernetes` application at production

## Outline
<!-- chapter: intro-to-kubernetes, duration: 2h -->
* Intro to `Kubernetes`
    * Containers
    * History
    * Architecture
    * Resources
    * Where to `go` for help
    * `Micro services`
<!-- chapter: installation-and-configuration, duration: 1h -->
* Installation and Configuration
    * Installation options
    * `Minikube` install
    * Install `Kubernetes`
<!-- chapter: cli-overview, duration: 1h -->
* `CLI` Overview
    * Overview
    * `CLI`
<!-- chapter: kubernetes-basics, duration: 1h -->
* `Kubernetes` Basics
    * Create a cluster
    * Deploy an app
<!-- chapter: expose-your-app, duration: 1h -->
* Expose Your App
    * Expose your app
<!-- chapter: scale-your-app, duration: 1h -->
* Scale Your App
    * Scale your app
<!-- chapter: kubernetes-resources, duration: 1h -->
* `Kubernetes` Resources
    * Master
    * Node
    * Pod
    * Labels
    * Configure Pods and Containers
<!-- chapter: dashboard, duration: 1h -->
* Dashboard
    * `Kubernetes` Dashboard
    * Dashboard Tour
    * Services
    * Controller Manager
    * Assign Memory and `CPU` to Containers
<!-- chapter: pods, duration: 2h -->
* Pods
    * Pod Life cycle
    * Pod Status
    * Container Health Checks
        * Liveness probes
        * Readiness probes
        * Startup probes
<!-- chapter: configmaps-and-secrets, duration: 1h -->
* `ConfigMaps` and Secrets
    * Why are they needed?
    * How to use them
    * Best practices for secret management
<!-- chapter: namespaces-and-multi-tenancy, duration: 1h -->
* Namespaces and Multi-tenancy
    * Resource isolation
    * Namespace strategies
    * Resource quotas
<!-- chapter: controllers, duration: 1h -->
* Controllers
    * Deployment
    * StatefulSet
    * DaemonSet
    * Controllers
<!-- chapter: services, duration: 1h -->
* Services
    * Defining a Service
    * Discovering Services
    * Virtual `IPs`
    * Services
<!-- chapter: volumes, duration: 1h -->
* Volumes
    * Overview
    * PersistentVolume
    * Configure a Pod to Use a Volume for Storage
    * Configure a Pod to Use Persistent Volume
<!-- chapter: kubernetes-networking, duration: 1h -->
* `Kubernetes` Networking
    * Pod-to-Pod communication
    * Service networking and ClusterIP
    * NodePort and LoadBalancer services
    * Network policies
    * `DNS` in `Kubernetes`
<!-- chapter: ingress-controllers, duration: 1h -->
* Ingress Controllers
    * What is Ingress?
    * Popular Ingress controllers (`NGINX`, `Traefik`)
    * `TLS`/`SSL` termination
    * Path-based and host-based routing
<!-- chapter: container-registries-and-image-management, duration: 1h -->
* Container Registries and Image Management
    * `Docker` Hub and private registries
    * Image tagging strategies
    * Pull policies and secrets
    * Image security scanning basics
<!-- chapter: resource-management, duration: 1h -->
* Resource Management
    * `CPU` and Memory requests/limits
    * Quality of Service (QoS) classes
    * Resource quotas
    * LimitRanges
<!-- chapter: security-fundamentals, duration: 2h -->
* Security Fundamentals
    * Role-Based Access Control (`RBAC`)
    * ServiceAccounts
    * Security contexts
    * Pod security policies/standards
    * Network policies for security
<!-- chapter: troubleshooting-and-debugging, duration: 2h -->
* Troubleshooting and Debugging
    * Common `Kubernetes` issues
    * Using `kubectl` debug
    * Analyzing logs and events
    * Debugging CrashLoopBackOff
    * Performance troubleshooting
<!-- chapter: helm-package-manager, duration: 2h -->
* Helm Package Manager
    * Introduction to Helm
    * Charts and repositories
    * Installing and managing applications
    * Creating custom charts
    * Helm templating basics
<!-- chapter: gitops-and-ci-cd-integration, duration: 1h -->
* `GitOps` and `CI/CD` Integration
    * `Kubernetes` in `CI/CD` pipelines
    * `GitOps` principles
    * Deployment strategies (rolling, blue-green, canary)
    * Introduction to `ArgoCD`/`Flux` (overview)
<!-- chapter: cluster-administration, duration: 2h -->
* Cluster Administration
    * `CLI`
    * Contexts
    * Scaling
    * Monitoring with metrics-server
    * Dashboards
    * Backup and disaster recovery basics
    * Cluster upgrades
<!-- chapter: advanced-topics-if-time-permits, duration: 3h -->
* Advanced Topics (if time permits)
    * Advanced workload types (StatefulSet, DaemonSet, Job, CronJob)
    * Multi-container patterns (sidecar, init containers, ambassador)
    * Custom Resource Definitions (CRDs)
    * Operators pattern
    * Service mesh overview (`Istio`/`Linkerd`)

## Installations
Each student should have:

* An `Ubuntu` 24:04 machine
* 8 GB `RAM` for each machine because we are going to practice `Kubernetes` with `Minikube`. This requires some `RAM`.
* Free, wide band, access to the internet from all machines with no weird corporate firewalls that might stop us from installing software.
* Username and password of a user that has `sudo` privileges on the machine.
* [`https`://www.linuxvmimages.com/images/ubuntu-2204/](https://www.linuxvmimages.com/images/`ubuntu`-2204/)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
