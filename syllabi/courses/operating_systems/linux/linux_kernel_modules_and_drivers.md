---
tags:
  - infrastructure:linux
  - infrastructure:kernel
  - concepts:systems-programming
  - concepts:concurrency
  - concepts:locking
level: advanced
category: operating-systems
duration_hours: 40
audience:
  - audiences:developers
  - audiences:systems-programmers
  - audiences:embedded-developers
  - audiences:firmware-developers
---
<!-- course: linux_kernel_modules_and_drivers -->
# `Linux` Kernel Modules and Drivers

## Description
The `Linux` kernel course in the catalog is a broad treatment of kernel internals. This course is the focused
sibling: how to write kernel modules and drivers. It is for engineers who need to ship code that runs in
kernel context against the actual driver model of a recent kernel, not for engineers who only want to
understand it from the outside.

This five day course covers the kernel module mechanics, the kernel programming environment and the rules
that distinguish it from user space, the major driver frameworks (character, block, network, platform),
the bus subsystems (`PCI`, `USB`, `I2C`, `SPI`), the device-tree and `ACPI` integration, the kernel
synchronization primitives, the memory and `DMA` APIs, the `sysfs`/`procfs`/`debugfs` interfaces, and the
debugging story including `printk`, `ftrace`, `kgdb`, and live patching. The course tracks current `LTS`
kernels and avoids deprecated APIs. Participants leave able to write, debug, and submit kernel modules and
drivers.

## Duration
40 hours / 5 days

## Intended Audience
* developers writing or maintaining kernel modules and drivers
* systems programmers crossing into kernel work
* embedded engineers working at the `Linux`-driver layer
* engineers debugging kernel-level issues that require module-level changes

## Prerequisites
* `solid` C programming experience
* working knowledge of `Linux` user-space programming
* basic familiarity with computer architecture (interrupts, `MMU`, caches)
* exposure to a `Linux` kernel build is helpful

## Objectives
* build, load, and unload kernel modules cleanly
* use the kernel programming environment correctly
* implement character, block, and network drivers
* interface with the `PCI`, `USB`, `I2C`, and `SPI` subsystems
* use the kernel synchronization primitives correctly
* manage memory and `DMA` from a driver
* expose driver state through `sysfs` and `debugfs`
* debug a misbehaving driver in production

## Outline
<!-- chapter: the-kernel-programming-environment, duration: 2h -->
* The kernel programming environment
    * what is and is not available in kernel context
    * no `libc`, no floating point in most cases, no user-space copy
    * `GFP_*` flags and the realities of allocation
    * the per-`CPU` model
    * preemption, interrupt context, atomic context
    * cross-reference to the kernel internals material
<!-- chapter: kernel-module-mechanics, duration: 3h -->
* Kernel module mechanics
    * module entry and exit, `module_init`, `module_exit`
    * `MODULE_LICENSE`, `MODULE_AUTHOR`, `MODULE_DESCRIPTION`
    * module parameters
    * symbol export with `EXPORT_SYMBOL`
    * dependencies and `modprobe`
    * `KBuild` and out-of-tree modules
    * dynamic loading vs `built-in`
<!-- chapter: the-driver-model, duration: 3h -->
* The driver model
    * `struct device`, `struct device_driver`
    * the bus, driver, device triangle
    * probe and release
    * the device-tree binding model
    * `ACPI` for non-`DT` platforms
    * the platform driver
<!-- chapter: character-drivers, duration: 3h -->
* Character drivers
    * major and minor numbers
    * `cdev` and `register_chrdev_region`
    * `file_operations` table
    * `read`, `write`, `ioctl`, `mmap`
    * blocking and non-blocking `IO`
    * `poll`, `select`, `epoll` from a driver perspective
    * `udev` and device-node creation
<!-- chapter: block-drivers, duration: 3h -->
* Block drivers
    * the block layer in modern kernels
    * `blk-mq` and the multi-queue model
    * `request` vs `bio`
    * partition handling
    * `IO` schedulers from the driver side
    * a minimal block driver walkthrough
<!-- chapter: network-drivers, duration: 4h -->
* Network drivers
    * `net_device` and `net_device_ops`
    * `sk_buff` lifecycle
    * `NAPI` and polling
    * transmit and receive paths
    * checksum offload, `GSO`, `TSO`, `LRO`
    * `XDP` from the driver side
    * `ethtool` integration
<!-- chapter: pci-and-pcie, duration: 3h -->
* `PCI` and `PCIe`
    * `PCI` configuration space
    * `pci_driver` registration
    * `BAR` mapping
    * `MSI` and `MSI-X`
    * `PCIe` link power and capabilities
    * `IOMMU` and `DMA` mappings
<!-- chapter: usb-i2c-spi, duration: 3h -->
* `USB`, `I2C`, `SPI`
    * `USB` driver framework, endpoints, urbs
    * `I2C` master and slave drivers
    * `SPI` controller and device drivers
    * common embedded peripheral drivers
    * device-tree bindings for these buses
<!-- chapter: synchronization-primitives, duration: 3h -->
* Synchronization primitives
    * spinlocks, mutexes, rw locks
    * `RCU` from the driver side
    * atomics and memory barriers
    * completions and wait queues
    * sequence locks
    * the right primitive for the right context
    * cross-reference to the Concurrency and Parallelism course
<!-- chapter: memory-and-dma, duration: 3h -->
* Memory and `DMA`
    * `kmalloc`, `kzalloc`, `vmalloc`, slab caches
    * `dma_alloc_coherent` vs streaming `DMA`
    * `IOMMU` and bounce buffers
    * memory mapping into user space
    * the `dma-buf` framework
    * common memory-leak patterns in drivers
<!-- chapter: interrupts-and-bottom-halves, duration: 3h -->
* Interrupts and bottom halves
    * `request_irq` and the handler contract
    * shared interrupts
    * threaded `IRQs`
    * tasklets, workqueues, kthreads
    * the bottom-half evolution and current best practice
    * timing constraints from interrupt context
<!-- chapter: sysfs-procfs-debugfs, duration: 2h -->
* `sysfs`, `procfs`, `debugfs`
    * exposing driver state to user space
    * `kobject` and `attribute_group`
    * `procfs` for legacy interfaces
    * `debugfs` for debugging-only interfaces
    * `seq_file` for read-mostly interfaces
    * keeping interfaces stable across kernel versions
<!-- chapter: power-management-and-runtime-pm, duration: 1h -->
* Power management and runtime `PM`
    * `suspend`/`resume` callbacks
    * runtime `PM` and reference counting
    * `device tree` power domains
    * the `PM` quality of service
<!-- chapter: debugging-kernel-modules, duration: 3h -->
* Debugging kernel modules
    * `printk` and the kernel ring buffer
    * `dynamic debug` and `pr_debug`
    * `ftrace` and tracing kernel functions
    * `KASAN` and other sanitizers
    * `kgdb` and live debugging
    * `crashdump` analysis with `crash`/`gdb`
    * common driver bug patterns
<!-- chapter: stable-api-thinking-and-upstreaming-and-wrap-up, duration: 1h -->
* Stable-`API` thinking, upstreaming and wrap up
    * the "no stable kernel `API`" reality
    * keeping out-of-tree modules current
    * the upstream submission process
    * style: `checkpatch.pl`, `Documentation/process/`
    * licensing and `GPL`-only symbols
    * recommended reading: `Linux Kernel Development` (Love), `LDD3` (historical), kernel `Documentation/`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
