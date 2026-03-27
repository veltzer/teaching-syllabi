---
tags:
  - linux
  - c
  - systems-programming
  - multithreading
  - ipc
  - networking
  - io
level: advanced
category: operating-systems
duration_days: 8
audience:
  - developers
---
# `Linux` systems programming

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course is about user space programming in `Linux` in `C`.
It covers all major areas of programming (processes, threads, IO,
networking, synchronization and more).
It includes exercises (usually one exercise for every major chapter).

`C++` is not covered as it is yet another thin layer on top of `C` and does not
change the system `API` in any way nor change any of the best practices learned
in this course.

The course can be shortened to 5 days if we remove the exercises, but this should
be done only for experienced developers and in this case the instructor will show
examples instead.

## Duration
64 hours / 8 days

## Intended Audience
* software developers working on Linux-based systems
* system administrators and DevOps engineers

## Prerequisites
* Experience in `C` programming is a must.

## Objectives
* understand the core concepts and principles of Linux` systems programming
* gain practical knowledge of Boot sequence
* gain practical knowledge of Protected operating system theory
* gain practical knowledge of Tools (this chapter is needed for the following exercises)

## Outline
* Boot sequence
    * `grub`/`uboot` - loading and booting the image
    * secure boot - what is a TPM?
* Protected operating system theory
    * Protected OS definition.
    * Why is the definition important?
    * How does privilege work?
    * How does memory protection work?
    * How do system calls work?
* Tools (this chapter is needed for the following exercises)
    * The `GCC` compiler.
    * Some make syntax.
    * Compiling apps.
    * Compiling libraries.
    * Making the apps find the libraries.
    * Best practices.
    * Comparing build tools: make, cmake, ninja, ...
* Processes
    * The process tree.
    * /sbin/init and startup/shutdown.
    * review of systemd and it's properties.
    * initializing containers
        * default user in `Docker`
        * initialization in `Docker`
        * dumb-init
    * Creating processes.
    * Waiting for processes to change state/die.
        * With signals handling.
        * With the `wait(2)` family of functions.
        * Using a `signalfd(2)` and multiplexing.
    * Analyzing the processes return value.
    * Process state transition.
    * Adoption.
    * Zombies and solutions.
    * Fork performance and `vfork(2)`.
    * `fork(2)/exec(2)` way of doing things.
    * `system(3),popen(3)`
    * shells and how are they implemented.
    * Is `fork(2)` a good `API`? (compared to other operating systems).
    * There are no threads in `Linux` and `clone(2)`.
    * Advanced material:
        * Process groups.
        * Sessions.
        * Controlling terminals.
        * Writing your own process reapers.
        * Children getting signals about their parents dying.
* Pipes
    * What is a pipe/fifo.
    * The `pipe(2)` system call.
    * EOF condition.
    * SIGPIPE.
    * File descriptor table after fork.
    * File descriptor table after exec.
    * Using `dup(2)`.
    * `popen(3)`.
    * inetd example - Sockets instead of pipes but still the same.
    * Limitations of `pipe(2)`.
    * Named pipes.
* Allocating memory
    * `malloc(3)` and it's issues.
    * `mmap(2)`
    * writing your own heap.
    * `TLS`.
    * obstacks
    * allocating on the stack (`alloca(3)` and C99 stack allocation).
* Signal Handling
    * Why signals?
    * The problems created by asynchronous delivery.
    * Overcoming the async problem of signals.
        * routing back to main context.
        * `sigprocmask(2)/rt_sigprocmask(2)`
        * signal safe functions
    * How are signals implemented?
        * When a process is in user space.
        * When a process is in kernel space.
        * In real time `Linux`.
    * Receiving signals synchronously.
    * The problem of signal delivery.
    * Jumping out of signal context to regular context.
    * Signal interruption.
    * The various signals and their semantics and usage.
* Real time signals
    * The problem
    * The solution.
    * Queuing real time signals.
    * Real time signals and queues in `Linux`.
* Threads
    * The `pthread` library.
    * Creating threads.
    * Waiting for threads to die.
    * Detached threads.
    * Thread mutexes and their kinds.
    * How are futexes implemented?
        * Using futexes for process synchronization.
    * Barriers
    * Conditions
    * Readers/Writer locks.
    * Spin locks.
    * pthreads and signals
    * cleanup facilities
    * cancellation facilities
    * thread affinities.
    * threads are not file descriptors and what can you do about it.
* File `API`
    * The per process file descriptor table.
    * `open/read/write/close`
    * Explanation of the semantics of read/write.
    * Overcoming the read/write issues
        * `mmap(2)`
        * `ioctl(2)`
        * `FILE` `APIs`.
        * C++ streaming `APIs`.
    * Manipulating files.
    * No locking in `UNIX`.
    * Directories.
    * Symbolic links.
    * Other file types.
    * Passing file descriptors between unrelated processes.
    * `inotify` and its pitfalls
* The IO subsystem
    * How does it work?
    * The kernel page and buffer caches.
    * The performance of the io subsystem
    * `ionice(2)` and it's uses to control IO priority.
    * Overcoming the copy problem with `O_DIRECT` and it's problems.
    * Overcoming the copy problem with `mmap`.
* Sys V IPC
    * Semaphores
    * Shared Memory
    * Message queues
    * Performance compared to `POSIX` equivalents.
* `POSIX` IPC
    * Semaphores
    * Shared Memory
    * Message queues.
    * Performance compared to SYS V equivalents.
* Networking
    * Writing `SOCK_STREAM` (`TCP`) servers and clients.
    * Writing `SOCK_DGRAM` (`UDP`) apps.
    * The various domains
        * `AF_UNIX` vs `AF_INET`
    * Using raw sockets.
    * Debugging tools for networking apps.
    * Netlink especially `RT_NETLINK`
    * Network namespaces
    * VRFs devices and differences from namespaces
* Time
    * What is the current time?
    * How long does it take to know what time is it?
    * The various clocks under the operating system
    * Sleeping precisely.
    * Working with the right clock.
    * `timerfd(2)` - a file descriptor for a clock.
    * Measuring very short functions accurately.
* Multiple IO `APIs`
    * `readv(2)/writev(2)`
    * `io_uring(7)`
* Async IO
    * What is async io?
    * Comparing async io with zero copy and multiplexing
    * Using the `aio(2)` functions
    * Using the `uring(2)` functions
* Multiplexing IO
    * What is the problem to solve?
    * What are the two possible solutions (multiplexing and ioports) and why is multiplexing better.
    * Comparing the various `APIs` for multiplexing in `Linux`
        * `select(2)`
        * `poll(2)`
        * `epoll(2)`
        * `uring(2)`
        * `aio(2)`
    * Doing classical multiplexing
        * How to do multiplexing correctly?
        * Design patterns on top of multiplexing (Reactor/Proactor).
        * Libraries built on top of multiplexing (libuv)
* Zero copy
    * What is the problem to solve?
    * The various `APIs`:
        * `sendfile(2)`
        * `pipe(2)`
        * `splice(2)`
        * `tee(2)`
        * `vmsplice(2)`
        * `uring(2)`
    * Other ways of solving the problem:
        * `mmap(2)`
        * DPDK
        * other solutions
* Working with device drivers
    * Everything is a file in `UNIX` - what does this mean?
    * The `/dev` folder and it's content.
    * Working with a simple serial port.
    * `ioctl(2)` and it's uses.
    * `read(2)/write(2)` performance.
    * `mmap(2)` and it's uses.
    * The various taxonomies of device drivers.
* Advanced IO
    * File Locking
    * Asynchronous I/O
    * Network server design
* Framework issues
    * Namespaces and cgroups (what it is? when to use it?)
    * Capabilities and how to use them properly
* Secure development
    * Stack separation between threads
    * AppArmor vs SELinux
    * ASLR
        * for libraries
        * for binaries
        * how to turn it off for debugging

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
