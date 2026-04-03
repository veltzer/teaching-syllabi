---
tags:
  - infrastructure:cloud
  - infrastructure:virtualization
  - practices:devops
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:architects
  - audiences:developers
---
<!-- course: openstack -->
# OpenStack

## Description
This course provides a comprehensive exploration of OpenStack, the leading open-source platform for building and managing private and hybrid clouds. Participants will learn the architecture and core services of OpenStack, including identity management, compute, networking, storage, and orchestration. The course covers both operational knowledge and hands-on deployment using DevStack and Kolla, preparing participants to deploy, manage, and troubleshoot production OpenStack environments.

## Duration
24 hours / 3 days

## Intended Audience
* System administrators looking to build and manage private cloud infrastructure.
* `DevOps` engineers integrating OpenStack into their workflows.
* Solutions architects designing private and hybrid cloud deployments.
* Developers building applications on OpenStack-based platforms.

## Prerequisites
* `Solid` understanding of `Linux` system administration.
* Familiarity with virtualization concepts (`KVM`, hypervisors).
* Basic knowledge of networking (`IP` addressing, VLANs, routing).

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Explain private cloud concepts and how OpenStack fits into the cloud landscape.
* Describe the OpenStack architecture and the role of each core service.
* Configure and manage identity, authentication, and authorization with Keystone.
* Provision and manage virtual machines using Nova.
* Design and configure software-defined networks with Neutron.
* Manage block storage with Cinder and object storage with `Swift`.
* Work with virtual machine images using Glance.
* Orchestrate multi-service deployments with Heat templates.
* Navigate and use the Horizon dashboard for day-to-day operations.
* Deploy OpenStack environments using DevStack and Kolla.
* Monitor and operate an OpenStack cloud in production.

## Outline
<!-- chapter: private-cloud-concepts, duration: 2h -->
* Private Cloud Concepts
    * Public, private, and hybrid cloud models
    * Why private cloud and `when` to use it
    * OpenStack vs. other private cloud platforms
<!-- chapter: openstack-architecture, duration: 2h -->
* OpenStack Architecture
    * High-level architecture overview
    * Service catalog and APIs
    * Message queue and database backends
    * Deployment topologies
<!-- chapter: keystone-identity-service, duration: 2h -->
* Keystone - Identity Service
    * Authentication and authorization
    * Domains, projects, users, and roles
    * Token management
    * Integration with `LDAP` and external identity providers
<!-- chapter: nova-compute-service, duration: 2h -->
* Nova - Compute Service
    * Nova architecture and components
    * Launching and managing instances
    * Flavors and availability zones
    * Live migration and evacuation
<!-- chapter: neutron-networking-service, duration: 2h -->
* Neutron - Networking Service
    * Software-defined networking in OpenStack
    * Networks, subnets, and routers
    * Security groups and floating `IPs`
    * Neutron plugins and agents
<!-- chapter: cinder-block-storage, duration: 2h -->
* Cinder - Block Storage
    * Block storage concepts
    * Volume creation, attachment, and snapshots
    * Storage backends and drivers
    * Backup and restore
<!-- chapter: swift-object-storage, duration: 2h -->
* `Swift` - Object Storage
    * Object storage concepts and architecture
    * Containers and objects
    * Replication and data durability
    * Access control and temporary URLs
<!-- chapter: glance-image-service, duration: 2h -->
* Glance - Image Service
    * Image formats and properties
    * Uploading and managing images
    * Image sharing between projects
    * Image caching
<!-- chapter: heat-orchestration-service, duration: 2h -->
* Heat - Orchestration Service
    * Infrastructure as code with Heat
    * Heat Orchestration Template (HOT) syntax
    * Stacks, resources, and parameters
    * Auto-scaling with Heat
<!-- chapter: horizon-dashboard, duration: 2h -->
* Horizon - Dashboard
    * Navigating the Horizon interface
    * Managing resources through the dashboard
    * Customizing Horizon
<!-- chapter: deployment-with-devstack-and-kolla, duration: 2h -->
* Deployment with DevStack and Kolla
    * Setting up DevStack for development and testing
    * Kolla containers and Kolla-`Ansible`
    * Deployment best practices
    * Upgrading OpenStack releases
<!-- chapter: operations-and-monitoring, duration: 2h -->
* Operations and Monitoring
    * Log management and centralized logging
    * Monitoring with Ceilometer and `Prometheus`
    * Capacity planning
    * Troubleshooting common issues
    * Backup and disaster recovery

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
