---
tags:
  - tools:nix
  - tools:nixos
  - build:reproducible
  - practices:build-automation
  - infrastructure:package-management
level: advanced
category: build-system
duration_hours: 24
audience:
  - audiences:developers
  - audiences:devops
  - audiences:sysadmins
---
<!-- course: nix -->
# `Nix`

## Description
`Nix` is a purely functional package manager and build system that guarantees reproducible, declarative, and
reliable software environments across development, staging, and production. This advanced course teaches
participants the `Nix` expression language, the `Nix` store model, and the derivation-based build system,
progressing from writing individual packages to managing entire system configurations with `NixOS`. Topics
include `Nix` Flakes for hermetic, versioned dependencies, overlay patterns for customisation, and integrating
`Nix`-based builds into `CI/CD` pipelines and container workflows.

## Duration
24 hours / 3 days

## Intended Audience
* Developers who need truly reproducible build environments across teams and machines.
* `DevOps` and platform engineers managing complex software delivery infrastructure.
* System administrators interested in declarative system configuration with `NixOS`.
* Anyone frustrated by "works on my machine" problems and seeking a principled solution.

## Prerequisites
* Strong comfort with the `Linux` command line and shell scripting.
* Experience with at least one functional or dynamically typed language is helpful.
* Familiarity with package management concepts (`apt`, `brew`, pip, etc.).
* Some exposure to system administration or `DevOps` practices is assumed.

## Objectives
* Explain the `Nix` store model and how it guarantees reproducibility.
* Read and write `Nix` expressions using the `Nix` language.
* Write derivations to package software from source.
* Use `Nix` Flakes to create hermetic, versioned project environments.
* Configure a `NixOS` system declaratively.
* Create and share reproducible development shells with `nix-shell` and `nix develop`.
* Customise the `Nixpkgs` package set using overlays and overrides.
* Integrate `Nix` builds into `CI/CD` pipelines.
* Build and deploy software inside containers using `Nix`.

## Outline
<!-- chapter: introduction-to-nix, duration: 2h -->
* Introduction to `Nix` and Reproducible Builds:
    * The reproducibility problem in software engineering.
    * `Nix` philosophy: purely functional package management.
    * The `Nix` ecosystem: `Nix`, `Nixpkgs`, `NixOS`, and `Nix` Flakes.
    * Installing `Nix` and exploring the nix `CLI`.
    * The `Nix` store: content-addressed storage fundamentals.
<!-- chapter: nix-language-fundamentals, duration: 3h -->
* `Nix` Language Fundamentals:
    * Data types: strings, integers, booleans, lists, and attribute sets.
    * Functions, let-`in` expressions, and `with` clauses.
    * `import`, `builtins`, and the standard library.
    * String interpolation and multi-line strings.
    * Lazy evaluation and its implications.
    * Common patterns: recursive attribute sets, `lib` utilities.
<!-- chapter: nix-store-and-derivations, duration: 2h -->
* `Nix` Store and Derivations:
    * Store paths and cryptographic hashing.
    * What is a derivation?
    * The `derivation` built-in and its attributes.
    * Build inputs, outputs, and sandboxing.
    * Querying the store with `nix-store` and `nix path-info`.
<!-- chapter: writing-your-first-package, duration: 3h -->
* Writing Your First Package:
    * Using `stdenv.mkDerivation`.
    * Fetch sources: `fetchurl`, fetchFromGitHub, `fetchTarball`.
    * Build phases: unpack, patch, configure, build, install.
    * Overriding phases and adding hooks.
    * Packaging scripts, `Python`, and `Node.js` applications.
    * Testing packages with `nix build` and `nix run`.
<!-- chapter: nix-flakes, duration: 3h -->
* `Nix` Flakes:
    * Motivation: reproducibility and version pinning.
    * The `flake.nix` schema: inputs, outputs, and schemas.
    * `flake.lock` and input updates.
    * Defining packages, apps, dev shells, and overlays in a flake.
    * Consuming flakes as dependencies.
    * Flake-based CI and remote builders.
<!-- chapter: nixos-configuration, duration: 3h -->
* `NixOS` Configuration:
    * `NixOS` module system: options and config.
    * The `configuration.nix` file and system rebuild.
    * Managing users, services, and network configuration declaratively.
    * Enabling and configuring `systemd` services with `Nix`.
    * Home Manager for user-level declarative configuration.
    * Rolling back system generations.
<!-- chapter: development-environments, duration: 2h -->
* Development Environments with `nix-shell` and `nix develop`:
    * `nix-shell` for ad-hoc environments.
    * `shell.nix` for project-scoped environments.
    * `nix develop` with Flakes.
    * `direnv` and `nix-direnv` for automatic environment activation.
    * Sharing dev environments across teams.
<!-- chapter: overlays-and-customisation, duration: 2h -->
* Overlays and Customisation:
    * What is an overlay and why use one?
    * Writing and composing overlays.
    * Overriding packages and adding patches.
    * Package sets and module extensions.
    * Pinning `Nixpkgs` for long-term stability.
<!-- chapter: cicd-with-nix, duration: 2h -->
* `CI/CD` with `Nix`:
    * Running `Nix` builds in `GitHub Actions` and `GitLab CI`.
    * Binary caches: `cachix` and self-hosted substituters.
    * Hydra: the `NixOS` continuous integration server.
    * Remote builders and distributed builds.
<!-- chapter: nix-in-containers, duration: 2h -->
* `Nix` in Containers:
    * Building minimal `Docker` images with `dockerTools`.
    * Layered images for efficient image distribution.
    * `Nix`-built images vs. `Dockerfile`-based images.
    * `OCI` image standards and multi-architecture builds.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
