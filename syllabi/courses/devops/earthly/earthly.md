---
tags:
  - tools:earthly
  - practices:ci-cd
  - practices:build-systems
  - tools:docker
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: earthly -->
# `Earthly`

## Description
This course covers `Earthly`, a build automation tool that combines the best of `Dockerfile`
and `Makefile` syntax to create reproducible, containerized build pipelines. Participants will
learn how to write Earthfiles, manage artifacts and images, leverage caching, handle
multi-platform builds, and integrate `Earthly` with existing CI systems. The course also
compares `Earthly` with alternative build tools and approaches.

## Duration
16 hours / 1 day

## Intended Audience
* developers looking for reproducible and portable build pipelines.
* `devops` engineers seeking to simplify `CI/CD` build definitions.
* teams dealing with complex build processes across multiple projects.

## Prerequisites
* familiarity with `Docker` and `Dockerfile` syntax.
* experience with build tools (`Make`, `npm`, `Maven`, etc.).
* basic understanding of `CI/CD` concepts.

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)

## Objectives
* understand `Earthly` concepts and how it differs from traditional build tools.
* write Earthfiles to define reproducible build pipelines.
* leverage caching, secrets, and multi-platform builds.
* integrate `Earthly` into existing CI systems.

## Outline
<!-- chapter: earthly-overview, duration: 1h -->
* `Earthly` overview
    * what is `Earthly`
    * `Dockerfile` + `Makefile` concept
    * reproducibility and containerized builds
    * `when` to use `Earthly`
<!-- chapter: earthfile-syntax, duration: 2h -->
* Earthfile syntax
    * targets and dependencies
    * FROM and base images
    * COPY and `file` operations
    * RUN commands
    * `SAVE IMAGE` and `SAVE ARTIFACT`
    * target references and dependencies
<!-- chapter: artifacts-and-images, duration: 1h -->
* Artifacts and images
    * saving build artifacts
    * exporting container images
    * artifact sharing between targets
    * local and remote artifact outputs
<!-- chapter: caching, duration: 1h -->
* Caching
    * layer caching
    * cache mounts
    * inline caching
    * cache optimization strategies
<!-- chapter: multi-platform-builds, duration: 1h -->
* Multi-platform builds
    * building for multiple architectures
    * --platform flag
    * cross-compilation strategies
    * emulation vs native builds
<!-- chapter: secrets, duration: 1h -->
* Secrets
    * passing secrets to builds
    * secret management best practices
    * integration with secret stores
<!-- chapter: build-arguments, duration: 1h -->
* Build arguments
    * defining and using build arguments
    * conditional logic
    * argument propagation
    * default values
<!-- chapter: user-defined-commands-udcs, duration: 1h -->
* User-defined commands (UDCs)
    * creating reusable commands
    * parameterized commands
    * sharing UDCs across projects
    * command libraries
<!-- chapter: earthly-satellites-remote-execution, duration: 1h -->
* `Earthly Satellites` (remote execution)
    * remote build runners
    * shared caching
    * performance benefits
    * setup and configuration
<!-- chapter: earthly-cloud, duration: 1h -->
* `Earthly Cloud`
    * cloud-based features
    * secrets management in the cloud
    * collaboration features
<!-- chapter: integration-with-ci-systems, duration: 1h -->
* Integration with CI systems
    * `GitHub Actions` integration
    * `GitLab CI` integration
    * `Jenkins` integration
    * CI-agnostic build definitions
<!-- chapter: monorepo-builds, duration: 1h -->
* Monorepo builds
    * multi-project Earthfile structures
    * selective builds based on changes
    * shared dependencies
    * build orchestration
<!-- chapter: comparison-with-other-tools, duration: 1h -->
* Comparison with other tools
    * `Earthly` vs `Docker` multi-stage builds
    * `Earthly` vs `Bazel`
    * `Earthly` vs traditional CI scripts
    * choosing the right tool
<!-- chapter: debugging-builds, duration: 2h -->
* Debugging builds
    * interactive debugging
    * verbose output and logging
    * common issues and solutions
    * build reproducibility troubleshooting

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
