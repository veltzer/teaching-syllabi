---
tags:
  - security:security
  - tools:docker
  - tools:kubernetes
level: advanced
category: security
duration_hours: 24
audience:
  - audiences:security-professionals
  - audiences:developers
  - audiences:architects
  - audiences:devops
---
<!-- course: container_and_kubernetes_security -->
# Container and `Kubernetes` Security

## Description
Containers and `Kubernetes` have become the standard for deploying modern applications, but they introduce unique security challenges at every layer of the stack. This advanced course covers container security from image building through runtime, `Kubernetes` security architecture, policy enforcement, supply chain integrity, and runtime threat detection. Participants will learn to secure containerized workloads using industry-leading tools and practices.

## Duration
24 hours / 3 days

## Intended Audience
* Security professionals and security architects
* Software developers working with containerized applications
* `DevOps` and platform engineers managing `Kubernetes` clusters
* Site reliability engineers (SREs)
* Cloud architects designing container platforms
* Anyone responsible for securing container-based infrastructure

## Prerequisites
* Working knowledge of `Docker` and container fundamentals
* Basic understanding of `Kubernetes` architecture (pods, deployments, services)
* Familiarity with `Linux` command-line and system administration
* Understanding of networking concepts (`TCP`/`IP`, `DNS`, load balancing)
* Basic knowledge of `YAML` and configuration management
* Familiarity with `CI/CD` pipeline concepts
* Understanding of basic security principles (authentication, authorization, encryption)

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Identify and mitigate security risks across the container lifecycle
* Build secure container images following `Dockerfile` best practices
* Understand and leverage `Linux` security primitives that underpin container isolation
* Configure `Kubernetes` `RBAC`, Pod Security Standards, and network policies
* Implement admission controllers using `OPA Gatekeeper` and `Kyverno`
* Deploy service mesh security with mutual `TLS` using `Istio`
* Establish supply chain security with `SBOM` generation, `Sigstore`, and `cosign`
* Set up runtime threat detection using Falco and Tetragon
* Perform container forensics and incident response
* Apply CIS benchmarks and compliance scanning to container environments

## Outline
<!-- chapter: container-security-fundamentals, duration: 1h -->
* Container Security Fundamentals
    * Container architecture and attack surface overview
    * Container isolation vs virtual machine isolation
    * Common container security threats and vulnerabilities
    * Container security lifecycle: build, ship, run
    * Threat modeling for containerized applications
    * Container security principles and defense in depth
<!-- chapter: image-security, duration: 2h -->
* Image Security
    * Container image layers and security implications
    * Choosing secure base images and Distroless images
    * Image vulnerability scanning with `Trivy`, `Grype`, and Snyk
    * Image signing and verification workflows
    * Private registry security and access control
    * Image provenance and attestation
    * Minimizing image attack surface and reducing image size
<!-- chapter: dockerfile-best-practices, duration: 2h -->
* `Dockerfile` Best Practices
    * Multi-stage builds for minimal production images
    * Running containers as non-root users
    * Avoiding secrets in `Dockerfile` layers and build arguments
    * Pinning base image versions and dependency versions
    * Using COPY vs ADD and reducing layer count
    * Linting Dockerfiles with hadolint
    * Read-only `file` systems and minimal capabilities
<!-- chapter: linux-security-primitives-for-containers, duration: 2h -->
* `Linux` Security Primitives for Containers
    * `Linux` namespaces and isolation boundaries
    * `cgroups` for resource constraints and abuse prevention
    * seccomp profiles for system call filtering
    * `AppArmor` profiles for mandatory access control
    * `SELinux` policies for container confinement
    * Capabilities and privilege escalation prevention
    * User namespaces and rootless containers
<!-- chapter: kubernetes-security-model, duration: 2h -->
* `Kubernetes` Security Model
    * `Kubernetes` architecture and security boundaries
    * `API` server authentication and authorization mechanisms
    * etcd security and encryption of data at `rest`
    * Kubelet security and node authorization
    * Securing the `Kubernetes` control plane
    * `Kubernetes` security audit and threat model
    * Cluster hardening and version management
<!-- chapter: role-based-access-control-rbac, duration: 1h -->
* Role-Based Access Control (`RBAC`)
    * `Kubernetes` `RBAC` architecture: roles, bindings, and subjects
    * Designing least-privilege `RBAC` policies
    * Cluster roles vs namespace roles
    * Service account management and token security
    * Auditing `RBAC` configurations and detecting over-permissioned accounts
    * `RBAC` testing and validation strategies
<!-- chapter: pod-security-standards-and-policies, duration: 1h -->
* Pod Security Standards and Policies
    * Pod Security Standards: privileged, baseline, and restricted
    * Pod Security Admission controller configuration
    * Security contexts at pod and container level
    * Restricting privileged containers and host access
    * Volume and mount security considerations
    * Ephemeral containers for debugging and security implications
<!-- chapter: network-policies, duration: 2h -->
* Network Policies
    * `Kubernetes` network model and default behavior
    * Network policy specification and label-based selection
    * `Ingress` and egress traffic controls
    * Default deny policies and micro-segmentation
    * Network policy providers: Calico, Cilium, Weave
    * `DNS`-based and FQDN-based network policies
    * Monitoring and troubleshooting network policies
<!-- chapter: secrets-management-in-kubernetes, duration: 1h -->
* Secrets Management in `Kubernetes`
    * `Kubernetes` secrets architecture and limitations
    * Encrypting secrets at `rest` with EncryptionConfiguration
    * External secret management with `External Secrets Operator`
    * Integration with `HashiCorp Vault` and CSI secret store driver
    * `Sealed secrets` and `GitOps`-friendly workflows
    * Secret rotation and lifecycle management
<!-- chapter: service-mesh-security, duration: 2h -->
* Service Mesh Security
    * Service mesh architecture and security benefits
    * Mutual `TLS` (mTLS) with `Istio`
    * `Istio` authorization policies and traffic control
    * `Istio` peer authentication and request authentication
    * Certificate management and rotation in the mesh
    * Observability and security monitoring with service mesh
    * `Linkerd` security features and comparison
<!-- chapter: admission-controllers, duration: 2h -->
* Admission Controllers
    * Admission controller architecture: validating and mutating
    * `OPA Gatekeeper` policies and constraint templates
    * `Kyverno` policy engine and policy types
    * Enforcing image policies and registry restrictions
    * Mutating defaults for security contexts
    * Policy testing and `CI/CD` integration
    * Policy exceptions and emergency overrides
<!-- chapter: supply-chain-security, duration: 2h -->
* Supply Chain Security
    * Software supply chain threats in the container ecosystem
    * Software bill of materials (`SBOM`) generation and consumption
    * `Sigstore` ecosystem: `cosign`, Rekor, and `Fulcio`
    * Container image signing with `cosign`
    * Build provenance with `SLSA` framework
    * Verifying artifacts in admission controllers
    * Secure `CI/CD` pipeline design for container workloads
<!-- chapter: runtime-threat-detection, duration: 2h -->
* Runtime Threat Detection
    * Runtime security monitoring architecture
    * Falco rules engine and custom rule authoring
    * Tetragon `eBPF`-based security observability
    * Detecting anomalous process execution and network activity
    * `File` integrity monitoring in containers
    * Automated response and kill chains
    * Integration with `SIEM` and alerting systems
<!-- chapter: container-forensics-and-incident-response, duration: 1h -->
* Container Forensics and Incident Response
    * Container forensics challenges and methodology
    * Collecting evidence from running and stopped containers
    * Analyzing container `file` systems and logs
    * Network traffic capture and analysis in container environments
    * Incident response playbooks for container breaches
    * Post-incident recovery and hardening
<!-- chapter: cis-benchmarks-and-compliance-scanning, duration: 1h -->
* CIS Benchmarks and Compliance Scanning
    * CIS benchmarks for `Docker` and `Kubernetes`
    * Automated compliance scanning with kube-bench
    * `Kubernetes` cluster compliance with Polaris and kubescape
    * Continuous compliance monitoring and reporting
    * Remediation strategies for common benchmark failures
    * Compliance as code and policy-driven governance

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
