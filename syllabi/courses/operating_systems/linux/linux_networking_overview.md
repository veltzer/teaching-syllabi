---
tags:
  - infrastructure:linux
  - networking:networking
  - networking:tcp-ip
  - infrastructure:kernel
  - linuxkernel:ebpf
  - networking:netfilter
  - infrastructure:namespaces
level: advanced
category: operating-systems
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: linux_networking_overview -->
# `Linux` networking overview

## Description
This is a comprehensive course about the various subsystems in `Linux` which have to do with networking.
It scans both the user space APIs and the networking stack in the kernel including the role of the network
device driver itself. It also teaching about other technologies that have an interaction with networking like
`eBPF`, `iptables`, `netfilter`, namespaces and more

## Duration
24 hours / 3 days

## Intended Audience
* software developers working on `Linux`-based systems
* system administrators and `DevOps` engineers

## Prerequisites
* familiarity with `Linux` command line and system administration

## Objectives
* understand the core concepts and principles of `Linux`` networking overview
* gain practical knowledge of `TCP``/``IP`` essentials
* gain practical knowledge of The `Linux` networking stack
* gain practical knowledge of Network `C` Programming essentials

## Outline
<!-- chapter: tcp-ip-essentials, duration: 2h -->
* `TCP`/`IP` essentials
    * Introduction to `TCP`/`IP`
    * Internet Protocol (`IP`)
    * Transmission Control Protocol (`TCP`)
    * User Datagram Protocol (`UDP`)
    * Concepts: Router, Modem, Switch, Gateway, Server, Client, `NAT`, `DNS`
<!-- chapter: the-linux-networking-stack, duration: 2h -->
* The `Linux` networking stack
    * What is the role of net_device and network device drivers
    * The `Linux` protocol stack (`TCP`/`IP`)
    * Sockets
    * The socket <-> protocol interface
    * The link layer
    * The user space `API`
<!-- chapter: network-c-programming-essentials, duration: 3h -->
* Network `C` Programming essentials
    * Stream socket server and client coding
        * socket, `bind`, connect, listen, accept
        * read, write, recv, send
    * `C` library utility functions: gethostbyname, getservbyname
    * Datagram coding: socket, `bind`, connect, recvfrom, sendto
    * Socket options, especially DSCP/TOS using IP_TOS
    * Out of band data
    * Using the command line tc to handle priorities
<!-- chapter: various-command-line-tools-that-control-networking, duration: 3h -->
* Various command line tools that control networking
    * Information tools: `/proc/[pid]/fd`, `netstat`, `ip`, ss
    * Low level tools: ethtool, mii-tool, `arp`
    * Configuration tools: `ifconfig`, `ip`, `ifup`/`ifdown`, route, iwconfig, iwlist, iwpriv
    * performance tools: jnettop, netperf, lnstat rtmon rtstat nstat rtacct routef routel ctstat
    * Tapping tools: nc, `netcat`, `tcpdump`, `wireshark`
    * Quality control: tc
    * Debugging tools: telnet, `ping`, `traceroute`, `nmap`
<!-- chapter: linux-module-primer, duration: 2h -->
* `Linux` module primer
    * Module initialization
    * Module cleanup
    * Compiling a kernel module
    * Kernel logging
<!-- chapter: network-device-overview, duration: 3h -->
* Network Device overview
    * sk_buff
    * The net_device structure
    * Registering a network driver
    * Network driver private data
    * Network device operations: ndo_open, ndo_stop, start_xmit
    * Handling interrupts, mitigating large number of interrupts
    * Memory mapping
<!-- chapter: tcp-ip-firewall, duration: 2h -->
* `TCP`/`IP` `Firewall`
    * What is a `firewall`?
    * What is `IP` filtering?
    * `Linux` and firewalling
    * `IP` tables
    * Testing a `firewall` configuration
<!-- chapter: net-filters, duration: 2h -->
* Net Filters
    * Implementing netfilters in user space
    * Hooking points
    * Hook functions
    * Registering a `netfilter`
    * Removal of netfilters
    * Implementing netfilters in kernel space
<!-- chapter: namespaces, duration: 3h -->
* Namespaces
    * What are namespaces
    * Types of namespaces
    * `Cgroups` and their relation to namespaces
    * Creating namespaces and `cgroups`
    * Inspecting a namespace from the outer world
    * Connecting namespaces
    * Using net_prio and net_cls to prioritize networking for containers
<!-- chapter: ebpf-overview-and-usage-optional-second-priority, duration: 2h -->
* `eBPF` Overview and Usage Optional, second priority
    * The extended Berkeley packet filter
    * cBPF vs. `eBPF`
    * The architecture of `eBPF`
    * Creating and running `eBPF` code
    * Off the shelf `eBPF` program collections

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
