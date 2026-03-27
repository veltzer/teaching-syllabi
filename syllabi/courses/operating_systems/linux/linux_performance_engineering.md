---
tags:
  - linux
  - performance
  - optimization
  - profiling
  - benchmarking
  - kernel
level: advanced
category: operating-systems
duration_days: 3
audience:
  - developers
  - sysadmins
  - devops
  - performance-engineers
---
# `Linux` Performance Engineering

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course provides a deep dive into `Linux` performance engineering, covering the
methodologies, tools, and techniques required to analyze, diagnose, and resolve performance
problems in `Linux` systems and applications. The course covers the full performance
engineering lifecycle: from establishing baselines and setting goals, through profiling
and tracing, to applying targeted optimizations at the application, system, and kernel levels.

Participants will learn to use modern observability tools such as `perf`, `bpftrace`, `eBPF`,
and `FlameGraphs` to identify bottlenecks, and will gain a deep understanding of how the
`Linux` kernel manages CPU, memory, I/O, and networking resources.

## Duration
24 hours / 3 days

## Intended Audience
* Developers who need to write high-performance applications on `Linux`
* System administrators and `DevOps` engineers responsible for tuning production `Linux` systems
* Performance engineers who need to diagnose and resolve performance issues
* Software architects who need to understand the performance implications of their design decisions

## Prerequisites
* Solid understanding of `Linux` fundamentals and the command line
* `C`/`C++` programming experience is a strong advantage
* Familiarity with basic operating system concepts (processes, threads, virtual memory, file systems)

## Objectives
* Understand the `Linux` performance engineering methodology and how to approach performance problems systematically
* Use modern profiling and tracing tools to identify bottlenecks in applications and systems
* Understand how the `Linux` kernel manages CPU scheduling, memory, disk I/O, and networking
* Apply targeted optimizations at the application, library, kernel, and hardware levels
* Read and interpret `FlameGraphs`, `perf` reports, and `eBPF` traces
* Set up continuous performance monitoring and regression detection

## Outline
* Performance engineering methodology
    * Defining performance goals and `SLAs`
    * The `USE` method (Utilization, Saturation, Errors)
    * The `RED` method (Rate, Errors, Duration)
    * Workload characterization
    * Baseline measurement and benchmarking
    * Anti-patterns in performance analysis
    * Amdahl's law and its practical implications
* CPU performance
    * CPU architecture overview: cores, caches, `NUMA` topology
    * The `Linux` `CFS` scheduler in depth
    * Scheduler tuning: nice, `ionice`, `chrt`, `taskset`
    * `CPU` pinning and affinity
    * `NUMA` awareness and `numactl`
    * Context switch overhead and how to minimize it
    * Run queue latency and saturation
    * `IPC` (instructions per cycle) and `CPU` micro-architecture effects
    * Compiler optimization flags and their impact
    * Profiling CPU with `perf stat`, `perf record`, `perf report`
    * Using hardware performance counters (`PMU`)
* Memory performance
    * Virtual memory architecture in `Linux`
    * Page tables, `TLB`, and `TLB` misses
    * Huge pages and transparent huge pages
    * `NUMA` memory allocation policies
    * Page faults: minor vs major
    * Memory allocation patterns and fragmentation
    * The `slab` allocator
    * `OOM` killer behavior and tuning
    * Swap tuning and `swappiness`
    * `cgroups` memory limits and accounting
    * Profiling memory with `perf mem`, `valgrind`, `massif`
    * Cache line effects: false sharing, alignment, prefetching
* Profiling and tracing tools
    * `perf` in depth: `stat`, `record`, `report`, `top`, `annotate`
    * `FlameGraphs`: generation, interpretation, on-CPU and off-CPU
    * `ftrace` and the `tracefs` interface
    * Introduction to `eBPF` and `bpftrace`
    * `bpftrace` one-liners for common performance questions
    * `BCC` tools: `biolatency`, `execsnoop`, `opensnoop`, `tcplife`
    * `strace` and `ltrace` for syscall and library call tracing
    * Static tracepoints vs dynamic probes (`kprobes`, `uprobes`)
    * When to use which tool
* Disk and file system performance
    * The `Linux` I/O stack: application, VFS, file system, block layer, device driver
    * I/O schedulers: `mq-deadline`, `bfq`, `none`
    * Direct I/O vs buffered I/O
    * Page cache behavior and tuning
    * `readahead` and its configuration
    * File system choice and performance implications (`ext4`, `XFS`, `btrfs`)
    * `io_uring` and asynchronous I/O
    * Measuring I/O with `iostat`, `iotop`, `blktrace`
    * `fio` for I/O benchmarking
    * `NVMe` and storage hardware considerations
* Network performance
    * The `Linux` network stack: socket, transport, IP, device driver
    * TCP tuning: buffer sizes, congestion control algorithms
    * `SO_REUSEPORT` and multi-queue `NICs`
    * Interrupt coalescing and `NAPI`
    * `RSS`, `RPS`, `RFS` for network load distribution
    * `XDP` and `AF_XDP` for high-performance packet processing
    * Measuring network performance with `iperf3`, `netperf`
    * Analyzing network issues with `ss`, `nstat`, `ethtool`
    * TCP retransmit analysis and troubleshooting
* Application-level optimization
    * Lock contention and lock-free data structures
    * System call overhead and batching
    * Memory-mapped I/O and zero-copy techniques
    * Thread pool sizing and configuration
    * Connection pooling
    * User-space vs kernel-space trade-offs
    * Profiling application code with `perf` and `FlameGraphs`
    * Using `compiler intrinsics` and `SIMD` where appropriate
* Continuous performance engineering
    * Setting up performance regression testing
    * Monitoring with `Prometheus` and `Grafana`
    * Using `sar` and `sysstat` for historical analysis
    * Kernel tuning via `sysctl` and persistent configuration
    * `cgroups` v2 for resource isolation and control
    * Performance-oriented `Linux` kernel configuration
    * Documenting and communicating performance findings

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
