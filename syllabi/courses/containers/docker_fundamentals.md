---
tags:
  - infrastructure:docker
  - infrastructure:containers
  - practices:devops
  - practices:ci-cd
level: beginner
category: containers
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: docker_fundamentals -->
# `Docker` Fundamentals

## Description
This course provides a comprehensive introduction to `Docker` and containerization technology.
Students will learn how to build, ship, and run applications using `Docker` containers.
The course covers everything from basic container concepts to advanced topics such as
multi-stage builds, networking, storage, and security best practices. By the end of the
course, students will be able to confidently containerize applications and manage
container-based environments.

## Duration
16 hours / 2 days

## Intended Audience
* Developers who want to containerize their applications.
* System administrators looking to adopt container technology in their infrastructure.
* `DevOps` engineers who need to integrate `Docker` into their `CI/CD` pipelines.
* Anyone interested in understanding modern containerization concepts and practices.

## Prerequisites
* Basic familiarity with the `Linux` command line.
* Understanding of basic networking concepts (`IP` addresses, ports, `DNS`).
* Some experience with application development in any language.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand the core concepts of containerization and how `Docker` works
* Build and manage `Docker` images using `Dockerfile`
* Run, inspect, and troubleshoot `Docker` containers
* Configure container networking and persistent storage
* Use `Docker Compose` to define and run multi-container applications
* Apply security best practices when building and running containers

## Outline
<!-- chapter: introduction-to-containers-and-docker, duration: 1h -->
* Introduction to Containers and `Docker`
    * What are containers and why do we need them?
    * Containers vs virtual machines
    * The history and evolution of containerization
    * `Docker` architecture: daemon, client, and registry
    * Installing `Docker` on `Linux`
    * The `Docker` `CLI` overview
<!-- chapter: docker-images, duration: 2h -->
* `Docker` Images
    * What is a `Docker` image?
    * Image layers and the union file system
    * Pulling images from `Docker Hub` and other registries
    * Listing, inspecting, and removing images
    * Image tagging and versioning strategies
    * Working with private registries
<!-- chapter: running-containers, duration: 2h -->
* Running Containers
    * Creating and running containers
    * Container lifecycle: start, stop, restart, remove
    * Running containers in the foreground and background
    * Attaching to and executing commands in running containers
    * Inspecting container logs and metadata
    * Resource limits: `CPU` and memory constraints
    * Environment variables and container configuration
<!-- chapter: building-images-with-dockerfile, duration: 3h -->
* Building Images with `Dockerfile`
    * `Dockerfile` syntax and instructions
    * FROM, RUN, COPY, ADD, WORKDIR, ENV, EXPOSE
    * CMD vs ENTRYPOINT
    * Build context and .dockerignore
    * Layer caching and build optimization
    * Multi-stage builds
        * Reducing image size with multi-stage builds
        * Separating build and runtime dependencies
        * Using named build stages
<!-- chapter: docker-networking, duration: 2h -->
* `Docker` Networking
    * `Docker` networking overview
    * Bridge, host, and none network drivers
    * Creating and managing custom networks
    * Container-to-container communication
    * Exposing and publishing ports
    * `DNS` resolution in `Docker` networks
<!-- chapter: docker-volumes-and-storage, duration: 2h -->
* `Docker` Volumes and Storage
    * The need for persistent storage
    * Volume types: named volumes, `bind` mounts, and `tmpfs`
    * Creating and managing volumes
    * Sharing data between containers
    * Volume drivers and storage backends
    * Backup and restore strategies
<!-- chapter: docker-compose, duration: 2h -->
* `Docker Compose`
    * What is `Docker Compose` and why use it?
    * The `docker`-compose.yml file structure
    * Defining services, networks, and volumes
    * Building and running multi-container applications
    * Environment files and variable substitution
    * Scaling services
    * Compose profiles and overrides
<!-- chapter: docker-security-best-practices, duration: 2h -->
* `Docker` Security Best Practices
    * Running containers as non-root users
    * Minimizing the attack surface with minimal base images
    * Scanning images for vulnerabilities
    * Using read-only file systems
    * Managing secrets securely
    * `Docker` Content Trust and image signing
    * Security considerations for the `Docker` daemon

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
