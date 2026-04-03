---
tags:
  - infrastructure:linux
  - practices:performance
  - practices:tuning
  - practices:profiling
level: advanced
category: operating-systems
duration_hours: 24
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:performance-engineers
  - audiences:sres
---
<!-- course: linux_performance_tuning -->
# `Linux` Performance Tuning

## Description
Effective performance tuning on `Linux` requires a deep understanding of how the kernel manages `CPU`, memory, `I/O`, and network resources. This course teaches a systematic approach to identifying and resolving performance bottlenecks using modern profiling tools and tuning techniques. Students will learn the USE method, master tools like `perf`, `ftrace`, and bpftrace, and apply kernel-level tuning to optimize production workloads.

## Duration
24 hours / 3 days

## Intended Audience
* System administrators responsible for high-performance `Linux` systems
* `DevOps` engineers optimizing application infrastructure
* Performance engineers conducting system-level analysis
* Site reliability engineers managing service performance

## Prerequisites
* `Solid` `Linux` system administration experience
* Understanding of `Linux` kernel basics (processes, memory, filesystems)
* Command-line proficiency

## Objectives
* Apply a systematic methodology to performance analysis
* Profile systems using `perf`, `ftrace`, and bpftrace
* Tune `CPU` scheduling, memory, `I/O`, and network subsystems
* Use `cgroups` for resource isolation and control
* Conduct meaningful benchmarks and interpret results
* Optimize `Linux` systems for specific workload patterns

## Outline
<!-- chapter: performance-analysis-methodology, duration: 2h -->
* Performance Analysis Methodology
    * The USE method (utilization, saturation, errors)
    * Workload characterization
    * Latency analysis
    * Anti-patterns in performance tuning
    * Observability tools overview
    * Baseline establishment
<!-- chapter: cpu-tuning, duration: 3h -->
* `CPU` Tuning
    * `CPU` architecture and scheduling overview
    * CFS and deadline schedulers
    * Process and thread priorities (nice, chrt)
    * `CPU` affinity and pinning (taskset, cpuset)
    * `CPU` frequency governors
    * `IRQ` balancing
    * NUMA topology and `CPU` placement
    * Context switch analysis
<!-- chapter: memory-tuning, duration: 4h -->
* Memory Tuning
    * Virtual memory architecture
    * sysctl vm parameters
    * Page cache tuning
    * Huge pages and transparent huge pages
    * NUMA memory policy (numactl)
    * Swap configuration and swappiness
    * Memory overcommit settings
    * OOM killer tuning
    * Memory compaction
<!-- chapter: i-o-tuning, duration: 3h -->
* `I/O` Tuning
    * Block `I/O` architecture
    * `I/O` schedulers (mq-deadline, BFQ, kyber, none)
    * Readahead configuration
    * Direct `I/O` vs buffered `I/O`
    * `I/O` priorities (ionice)
    * Block device queue parameters
    * NVMe tuning considerations
    * `I/O` monitoring with iostat, blktrace, and biosnoop
<!-- chapter: network-tuning, duration: 3h -->
* Network Tuning
    * Network stack architecture
    * `TCP` buffer sizes (rmem, wmem)
    * `TCP` congestion control algorithms
    * Socket buffer tuning
    * Network interrupt coalescing
    * Receive Side Scaling (RSS) and RPS/RFS
    * `TCP` fastopen and other optimizations
    * Network monitoring with ss, nstat, and tcptrace
<!-- chapter: filesystem-tuning, duration: 2h -->
* Filesystem Tuning
    * `ext4`, `XFS`, and `Btrfs` tuning options
    * Mount options for performance
    * Journal configuration
    * Inode and directory optimization
    * `File` allocation strategies
<!-- chapter: cgroups-for-resource-control, duration: 2h -->
* `cgroups` for Resource Control
    * `cgroups` v1 vs v2
    * `CPU` resource limits and shares
    * Memory limits and accounting
    * `I/O` bandwidth control
    * Integration with `systemd`
<!-- chapter: profiling-tools, duration: 2h -->
* Profiling Tools
    * `perf` (stat, record, report, `top`, flame graphs)
    * `ftrace` (function tracing, function_graph, tracepoints)
    * bpftrace (one-liners, scripts, probes)
    * BCC tools (execsnoop, opensnoop, biolatency, tcplife)
    * `strace` and `ltrace`
    * Flame graphs generation and interpretation
<!-- chapter: benchmarking, duration: 3h -->
* Benchmarking
    * Benchmarking methodology
    * `CPU` benchmarks (sysbench, stress-ng)
    * Memory benchmarks (stream, mbw)
    * `I/O` benchmarks (fio, dd)
    * Network benchmarks (iperf3, netperf)
    * Application-level benchmarking
    * Statistical analysis of results

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
