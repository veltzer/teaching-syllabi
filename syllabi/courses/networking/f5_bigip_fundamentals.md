---
tags:
  - networking:http
  - networking:tcp-ip
  - networking:dns
  - networking:performance
  - networking:troubleshooting
  - architecture:load-balancing
  - architecture:caching
  - practices:sysadmin
  - security:tls
level: beginner
category: networking
duration_hours: 24
audience:
  - audiences:network-engineers
  - audiences:sysadmins
  - audiences:devops
---

<!-- course: f5_bigip_fundamentals -->
# `F5` `BIG-IP` `LTM` Fundamentals

## Description
The `F5` `BIG-IP` Local Traffic Manager (`LTM`) is the application delivery controller that sits in front of
many enterprise applications. It terminates client connections, load balances them across pools of servers,
translates addresses, offloads `TCP` and `HTTP` processing from the servers, and applies traffic policies on
the way. A data communications team that runs `BIG-IP` needs to be able to bring a device up, build the
objects that carry traffic, and tune how that traffic is handled.

This three day course gives engineers a practical foundation in `BIG-IP` `LTM` administration and traffic
processing. It starts with setting up a `BIG-IP` system from scratch: management interface, licensing,
provisioning, network, `NTP` and `DNS`. It then builds the core traffic processing objects (virtual servers,
pools and load balancing), introduces the Traffic Management Shell (`tmsh`) and the way `BIG-IP` stores and
saves its configuration, and adds health monitors so that traffic only reaches servers that can serve it.
The middle of the course covers how profiles change traffic behavior, how persistence keeps a client on the
same server, and how `BIG-IP` terminates and re-encrypts `SSL/TLS` traffic. The last part covers how `NAT`
and `SNAT` solve addressing and routing problems, how local traffic policies customize application delivery
without writing code, and how two `BIG-IP` systems are joined into a high availability pair.

The course is hands on. Every topic is practiced on lab `BIG-IP` systems with real backend servers. It is
the natural prerequisite for the `F5` `BIG-IP` Advanced iRules course.

## Duration
24 hours / 3 days

## Intended Audience
* data communications and network engineers who are starting to administer `BIG-IP` `LTM`
* system administrators responsible for applications delivered through `BIG-IP`
* `DevOps` engineers who need to understand how their traffic is load balanced and processed
* anyone who has inherited a `BIG-IP` deployment and needs to understand how it is configured

## Prerequisites
* solid understanding of `TCP/IP` networking: addressing, subnets, routing, `VLAN`s and `ARP`
* basic understanding of `HTTP`: methods, headers, status codes and cookies
* basic familiarity with `SSL/TLS` and certificates
* comfort working on a `Linux` command line is helpful. No prior `BIG-IP` experience is required

## Objectives
* set up a `BIG-IP` system: management interface, license, provisioning, network, `NTP` and `DNS`
* archive the `BIG-IP` configuration and use `F5` support resources and tools
* configure virtual servers and pools and choose a load balancing method
* view statistics and logs to verify how traffic is processed
* monitor the health of nodes and pool members with built in and custom monitors
* navigate and configure the system with `tmsh`, and manage the configuration state and files
* modify traffic behavior using `TCP`, `HTTP`, `HTTP/2`, `OneConnect`, compression, caching and stream profiles
* keep clients on the same server with cookie, source address and other persistence methods
* offload `SSL/TLS` processing with client `SSL` and server `SSL` profiles and manage certificates and keys
* use `NAT`s and `SNAT`s to solve addressing and routing problems and to avoid port exhaustion
* customize application delivery with local traffic policies
* build a high availability pair with device trust, config sync and failover

## Exercises
The course is lab driven. Each student gets two `BIG-IP` Virtual Edition systems with a set of backend web
servers, sets the first one up from the initial configuration, builds an application delivery configuration
step by step, and finally joins the second system to form a high availability pair.

## Outline
<!-- chapter: setting-up-the-big-ip-system, duration: 2h -->
* Setting up the `BIG-IP` system
    * Introducing the `BIG-IP` system
        * The `BIG-IP` platform and the traffic management microkernel (`TMM`)
        * Full proxy architecture: client side and server side connections
    * Initially setting up the `BIG-IP` system
    * Configuring the management interface
    * Activating the software license
    * Provisioning modules and resources
    * Importing a device certificate
    * Specifying `BIG-IP` platform properties
    * Configuring the network: interfaces, `VLAN`s, self `IP` addresses and routes
    * Configuring Network Time Protocol (`NTP`) servers
    * Configuring Domain Name System (`DNS`) settings
    * Archiving the `BIG-IP` configuration
    * Leveraging `F5` support resources and tools (`AskF5`, `iHealth`, `qkview`)
<!-- chapter: traffic-processing-building-blocks, duration: 3h -->
* Traffic processing building blocks
    * Identifying `BIG-IP` traffic processing objects
        * Nodes, pool members, pools and virtual servers
    * Configuring virtual servers and pools
    * Load balancing traffic
        * Static and dynamic load balancing methods
        * Priority group activation
    * Viewing module statistics and logs
    * Using the Traffic Management Shell (`tmsh`)
        * Understanding the `tmsh` hierarchical structure
        * Navigating the `tmsh` hierarchy
    * Managing `BIG-IP` configuration state and files
        * `BIG-IP` system configuration state: running and stored configuration
        * Loading and saving the system configuration
        * Shutting down and restarting the `BIG-IP` system
        * Saving and replicating configuration data (`UCS` and `SCF`)
<!-- chapter: monitoring-application-health, duration: 2h -->
* Monitoring application health
    * Why monitor: marking nodes and pool members up and down
    * Monitor types: address, service, content and performance checks
    * Built in monitors (`icmp`, `tcp`, `http`, `https`) and custom monitors
        * Send and receive strings for `HTTP` monitors
        * Interval and timeout settings
    * Assigning monitors to nodes, pools and pool members
    * Combining monitors and setting the availability requirement
    * Reading monitor status and troubleshooting a member that is marked down
<!-- chapter: modifying-traffic-behavior-with-profiles, duration: 5h -->
* Modifying traffic behavior with profiles
    * Profiles overview
        * Profile types, parent profiles and inheritance
        * Assigning profiles to a virtual server
    * `TCP` Express optimization
    * `TCP` profiles overview
    * `HTTP` profile options
    * `HTTP/2` profile options
    * `OneConnect`
    * Offloading `HTTP` compression to `BIG-IP`
    * Web acceleration profile and `HTTP` caching
    * Stream profiles
    * `F5` acceleration technologies
<!-- chapter: maintaining-session-state-with-persistence, duration: 2h -->
* Maintaining session state with persistence
    * Why applications need persistence
    * Source address affinity persistence
    * Cookie persistence: insert, rewrite, passive and hash modes
    * Other persistence methods (destination address, `SSL` session, universal)
    * Persistence and `OneConnect`
    * Fallback persistence and match across services, virtual servers and pools
    * Viewing and clearing persistence records
<!-- chapter: processing-ssl-traffic, duration: 3h -->
* Processing `SSL` traffic
    * `SSL/TLS` termination on a full proxy: offload, re-encryption and pass through
    * Managing certificates and keys on `BIG-IP`
        * Importing certificates, keys and certificate chains
        * Creating certificate signing requests
    * Client `SSL` profiles
        * Certificate, key and chain configuration
        * Protocol versions and cipher strings
    * Server `SSL` profiles and re-encrypting traffic to the servers
    * `SNI`: serving several certificates on one virtual server
    * Viewing `SSL` statistics and troubleshooting handshakes with `openssl s_client` and `tcpdump`
<!-- chapter: using-nats-and-snats, duration: 2h -->
* Using `NAT`s and `SNAT`s
    * Address translation on the `BIG-IP` system
    * Mapping `IP` addresses with `NAT`s
    * Solving routing issues with `SNAT`s
    * Configuring `SNAT` auto map on a virtual server
    * `SNAT` pools
    * Monitoring for and mitigating port exhaustion
<!-- chapter: customizing-application-delivery-with-local-traffic-policies, duration: 2h -->
* Customizing application delivery with local traffic policies
    * Getting started with local traffic policies
        * What local traffic policies can do and where they fit next to profiles and iRules
        * Draft and published policies
    * Configuring and managing policy rules
        * Conditions, actions and rule ordering
        * Matching strategies
    * Common use cases: `HTTP` to `HTTPS` redirection, `URI` based pool selection and header insertion
<!-- chapter: configuring-high-availability, duration: 3h -->
* Configuring high availability
    * High availability concepts: active-standby and active-active
    * Configuring high availability options
        * `ConfigSync`, failover and mirroring addresses
    * Establishing device trust between `BIG-IP` systems
    * Creating a sync-failover device group
    * Traffic groups and floating self `IP` addresses
    * Synchronizing the configuration between devices
    * Failover triggers: network failover, `HA` groups and `VLAN` failsafe
    * Connection and persistence mirroring
    * Testing failover and verifying that traffic keeps flowing

## Installations
Each student needs access to a lab environment with:

* Two `BIG-IP` Virtual Edition systems (trial or lab licenses) with `LTM` provisioned, access to their
management interfaces, and a network between them for the high availability chapter
* Two or more backend `HTTP` servers behind the `BIG-IP`, real or virtual, that the student can send traffic to
* A workstation with a modern browser, `curl` and `openssl`
* `SSH` access to the `BIG-IP` for `tmsh` and reading the logs

The lab environment can be provided by the training organization or built by the customer in advance.
The instructor will assist with setup on the first morning.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
