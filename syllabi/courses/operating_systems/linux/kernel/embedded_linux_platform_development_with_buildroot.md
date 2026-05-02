---
tags:
  - infrastructure:linux
  - hardware-and-embedded:embedded
  - tools:buildroot
  - infrastructure:cross-compilation
  - hardware-and-embedded:toolchain
  - practices:build-systems
level: advanced
category: operating-systems
duration_hours: 24
audience:
  - audiences:developers
  - audiences:embedded-engineers
---
<!-- course: embedded_linux_platform_development_with_buildroot -->
# Embedded `Linux` Platform Development with `Buildroot`

## Description
`Buildroot` is still one of the most heavily used tools to build embedded systems based on the `Linux` kernel.
This course introduces `buildroot` to embedded software engineers and explains how to configure and use the tool
correctly, as well as it's advantages and disadvantages when compared to other tools or approaches being used to build embedded `Linux` systems.

## Duration
24 hours / 3 days

## Intended Audience
* Companies already using or interested in using `Buildroot` to build their embedded `Linux` systems.
* Embedded software engineers familiar with other embedded operating system and wish to learn about the `Linux` way of doing things.

## Prerequisites
* Knowledge and practice of `UNIX` or GNU/`Linux` commands.
* Some embedded experience (in `Linux` or other systems) is a must.
* Kernel `Linux` programming is an advantage.
* Embedded Knowledge in `Linux` is an advantage.
* Knowledge in Building `Linux` images with other tools (`Yocto`?) is an advantage.

## Objectives
* Be able to understand the role and principle of an embedded `Linux` build system, and compare `Buildroot` to other tools offering similar functionality.
* Be able to create a simple embedded `Linux` system with `Buildroot`: create a configuration, run the build, install the result on an embedded platform.
* Be able to adjust the `Buildroot` configuration to build an embedded `Linux` system tailored to specific needs: choice of the cross compilation toolchain, management of the `Linux` kernel configuration, customization of the root filesystem contents, etc.
* Be able to create new packages in `Buildroot` to integrate additional applications and libraries into the embedded `Linux` system.
* Be able to use the tools offered by `Buildroot` to manage and analyze the build: security vulnerability tracking, license compliance, etc.
* Be able to develop and debug `Linux` user-space applications in the context of `Buildroot`.
* Be able to interact with the `Buildroot` open-source community, and to understand the internals of `Buildroot`

## Outline
<!-- chapter: embedded-linux-and-build-system-introduction, duration: 1h -->
* Embedded `Linux` and build system introduction
    * The general architecture of an embedded `Linux` system
    * Build systems vs. binary distributions
    * Role of a build system
    * Comparison of existing build systems
<!-- chapter: introduction-to-buildroot, duration: 1h -->
* Introduction to `Buildroot`
    * Key facts about the project
    * Getting `Buildroot`
    * Basic configuration of `Buildroot`
    * Doing a first build
<!-- chapter: managing-the-build-and-configuration, duration: 1h -->
* Managing the build and configuration
    * Out of tree build
    * Using and creating defconfigs
    * Defconfig fragments
    * Other building tips
<!-- chapter: buildroot-source-and-build-trees, duration: 1h -->
* `Buildroot` source and build trees
    * Details about the `Buildroot` source code organization
    * Details about the `Buildroot` build tree
<!-- chapter: toolchains-in-buildroot, duration: 1h -->
* Toolchains in `Buildroot`
    * The different choices for using toolchains in `Buildroot`
    * Overview of the toolchain options
    * Using existing binary toolchains, such as Bootlin toolchains, understanding multilib capabilities and integration of toolchains in `Buildroot`
    * Generating custom toolchains with Crosstool-NG, and re-use them as external toolchains
<!-- chapter: managing-the-linux-kernel-configuration, duration: 1h -->
* Managing the `Linux` kernel configuration
    * Loading, changing and saving the kernel configuration
<!-- chapter: root-filesystem-construction-in-buildroot, duration: 2h -->
* Root filesystem construction in `Buildroot`
    * Understand how `Buildroot` builds the root filesystem: skeleton, installation of packages, overlays, post-build and post-image scripts.
    * Customization of the root filesystem contents
    * System configuration: console selection, various /dev management methods, the different init implementations, etc.
    * Understand how `Buildroot` generates filesystem images
<!-- chapter: download-infrastructure-in-buildroot, duration: 2h -->
* Download infrastructure in `Buildroot`
    * Downloading logic
    * Primary site and backup site, doing offline builds
    * VCS download, integrity checking
    * Download-related `make` targets
<!-- chapter: gnu-make-101, duration: 2h -->
* GNU Make 101
    * Basics of `make` rules
    * Defining and referencing variables
    * Conditions, functions
    * Writing recipes
<!-- chapter: integrating-new-packages-in-buildroot, duration: 2h -->
* Integrating new packages in `Buildroot`
    * How to integrate new packages in the `Buildroot` configuration system
    * Understand the different package infrastructures: for generic, `autotools`, `CMake`, `Python` packages and more.
    * Writing a package Config.in file: how to express dependencies on other packages, on toolchain options, etc.
    * Details on writing a package recipe: describing the package source code location, download method, configuration, build and installation steps, handling dependencies, etc.
<!-- chapter: advanced-package-aspects, duration: 3h -->
* Advanced package aspects
    * Licensing report
    * Patching support: patch ordering and format, global patch directory, etc.
    * User, permission, device tables
    * Init scripts and `systemd` unit files
    * Config scripts
    * Understanding hooks
    * Overriding commands
    * Legacy handling
    * Virtual packages
<!-- chapter: analyzing-the-build-licensing-dependencies-build-time, duration: 1h -->
* Analyzing the build: licensing, dependencies, build time
    * Usage of the legal information infrastructure
    * Graphing dependencies of packages
    * Collecting and graphing build time information
<!-- chapter: advanced-topics, duration: 2h -->
* Advanced topics
    * BR2_EXTERNAL to store customization outside of the `Buildroot` sources
    * Package-specific targets
    * Understanding rebuilds
    * Tips for building faster
<!-- chapter: application-development-with-buildroot, duration: 2h -->
* Application development with `Buildroot`
    * Using `Buildroot` during application development
    * Usage of the `Buildroot` environment to build applications outside of `Buildroot`
    * Generate an `SDK` for other developers
    * Remote debugging with `Buildroot`
<!-- chapter: understanding-buildroot-internals, duration: 1h -->
* Understanding `Buildroot` internals
    * Detailed description of the `Buildroot` build process: toolchain, packages, root filesystem construction, stamp files, etc.
    * Understanding virtual packages.
<!-- chapter: getting-support-and-contributing, duration: 1h -->
* Getting support and contributing
    * Getting support: Bugzilla, mailing list, IRC
    * Contributing: understanding the development process, how to submit patches

## References
* [slides for this course](`https`://bootlin.com/doc/training/`buildroot`/)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
