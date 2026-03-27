---
tags:
  - linux
  - sysadmin
  - storage
  - networking
  - security
  - monitoring
level: intermediate
category: operating-systems
duration_days: 5
audience:
  - sysadmins
  - devops
---
# `Linux` System Administration

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This intensive course covers essential `Linux` system administration concepts and practices. Students will learn to manage, secure, and maintain `Linux` systems in production environments. The course focuses on practical skills required for professional system administration.

## Duration
40 hours / 5 days

## Intended Audience
* System administrators who need to manage `Linux` systems in production environments
* `DevOps` engineers who need solid `Linux` administration skills
* IT professionals transitioning to `Linux`-based infrastructure

## Prerequisites
* Basic `Linux` command line experience
* Familiarity with basic text editors (vim/nano)
* Understanding of basic networking concepts

## Objectives
* Manage `Linux` system architecture, boot process, and package management
* Configure and maintain storage, filesystems, and backup solutions
* Implement user management, access controls, and system hardening
* Set up and administer network services and firewalls
* Monitor system performance, troubleshoot issues, and plan disaster recovery

## Exercises
* Done on `Ubuntu` 24.04 machines, real or virtual.

## Outline
* Core System Architecture
    * `Linux` filesystem hierarchy standard (FHS)
    * The `/usr` and `/var` hierarchies
    * System boot process
        * BIOS vs UEFI
        * `GRUB2` bootloader and recovery
        * `initramfs`
        * Boot troubleshooting (rescue and emergency mode)
    * `systemd` in depth
        * Unit files and unit types
        * Service types and advanced directives
        * `systemctl` usage (basic and advanced)
        * `systemd` targets (runlevels)
        * `systemd` timers and calendar expressions
        * `journalctl` and the journal
        * Journal persistence configuration
        * Socket activation
        * `systemd-tmpfiles`, `systemd-sysusers`, `systemd-networkd`
    * Control groups (`cgroups`) and resource control
    * Understanding `/proc` and `/sys` filesystems
    * Kernel tuning with `sysctl` and `/proc/sys`
        * Kernel parameters for production
    * Kernel modules and `udev` device management
    * Kernel version management and crash dumps (`kdump`)
    * Device mapper overview
    * Managing shared libraries and dependencies
    * Understanding load average
    * File descriptors and limits
    * Locale and timezone configuration
* Package Management Deep Dive
    * Package management ecosystem (`apt`/`dpkg` vs `dnf`/`rpm`)
    * `dpkg`: low-level package tool
        * Package states and troubleshooting
        * `dpkg` triggers
        * Debian package internals
    * `apt`: high-level package tool
        * Install options and upgrade strategies
        * `apt-mark` for managing package state
        * `apt-cache` for querying package information
        * `apt-file` for finding files in packages
        * Transaction simulation
    * `dnf`/`yum` and `rpm` (RHEL/Fedora)
    * `apt` vs `dnf` comparison
    * Repository management and configuration
        * Adding third-party repositories
        * Repository pinning and priorities
    * Creating and managing custom repositories
        * Hosting repositories with a web server
    * `apt` caching proxy (`apt-cacher-ng`)
    * Managing software from source code
        * Building `.deb` packages
        * Package scripts (pre/post install/remove)
    * Package verification and security
    * Dependency resolution and troubleshooting
    * Virtual packages and essential packages
    * Package lifecycle
    * Package downgrade procedures
    * Package changelog and history
    * `apt` proxy and offline install (`apt-offline`)
    * Package management automation
    * Unattended upgrades for security patches
    * Comparing package versions across systems
    * `Snap` and `Flatpak`
    * Package management best practices
    * Troubleshooting package issues
* Storage Management and File Systems
    * Storage device management and block devices
    * `SMART` disk monitoring
    * Partitioning and filesystem creation
        * Partition alignment and best practices
        * Filesystem types comparison (`ext4`, `XFS`, `Btrfs`, `ZFS`)
        * `ext4` tuning options
    * Mounting filesystems and `/etc/fstab`
        * Advanced mount options
        * Mount troubleshooting
    * Swap space management
    * Filesystem quotas
    * Disk monitoring and maintenance
        * Finding disk space hogs
        * Disk I/O scheduling
        * `fstrim` for SSD maintenance
    * Backup strategies and tools (`rsync`, `tar`, `borgbackup`, snapshots)
    * `NFS` and `Samba` shared filesystems
    * Filesystem integrity and recovery
    * `Btrfs` filesystem and snapshots
    * Disk encryption with `LUKS`
    * Automounting with `autofs`
    * Loop devices
    * Multipath I/O
    * Storage planning for production
    * `iSCSI` overview
    * Disk cloning with `dd`
    * Disk performance benchmarking (`fio`, `hdparm`)
    * `ZFS` on `Linux` overview
    * Storage monitoring scripts
    * Logical vs physical sector size
* User Management and System Security
    * Advanced user and group management
        * Understanding `/etc/passwd` and `/etc/shadow`
        * Password policies and hash algorithms
        * Special user accounts
    * `Linux` permission model and `umask`
    * Access Control Lists (ACLs)
    * PAM (Pluggable Authentication Modules)
        * Common PAM modules
        * Login restrictions
        * Two-factor authentication with PAM
    * `sudo` configuration (basic and advanced)
    * `SSH` in depth
        * Key types and best practices
        * `SSH` config files (basic and advanced)
        * Tunneling and jump hosts
        * `SSH` hardening
        * `SSH` certificates
    * System hardening techniques
        * `fail2ban`
        * File integrity monitoring (`AIDE`/`Tripwire`)
        * Kernel hardening with `sysctl`
        * Immutable and append-only files (`chattr`)
        * `systemd` service security features
    * Security auditing tools (`auditd`)
    * Certificate management and Let's Encrypt
    * System logging and security monitoring
    * LDAP/NSS overview and `sssd` client
    * `nscd` name service cache
    * CIS benchmarks and security scanning (`Lynis`)
    * Chroot jails
    * `Linux` file capabilities
    * Restricted shells
    * `ulimits` deep dive
    * Console access control (`/etc/securetty`)
    * `SELinux` quick overview for `Ubuntu`
    * Security incident response
    * Security compliance frameworks (CIS, STIG, PCI-DSS)
* Network Services and Configuration
    * Network interface configuration
        * The `ip` command in depth
        * Network interface naming schemes
        * Network bonding and VLANs
    * `Netplan` (`Ubuntu`)
    * Name resolution (`/etc/hosts`, `/etc/resolv.conf`, `nsswitch.conf`)
        * `systemd-resolved`
        * DNS client troubleshooting
    * `DHCP` server configuration
    * Time synchronization (`chrony`/`NTP`)
    * Firewall configuration (`nftables`/`iptables`)
        * NAT and port forwarding
        * Firewall logging and debugging
    * Network monitoring tools (`ss`, `tcpdump`, `nmap`)
    * Network diagnostics and troubleshooting methodology
        * ARP and neighbor discovery
        * Packet loss troubleshooting
    * `SSL`/`TLS` configuration and testing
    * Virtual private networks (`WireGuard`, `OpenVPN`)
    * IPv6 configuration
    * Network namespaces and bridge networking
    * Traffic shaping with `tc`
    * Proxy configuration
    * `iproute2` advanced usage
    * `NetworkManager` vs `systemd-networkd`
    * Network boot (PXE) and Wake-on-LAN
    * `ethtool` for NIC diagnostics
    * Network performance testing (`iperf3`)
    * VXLAN overlay networks
    * `keepalived` for high availability
    * Network configuration backup and restore
    * Legacy networking (`/etc/network/interfaces`)
    * Wireless networking basics
* System Monitoring and Maintenance
    * Performance monitoring tools (`top`/`htop`, `vmstat`, `iostat`, `sar`, `dstat`, `perf`)
        * Understanding `top` output and load average
        * `sar` historical data
        * Memory analysis in depth (`/proc/meminfo`)
        * CPU analysis tools
    * Troubleshooting tools (`strace`, `lsof`, `dmesg`)
    * `BPF`/`bpftrace` and BCC tools
    * Process accounting
    * Log management and rotation (`journalctl`, `logrotate`, `rsyslog`)
        * Centralized logging
    * Automated monitoring solutions (`Prometheus`, `Grafana`, `Nagios`/`Zabbix`)
        * `Prometheus` configuration and alert rules
        * `Grafana` dashboards
    * `collectd` and `Netdata`
    * Scheduled tasks (`crontab`, `at`, `systemd` timers)
    * Disaster recovery planning
    * Incident response
    * System updates and patches
        * Unattended upgrades
    * Automation with `Ansible` (playbooks, roles, ad-hoc commands)
    * `systemd` service watchdogs
    * Kernel live patching
    * Configuration drift detection (`etckeeper`, `debsums`)
    * `/proc/diskstats` explained
    * Capacity planning
    * Change management workflow
    * Best practices for production environments
* Network Services (`nginx`, `Apache`, `HAProxy`, `Postfix`) (optional)
    * Web server administration with `nginx`
        * Configuration structure and reverse proxy
        * SSL, performance, and security headers
        * Logging, debugging, and worker tuning
        * Reverse proxy for `WebSocket`
    * Web server administration with `Apache`
        * SSL and reverse proxy
        * MPM models
        * `.htaccess` configuration
    * Load balancer setup with `HAProxy`
        * SSL termination and algorithms
        * ACLs, routing, and health checks
        * Stick tables
    * Email server basics with `Postfix`
        * Relay and security
        * Virtual domains and aliases
    * Let's Encrypt with web servers
    * Load testing web services
* `LVM` and `RAID` (optional)
    * LVM (Logical Volume Management)
        * Physical volumes, volume groups, and logical volumes
        * Creating, extending, and reducing volumes
        * Moving data between disks
        * Snapshots
        * Thin provisioning
        * Striping and mirroring
        * LVM cache (`dm-cache`)
        * LVM on top of RAID
        * LVM best practices for virtual machines
        * LVM troubleshooting
    * RAID configuration and management (`mdadm`)
        * RAID levels (0, 1, 5, 6, 10) and selection guide
        * Creating and monitoring RAID arrays
        * RAID with spare disks
        * Recovering from disk failures
        * RAID performance tuning
        * RAID monitoring with email alerts
        * Understanding `mdadm.conf`
* `SELinux`/`AppArmor` (optional)
    * Mandatory Access Control concepts
        * DAC vs MAC comparison
    * `SELinux` modes (enforcing, permissive, disabled)
    * `SELinux` contexts, booleans, and policies
        * File context management
        * Port labeling
        * Common booleans reference
        * Building custom policy modules
    * Troubleshooting `SELinux` denials (`audit2why`, `audit2allow`)
        * Troubleshooting workflow
    * `AppArmor` profiles and modes
        * Profile structure and permission flags
        * Abstractions
        * Network rules
    * Writing and debugging `AppArmor` profiles
    * `SELinux` vs `AppArmor` comparison
    * MAC in container environments
* `DNS` Server Administration (optional)
    * `DNS` concepts and resolution process
    * `DNS` record types
    * `DNS` query tools (`dig`, `nslookup`, `host`)
    * Setting up `BIND`
        * Security options
        * Logging configuration
    * Setting up `dnsmasq`
    * Zone files and zone transfers
    * Forward and reverse lookups
    * `DNS` troubleshooting
    * `DNS` security (`DNSSEC` basics and validation)
    * `DNS` caching with `unbound`
    * Split-horizon `DNS`
    * `DNS`-based load balancing
    * `DNS` monitoring and alerting
    * Advanced `dig` usage
    * `DNS` over HTTPS and `DNS` over TLS
    * `DNS` migration strategies
* Containerization (optional)
    * Container concepts and architecture
        * Containers vs virtual machines
        * `Linux` kernel features (namespaces, `cgroups`)
    * `Docker` basics (images, containers, volumes, networks)
        * Run options and image layers
        * Network types
        * Container networking deep dive
        * Overlay storage drivers
    * Writing `Dockerfiles` and best practices
    * `Docker` Compose
    * `podman` as a rootless alternative
        * `Podman` pods
    * Container logging and health checks
    * Container debugging
    * Image scanning and security
    * Multi-architecture builds
    * Private `Docker` registry
    * Container backup strategies
    * Container resource monitoring
    * `systemd-nspawn` containers
    * Container orchestration overview
    * Container management and lifecycle
    * Container security best practices
* `Wireshark` Network Analysis (optional)
    * `Wireshark` vs `tcpdump`
    * Capturing packets
    * Capture filters (BPF syntax)
    * Display filters (basic and advanced)
    * `tshark`: command-line `Wireshark`
    * Following TCP streams
    * Statistics and analysis
    * Analyzing common issues (retransmissions, DNS, TLS)
    * Remote capture workflows
    * Coloring rules
    * IO graphs
    * Expert information
    * Decrypting TLS with pre-master secret
    * `Wireshark` profiles
    * Packet injection detection
    * Command-line one-liners
    * `mergecap` and `editcap` utilities
    * Wireless packet capture
    * Security considerations and best practices
* Maintaining `Linux` Systems in Air-Gapped Environments (optional)
    * Air-gap architecture and network design
    * Local repository management
        * Building a complete local mirror
    * Package transport mechanisms
        * Dependency resolution for offline install
    * Security patch evaluation
        * CVE monitoring
    * Update verification procedures
    * System update protocols
        * Update rollback procedures
    * Vulnerability management
        * Compliance scanning (`OpenSCAP`)
    * Documentation and emergency procedures
    * Configuration management in air-gapped environments
    * Media transfer security
    * USB device policy enforcement
    * Network diode configuration
    * Offline container registry
    * Offline `Ansible` management
    * Hardware security modules
    * Audit trail and chain of custody
    * Offline monitoring tools
    * Best practices for isolated systems

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
