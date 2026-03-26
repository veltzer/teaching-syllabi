---
tags:
  - aws
  - cloud
  - architecture
  - scalability
level: intermediate
category: cloud
duration_days: 5
audience:
  - developers
  - sysadmins
  - devops
  - architects
---
# `AWS` architecting

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

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
* [Real live exercises](https://amazon.qwiklabs.com)

## Outline
* `AWS` overview. 1h
* Types of applications: 1h
    * pure cloud
    * hybrid
    * on-prem
* Principles of designing highly available, fault tolerant, scalable systems. 1h
* IASS services intro. 1h
    * regions
    * availability zones
    * best practices
* Infrastructure services 4h
    * `VPC`
    * subnets
    * security groups
    * NACLS
    * IGW
    * Elastic IPs
    * ELB
    * Standard patterns
        * multiple availability zones
        * load balancers on entry
        * load balancers between layers
        * separation of subnets
        * multiple VPCs
        * bastion hosts
        * multiple accounts
* Identity and secure access services 3h
    * `IAM`
    * users, groups, roles
    * best practices
    * interfacing other identity systems.
* `EC2` 3h
    * machine types
    * AMIs
    * EBS
    * Ephemeral storage
    * Pricing
    * Monitoring (CloudWatch)
    * Auto scaling
* Storage and mass data access services 8h
    * `S3`
    * Glacier
    * Storage Gateway
    * Snow family
    * EFS
    * FSx
    * `AWS` Backup.
    * Cloud Front
    * Security and encryption
    * Route53.
    * Other offerings
* Application services 4h
    * SQS
    * SNS
    * Elastic Transcoder
    * Workspaces
    * Other offerings
* Database services 4h
    * RDS
    * `DynamoDB`
    * Database Migration Service (DMS).
    * Aurora
    * ElastiCache
    * Redshift
    * Other offerings
* High level services 2h
    * Elastic Beanstalk
    * OpsWorks
    * Cloud Formation
    * Other offerings
* Networking services 1h
    * PrivateLink
    * Direct Connect
    * Transit Gateway
    * Other offerings
* Developer and Devops services 2h
    * CodeCommit
    * CodeBuild
    * CodePipeline
    * CodeDeploy
    * CodeStar
    * Other offerings
* Container and Serverless services 3h
    * Container Registry
    * `EKS`
    * `ECS`
    * Fargate
    * `API` Gateway
    * `Lambda`
    * How to combine with `API` gateway, Kinesis, `S3`, DynamoDb, ...
    * Step Functions
    * Other offerings
* Conclusions 2h
    * Cloud best practices.
    * Keeping up with `AWS`
