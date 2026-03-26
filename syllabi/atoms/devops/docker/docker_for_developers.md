---
tags:
  - docker
  - containers
  - devops
  - networking
level: intermediate
category: devops
duration_days: 3
audience:
  - developers
---
# `Docker` for developers

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Docker` is the dominant container technology used today and this course is all about
developing using that technology.

The course starts with the reasons why we need container technology to begin with
and then dives into specifics of the `Docker` platform.

The next big topics is how to package your application as a `docker` image and how to
write the `Dockerfile`. After that the course talks about to connect your container
to the outside world at runtime in terms of networking and storage. Another topics
which is presented is how to manage your container in terms of resources, logging
and more.

## Duration
24 hours / 3 days

## Intended Audience
Developers who have the need to develop application with `Docker` as the target platform.
This is usually required by developers who need to host their apps on either a public
cloud provider or an on premise cloud, or just developer who wish to gain more determinism
and clarity from their development, testing and production environments.

## Prerequisites
Developers of any type are welcome. Experience in developing web applications is beneficial
but not mandatory.

## Objectives
Participants will gain an understanding of what container technology is and in what
circumstances they need it.
Participants will be able to create `Docker` images containing their applications, run their
`Docker` images locally or remotely, debug their applications even when they running within
`Docker` containers and handle their application logs.

## Exercises
The coding examples in this course will be presented in `Python`. The examples are short
and should not present any problems for the developers. If you would like the examples
to be tailored to the language of your choosing please let me know at <mark.veltzer@gmail.com>.
The training platform is `Linux` so prior to class arrangements should be made to make
sure that the participants have an access to `Linux` boxes.

## Outline
* `Docker` Theory
    * What is `Docker`?
    * `Docker` benefits
        * Determinism
        * Security
        * Ease of debugging
        * Solve issues of multiple distributions
        * Solve issues of apps having access to data of other apps
        * Solve issue of how to package apps
        * Solve dependency hell issues
        * Minimal attack surface
        * Suitability for Micro-Service architecture
        * Application store
    * `Docker` tools
* `Docker` under the hood
    * How virtual machines work
    * Containers vs virtual machines
    * The `Docker` Architecture
    * The `Docker` Engine
* Starting out
    * Installing `docker`
    * Running your first container
    * `Docker` concepts: Image vs Container
    * `Docker HUB`
* Creating your own `docker` images
    * The `Dockerfile`
    * Creating your first image
    * Running your image
* Crafting your image
    * The `Dockerfile` language.
    * The various keywords then their meaning.
* Dead containers
    * How to see them
    * How to see their logs
    * How to revive/restart them
* Handling logs
    * Log handlers in `Docker`
    * Writing your application correctly
* Networking with `Docker`
    * Opening ports
    * Network devices
* `Docker` and Volumes
    * Why do we need data volumes?
    * Types of data volumes
    * Working with data volumes
    * Bind mounts vs named volumes
    * Volume backup strategies
    * Volume plugins and drivers
    * Best practices for persistent data
* Security with `Docker`
    * Under which security context are you running in inside `Docker`?
    * Running as not root
    * Tuning capabilities
    * Secrets management
* Development Workflow
    * `Docker` in `CI/CD` pipelines
    * Local development best practices
    * Multi-stage builds for development vs production
    * `IDE` integration tips
* Performance Optimization
    * Image size optimization
    * Layer caching strategies
    * Resource limits and constraints
    * Monitoring and metrics
* Troubleshooting and Debugging
    * Common issues and solutions
    * `Docker` inspect deep dive
    * Remote debugging techniques
    * Health checks implementation

## Installations
* A real `Ubuntu` >= 22.04 running on a laptop.
* A `Windows`/macOS system running on a laptop with an `Ubuntu` >= 22.04 virtual machine on top. This could be done using Hyper-V or `Oracle` VirtualBox.
* Access to a remote `Ubuntu` >= 22.04 machine via ssh (command line, putty, MobaXterm, ...). The machine could be in a company private cloud or a public cloud.
* In any case the student must have sudo/root on this virtual machine.
* In all cases the installations are not a must and the instructor will guide the students how to do the installations on the first day of the course.
* The virtual machines should have at least 4GB of memory.
