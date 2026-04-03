---
tags:
  - infrastructure:aws
  - infrastructure:cloud
  - concepts:architecture
  - concepts:scalability
level: intermediate
category: cloud
duration_hours: 40
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:architects
  - audiences:devops
  - audiences:managers
---
<!-- course: aws_architecting -->
# `AWS` architecting

## Description
The Cloud is the most important advance in designing highly available, fault
tolerant and scalable web or data processing applications. `AWS` is the premiere
cloud provider today. This course teaches how to utilize the services offered
by `AWS` in order to design and implement the most efficient, cost effective,
easy to code and easy to maintain systems which will run on `AWS` infrastructure.

We will cover both IASS and PASS topics teaching both how to port on-prem
applications to the cloud and use `AWS` as a IASS provider but also how
to use `AWS` as a PASS provider which should cut costs and investment.

## Duration
40 hours / 5 days

## Intended Audience
This could can be attended by anyone with IT experience. In fact attendees often
have diverse backgrounds: Infrastructure, IT, programmers, data base administrators,
system administrators, `DevOps` people, team leaders, architects,
finance administrators, managers and more.

Experience in IT is a requirement and a plus.

## Prerequisites
Experience in IT in some field is required.

## Objectives
* The participants will be able to receive requirements for applications and design the right architecture for this
application in the `AWS` cloud. This means they will be able to distinguish between
the different main services that `AWS` provides, decide which will be more effective
in which case and be able to monitor and change their decisions as conditions change.
* This course can also be used to prepare one for `AWS` associate architect certification
exam.

## Exercises
* [Real live exercises](`https`://amazon.qwiklabs.com)

## Outline
<!-- chapter: aws-overview, duration: 1h -->
* `AWS` overview.
<!-- chapter: types-of-applications, duration: 1h -->
* Types of applications:
    * pure cloud
    * hybrid
    * on-prem
<!-- chapter: principles-of-designing-highly-available-fault-tolerant-scalable-systems, duration: 1h -->
* Principles of designing highly available, fault tolerant, scalable systems.
<!-- chapter: iass-services-intro, duration: 2h -->
* IASS services intro.
    * regions
    * availability zones
    * best practices
<!-- chapter: infrastructure-services, duration: 8h -->
* Infrastructure services
    * `VPC`
    * subnets
    * security groups
    * NACLS
    * IGW
    * Elastic `IPs`
    * `ELB`
    * Standard patterns
        * multiple availability zones
        * load balancers on entry
        * load balancers between layers
        * separation of subnets
        * multiple VPCs
        * bastion hosts
        * multiple accounts
<!-- chapter: identity-and-secure-access-services, duration: 2h -->
* Identity and secure access services
    * `IAM`
    * users, groups, roles
    * best practices
    * interfacing other identity systems.
<!-- chapter: ec2, duration: 3h -->
* `EC2`
    * machine types
    * `AMIs`
    * `EBS`
    * Ephemeral storage
    * Pricing
    * Monitoring (`CloudWatch`)
    * `Auto scaling`
<!-- chapter: storage-and-mass-data-access-services, duration: 5h -->
* Storage and mass data access services
    * `S3`
    * `Glacier`
    * Storage Gateway
    * Snow family
    * `EFS`
    * `FSx`
    * `AWS` Backup.
    * Cloud Front
    * Security and encryption
    * Route53.
    * Other offerings
<!-- chapter: application-services, duration: 2h -->
* Application services
    * `SQS`
    * `SNS`
    * Elastic Transcoder
    * Workspaces
    * Other offerings
<!-- chapter: database-services, duration: 3h -->
* Database services
    * `RDS`
    * `DynamoDB`
    * Database Migration Service (DMS).
    * Aurora
    * ElastiCache
    * `Redshift`
    * Other offerings
<!-- chapter: high-level-services, duration: 2h -->
* High level services
    * Elastic Beanstalk
    * OpsWorks
    * Cloud Formation
    * Other offerings
<!-- chapter: networking-services, duration: 2h -->
* Networking services
    * PrivateLink
    * `Direct Connect`
    * `Transit Gateway`
    * Other offerings
<!-- chapter: developer-and-devops-services, duration: 3h -->
* Developer and `Devops` services
    * CodeCommit
    * CodeBuild
    * CodePipeline
    * `CodeDeploy`
    * CodeStar
    * Other offerings
<!-- chapter: container-and-serverless-services, duration: 4h -->
* Container and Serverless services
    * Container Registry
    * `EKS`
    * `ECS`
    * Fargate
    * `API` Gateway
    * `Lambda`
    * How to combine with `API` gateway, `Kinesis`, `S3`, `DynamoDb`, ...
    * `Step Functions`
    * Other offerings
<!-- chapter: conclusions, duration: 1h -->
* Conclusions
    * Cloud best practices.
    * Keeping up with `AWS`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
