---
tags:
  - infrastructure:cloud
  - concepts:architecture
  - concepts:scalability
  - concepts:design-patterns
level: intermediate
category: cloud
duration_hours: 32
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:architects
  - audiences:devops
---
<!-- course: architecting_in_the_cloud -->
# Architecting in the Cloud

## Description
The cloud, either public or private, is the new development environment for web or other types of
applications. As a new environment is espouses new paradigms and ideas and requires architects that
have a good grasp of these new paradigms and ideas. This course teaches these paradigms and ideas.
This is an architecture course, this means it does not deal a lot with actual programming, but rather
with the right tools, paradigms and `design patterns` that should be used for scalable, fault tolerant,
frugal and efficient application in the cloud.

## Duration
32 hours / 4 days

## Intended Audience
* System administrators, `Devops` people, Developers and Team leaders who would like to learn cloud related architecture.
* Architects which are familiar with old school designs but are not familiar with the cloud.
* Cloud practitioners who would like to learn the new "server-less" patterns in the modern cloud.

## Prerequisites
* Tech affinity is a plus
* Experience with any type of cloud is a plus

## Objectives
* Understand principles of application design in the cloud
* Understand `design patterns` in the cloud
* Understand anti-patterns and how to avoid them
* Understand where PAAS can help design of modern applications.
* Create designs of scalable, fault tolerant, frugal and efficient cloud apps.
* Be able to weigh designs one against another.
* Describe various `design patterns` of cloud apps.
* Describe the benefits of various PAAS systems and decide `when` to use them and `when` to build their own.

## Outline
<!-- chapter: introduction, duration: 2h -->
* Introduction
    * Advantages of `cloud computing`
    * Well architected apps: basic principles
    * First example of a scalable cloud architecture
<!-- chapter: identity-and-security-in-the-cloud, duration: 2h -->
* Identity and security in the cloud
    * Mapping corporate identities to cloud identities
    * Creating `VPN` with the cloud
    * Dedicated connections to the cloud
    * Working with several accounts
<!-- chapter: renting-machines, duration: 4h -->
* Renting machines
    * What are machines in the cloud?
    * What is your responsibility?
    * Should you get your own machine?
    * Security on your own machine
    * Where is my machine, anyway?
    * Cost issues.
    * Organizing your machines.
    * Disks for your machines.
<!-- chapter: basic-application-scalability, duration: 2h -->
* Basic application scalability
    * Scalable load balancers
    * Defining rules for scalability
    * Spreading across data centers
    * Should you `go` "server-less"?
<!-- chapter: distributed-storage, duration: 2h -->
* Distributed storage
    * What do you get?
    * How costly is it?
    * How is it different from a disk?
    * What types of durability do you get?
<!-- chapter: distributed-queues, duration: 3h -->
* Distributed queues
    * What do you get?
    * How costly is it?
    * Is it better to do it on your own?
    * What guarantees do you get from various cloud queues?
<!-- chapter: container-orchestration-in-the-cloud, duration: 2h -->
* Container Orchestration in the Cloud
    * Introduction
    * Managed k8s
    * Do you need a cloud portable application anyway?
<!-- chapter: cloud-functions, duration: 3h -->
* `Cloud functions`
    * What is it?
    * How do you pay?
    * Why is it better than renting your own machines?
    * Chains of functions and other various patterns.
<!-- chapter: disaster-recovery-in-the-cloud, duration: 2h -->
* Disaster recovery in the cloud
    * Using the cloud as a disaster recovery
    * Using fault tolerance instead of disaster recovery
    * patterns of disaster recovery in the cloud
<!-- chapter: data-storage-in-the-cloud, duration: 3h -->
* Data storage in the cloud
    * Relational vs `NoSQL`
    * Managed relational databases
    * Managed `NoSQL` databases
    * Rolling databases on your own.
    * Caching in the cloud
<!-- chapter: caching, duration: 2h -->
* Caching
    * Caching close to the client
    * Managed caches inside the app
<!-- chapter: patterns, duration: 2h -->
* Patterns
    * Allowing apps to access cloud services
    * Allowing direct download from cloud scalable storage
    * Allowing direct access to non data center caches
<!-- chapter: other-cloud-services, duration: 3h -->
* Other cloud services
    * `DevOps`
    * mobile
    * testing
    * `AI`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
