---
tags:
  - tools:podman
  - practices:devops
  - practices:automation
  - tools:docker
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: podman -->
# Podman: Daemonless Container Engine

## Description
This course covers Podman, a daemonless and rootless container engine for developing, managing, and running `OCI` containers. Participants will learn how to build images, run containers, work with pods, and integrate with `systemd`. The course also covers Buildah, Skopeo, and migration strategies from `Docker`.

## Duration
16 hours / 1 day

## Intended Audience
* Developers working with containers in development and `CI/CD`
* `DevOps` engineers evaluating alternatives to `Docker`
* System administrators managing containerized workloads

## Prerequisites
* Basic understanding of containers and container images.
* Familiarity with `Linux` command line.
* Experience with `Docker` is helpful but not required.

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand the Podman architecture and its differences from `Docker`.
* Build container images using Containerfile/`Dockerfile`.
* Run and manage containers and pods with Podman.
* Configure rootless containers for improved security.
* Use Buildah for advanced image building and Skopeo for image management.
* Integrate containers with `systemd` for service management.
* Generate `Kubernetes` `YAML` from Podman pods.

## Outline
<!-- chapter: introduction-to-podman, duration: 1h -->
* Introduction to Podman:
    * Podman overview and history
    * Daemonless architecture
    * Podman vs `Docker`
    * `OCI` standards and compatibility
<!-- chapter: container-fundamentals-with-podman, duration: 2h -->
* Container Fundamentals with Podman:
    * Pulling and listing images
    * Running containers
    * Container lifecycle management
    * Inspecting and logging
    * Environment variables and resource limits
<!-- chapter: building-images, duration: 1h -->
* Building Images:
    * Containerfile/`Dockerfile` syntax
    * Building images with `podman build`
    * Multi-stage builds
    * Layer caching and optimization
<!-- chapter: pods, duration: 1h -->
* Pods:
    * Pod concept in Podman
    * Creating and managing pods
    * Shared namespaces within pods
    * Use cases for pods
<!-- chapter: networking, duration: 2h -->
* Networking:
    * Container networking modes
    * Port mapping and publishing
    * CNI and Netavark network backends
    * Creating custom networks
    * Container-to-container communication
<!-- chapter: volumes-and-storage, duration: 1h -->
* Volumes and Storage:
    * Named volumes
    * `Bind` mounts
    * `Tmpfs` mounts
    * Volume management
<!-- chapter: podman-compose, duration: 1h -->
* `Podman Compose`:
    * Installing and using `Podman Compose`
    * Compose `file` compatibility
    * Differences from `Docker Compose`
<!-- chapter: systemd-integration, duration: 1h -->
* `systemd` Integration:
    * Generating `systemd` unit files
    * Running containers as `systemd` services
    * Auto-update and rollback
    * Quadlet for container definitions
<!-- chapter: buildah-for-advanced-image-building, duration: 1h -->
* Buildah for Advanced Image Building:
    * Buildah command-line usage
    * Building images without a `Dockerfile`
    * Scripted image builds
    * Minimizing image size
<!-- chapter: skopeo-for-image-management, duration: 1h -->
* Skopeo for Image Management:
    * Inspecting remote images
    * Copying images between registries
    * Signing and verifying images
<!-- chapter: rootless-containers-and-security, duration: 1h -->
* Rootless Containers and Security:
    * Rootless container architecture
    * User namespace mapping
    * Security benefits and limitations
    * `SELinux` and seccomp profiles
<!-- chapter: migration-from-docker, duration: 1h -->
* Migration from `Docker`:
    * `Docker` `CLI` compatibility
    * Migrating scripts and workflows
    * `Docker` socket emulation
<!-- chapter: kubernetes-yaml-generation, duration: 1h -->
* `Kubernetes` `YAML` Generation:
    * Generating `Kubernetes` manifests from pods
    * Playing `Kubernetes` `YAML` with Podman
<!-- chapter: ci-cd-integration, duration: 1h -->
* `CI/CD` Integration:
    * Using Podman in `CI/CD` pipelines
    * `GitHub Actions` and `GitLab CI` examples
    * Rootless containers in CI environments

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
