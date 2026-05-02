---
tags:
  - infrastructure:linux
  - concepts:systems-programming
  - concepts:operations
  - concepts:best-practices
level: intermediate
category: operating-systems
duration_hours: 24
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:senior-developers
  - audiences:embedded-developers
---
<!-- course: systemd_in_depth -->
# `systemd` in Depth

## Description
The catalog has `Linux Fundamentals`, `Linux for Developers`, `Linux System Administration`,
`Embedded Linux for User Space Developers`, and several `Linux` debugging and performance courses.
None of those is the focused course on `systemd` — the init system, service manager, dependency
graph, and broader platform component that runs on essentially every modern `Linux` system. `systemd`
is more than `service` start; it is the logging system (`journald`), the network configuration
(`networkd`, `resolved`), the unit-file framework, the timer subsystem (the `cron` replacement), the
sandboxing primitives that container runtimes use under the hood, the resource-control layer, and the
`user-session` framework. Operating modern `Linux` without understanding `systemd` is operating
blind.

This three day course covers `systemd` as a focused topic. It covers the unit-file model (services,
sockets, timers, paths, mounts, slices, scopes, targets), the dependency graph (`Wants`, `Requires`,
`After`, `Before`), the activation model (the `socket-activated` service, the `path-activated`
service), the resource-control story (`cgroups`-via-`systemd`, slices, `MemoryMax`, `CPUQuota`,
`IOWeight`), the security primitives (`PrivateTmp`, `ProtectSystem`, `NoNewPrivileges`, capability
bounding, system call filters), the `journald` story (structured logging, log retention, integration
with the broader stack), the timer story (`OnCalendar`, `OnUnitActiveSec`), the user-session model,
the `networkd` and `resolved` stack, the embedded-`Linux` use case, and the patterns that distinguish
"we use `systemd` because we have to" from "we use `systemd` deliberately." Examples include real
production deployments. Participants leave able to write, debug, and operate `systemd` units that
work and that fail safely.

## Duration
24 hours / 3 days

## Intended Audience
* `sysadmins` operating modern `Linux`
* `DevOps` engineers writing service deployments
* senior developers shipping `Linux` services
* embedded developers using `systemd` for the system layer

## Prerequisites
* `solid` `Linux` knowledge
* exposure to the `Linux Fundamentals` course
* working experience as either developer or `sysadmin` on a modern distribution
* basic shell knowledge

## Objectives
* explain `systemd`'s architecture and purpose
* write a `systemd` service unit correctly
* use `systemd` activation models (`socket`, `path`, `timer`)
* apply `systemd`'s security primitives
* operate `journald` for production logging
* manage resources with `systemd` slices and `cgroups`
* debug a misbehaving `systemd` unit

## Outline
<!-- chapter: what-systemd-actually-is, duration: 1h -->
* What `systemd` actually is
    * init system, service manager, and more
    * the controversial history
    * what it replaces (`SysV`, `Upstart`, `cron`, `inetd`)
    * cross-reference to the `Linux Fundamentals` course
    * why the design choices
<!-- chapter: the-unit-file-model, duration: 2h -->
* The unit-file model
    * `service`, `socket`, `timer`, `path`, `mount`, `slice`, `scope`, `target`
    * the `[Unit]`, `[Service]`, `[Install]` sections
    * the per-user vs system unit
    * the drop-in directories
    * the `systemctl edit` workflow
<!-- chapter: dependencies-and-ordering, duration: 2h -->
* Dependencies and ordering
    * `Wants`, `Requires`, `Requisite`, `BindsTo`
    * `After`, `Before`
    * the difference between dependency and ordering
    * the `target` as the boot milestone
    * the "the service started before the network" failure
<!-- chapter: writing-a-good-service, duration: 3h -->
* Writing a good service
    * `Type=simple`, `forking`, `notify`, `oneshot`, `exec`, `idle`
    * the `ExecStart`, `ExecStop`, `ExecReload`
    * the `Restart=` policies
    * the `WatchdogSec=` integration
    * the per-state-transition hooks
    * the worked example
<!-- chapter: socket-and-path-activation, duration: 2h -->
* Socket and path activation
    * the `socket`-activated service
    * the `inetd` replacement
    * the `path`-activated service
    * the lazy-startup argument
    * the security argument (start-on-demand-only)
<!-- chapter: timers-as-cron-replacement, duration: 1h -->
* Timers as `cron` replacement
    * `OnCalendar`, `OnUnitActiveSec`, `OnBootSec`
    * persistent vs non-persistent
    * the `timer`-and-`service` pair
    * the `journalctl` for timer history
    * the migration from `cron`
<!-- chapter: security-primitives, duration: 3h -->
* Security primitives
    * `PrivateTmp`, `PrivateDevices`, `PrivateNetwork`
    * `ProtectSystem`, `ProtectHome`
    * `NoNewPrivileges`, `CapabilityBoundingSet`
    * `SystemCallFilter`
    * `DynamicUser`
    * the "we ran as root for no reason" reality
    * the `systemd-analyze security` workflow
<!-- chapter: resource-control, duration: 2h -->
* Resource control
    * `cgroups` via `systemd`
    * `MemoryMax`, `CPUQuota`, `IOWeight`, `TasksMax`
    * the slice hierarchy
    * the per-user slice
    * the relationship to container runtimes
    * cross-reference to the `Linux` Performance Engineering course
<!-- chapter: journald-and-structured-logging, duration: 2h -->
* `journald` and structured logging
    * the journal file format
    * structured fields per entry
    * `journalctl` for querying
    * retention and rotation
    * forwarding to `syslog`, `Loki`, `Elasticsearch`
    * cross-reference to the `Loki` course
<!-- chapter: networkd-and-resolved, duration: 2h -->
* `networkd` and `resolved`
    * `systemd-networkd` for network configuration
    * the `.network` and `.netdev` files
    * `systemd-resolved` for `DNS`
    * the `NetworkManager` vs `networkd` decision
    * the embedded-`Linux` use case
<!-- chapter: user-sessions-and-logind, duration: 1h -->
* User sessions and `logind`
    * `systemd-logind`
    * the per-user `systemd` instance
    * the seat and session
    * the lingering-user case
    * the `loginctl` command
<!-- chapter: debugging-systemd, duration: 2h -->
* Debugging `systemd`
    * `systemctl status`
    * `journalctl -u`
    * `systemd-analyze blame`, `critical-chain`
    * the `bootchart` story
    * the "the unit failed silently" debugging
<!-- chapter: systemd-in-embedded, duration: 1h -->
* `systemd` in embedded
    * the boot-time concern
    * the trim-the-units strategy
    * `Yocto` and `systemd`
    * cross-reference to the Embedded `Linux` Boot Time Optimization course
    * the "we removed `systemd` for size" trade-off

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
