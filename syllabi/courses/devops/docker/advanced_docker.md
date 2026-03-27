---
tags:
  - tools:docker
  - infrastructure:containers
  - practices:devops
  - networking:networking
level: advanced
category: devops
duration_days: 2
audience:
  - audiences:developers
  - practices:devops
---
# Advanced `Docker`

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Docker` is an open-source project that automates the deployment of
application inside software containers. `Docker` provides an integrated
technology suite that enables development and IT operations teams to build,
ship, and run distributed applications anywhere. `Docker` lets you run
your software components on any platform that supports `Docker` containers.

## Duration
16 hours / 2 days

## Intended Audience
This course is for developers and IT operations teams who already use `Docker`
and wish to acquire a deeper understanding of underlying infrastructure in
order to improve the way they operate containerized workloads.

## Prerequisites
* Basic experience building and running `Docker` containers.
* Basic `Docker` CLI knowledge.
* Prior experience in developing web applications will be helpful but is not required.
* Basic knowledge of `Linux` file system and network stack.

## Objectives
* Understand the more advanced aspects of `Docker` container deployment like volumes and networking.

## Outline
* `Docker` Internals and Architecture
    * `Docker` engine architecture deep dive
    * Containerd and runc: the building blocks of `Docker`
    * Namespaces and cgroups: the core of container isolation
    * OCI (Open Container Initiative) specifications
    * `Docker` daemon and `API`
    * Comparison with other containerization technologies
* Advanced Dockerfile Techniques and Image Optimization
    * Multi-stage builds for optimized images
    * Dockerfile best practices for security and efficiency
    * BuildKit and new Dockerfile features
    * Creating minimal base images
    * Optimizing layer caching
    * Image inspection and analysis
    * Custom base image creation
* `Docker` Networking in Depth
    * Network drivers: bridge, host, overlay, macvlan
    * Creating and managing custom bridge networks
    * Network namespaces and how `Docker` uses them
    * Network plugins and extensibility
    * Troubleshooting `Docker` networking issues
    * `DNS` and service discovery in `Docker`
    * Container-to-container communication
    * Exposing container services to the outside world
* Advanced `Docker` Storage and Volumes
    * Storage drivers: overlay2, devicemapper, btrfs
    * Volume plugins and remote storage integration
    * Data management and backup strategies
    * Persistent storage patterns for stateful applications
    * Copy-on-write (CoW) filesystem internals
    * Tmpfs mounts for non-persistent state
    * Bind mounts vs volumes: when to use each
    * Managing data in multi-container applications
* `Docker` Security and Compliance
    * Securing the `Docker` daemon and engine
    * Container isolation techniques
    * `Linux` capabilities and seccomp profiles
    * `Docker` Content Trust and image signing
    * Security scanning for `Docker` images
    * CIS `Docker` Benchmark implementation
    * AppArmor and SELinux with `Docker`
    * Runtime privilege and access control
    * Network security in `Docker`
* `Docker` in Production
    * Logging drivers and log management
    * Monitoring `Docker` containers and the `Docker` engine
    * Debugging containers in production environments
    * Implementing health checks and auto-healing
    * Resource constraints and performance tuning
    * `Docker` daemon configuration for production
    * Container lifecycle management
    * Backup and restore strategies for `Docker` environments
    * `Docker` upgrade and maintenance in production

## Installations
* A real `Ubuntu` >= 22.04 running on a laptop.
* A `Windows`/macOS system running on a laptop with an `Ubuntu` >= 22.04 virtual machine on top. This could be done using Hyper-V or `Oracle` VirtualBox.
* Access to a remote `Ubuntu` >= 22.04 machine via ssh (command line, putty, MobaXterm, ...). The machine could be in a company private cloud or a public cloud.
* In any case the student must have sudo/root on this virtual machine.
* In all cases the installations are not a must and the instructor will guide the students how to do the installations on the first day of the course.
* The virtual machines should have at least 4GB of memory.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
