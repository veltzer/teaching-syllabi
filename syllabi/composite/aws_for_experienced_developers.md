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
152 hours/9 days

## Intended Audience
This course is intended for people with experience in IT who wish to extend their
capabilities to include the `AWS` cloud.

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
[Real live exercises on Qwiklabs](https://amazon.qwiklabs.com)

## Outline
* `AWS` overview.
* Types of applications:
    * pure cloud
    * hybrid
    * on-prem
* Principles of designing highly available, fault tolerant, scalable systems.
* IASS services intro.
    * regions
    * availability zones
    * best practices
* Infrastructure services
    * `VPC`
    * subnets
    * security groups
    * NACLS
    * Private endpoints
    * VGW, IGW and other network connections
    * Elastic IPs
    * Load balancing (ALB, ELB)
    * `VPC` Peering options and transit GW.
    * Standard patterns
        * multiple availability zones
        * load balancers on entry
        * load balancers between layers
        * separation of subnets
        * multiple VPCs
        * bastion hosts
        * multiple accounts
* Identity and secure access services
    * `IAM`
    * users, groups, roles
    * best practices
    * interfacing other identity systems.
    * `AWS` organization.
    * Landing Zone.
* Security
    * KMS
    * Encryption in transit and at rest.
* `EC2`
    * machine types
    * AMIs
    * EBS
    * Ephemeral storage
    * Pricing
    * Monitoring (CloudWatch)
    * Auditing (CloudTrail)
    * Auto scaling
* Storage and mass data access services
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
* Application services
    * SQS
    * SNS
    * Elastic Transcoder
    * Workspaces
    * Other offerings
* Database and Analytics services
    * RDS
    * `DynamoDB`
    * Database Migration Service (DMS).
    * Aurora
    * ElastiCache
    * Redshift
    * Other offerings
* High level services
    * Elastic Beanstalk
    * OpsWorks
    * Cloud Formation
    * `Terraform` on `AWS`
    * Other offerings
* Networking services
    * PrivateLink
    * Direct Connect
    * Transit Gateway
    * Other offerings
* Developer and Devops services
    * CodeCommit
    * CodeBuild
    * CodePipeline
    * CodeDeploy
    * CodeStar
    * Other offerings
* Container and Serverless services
    * Container Registry
    * `EKS`
    * `ECS`
    * Fargate
    * `API` Gateway
    * `Lambda`
    * How to combine with `API` gateway, Kinesis, `S3`, DynamoDb, ...
    * Step Functions
    * Other offerings
* Machine learning services
    * Amazon Polly
    * Amazon Transcribe
    * Amazon SageMaker
    * Amazon Lex
    * Amazon Rekognition
    * Amazon Comprehend
    * Amazon Translate
* Managing application users
    * Cognito
    * `AWS` SSO.
* Conclusions
    * Cloud best practices.
    * Keeping up with `AWS`

## Copyright
Mark Veltzer, © 2026
