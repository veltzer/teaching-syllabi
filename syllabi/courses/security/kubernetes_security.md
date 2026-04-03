---
tags:
  - security:security
  - security:kubernetes-security
  - infrastructure:kubernetes
  - infrastructure:containers
  - security:rbac
  - security:runtime-security
level: advanced
category: security
duration_hours: 16
audience:
  - audiences:devops
  - audiences:developers
  - audiences:architects
  - audiences:security-professionals
  - audiences:sres
---
<!-- course: kubernetes_security -->
# `Kubernetes` Security

## Description
Securing `Kubernetes` clusters requires deep knowledge of the platform's security primitives and best practices. This course covers pod security standards, network policies, admission controllers, role-based access control, secrets management, container image scanning, and runtime security. Participants will learn how to harden `Kubernetes` environments against real-world threats and implement defense-in-depth strategies for containerized workloads.

## Duration
16 hours / 2 days

## Intended Audience
* `Kubernetes` administrators and platform engineers
* `DevOps` and `DevSecOps` engineers
* Cloud security engineers and architects
* Site reliability engineers (SRE)
* Software engineers deploying to `Kubernetes`
* Anyone responsible for securing containerized workloads

## Prerequisites
* Hands-on experience with `Kubernetes` (deploying and managing workloads)
* Understanding of `Kubernetes` architecture: control plane, nodes, pods, services
* Familiarity with `Docker` and container fundamentals
* Basic knowledge of `Linux` security concepts and command-line usage
* Understanding of networking fundamentals (`TCP`/`IP`, `DNS`, load balancing)
* Experience with `YAML` and `Kubernetes` manifest files
* Familiarity with `kubectl` and `Helm`

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)
* `Helm` (or equivalent experience)

## Objectives
* Implement and enforce `Pod Security Standards` across namespaces
* Design and apply `Network Policies` to control pod-to-pod and external traffic
* Configure admission controllers including `OPA Gatekeeper` and `Kyverno` for policy enforcement
* Implement fine-grained `RBAC` policies following the principle of least privilege
* Manage secrets securely using `Kubernetes` secrets, `Sealed Secrets`, and external secret operators
* Integrate container image scanning into `CI/CD` pipelines and enforce image policies
* Deploy and configure runtime security tools for threat detection and response
* Harden `Kubernetes` cluster components and `API` server configurations

## Outline
<!-- chapter: kubernetes-security-fundamentals, duration: 2h -->
* `Kubernetes` Security Fundamentals
    * `Kubernetes` attack surface and threat landscape
    * Security layers in `Kubernetes`: cluster, node, pod, container
    * `CIS Kubernetes Benchmark` overview and assessment
    * `API` server authentication and authorization mechanisms
    * `Kubernetes` security context and security-related fields
    * Supply chain security for `Kubernetes` deployments
<!-- chapter: pod-security-standards, duration: 2h -->
* Pod Security Standards
    * Evolution from PodSecurityPolicy to `Pod Security Standards`
    * Privileged, Baseline, and Restricted profiles
    * Configuring `Pod Security Admission` controller
    * Enforcing security contexts: runAsNonRoot, readOnlyRootFilesystem, allowPrivilegeEscalation
    * `Linux` capabilities management: dropping and adding capabilities
    * Seccomp profiles and `AppArmor`/`SELinux` integration
    * Pod-level vs container-level security settings
<!-- chapter: network-policies, duration: 2h -->
* Network Policies
    * `Kubernetes` networking model and security implications
    * Network policy specification: `ingress` and egress rules
    * Namespace isolation and default deny policies
    * Label-based traffic selection and CIDR-based rules
    * Network policy providers: Calico, Cilium, Weave
    * Service mesh security with `Istio` and `Linkerd`
    * Mutual `TLS` (mTLS) for service-to-service communication
    * Monitoring and troubleshooting network policies
<!-- chapter: admission-controllers, duration: 2h -->
* Admission Controllers
    * Built-in admission controllers and their security roles
    * Validating and mutating admission webhooks
    * `OPA Gatekeeper`: architecture, constraint templates, and constraints
    * `Kyverno`: policy definitions and enforcement modes
    * Policy examples: image registry restrictions, resource limits, label requirements
    * Audit mode vs enforcement mode strategies
    * Managing policy exceptions and exemptions
    * Testing and validating admission policies
<!-- chapter: role-based-access-control-rbac, duration: 2h -->
* Role-Based Access Control (`RBAC`)
    * `RBAC` components: Roles, ClusterRoles, RoleBindings, ClusterRoleBindings
    * Designing least-privilege `RBAC` policies
    * Service account management and token security
    * Aggregated ClusterRoles and role composition
    * `RBAC` for multi-tenant clusters
    * Auditing `RBAC` configurations and detecting excessive permissions
    * Integration with external identity providers (`OIDC`, `LDAP`)
    * Automating `RBAC` management and drift detection
<!-- chapter: secrets-management, duration: 2h -->
* Secrets Management
    * `Kubernetes` secrets: types, creation, and limitations
    * Encryption at `rest` for etcd secret storage
    * `Sealed Secrets` for `GitOps`-safe secret management
    * External secrets operators: `AWS Secrets Manager`, `HashiCorp Vault`, `Azure Key Vault`
    * CSI Secret Store driver for volume-mounted secrets
    * Secret rotation and lifecycle management
    * Preventing secret exposure in logs and environment variables
<!-- chapter: container-image-scanning, duration: 2h -->
* Container Image Scanning
    * Container image security fundamentals and layered filesystem risks
    * Image scanning tools: `Trivy`, `Grype`, `Snyk Container`
    * Vulnerability databases and severity scoring
    * Integrating image scanning into `CI/CD` pipelines
    * Image signing and verification with `Cosign` and `Sigstore`
    * Enforcing trusted image registries with admission controllers
    * Base image selection and minimal image strategies (distroless, scratch)
    * Continuous monitoring for newly discovered vulnerabilities
<!-- chapter: runtime-security, duration: 2h -->
* Runtime Security
    * Runtime threat detection with Falco and Tetragon
    * System call monitoring and anomaly detection
    * `File` integrity monitoring in containers
    * Process execution monitoring and whitelisting
    * Runtime network monitoring and anomalous connection detection
    * Forensics and incident response in `Kubernetes` environments
    * `eBPF`-based security observability
    * Automated response and workload isolation strategies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
