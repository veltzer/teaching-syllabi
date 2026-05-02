---
tags:
  - infrastructure:linux
  - concepts:observability
  - concepts:security
  - concepts:performance
  - concepts:best-practices
level: advanced
category: operating-systems
duration_hours: 32
audience:
  - audiences:senior-developers
  - audiences:devops
  - audiences:sres
  - audiences:security-engineers
---
<!-- course: ebpf_in_production -->
# `eBPF` in Production

## Description
`eBPF` is the most consequential `Linux` kernel innovation of the past decade. It lets you run sandboxed
programs inside the kernel — for observability, networking, and security — without writing kernel
modules and without restarting the system. The catalog has `Linux Performance Engineering`,
`Linux Debugging`, and `Linux Networking`, all of which mention `eBPF` in passing. None of them treats
`eBPF` as the engineering practice it has become. Modern observability (`Pixie`, `Parca`, `Cilium`
`Hubble`), modern networking (`Cilium`, `Calico` with `eBPF` data plane), modern security (`Tetragon`,
`Falco`'s `eBPF` driver), and modern performance work all run on `eBPF`.

This four day course covers `eBPF` from the verifier up to a production deployment. It covers the
program types, the verifier's reasoning, `BPF` maps, the `CO-RE` (compile-once-run-everywhere) story
that makes portable `eBPF` possible, the toolchain (`libbpf`, `BCC`, `bpftrace`, `Cilium ebpf-go`,
`Aya` for Rust), the observability use cases (`bcc-tools`, `bpftrace` one-liners, `Pixie`, `Parca`,
continuous profiling), the networking use cases (`Cilium` data plane, `kube-proxy` replacement,
service mesh acceleration), the security use cases (`Tetragon`, runtime threat detection), the
operational story (loading, lifecycle, monitoring overhead), the failure modes (verifier rejection,
kernel-version skew, performance regressions), and the security model of running `eBPF` itself.
Participants leave able to write, ship, and operate `eBPF` programs in production.

## Duration
32 hours / 4 days

## Intended Audience
* senior developers extending observability or networking
* platform engineers operating `eBPF`-based infrastructure
* `SRE` debugging production with `eBPF` tools
* security engineers using `eBPF` for runtime defense

## Prerequisites
* `solid` `Linux` knowledge (the `Linux Fundamentals` and `Linux Programming` courses)
* working C or Go experience
* exposure to the `Linux Networking` course is helpful
* basic understanding of `Linux` kernel concepts

## Objectives
* explain the `eBPF` execution model and the verifier
* write `eBPF` programs in C with `libbpf` and `CO-RE`
* use `bpftrace` for ad-hoc kernel observability
* deploy `Cilium` and reason about its data plane
* deploy `Tetragon` for runtime security observability
* operate `eBPF` programs in production safely
* recognize when `eBPF` is the wrong tool

## Outline
<!-- chapter: what-ebpf-actually-is, duration: 2h -->
* What `eBPF` actually is
    * the in-kernel virtual machine
    * the verifier as the safety boundary
    * the program types
    * the difference from kernel modules
    * cross-reference to the `Linux` Kernel Modules and Drivers course
    * why this changed the kernel
<!-- chapter: program-types-and-attach-points, duration: 2h -->
* Program types and attach points
    * `kprobes`, `kretprobes`, `tracepoints`
    * `uprobes` for user-space tracing
    * `XDP` and `tc` for networking
    * `LSM` for security
    * `socket-filter`, `cgroup`, and the `rest`
    * picking the right type
<!-- chapter: bpf-maps, duration: 2h -->
* `BPF` maps
    * the kernel-to-user data channel
    * `hash`, `array`, `lru-hash`, `percpu`
    * `ring buffer` and `perf event array`
    * the map size and the memory cost
    * the "we used the wrong map type and lost events" failure
<!-- chapter: the-verifier, duration: 3h -->
* The verifier
    * the safety guarantees
    * bounded loops
    * pointer-and-register state tracking
    * the "verifier rejected my program" debugging path
    * the kernel-version-and-verifier evolution
    * worked examples of rejection and fix
<!-- chapter: co-re-and-portability, duration: 2h -->
* `CO-RE` and portability
    * the kernel-version-skew problem
    * `BTF` (`BPF Type Format`)
    * `bpf2go`-style codegen
    * the "compile once, run everywhere" promise
    * the limits of `CO-RE`
<!-- chapter: the-ebpf-toolchain, duration: 3h -->
* The `eBPF` toolchain
    * `libbpf` and the C development model
    * `BCC` and the `Python`-front-end legacy
    * `bpftrace` for one-liners
    * `cilium/ebpf` for Go
    * `Aya` for Rust
    * picking for the use case
<!-- chapter: observability-with-ebpf, duration: 3h -->
* Observability with `eBPF`
    * `bcc-tools` and the canonical scripts
    * `bpftrace` one-liners
    * continuous profiling: `Parca`, `Pyroscope`
    * `Pixie` for `Kubernetes` observability
    * the "we replaced traditional `APM` with `eBPF`" reality
    * cross-reference to the `Linux` Performance Engineering course
<!-- chapter: ebpf-networking-and-cilium, duration: 4h -->
* `eBPF` networking and `Cilium`
    * the `eBPF` data plane idea
    * `Cilium` as `kube-proxy` replacement
    * `Cilium` `Hubble` for network observability
    * the service-mesh acceleration story
    * `Calico` with `eBPF`
    * the "we replaced `iptables` with `eBPF`" migration
<!-- chapter: ebpf-security-tetragon-and-falco, duration: 3h -->
* `eBPF` security: `Tetragon` and `Falco`
    * runtime threat detection with `eBPF`
    * `Tetragon` and policy-driven detection
    * `Falco`'s `eBPF` driver
    * the "we caught the container escape with `eBPF`" case
    * cross-reference to the Container and `Kubernetes` Security course
<!-- chapter: lifecycle-and-loading, duration: 2h -->
* Lifecycle and loading
    * loading from user space
    * pinning programs and maps
    * the `bpf` filesystem
    * the lifetime of an `eBPF` program
    * the "the loader exited and the program lived on" subtlety
<!-- chapter: production-operations, duration: 2h -->
* Production operations
    * the cost of always-on `eBPF`
    * sampling vs continuous
    * the kernel-version compatibility matrix
    * the rolling-out across the fleet
    * the "we shipped an `eBPF` program that crashed the kernel" failure (and why this is hard)
<!-- chapter: security-of-ebpf-itself, duration: 1h -->
* Security of `eBPF` itself
    * who can load `eBPF`
    * `CAP_BPF` and the unprivileged debate
    * the `eBPF` as attack surface
    * recent `eBPF` `CVEs`
    * the operational hardening
<!-- chapter: when-ebpf-is-not-the-answer, duration: 1h -->
* `When` `eBPF` is not the answer
    * problems user-space `tracing` already solves
    * environments without modern kernels
    * teams without the kernel knowledge to debug a verifier rejection
    * the "we used `eBPF` because it was new" failure
    * picking the right tool
<!-- chapter: case-studies-and-recommended-reading, duration: 2h -->
* Case studies and recommended reading
    * `Cilium` deployment walkthrough
    * `Tetragon` policy walkthrough
    * `Pixie` deployment walkthrough
    * `bpftrace` debugging walkthrough
    * recommended reading: `Brendan Gregg`'s `BPF Performance Tools`, the `Cilium` docs

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
