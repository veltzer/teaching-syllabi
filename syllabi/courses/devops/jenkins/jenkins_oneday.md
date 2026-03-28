---
tags:
  - tools:jenkins
  - practices:ci-cd
  - practices:devops
level: beginner
category: devops
duration_hours: 8
audience:
  - practices:devops
  - audiences:developers
---
# `Jenkins`

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Jenkins` is a very wide spread software building, testing and deployment tool. It enabled `CI/CD`
pipelines and agile development, can utilize such technologies as the public cloud, git and
`Docker` and has many plugins making it tunable to many environments.

## Duration
8 hours / 1 days

## Intended Audience
* Devops people who wish to install, configure and control the building and testing of software.
* Developers who wish to build complex pieces of software and to customize the build and test phases.
* Scrum masters who would like to integrate new features into their production pipelines.
* Anyone with some programming experience in the software industry.

## Prerequisites
No programming skills are required but are certainly welcome.
A year of experience in the software industry in any technical position is required.

## Objectives
* Install a `Jenkins` server.
* Describe the theory behind `CI/CD` pipelines.
* Understand the different pipelines in `Jenkins`.
* Learn some groovy syntax
* Write your own pipeline scripts
* Connect `Jenkins` to GitHub
* Learn how to trouble-shoot `Jenkins`
* Describe `Jenkins` best practices.

## Outline
* How to install `Jenkins` (3 possible ways)
* Continuous Integration (CI) Concepts
    * Why CI?
    * Why CD?
    * Organizational issues.
* Basic `Jenkins` example
* Pulling your code from GitHub using polling or a webhook
* The various pipeline types in `Jenkins`
    * Which should you choose?
* Agents in `Jenkins`
    * What are Agents?
    * Different types of Agents
    * `Jenkins` in the Cloud using cloud native agents
* Some groovy syntax
    * Variables
    * Loops
    * Conditional statements
    * Basic functions
    * Going beyond the basics
* Examples of pipelines
* Trouble shooting `Jenkins`
    * Logging
    * Printing from within `Docker` processes
    * Getting the `Docker` logs
    * Understanding what causes failure:
        * environment variables
        * user who is running and permission issues
        * current folder
        * files
* Best Practices in `CI/CD` process with `Jenkins`
    * Using Jenkinsfile
    * Using Dockers
* Speeding your builds and tests
    * Doing things in Parallel
    * Pre-prepared `Docker` images
    * Pre-installed software
    * Pre-installed wheels for `Python`

## Installations
* `Linux` virtual machine with recent version of `Ubuntu` (20.10 and above) for each student with 4GB (better 8GB) of RAM.
* The virtual machines should have a connection to the internet (so we could download any software we need).
* The virtual machines should have a working graphical display (so we could run graphical applications on them).
* The user should have `sudo` privileges on those machines.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
