---
tags:
  - cloud
  - architecture
  - scalability
  - design-patterns
level: intermediate
category: cloud
duration_days: 4
audience:
  - developers
  - sysadmins
  - devops
  - architects
---
# Architecting in the Cloud

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
The cloud, either public or private, is the new development environment for web or other types of
applications. As a new environment is espouses new paradigms and ideas and requires architects that
have a good grasp of these new paradigms and ideas. This course teaches these paradigms and ideas.
This is an architecture course, this means it does not deal a lot with actual programming, but rather
with the right tools, paradigms and design patterns that should be used for scalable, fault tolerant,
frugal and efficient application in the cloud.

## Duration
32 hours / 4 days

## Intended Audience
* System administrators, Devops people, Developers and Team leaders who would like to learn cloud related architecture.
* Architects which are familiar with old school designs but are not familiar with the cloud.
* Cloud practitioners who would like to learn the new "server-less" patterns in the modern cloud.

## Prerequisites
* Tech affinity is a plus
* Experience with any type of cloud is a plus

## Objectives
* Understand principles of application design in the cloud
* Understand design patterns in the cloud
* Understand anti-patterns and how to avoid them
* Understand where PAAS can help design of modern applications.
* Create designs of scalable, fault tolerant, frugal and efficient cloud apps.
* Be able to weigh designs one against another.
* Describe various design patterns of cloud apps.
* Describe the benefits of various PAAS systems and decide when to use them and when to build their own.

## Outline
* Introduction
    * Advantages of cloud computing
    * Well architected apps: basic principles
    * First example of a scalable cloud architecture
* Identity and security in the cloud
    * Mapping corporate identities to cloud identities
    * Creating `VPN` with the cloud
    * Dedicated connections to the cloud
    * Working with several accounts
* Renting machines
    * What are machines in the cloud?
    * What is your responsibility?
    * Should you get your own machine?
    * Security on your own machine
    * Where is my machine, anyway?
    * Cost issues.
    * Organizing your machines.
    * Disks for your machines.
* Basic application scalability
    * Scalable load balancers
    * Defining rules for scalability
    * Spreading across data centers
    * Should you go "server-less"?
* Distributed storage
    * What do you get?
    * How costly is it?
    * How is it different from a disk?
    * What types of durability do you get?
* Distributed queues
    * What do you get?
    * How costly is it?
    * Is it better to do it on your own?
    * What guarantees do you get from various cloud queues?
* `Kubernetes` (`k8s`)
    * Introduction
    * Managed `k8s`
    * Do you need a cloud portable application anyway?
* Cloud functions
    * What is it?
    * How do you pay?
    * Why is it better than renting your own machines?
    * Chains of functions and other various patterns.
* Disaster recovery in the cloud
    * Using the cloud as a disaster recovery
    * Using fault tolerance instead of disaster recovery
    * patterns of disaster recovery in the cloud
* Data storage in the cloud
    * Relational vs `NoSQL`
    * Managed relational databases
    * Managed `NoSQL` databases
    * Rolling databases on your own.
    * Caching in the cloud
* Caching
    * Caching close to the client
    * Managed caches inside the app
* Patterns
    * Allowing apps to access cloud services
    * Allowing direct download from cloud scalable storage
    * Allowing direct access to non data center caches
* Other cloud services
    * `DevOps`
    * mobile
    * testing
    * `AI`

## Copyright
Mark Veltzer, © 2026
