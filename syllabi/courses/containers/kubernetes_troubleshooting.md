---
tags:
  - infrastructure:kubernetes
  - infrastructure:containers
  - practices:devops
level: advanced
category: containers
duration_hours: 16
audience:
  - audiences:devops
  - audiences:sres
  - audiences:sysadmins
---
<!-- course: kubernetes_troubleshooting -->
# `Kubernetes` Troubleshooting

## Description
This two day advanced course equips engineers with the skills to diagnose and resolve common and complex issues in `Kubernetes` clusters. Students will learn systematic approaches to debugging pods, networking, `DNS`, resource constraints, and node-level problems using built-in tools such as `kubectl debug` and ephemeral containers, as well as strategies for cluster recovery.

## Duration
16 hours / 2 days

## Intended Audience
* `DevOps` engineers managing `Kubernetes` clusters
* Site reliability engineers responsible for cluster uptime
* Platform engineers building internal developer platforms on `Kubernetes`

## Prerequisites
* Working knowledge of `Kubernetes` concepts (pods, deployments, services, namespaces)
* Experience deploying applications on `Kubernetes`
* Familiarity with `Linux` command-line tools
* Basic understanding of container networking

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Develop a systematic methodology for troubleshooting `Kubernetes` workloads.
* Diagnose and resolve pod-level failures including CrashLoopBackOff and image pull errors.
* Identify and fix networking and `DNS` issues within a cluster.
* Use `kubectl debug` and ephemeral containers to inspect running workloads.
* Analyze resource limits and node conditions to resolve scheduling and performance problems.
* Perform cluster recovery procedures after failures.

## Outline
<!-- chapter: troubleshooting-methodology, duration: 1h -->
* Troubleshooting Methodology
    * Systematic approach to `Kubernetes` debugging
    * Understanding the `Kubernetes` control plane components
    * Reading and interpreting events and conditions
    * Common failure patterns and their root causes
<!-- chapter: debugging-pod-failures, duration: 2h -->
* Debugging Pod Failures
    * Pod lifecycle and status codes
    * Diagnosing CrashLoopBackOff
    * Image pull errors and registry authentication issues
    * OOMKilled and exit code analysis
    * Init container failures
    * Debugging multi-container pods
<!-- chapter: log-analysis, duration: 1h -->
* Log Analysis
    * Collecting logs with `kubectl logs`
    * Streaming and following logs across containers
    * Aggregating logs from multiple pods
    * Working with logging sidecars
    * Correlating application logs with `Kubernetes` events
<!-- chapter: using-kubectl-debug-and-ephemeral-containers, duration: 2h -->
* Using `kubectl debug` and Ephemeral Containers
    * Introduction to ephemeral containers
    * Attaching debug containers to running pods
    * Debugging distroless and minimal images
    * Node-level debugging with `kubectl debug node`
    * Copying pods for debugging with modified configurations
<!-- chapter: networking-troubleshooting, duration: 2h -->
* Networking Troubleshooting
    * `Kubernetes` networking model overview
    * Debugging Service connectivity issues
    * Ingress and load balancer troubleshooting
    * Network policy conflicts and misconfigurations
    * CNI plugin diagnostics
    * Using tools like `tcpdump`, `curl`, and `nslookup` from debug containers
<!-- chapter: dns-problems, duration: 2h -->
* `DNS` Problems
    * `CoreDNS` architecture and configuration
    * Diagnosing `DNS` resolution failures
    * `DNS` caching and `TTL` issues
    * Custom `DNS` policies and stub domains
    * `CoreDNS` performance and scaling
<!-- chapter: resource-limits-and-scheduling-issues, duration: 2h -->
* Resource Limits and Scheduling Issues
    * Understanding requests and limits
    * Diagnosing Pending pods and scheduling failures
    * Resource quota and limit range conflicts
    * Quality of service classes and eviction policies
    * Vertical and horizontal pod autoscaler issues
<!-- chapter: node-problems, duration: 2h -->
* Node Problems
    * Node conditions and status interpretation
    * kubelet diagnostics and logs
    * Disk pressure, memory pressure, and PID pressure
    * Node NotReady troubleshooting
    * Taints, tolerations, and node affinity issues
    * Container runtime troubleshooting
<!-- chapter: cluster-recovery, duration: 2h -->
* Cluster Recovery
    * etcd backup and restore procedures
    * Recovering from control plane failures
    * Handling split-brain scenarios
    * Certificate expiration and renewal
    * Disaster recovery planning and runbooks

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
