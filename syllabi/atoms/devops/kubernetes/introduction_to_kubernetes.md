---
tags:
  - kubernetes
  - docker
  - containers
  - devops
  - orchestration
level: beginner
category: devops
duration_days: 5
audience:
  - developers
  - devops
---
# Introduction to `Kubernetes`

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Kubernetes` (`k8s`) is fast becoming the industry standard for container orchestration and this is an introductory
course to that technology. The course takes the participants from no knowledge of containers and container
orchestration to a beginner level in using `docker` and orchestrating `docker` containers with `Kubernetes`.

The course includes training on real live systems and orchestrating real live clusters.

The course begins with an introduction to `Docker` and `Kubernetes` covering the basics and installation and configuration. Next, students will learn about resources, pods, and controllers. The course ends with a look into services, volumes, and cluster administration.

## Duration
40 hours / 5 days

## Intended Audience
* Developers who wish to deploy small applications or better understand their own production environments.
* Architects who wish to understand `Kubernetes` and container orchestration to utilize these technologies within
their respective companies and application design schemes.
* Devops people who are are not familiar with `Kubernetes` and `docker` and would like to add these technologies to their
tool chest.
* Cloud practitioners who wish to understand `Kubernetes` in order to better decide between `Kubernetes` and other
more cloud specific offering.

## Prerequisites
* Experience in tech environments is a must
* Understanding of web applications at a basic level is a must
* `DevOps` experience is a plus
* System administration experience is a plus
* Cloud familiarity with one of the big three cloud platforms is a plus

## Objectives
* Describe the `Docker` and `Kubernetes` technologies, their main uses, advantages and disadvantages.
* Create, manage run and debug `docker` images.
* Deploy `Kubernetes` clusters and manage them.
* Write `Kubernetes` deployment descriptors and modify them to their needs.
* Debug `Kubernetes` run time issues.
* Have a basic understanding of the various techniques to upgrade `Kubernetes` application at production

## Outline
* `Docker`
    * Overview
    * `Docker` Containers
    * `Docker` vs. Virtual Machines (`VM`)
    * `Docker` vs. Processes
* Intro to `Kubernetes`
    * Containers
    * History
    * Architecture
    * Resources
    * Where to go for help
    * `Micro services`
* Installation and Configuration
    * Installation options
    * Minikube install
    * Install `Kubernetes`
* CLI Overview
    * Overview
    * CLI
* `Kubernetes` Basics
    * Create a cluster
    * Deploy an app
* Expose Your App
    * Expose your app
* Scale Your App
    * Scale your app
* `Kubernetes` Resources
    * Master
    * Node
    * Pod
    * Labels
    * Configure Pods and Containers
* Dashboard
    * `Kubernetes` Dashboard
    * Dashboard Tour
    * Services
    * Controller Manager
    * Assign Memory and CPU to Containers
* Pods
    * Pod Life cycle
    * Pod Status
    * Container Health Checks
        * Liveness probes
        * Readiness probes
        * Startup probes
* ConfigMaps and Secrets
    * Why are they needed?
    * How to use them
    * Best practices for secret management
* Namespaces and Multi-tenancy
    * Resource isolation
    * Namespace strategies
    * Resource quotas
* Controllers
    * Deployment
    * StatefulSet
    * DaemonSet
    * Controllers
* Services
    * Defining a Service
    * Discovering Services
    * Virtual IPs
    * Services
* Volumes
    * Overview
    * PersistentVolume
    * Configure a Pod to Use a Volume for Storage
    * Configure a Pod to Use Persistent Volume
* `Kubernetes` Networking
    * Pod-to-Pod communication
    * Service networking and ClusterIP
    * NodePort and LoadBalancer services
    * Network policies
    * `DNS` in `Kubernetes`
* Ingress Controllers
    * What is Ingress?
    * Popular Ingress controllers (NGINX, Traefik)
    * `TLS`/SSL termination
    * Path-based and host-based routing
* Container Registries and Image Management
    * `Docker` Hub and private registries
    * Image tagging strategies
    * Pull policies and secrets
    * Image security scanning basics
* Resource Management
    * CPU and Memory requests/limits
    * Quality of Service (QoS) classes
    * Resource quotas
    * LimitRanges
* Security Fundamentals
    * Role-Based Access Control (RBAC)
    * ServiceAccounts
    * Security contexts
    * Pod security policies/standards
    * Network policies for security
* Troubleshooting and Debugging
    * Common `Kubernetes` issues
    * Using kubectl debug
    * Analyzing logs and events
    * Debugging CrashLoopBackOff
    * Performance troubleshooting
* Helm Package Manager
    * Introduction to Helm
    * Charts and repositories
    * Installing and managing applications
    * Creating custom charts
    * Helm templating basics
* GitOps and `CI/CD` Integration
    * `Kubernetes` in `CI/CD` pipelines
    * GitOps principles
    * Deployment strategies (rolling, blue-green, canary)
    * Introduction to ArgoCD/Flux (overview)
* Cluster Administration
    * CLI
    * Contexts
    * Scaling
    * Monitoring with metrics-server
    * Dashboards
    * Backup and disaster recovery basics
    * Cluster upgrades
* Advanced Topics (if time permits)
    * Advanced workload types (StatefulSet, DaemonSet, Job, CronJob)
    * Multi-container patterns (sidecar, init containers, ambassador)
    * Custom Resource Definitions (CRDs)
    * Operators pattern
    * Service mesh overview (Istio/Linkerd)

## Installations
Each student should have:

* An `Ubuntu` 24:04 machine
* 8 GB RAM for each machine because we are going to practice `Kubernetes` with Minikube. This requires some RAM.
* Free, wide band, access to the internet from all machines with no weird corporate firewalls that might stop us from installing software.
* Username and password of a user that has `sudo` privileges on the machine.
* [https://www.linuxvmimages.com/images/ubuntu-2204/](https://www.linuxvmimages.com/images/ubuntu-2204/)
