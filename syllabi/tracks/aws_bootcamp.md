# `AWS` oriented `DevOps` bootcamp

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course is tuned for people with little experiences taking them from very basic skills
to `DevOps` skilled tuned for the `AWS` environment.

## Duration
456 hours / 57 days

## Intended Audience
* Anyone coming into or transitioning into tech and wants to enter the industry as a `DevOps` person.

## Prerequisites
* Tech affinity.

## Objectives
* Understand the nature of the `DevOps` role
* Be familiar with some of the most common `DevOps` tools used in the industry
* Be able to perform their role as entry level `DevOps`
* Understand and command `AWS` cloud concepts and services.
* Acquire basic `AWS` architecting skills and understand the tradeoff between the various architectural decisions behind `AWS` apps.

## Outline
* `Linux` (48 hours)
    * Unix and `Linux`
    * GNU/`Linux`
    * `Linux` distributions (Debian `Ubuntu`, RedHat Fedora, Arch Manjaro)
    * Creating customs OS distribution.
    * Setup `Linux` Systems (install Vagrant, install VMWare, VirtualBox,KVM)
    * The Boot Process
    * File System
    * Files and Directories
    * Kernel Management
    * Users, Groups and Permissions Management
    * Software, Libraries and Package Management
    * Network and Tools
        * Interface Configuration
        * GUI and Cli
        * `ifconfig` and `ip`
        * `dhclient`
        * `hostname`
        * `arp`
        * Route
        * Ping
        * Ssh: Client and Server
    * Network File Sharing (NFS)
    * Samba
    * Domain Name Service (`DNS`)
    * Dynamic Host Configuration Protocol (`DHCP`)
    * Proxy
    * Firewall
* Scripting and Development Introduction (8 hours)
    * Programming Basic Concepts
    * Variables & Constants
    * Data Types
    * Flow Control
    * Input & Output
    * Arrays
    * Functions
    * Data Structure
    * Objects
* Shell Scripting: (24 hours)
    * Introduction To `Bash`
    * Shell Navigation
    * Basic Shell Commands
    * Regular Expressions
    * Unix Power Tools
    * File Path
    * Special Characters
    * Shell Scripting
    * Shell Automation
* `Python` Development(32 hours)
    * Introduction To `Python`
    * Types and Operators
    * Basic Statements
    * Functions
    * Modules
    * Classes
    * Exceptions
    * `Python` Libraries
    * Advanced `Python` : Automation with `Selenium`
* Introduction to Databases (32 hours)
    * Relational Databases, Structural Data and Tables
    * Database Concepts: Schemas, Migration
    * Database Types: `SQL` and `NoSQL`
    * Structured Query Language (`SQL`)
    * `SQL` Syntax
        * SELECT
        * INSERT
        * UPDATE
        * DELETE
    * `MySQL` Database
        * Installing `MySQL`
        * Configuration files
        * Users
        * Importing Data
    * `MongoDB` Database
        * Installing `MongoDB`
        * Configuration Files
        * Users
    * Object Relational Mappers (ORM)
* `Git` (32 hours)
    * Introduction to `Git`
        * History of `Git`
        * Who is using `Git`
        * Adopting `Git`
    * Core `Git` Concepts
        * Always on a branch
        * Everything is SHA1 (files, changes, tags, branches)
        * Everything has a parent except first change.
        * Never store anything twice
        * SHA includes all history
        * SHA is unique in the world
    * `Git` basics
        * Setting up a local repository
        * Setting up a client to a repository
            * local
            * remote
        * The staging area
        * Making your first change
        * Committing
        * Seeing history
        * Renaming, moving and removing files
    * Configuring `Git`
        * local and global config files
        * configuring `Git` commands
        * configuring signing
        * adding aliases
        * ignoring files
    * Undoing things
        * Staging area undoings
        * Undoing latest commit
        * Undoing last n commits
        * Cherry picking from latest commits
    * Remote repositories
        * Working with a remote repository
        * Setting up / publishing a repository
        * Understanding the repository structure
        * Working with Multiple remotes
        * Working with GitHub
    * Branches
        * Creating local branches
        * Working on local branches
        * Committing on local branches
        * Moving between local branches
        * Pruning branches
    * Merging changes
        * Fetch
        * Pull
        * Rebase
        * what is fast forwarding?
        * cherry picking
        * handling conflicts
            * basics
            * using merge tools
    * Merge vs Rebase
        * Which should you choose? (Rebase)
        * Why?
    * Workflows
        * `Git` does not force a workflow
        * feature branches
        * dev vs production
        * back porting changes
        * Examples of workflows
            * working on your own workflow
            * `Jenkins`
            * pull requests
    * Getting `Git` data
        * `Git` log and it's many options
        * Visual tools
        * Using programming (example is `Python`)
    * Tagging
        * Why tag?
        * difference between annotates and non annotated tags
        * pushing and pulling tags
        * Using tags in other `Git` commands
    * Rewriting History
        * Why you should never do it
        * How to do it anyway
    * Stashing
        * Why would you want stashing?
        * Creating and naming stashes
        * Apply a specific stash
        * Delete stashes
* `DevOps` in Theory (8 hours)
    * Core Concepts
    * Agile Methods
    * SCRUM usage
    * Iterative
    * Incremental
    * Continuous
    * Automated
    * Self-service
    * Collaborative
    * Holistic
* `DevOps` in Practice (8 hours)
    * Configuration Management (CM) Concepts
    * Infrastructure as a Service
    * Push and Pull Models
    * Configuration Management Tools: Chef, `Puppet`, `Ansible`
* `Jenkins` (32 hours)
    * Continuous Integration (CI) Concepts
    * CI and Automated Testing
    * `Jenkins` CI Server Overview
    * Installing and Running `Jenkins`
    * Administrating `Jenkins`
    * Jobs in `Jenkins`
    * Builds in `Jenkins`
    * `Jenkins` Plugins
    * Distributed Builds with `Jenkins`
    * Continuous Delivery (CD) Pipelines
    * Best Practices in `CI/CD` process with `Jenkins`
* `Docker` (32 hours)
    * Virtual Machines
    * Introduction to Containers
    * Introduction to `Docker`
    * Installing `Docker`
    * The `Docker` Architecture
    * The `Docker` Engine
    * Creating a `Docker` Container
    * Building `Docker` Images
    * Building Containers from Images
    * Registry Architecture
    * Deploying applications with `Docker`
* Web Concepts (16 hours)
    * Web Architecture and Frameworks
    * Web Scaling
    * Web Scale Architecture
    * `JavaScript` in theory
    * Exercise: building web servers in `Python`
* Micro-services theory (16 hours)
    * The problems with monolithic systems
    * What are Micro-services?
    * Implementation details
    * Scaling
    * Composition patterns
    * Exercises
* Cloud concepts (16 hours)
    * Introduction to Cloud Computing
    * Types of services
        * Infrastructure as a service (IAAS)
        * Platform as a service (PAAS)
        * Software as a service (SAAS)
    * Understanding Cloud Scope
        * Private Clouds
        * Public Clouds
        * Hybrid Clouds
    * Infrastructure as a Code
    * Cloud Support for `DevOps`
    * Examining the big three
        * `AWS`
        * `Google Cloud` Platform
        * `Azure`
* `Kubernetes` (32 hours)
    * Welcome & Introduction
    * From Monolith to Micro-services
    * Container Orchestration
    * `Kubernetes`
    * `Kubernetes` Architecture
    * Installing `Kubernetes`
    * Setting Up a Single Node `Kubernetes` Cluster Using Minikube
    * Accessing Minikube
    * `Kubernetes` Building Blocks
    * Services
    * Deploying a Stand-Alone Application
    * `Kubernetes` Volume Management
    * ConfigMaps and Secrets
    * Ingress
    * Advanced Topics
    * `Kubernetes` Community
* LogStash and Kibana (24 hours)
    * Introduction to `Elasticsearch`
        * What is `Elasticsearch`?
        * Lucene
        * `ELK` and elastic products
        * `Elasticsearch` Architecture
        * latest Version New Features
    * Setup and Configuration
        * Setup an `Elasticsearch` cluster
        * Configuration
        * `Elasticsearch`.yml
        * Configuration Tips
        * Lab: Setup and Configuration
    * Mapping and Data Manipulations
        * `Elasticsearch` Mapping and data types
        * Dynamic Mapping
        * Analyzers
        * Nested Object, Parent-Child and Geospatial support
        * Mapping Changes
        * Mapping Templates
        * Data Manipulations
        * Lab: Mapping and Data Manipulations
    * Querying `Elasticsearch`
        * Search `API`
        * Simple Query Examples
        * Query DSL
        * Complex Queries
        * Aggregations
        * Lab: Querying `Elasticsearch`
    * Introduction to Logstash
        * What is Logstash?
        * Configuration
        * Inputs and filters
        * Lab: Load data with Logstash
    * Introduction to Kibana
        * What is Kibana?
        * Installation and Configuration
        * Discover your data
        * Create a new visualization
        * Create a Dashboard
        * Lab: Create Dashboard and Visualizations
    * Introduction to Beats and APM
        * What is Beats?
        * Beats Types
        * APM
        * Lab: Using Metricbea
* Agile (24 hours)
    * History of Software Development and Processes
    * Motivations for Change: Iterative Development
    * Defining Iterative Development
    * Defining Evolutionary and Adaptive Development
    * Introducing Agile Development
        * What Is Agile?
        * Agile Principles and Practices
        * Agile Project Management
    * How to Become Agile
    * What Is Scrum: Methodology overview, process life-cycle, values, roles, practices, strategies, etc.
    * What Is Extreme Programming: Methodology overview, process life-cycle, values roles, practices, strategies, etc
    * Agile Development With the Unified Process: Methodology overview, process life-cycle, values, roles ,practices, strategies, etc
* `AWS` (72 hours)
    * `AWS` Cloud Services Overview
    * Regions and availability zones
    * Infrastructure services
        * `VPC`
        * subnets
        * security groups
        * `EC2`
        * Load balancing (ELB, ALB)
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
    * `IAM` and Roles
        * Setting up the account
        * Using Roles and groups
        * Connecting with other identity providers
    * Security
        * KMS
        * Encryption in transit and at rest.
    * Application services
        * `S3`
        * Dynamo DB
        * SQS
        * SNS
        * Elastic Transcoder
        * Workspaces
        * Other offerings
    * System on `AWS`
        * `DNS` and worldwide services
        * Route 53
        * Cloud watch
    * Cloud monitoring and logging
    * Cloud Watch
    * Cloud Trail
    * Continuous Integration and Continuous Delivery with `AWS`
        * `AWS` CodeCommit
        * `AWS` CodeDeploy
        * `AWS` CodePipeline
        * `AWS` CloudFormation
        * `AWS` OpsWorks
    * Serverless
        * `EKS`
        * `ECS`
        * `Lambda`
    * High level services
        * Cloud Formation
        * `Terraform` on `AWS`
    * Desktop services
        * Workspaces
    * Managing application users
        * Cognito
        * `AWS` SSO.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
