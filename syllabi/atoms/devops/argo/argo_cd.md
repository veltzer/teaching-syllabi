---
tags:
  - argo-cd
  - kubernetes
  - ci-cd
  - gitops
  - devops
level: intermediate
category: devops
duration_days: 2
audience:
  - devops
  - developers
---
# Argo CD

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
In the rapidly evolving world of software development and deployment, `Continuous Delivery` (`CD`) plays a
pivotal role in enabling teams to deliver high-quality applications faster and more efficiently. As
`Kubernetes` (`K8S`) has become the de facto standard for container orchestration, CD into `Kubernetes` has
become an essential skill for modern `DevOps` engineers and software developers.
The "`Argo CD`" course is a comprehensive 2-day program designed to equip participants with the
knowledge and hands-on experience necessary to master `Argo CD`, a powerful and open-source tool
tailored for `Continuous Delivery` in `Kubernetes` environments. Throughout the course, participants will gain
a deep understanding of `Argo CD's` principles, capabilities, and practical implementation to streamline
application deployments in `Kubernetes` clusters.

## Duration
16 hours / 2 days

## Intended Audience
* System administrators
* Developers

## Prerequisites
* Working knowledge of `Kubernetes`
* Experience with software deployment

## Objectives
* Understand the theory behind `Argo CD`, what problems it solves and why it is needed.
* Get hands on experience in deploying applications using Argo CD.
* Get to know how to deal with issues of Argo CD and in particular rollback.

## Exercises
Throughout the course, participants will engage in hands-on labs to reinforce the concepts learned. Labs
will include tasks such as:

* Installing Argo CD on a `Kubernetes` cluster.
* Configuring Argo CD applications to deploy sample applications.
* Setting up GitOps workflows with Argo CD.
* Creating and managing CD pipelines with Argo Workflows.

## Outline
* Introduction and Gitops Theory
    * Why? Advantaged and disadvantages vs older systems (`Jenkins`)...
* Overview of Argo CD Features and Architecture
    * Argo CD as a `Kubernetes` (K8S) controller
    * Components (`API` server, repository server, controller)
    * K8S with GitOps
* Exploring the Argo CD Workflow
    * Workflow phases
    * Desired versus observed states
* Getting Started with Argo CD
    * Configuring Argo CD
    * Command-line and web interfaces
    * Accessing the `API` server
* Creating an Application with Argo CD
    * Registering a cluster to deploy apps to
    * Creating and syncing apps
* Deploying an Application with Argo CD
    * Changing destination
    * Deployment history and rollback
    * Failed deployments
* Working with K8S Management Tools
    * Deployment and orchestration tools
    * Automated syncing
* Integrating Argo CD Into a `CI/CD` Pipeline
    * GitOps integration into a pipeline
    * Adding and monitoring apps
    * `CI/CD` workflow completion

## Copyright
Mark Veltzer, © 2026
