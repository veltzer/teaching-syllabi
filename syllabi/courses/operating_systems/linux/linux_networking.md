---
tags:
  - linux
  - networking
  - tcp-ip
  - sockets
  - device-drivers
  - dpdk
level: advanced
category: operating-systems
duration_days: 3
audience:
  - developers
  - sysadmins
---
# `Linux` networking

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Linux` is the premiere operation system used in today's tech world and it's networking support is extensive.
There are many tasks to be done in administering and configuring `Linux` networking: setting up device drivers,
tuning them, bonding, bridging, load balancing, firewalling and much more.

This course is for those who wish to understand the `Linux` networking stack from the ground up, from C up to
administration levels.

## Duration
24 hours / 3 days

## Intended Audience
* software developers working on Linux-based systems
* system administrators and DevOps engineers

## Prerequisites
* familiarity with Linux command line and system administration

## Objectives
* understand the core concepts and principles of Linux` networking
* gain practical knowledge of Networking for programmers
* gain practical knowledge of C user level `API` for networking.
* gain practical knowledge of Command line and information about the network stack in real time

## Outline
* Networking for programmers
    * Introduction to `TCP`/IP
    * Internet Protocol (IP)
    * Transmission Control Protocol (`TCP`)
    * User Datagram Protocol (`UDP`)
    * Concepts: Router, Modem, Switch, Gateway, Server, Client, NAT, `DNS`
* C user level `API` for networking.
    * Socket types: stream sockets (`TCP`) and datagram sockets (`UDP`).
    * Writing servers
    * Writing clients
    * Controlling socket properties (queue size and more...)
    * Sending and receiving data
    * Out of band data
    * Levels of service
* Command line and information about the network stack in real time
    * Information tools
        * `/proc/[pid]/fd`
        * `netstat`
        * `ip`
        * `ss`
    * Low level tools
        * `ethtool`
        * `mii-tool`
        * `arp`
    * Configuration tools
        * `ifconfig`
        * `ip`
        * `ifup`/`ifdown`
        * Persistent interface configuration.
        * `route`
        * `iwconfig`, `iwlist`, `iwpriv`
    * performance tools:
        * `jnettop`
        * `netperf`
        * `lnstat` `rtmon` `rtstat` `nstat` `rtacct` `routef` `routel` `ctstat`
    * Tapping tools
        * `nc`
        * `netcat`
        * `tcpdump`
        * `wireshark`
    * Debugging tools:
        * `telnet`
        * `ping` (and why it's not SUID, `getcap`)
        * `traceroute`
        * `nmap`
* More advanced configurations
    * Bonding
    * Load balancing.
    * Bridging.
* Routing
    * how to see the current routing table.
    * `route(1)`
    * `cat /proc/net/route`
    * Modifying and persisting the routing table
* Protocols support in the kernel.
    * How to see which protocols are supported?
    * How to add a protocol?
    * Protocols in the kernel are independent of the modules of transport.
* Kernel handling of packets
    * where are network packets caught? how are they handled?
    * load balancing of packet handling.
    * affinity between kernel code that handles the packets and the process that consumes them.
* the network device driver.
    * how are device drivers in the kernel written?
    * how are they named?
    * giving persistent names to certain devices.
* handling networking in user space
    * `netfilter`
    * `libpcap`
    * `DPDK`
    * `AF_PACKET`
    * `netmap`
    * `PF_RING`
    * `XDP`
    * `TUNTAP`
    * raw sockets.

## References
* [ku-latency](http://vilimpoc.org/research/ku-latency/)
* [vj_channels](http://vger.kernel.org/~davem/cgi-bin/blog.cgi/2006/01/27#vj_channels)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
