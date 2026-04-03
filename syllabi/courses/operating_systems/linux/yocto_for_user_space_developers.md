---
tags:
  - infrastructure:linux
  - tools:yocto
  - hardware-and-embedded:embedded
  - practices:build-systems
  - hardware-and-embedded:toolchain
level: intermediate
category: operating-systems
duration_hours: 16
audience:
  - audiences:developers
  - audiences:embedded-engineers
---
<!-- course: yocto_for_user_space_developers -->
# `Yocto` for Non-Kernel developers

## Description
This course is intended for non `Linux` kernel developers that need to maintain `Yocto` projects.
It introduces `Linux` user space and then proceeds to analyze how to debug and fix `Yocto` problems.

## Duration
16 hours / 2 days

## Intended Audience
* People without prior knowledge of `Linux` userspace or kernel space.
* People that need to maintain and update `Yocto` configurations.

## Prerequisites
* Tech affinity

## Objectives
* Understand how `Linux` kernel space and userspace is built.
* Understand how to debug build problems in third party components.
* Understand how `Yocto` works and how to debug problems in building `Yocto` targets.

## Outline
<!-- chapter: linux-user-space-basic-concepts, duration: 4h -->
* `Linux` user space basic concepts
    * binaries
    * scripts
    * libraries
        * dynamic libraries
        * static libraries
        * dependencies between libraries in userspace
        * LD_LIBRARY_PATH, LD_RUNPATH
    * daemons
    * kernel modules
<!-- chapter: building-linux-user-space-components, duration: 7h -->
* Building `Linux` user space components
    * Component dependencies
        * what are dependencies?
        * types of dependencies?
            * build tool dependencies
            * runtime library dependencies
            * runtime executable dependencies
            * daemon dependencies
    * Third party components types
        * libraries
        * applications
        * daemons
    * Components build types
        * `make`
        * `cmake`
        * autoconf
        * others (scons, `bazel`, `ant`, `gradle`, ivy, `maven`, ...)
<!-- chapter: understanding-toolchains, duration: 1h -->
* Understanding toolchains
    * How are toolchains made?
    * How to build my own toolchain?
<!-- chapter: yocto-intro, duration: 2h -->
* `Yocto` intro
    * How `Yocto` works
    * Poky
    * `Bitbake`
    * Customized Images.
    * Layers
<!-- chapter: trouble-shooting-yocto, duration: 2h -->
* Trouble shooting `Yocto`.
    * The types of build failures
    * Compilation errors
    * Dependency errors
    * Configuration errors

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
