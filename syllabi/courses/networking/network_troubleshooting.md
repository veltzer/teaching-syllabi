---
tags:
  - networking:networking
  - networking:tcp-ip
  - practices:debugging
level: intermediate
category: networking
duration_hours: 16
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:developers
  - audiences:sres
---
<!-- course: network_troubleshooting -->
# Network Troubleshooting

## Description
This course teaches a systematic approach to diagnosing and resolving network issues. Participants will work through the OSI model layer by layer, learning to use industry-standard tools such as `Wireshark`, `tcpdump`, `dig`, and `openssl` to identify and fix connectivity, performance, and security-related network problems. The course also covers network monitoring solutions for proactive issue detection.

## Duration
16 hours / 2 days

## Intended Audience
* System administrators managing network infrastructure.
* `DevOps` and SRE engineers responsible for service reliability.
* Developers troubleshooting application-level network issues.

## Prerequisites
* Experience working with `Linux` or `Windows` systems in a networked environment.
* Basic understanding of command-line tools.

## Required Knowledge
* `TCP`/`IP` Deep Dive or equivalent networking knowledge

## Objectives
* Apply a systematic troubleshooting methodology to network problems.
* Diagnose issues at each layer of the OSI model.
* Capture and analyze network traffic with `Wireshark` and `tcpdump`.
* Troubleshoot `DNS`, routing, `firewall`, and `TLS`/`SSL` issues.
* Identify and resolve network performance problems.
* Configure network monitoring tools for proactive detection.

## Outline
<!-- chapter: systematic-troubleshooting-methodology, duration: 1h -->
* Systematic Troubleshooting Methodology
    * Problem identification and scoping
    * The scientific method applied to networking
    * Documentation and communication during troubleshooting
    * Escalation procedures
    * Common troubleshooting workflows
<!-- chapter: osi-layer-by-layer-diagnosis, duration: 2h -->
* OSI Layer-by-Layer Diagnosis
    * Physical layer issues (cables, interfaces, link status)
    * Data link layer (`ARP`, MAC addressing, switching)
    * Network layer (`IP` addressing, subnetting, routing)
    * Transport layer (`TCP`, `UDP`, port connectivity)
    * Application layer (`HTTP`, `DNS`, `SMTP`)
    * Mapping symptoms to OSI layers
<!-- chapter: packet-analysis-with-wireshark, duration: 2h -->
* Packet Analysis with `Wireshark`
    * Capture configuration and filters
    * Display filters and coloring rules
    * `TCP` stream analysis
    * `HTTP` and `TLS` traffic inspection
    * Protocol-specific analysis
    * Identifying anomalies in packet captures
<!-- chapter: tcpdump-filters-and-techniques, duration: 1h -->
* `tcpdump` Filters and Techniques
    * Capture syntax and BPF filters
    * Remote capture techniques
    * Saving and reading capture files
    * Performance considerations for high-traffic captures
    * Combining `tcpdump` with `Wireshark`
<!-- chapter: dns-troubleshooting, duration: 1h -->
* `DNS` Troubleshooting
    * `dig` command and query types
    * `nslookup` usage
    * `DNS` resolution chain analysis
    * Common `DNS` issues (propagation, caching, SERVFAIL)
    * `DNSSEC` validation problems
<!-- chapter: routing-issues, duration: 1h -->
* Routing Issues
    * `traceroute` and mtr
    * Routing table analysis
    * Asymmetric routing detection
    * `BGP` and default route issues
    * Policy routing problems
<!-- chapter: firewall-debugging, duration: 1h -->
* `Firewall` Debugging
    * `iptables` and `nftables` rule inspection
    * Security group and cloud `firewall` analysis
    * Connection tracking and state issues
    * Logging and tracing `firewall` decisions
    * Common `firewall` misconfigurations
<!-- chapter: mtu-problems, duration: 1h -->
* MTU Problems
    * Path MTU discovery
    * Fragmentation issues
    * MTU mismatch detection
    * Tunnel and `VPN` MTU considerations
    * `ping` with size and DF bit testing
<!-- chapter: tls-ssl-debugging, duration: 2h -->
* `TLS`/`SSL` Debugging
    * `openssl s_client` for connection testing
    * Certificate chain verification
    * `TLS` version and cipher suite negotiation
    * Common `TLS` errors and their causes
    * Certificate expiry and renewal issues
<!-- chapter: performance-issues, duration: 2h -->
* Performance Issues
    * Latency measurement and analysis
    * Packet loss detection and causes
    * Bandwidth testing with iperf
    * `TCP` window scaling and buffering
    * Network congestion identification
    * Quality of Service (QoS) considerations
<!-- chapter: network-monitoring-tools, duration: 2h -->
* Network Monitoring Tools
    * `Nagios` monitoring and alerting
    * `Zabbix` configuration and dashboards
    * `SNMP` polling and traps
    * Baseline establishment and anomaly detection
    * Integrating monitoring into incident response

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
