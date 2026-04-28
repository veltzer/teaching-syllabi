---
tags:
  - infrastructure:linux
  - practices:performance
  - concepts:optimization
  - practices:profiling
  - practices:benchmarking
  - infrastructure:kernel
level: advanced
category: operating-systems
duration_hours: 40
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
  - audiences:sres
  - audiences:performance-engineers
  - audiences:architects
---
<!-- course: linux_performance_engineering -->
# `Linux` Performance Engineering

## Description
This five day course is a deep dive into `Linux` performance engineering. It covers the full performance lifecycle:
methodology and goal-setting, profiling and tracing, subsystem-by-subsystem analysis and tuning of `CPU`, memory, `I/O`,
filesystems and networking, application-level optimization, kernel tuning, resource isolation with `cgroups`,
benchmarking, and continuous performance regression detection.

Participants learn to use modern observability tools (`perf`, `ftrace`, `eBPF`/bpftrace, BCC, `FlameGraphs`) to identify
bottlenecks, gain a deep understanding of how the `Linux` kernel manages each major resource, and apply targeted
optimizations at the application, kernel and hardware levels. The course assumes a `solid` `Linux` background and
moves quickly into deep technical material.

## Duration
40 hours / 5 days

## Intended Audience
* developers writing high-performance applications on `Linux`
* system administrators and `DevOps` engineers responsible for tuning production systems
* `SREs` who own service performance and capacity
* performance engineers diagnosing and resolving bottlenecks
* architects who need to understand the performance implications of their designs

## Prerequisites
* `solid` `Linux` fundamentals and command-line proficiency
* `C`/`C++` programming experience is a strong advantage
* familiarity with operating system concepts (processes, threads, virtual memory, filesystems)
* basic understanding of computer architecture (caches, NUMA)

## Objectives
* apply a systematic performance methodology to real problems
* use `perf`, `ftrace`, `eBPF`/bpftrace and BCC to identify bottlenecks
* understand how the `Linux` kernel manages `CPU`, memory, `I/O` and networking
* tune each subsystem for specific workload patterns
* read and interpret `FlameGraphs`, `perf` reports and `eBPF` traces
* design meaningful benchmarks and interpret their results statistically
* use `cgroups` v2 for resource isolation and control
* set up performance regression detection in `CI` and production
* communicate performance findings effectively

## Outline
<!-- chapter: performance-engineering-methodology, duration: 2h -->
* Performance engineering methodology
    * defining performance goals and `SLAs`
    * the USE method (utilization, saturation, errors)
    * the RED method (rate, errors, duration)
    * workload characterization
    * baseline measurement
    * Amdahl's law and its practical implications
    * common anti-patterns in performance analysis
<!-- chapter: cpu-performance, duration: 4h -->
* `CPU` performance
    * `CPU` architecture overview: cores, caches, NUMA topology
    * the `Linux` `CFS` scheduler in depth
    * deadline and realtime schedulers
    * scheduler tuning: nice, ionice, chrt, taskset
    * `CPU` pinning and affinity
    * NUMA awareness and numactl
    * `CPU` frequency governors
    * `IRQ` balancing and interrupt affinity
    * context switch overhead and how to minimize it
    * run queue latency and saturation
    * `IPC` (instructions per cycle) and micro-architecture effects
    * profiling `CPU` with `perf stat`, `perf record`, `perf report`
    * using hardware performance counters (`PMU`)
<!-- chapter: memory-performance, duration: 4h -->
* Memory performance
    * virtual memory architecture in `Linux`
    * page tables, `TLB` and `TLB` misses
    * huge pages and transparent huge pages
    * NUMA memory allocation policies
    * page faults: minor vs major
    * memory allocation patterns and fragmentation
    * the slab allocator
    * `OOM` killer behavior and tuning
    * swap tuning and swappiness
    * memory overcommit and compaction
    * `cgroups` memory limits and accounting
    * profiling memory with `perf mem`, `valgrind`, massif
    * cache line effects: false sharing, alignment, prefetching
<!-- chapter: disk-and-filesystem-performance, duration: 4h -->
* Disk and filesystem performance
    * the `Linux` `I/O` stack: application, `VFS`, filesystem, block layer, device driver
    * `I/O` schedulers: mq-deadline, `BFQ`, kyber, none
    * direct `I/O` vs buffered `I/O`
    * page cache behavior and tuning
    * readahead and its configuration
    * filesystem choice and performance implications (`ext4`, `XFS`, `Btrfs`)
    * mount options for performance and journal configuration
    * inode and directory layout effects
    * io_uring and asynchronous `I/O`
    * `I/O` priorities and ionice
    * block device queue parameters
    * `NVMe` and storage hardware considerations
    * measuring `I/O` with iostat, `iotop`, blktrace, biosnoop
    * fio for `I/O` benchmarking
<!-- chapter: network-performance, duration: 4h -->
* Network performance
    * the `Linux` network stack: socket, transport, `IP`, device driver
    * `TCP` tuning: buffer sizes (`rmem`/`wmem`), congestion control algorithms
    * `TCP` fastopen and other socket-level optimizations
    * `SO_REUSEPORT` and multi-queue NICs
    * interrupt coalescing and `NAPI`
    * `RSS`, `RPS`, `RFS` for network load distribution
    * `XDP` and `AF_XDP` for high-performance packet processing
    * measuring with iperf3, netperf
    * analyzing with ss, nstat, ethtool, tcptrace
    * `TCP` retransmit analysis and troubleshooting
<!-- chapter: profiling-and-tracing-tools, duration: 5h -->
* Profiling and tracing tools
    * `perf` in depth: stat, record, report, `top`, annotate, mem
    * `FlameGraphs`: generation, interpretation, on-`CPU` and off-`CPU`
    * `ftrace` and the tracefs interface
    * function tracing and function_graph
    * `eBPF` fundamentals and bpftrace
    * bpftrace one-liners for common performance questions
    * BCC tools: biolatency, execsnoop, opensnoop, tcplife and friends
    * `strace` and `ltrace` for syscall and library call tracing
    * static tracepoints vs dynamic probes (`kprobes`, `uprobes`)
    * choosing the right tool for the question
<!-- chapter: benchmarking, duration: 3h -->
* Benchmarking
    * benchmarking methodology and pitfalls
    * `CPU` benchmarks: sysbench, stress-ng
    * memory benchmarks: stream, mbw
    * `I/O` benchmarks: fio, dd
    * network benchmarks: iperf3, netperf
    * application-level benchmarking
    * statistical analysis of results
    * detecting and explaining variance
<!-- chapter: cgroups-and-resource-control, duration: 3h -->
* `cgroups` and resource control
    * `cgroups` v1 vs v2
    * `CPU` resource limits, shares and weights
    * memory limits, low/high/max, accounting
    * `I/O` bandwidth control and `io.max`
    * `PID` and other controllers
    * integration with `systemd` slices and units
    * resource isolation patterns for multi-tenant hosts
<!-- chapter: application-level-optimization, duration: 4h -->
* Application-level optimization
    * lock contention and lock-free data structures
    * system call overhead and batching
    * memory-mapped `I/O` and zero-copy techniques
    * thread pool sizing and configuration
    * connection pooling
    * user-space vs kernel-space trade-offs
    * profiling application code with `perf` and `FlameGraphs`
    * `compiler intrinsics` and SIMD where appropriate
    * `LTO` and `PGO` for production builds
    * vendor-specific compilers and tools (see Intel Compiler Optimization for `Linux` course)
<!-- chapter: kernel-tuning, duration: 3h -->
* Kernel tuning
    * `sysctl` and `/proc/sys` parameters worth knowing
    * persistent configuration via `/etc/sysctl.d`
    * kernel command-line parameters
    * choosing and configuring kernels for performance workloads
    * preempt models (none, voluntary, full, `RT`)
    * boot-time vs runtime tunables
    * documenting and version-controlling kernel tuning
<!-- chapter: continuous-performance-engineering, duration: 3h -->
* Continuous performance engineering
    * setting up performance regression testing
    * historical analysis with sar and sysstat
    * monitoring with `Prometheus` and `Grafana`
    * `SLI`/`SLO` for performance
    * automated `FlameGraph` capture in production
    * detecting regressions in `CI` performance benchmarks
    * documenting and communicating performance findings
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * end-to-end analysis of a sample production performance issue
    * recommended reading: Brendan Gregg's books, kernel documentation
    * further study: `eBPF` programming, kernel internals

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
