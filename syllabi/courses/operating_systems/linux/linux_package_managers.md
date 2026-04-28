---
tags:
  - infrastructure:linux
  - infrastructure:unix
  - practices:command-line
  - audiences:sysadmin
level: intermediate
category: operating-systems
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: linux_package_managers -->
# `Linux` package managers

## Description
This course is a tour of the package management landscape on `Linux`. Modern `Linux` systems pull software from
many different sources: the distribution's own repositories (via `apt`, `dnf`, `yum`, `pacman` and
their low-level peers `dpkg` and `rpm`), cross-distribution sand-boxed formats (`flatpak`, `snap`, `appimage`),
declarative systems (`nix`, `guix`), language-specific package managers (`pip`, `cargo`, `npm`, `go modules`,
`gem`, `maven`), `GitHub` releases, container images, and old-fashioned source builds. Each ecosystem solves
a different subset of the same problems: dependency resolution, installation, upgrade, removal, security
updates, signing, and reproducibility. The goal of this course is to `make` sense of all of these so that the
practitioner can pick the right tool for the right task and avoid the common pitfalls of mixing them.

This course is not a development course. It does not deal with writing software. It deals with how software
arrives on a `Linux` machine, how to install it well, how to keep it up to date, how to remove it cleanly,
and how to audit what is on the system.

## Duration
16 hours / 2 days

## Intended Audience
* `Linux` users who want to understand where their software comes from.
* sysadmins who maintain `Linux` machines, fleets or images.
* `devops` engineers who build base images, `CI` pipelines or installation scripts.
* developers who ship software to `Linux` users and need to choose a packaging format.
* anyone who has ever been confused about whether to install something with `apt`, `pip`, `snap`, or from `GitHub`.

## Prerequisites
* Familiarity with the `Linux` command line.
* Basic `Linux` filesystem knowledge (`/usr`, `/etc`, `/var`, `$HOME`).
* Comfort editing text files and running commands as `root` or via `sudo`.

## Objectives
* understand the model of a package manager and the problems it solves
* gain practical knowledge of the `Debian` family tools (`dpkg`, `apt`)
* gain practical knowledge of the `Red Hat` family tools (`rpm`, `yum`, `dnf`)
* gain practical knowledge of universal package formats (`flatpak`, `snap`, `appimage`, `nix`)
* gain practical knowledge of language-specific package managers (`pip`, `cargo`, `npm`, ...)
* gain practical knowledge of installing from `GitHub` releases and from source
* be able to choose the right packaging tool for the right job

## Outline
<!-- chapter: introduction, duration: 2h -->
* Introduction to `Linux` package management
    * What problems does a package manager solve?
    * Dependency resolution
    * Versioning and upgrades
    * Reproducibility
    * Security and signing
    * Auditing what is installed
    * The cost of *not* using a package manager
    * The `Linux` packaging landscape: a map
    * High-level vs low-level tools
    * Distribution repositories vs third-party repositories vs upstream
<!-- chapter: dpkg-and-apt, duration: 3h -->
* The `Debian` family: `dpkg` and `apt`
    * What is a `.deb` `file`
    * Internals of a `.deb` archive (`ar`, `control.tar`, `data.tar`)
    * `dpkg`: the low-level tool
        * installing, removing, querying
        * package states (`ii`, `rc`, `hi`, ...)
        * triggers
    * `apt`: the high-level tool
        * `apt update`, `apt install`, `apt upgrade`, `apt full-upgrade`
        * `apt remove` vs `apt purge`
        * `apt-mark` for holding packages
        * `apt-cache` and `apt-file` for querying
    * Repositories
        * `/etc/apt/sources.list` and `sources.list.d/`
        * the `DEB822` modern format
        * components: `main`, `restricted`, `universe`, `multiverse`
        * adding third-party repositories with `signed-by`
        * `PPAs` on `Ubuntu`
    * Pinning and priorities
    * Building your own `.deb`
<!-- chapter: rpm-and-dnf, duration: 3h -->
* The `Red Hat` family: `rpm`, `yum`, and `dnf`
    * What is a `.rpm` `file`
    * Internals of an `.rpm` archive
    * `rpm`: the low-level tool
        * installing, upgrading, removing
        * querying installed and uninstalled packages
        * verification (`rpm -V`) and signatures
    * `yum` and its successor `dnf`
        * `dnf install`, `dnf upgrade`, `dnf remove`
        * `dnf history` and rollback
        * `dnf group` and `dnf module`
    * Repositories
        * `/etc/yum.repos.d/`
        * `EPEL` and other third-party repositories
        * `gpgcheck` and signing
    * Building your own `.rpm` with `rpmbuild`
    * `dnf` vs `apt`: side-by-side comparison
<!-- chapter: universal-formats, duration: 2h -->
* Universal and sand-boxed package formats
    * Why universal formats exist
    * `flatpak`
        * remotes, `flathub`
        * runtimes and applications
        * sandboxing model
    * `snap`
        * the `snap store`
        * channels (`stable`, `candidate`, `beta`, `edge`)
        * automatic updates: pros and cons
        * confinement modes
    * `appimage`
        * single-`file` applications
        * no installation required
        * integration with the desktop
    * `nix` and `guix`
        * declarative, reproducible builds
        * per-user package trees
    * Trade-offs vs native packages: size, integration, security, performance
<!-- chapter: language-package-managers, duration: 3h -->
* Language-specific package managers
    * Why every language has its own
    * `Python`: `pip`, `pipx`, `venv`, `uv`, `poetry`
        * `PyPI` and wheels
        * the `PEP 668` "externally managed" rule
        * virtual environments vs system `Python`
    * `Rust`: `cargo` and `crates.io`
    * `JavaScript`/`Node.js`: `npm`, `yarn`, `pnpm` and the `npm` registry
    * `Ruby`: `gem` and `bundler`
    * `Go`: `go modules` and the `GOPATH` model
    * `Java`: `maven` and `gradle`
    * `Haskell`: `cabal` and `stack`
    * Common themes
        * lockfiles and reproducibility
        * private registries and proxies
        * supply-chain risks (typosquatting, dependency confusion)
        * mixing language packages with system packages
<!-- chapter: github-and-source, duration: 2h -->
* `GitHub` releases and source builds
    * `GitHub` releases as a distribution channel
    * Downloading binaries from a release page
    * Verifying checksums and signatures (`cosign`, `gh attestation`)
    * The classic source build: `./configure`, `make`, `make install`
    * `cmake`, `meson`, `ninja`, `autotools`
    * Where to install: `/usr/local`, `$HOME/.local`, `/opt`, `GNU stow`
    * `checkinstall` to wrap a `make install` into a `.deb`
    * Why source builds are a last resort: no upgrades, no audit, no removal
<!-- chapter: comparison-and-best-practices, duration: 1h -->
* Choosing the right tool and best practices
    * A decision flow: which package manager for which need?
    * Mixing package managers safely
    * Keeping a system reproducible
    * Security best practices
        * always verify signatures
        * prefer signed repositories
        * audit what is installed
        * minimize the trust surface
    * Auditing and inventory
    * Common pitfalls
        * `pip install` as `root` outside a `venv`
        * `curl | sudo bash`
        * abandoned third-party repositories
        * version drift between `apt` and language packages
    * Closing exercise: package the same small tool four different ways and compare

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
