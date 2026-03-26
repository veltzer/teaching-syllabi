---
tags:
  - networking
  - tcp-ip
  - http
  - protocols
level: beginner
category: networking
duration_days: 1
audience:
  - developers
---
# Networking Basics

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
Networking fundamentals are essential for understanding how computers communicate across networks and the internet. This course covers core networking concepts, protocols, and technologies including the `OSI` model, `TCP`/`IP` stack, `HTTP` protocols, headers, cookies, and network security basics that form the foundation of modern web applications and distributed systems.

## Duration
8 hours / 1 day

## Intended Audience
* Software developers building networked applications
* System administrators and `DevOps` engineers
* Web developers needing deeper networking knowledge
* IT support specialists and network technicians
* Students pursuing networking or computer science degrees
* Anyone working with distributed systems or cloud technologies

## Prerequisites
* Basic computer literacy and operating system familiarity
* Understanding of basic internet usage and web browsing
* Familiarity with command-line interfaces (`Windows CMD`, `Linux`/`macOS` terminal)
* Basic understanding of software applications and services
* Mathematical comfort with binary numbers and basic calculations
* No prior networking experience required
* Access to a computer with network connectivity for hands-on exercises

## Objectives
* Understand the `OSI` model and `TCP`/`IP` protocol stack layers
* Configure and troubleshoot basic network connectivity using `IP` addressing and subnetting
* Analyze `HTTP`/`HTTPS` communication including request/response cycles
* Work with `HTTP` headers, cookies, and session management mechanisms
* Understand `DNS` resolution process and domain name system architecture
* Implement and troubleshoot common network protocols (`TCP`, `UDP`, `FTP`, `SMTP`)
* Use network diagnostic tools (`ping`, `traceroute`, `netstat`, `Wireshark`)
* Apply basic network security concepts including firewalls and `VPNs`
* Understand routing, switching, and network topology concepts
* Configure basic network services and analyze network traffic patterns

## Outline
* Introduction to Computer Networking
    * What is computer networking and why it matters
    * Network types: `LAN`, `WAN`, `MAN`, `PAN`, and internet
    * Network topologies: star, bus, ring, mesh, and hybrid
    * Client-server vs peer-to-peer architectures
    * Network components: routers, switches, hubs, and access points
    * Introduction to network protocols and standards
    * Setting up network analysis tools (`Wireshark`, `curl`, browser dev tools)
* `OSI` Model and Protocol Layers
    * Seven-layer `OSI` model detailed breakdown
    * Physical layer: cables, signals, and transmission media
    * Data Link layer: `Ethernet`, `MAC` addresses, and frame structure
    * Network layer: `IP` addressing, routing, and packet forwarding
    * Transport layer: `TCP` vs `UDP` protocols and port numbers
    * Session, Presentation, and Application layers overview
    * `TCP`/`IP` model vs `OSI` model comparison
    * Encapsulation and de-encapsulation process
* `IP` Addressing and Subnetting
    * `IPv4` address structure and classes (`A`, `B`, `C`, `D`, `E`)
    * Public vs private `IP` addresses (`RFC 1918`)
    * Subnet masks and `CIDR` notation
    * Subnetting calculations and network design
    * `IPv6` addressing basics and transition mechanisms
    * `DHCP` for dynamic `IP` assignment
    * `NAT` (Network Address Translation) and `PAT` concepts
* `TCP` and `UDP` Transport Protocols
    * `TCP` connection establishment: three-way handshake
    * `TCP` features: reliability, flow control, congestion control
    * `TCP` connection termination and state management
    * `UDP` characteristics: connectionless, unreliable, fast
    * Port numbers and well-known services (`HTTP` 80, `HTTPS` 443, `SSH` 22)
    * Socket programming concepts and network sockets
    * When to use `TCP` vs `UDP` in applications
* `HTTP` Protocol Deep Dive
    * `HTTP` request/response cycle and message structure
    * `HTTP` methods: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS`
    * `HTTP` status codes: `1xx`, `2xx`, `3xx`, `4xx`, `5xx` categories
    * `HTTP` versions: `HTTP/1.0`, `HTTP/1.1`, `HTTP/2`, `HTTP/3`
    * `HTTPS` and `SSL`/`TLS` encryption overview
    * `RESTful` `API` communication patterns
    * Content negotiation and `MIME` types
* `HTTP` Headers and Request/Response Details
    * Request headers: `Host`, `User-Agent`, `Accept`, `Authorization`, `Content-Type`
    * Response headers: `Server`, `Content-Length`, `Cache-Control`, `Set-Cookie`
    * Custom headers and `X-` prefix conventions
    * Header parsing and case-insensitive handling
    * Content encoding and compression (`gzip`, `deflate`)
    * Conditional requests: `If-Modified-Since`, `ETag`
    * `CORS` headers: `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`
* Cookies and Session Management
    * Cookie fundamentals: creation, storage, and transmission
    * Cookie attributes: `Domain`, `Path`, `Expires`, `Max-Age`, `Secure`, `HttpOnly`
    * Session cookies vs persistent cookies
    * Third-party cookies and privacy implications
    * Cookie-based session management patterns
    * `SameSite` attribute for `CSRF` protection
    * Cookie alternatives: `localStorage`, `sessionStorage`, tokens
* `DNS` and Domain Name Resolution
    * `DNS` hierarchy: root servers, `TLD` servers, authoritative servers
    * `DNS` record types: `A`, `AAAA`, `CNAME`, `MX`, `TXT`, `NS`
    * `DNS` resolution process and caching mechanisms
    * `DNS` configuration and troubleshooting tools (`nslookup`, `dig`)
    * Reverse `DNS` lookups and `PTR` records
    * `DNS` security: `DNSSEC` and `DNS` over `HTTPS` (`DoH`)
    * Content Delivery Networks (`CDN`) and `DNS` optimization
* Network Diagnostic Tools and Troubleshooting
    * `ping` for connectivity testing and latency measurement
    * `traceroute`/`tracert` for path discovery and hop analysis
    * `netstat` for connection and port monitoring
    * `nmap` for network scanning and service discovery
    * `Wireshark` for packet capture and protocol analysis
    * Network monitoring and performance analysis techniques
    * Common network problems and systematic troubleshooting approaches
