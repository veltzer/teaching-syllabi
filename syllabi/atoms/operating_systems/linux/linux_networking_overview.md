---
tags:
  - linux
  - networking
  - tcp-ip
  - kernel
  - ebpf
  - netfilter
  - namespaces
level: advanced
category: operating-systems
duration_days: 3
audience:
  - developers
  - sysadmins
---
# `Linux` networking overview

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This is a comprehensive course about the various subsystems in `Linux` which have to do with networking.
It scans both the user space `APIs` and the networking stack in the kernel including the role of the network
device driver itself. It also teaching about other technologies that have an interaction with networking like
`eBPF`, `iptables`, `netfilter`, namespaces and more

## Duration
24 hours / 3 days

## Outline
* `TCP`/IP essentials
    * Introduction to `TCP`/IP
    * Internet Protocol (IP)
    * Transmission Control Protocol (`TCP`)
    * User Datagram Protocol (`UDP`)
    * Concepts: Router, Modem, Switch, Gateway, Server, Client, NAT, `DNS`
* The `Linux` networking stack
    * What is the role of `net_device` and network device drivers
    * The `Linux` protocol stack (`TCP`/IP)
    * Sockets
    * The socket <-> protocol interface
    * The link layer
    * The user space `API`
* Network C Programming essentials
    * Stream socket server and client coding
        * `socket`, `bind`, `connect`, `listen`, `accept`
        * `read`, `write`, `recv`, `send`
    * C library utility functions: `gethostbyname`, `getservbyname`
    * Datagram coding: `socket`, `bind`, `connect`, `recvfrom`, `sendto`
    * Socket options, especially DSCP/TOS using `IP_TOS`
    * Out of band data
    * Using the command line `tc` to handle priorities
* Various command line tools that control networking
    * Information tools: `/proc/[pid]/fd`, `netstat`, `ip`, `ss`
    * Low level tools: `ethtool`, `mii-tool`, `arp`
    * Configuration tools: `ifconfig`, `ip`, `ifup`/`ifdown`, `route`, `iwconfig`, `iwlist`, `iwpriv`
    * performance tools: `jnettop`, `netperf`, `lnstat` `rtmon` `rtstat` `nstat` `rtacct` `routef` `routel` `ctstat`
    * Tapping tools: `nc`, `netcat`, `tcpdump`, `wireshark`
    * Quality control: `tc`
    * Debugging tools: `telnet`, `ping`, `traceroute`, `nmap`
* `Linux` module primer
    * Module initialization
    * Module cleanup
    * Compiling a kernel module
    * Kernel logging
* Network Device overview
    * `sk_buff`
    * The `net_device` structure
    * Registering a network driver
    * Network driver private data
    * Network device operations: `ndo_open`, `ndo_stop`, `start_xmit`
    * Handling interrupts, mitigating large number of interrupts
    * Memory mapping
* `TCP`/IP Firewall
    * What is a firewall?
    * What is IP filtering?
    * `Linux` and firewalling
    * IP tables
    * Testing a firewall configuration
* Net Filters
    * Implementing netfilters in user space
    * Hooking points
    * Hook functions
    * Registering a netfilter
    * Removal of netfilters
    * Implementing netfilters in kernel space
* Namespaces
    * What are namespaces
    * Types of namespaces
    * Cgroups and their relation to namespaces
    * Creating namespaces and cgroups
    * Inspecting a namespace from the outer world
    * Connecting namespaces
    * Using `net_prio` and `net_cls` to prioritize networking for containers
* eBPF Overview and Usage Optional, second priority
    * The extended Berkeley packet filter
    * cBPF vs. eBPF
    * The architecture of eBPF
    * Creating and running eBPF code
    * Off the shelf eBPF program collections
