---
tags:
  - security:penetration-testing
  - security:network-security
  - security:offensive
level: advanced
category: security
duration_hours: 32
audience:
  - audiences:security-engineers
  - audiences:penetration-testers
---
<!-- course: network_penetration_testing -->
# Network Penetration Testing

## Description
Network penetration testing is the practice of systematically probing an organization's network infrastructure to discover and exploit vulnerabilities before malicious actors do. This intensive course covers the full penetration testing lifecycle from scoping and reconnaissance through exploitation, post-exploitation, and professional report writing, using the same tools and techniques employed by professional red teams. Participants will gain practical skills with industry-standard tools including `Metasploit`, Nmap, `Nessus`, Wireshark, and `Aircrack-ng`, working through realistic lab scenarios that mirror real-world network environments. The course places equal emphasis on technical execution and the legal, ethical, and methodological rigor required of professional penetration testers.

## Duration
32 hours / 4 days

## Intended Audience
* Security engineers transitioning into offensive security roles
* Professional and aspiring penetration testers seeking structured training
* Red team members expanding their network exploitation skill set

## Prerequisites
* Strong `Linux` command-line proficiency (file system, networking, process management)
* `Solid` understanding of networking protocols (```TCP``/``IP```, `UDP`, `ICMP`, `ARP`, `DNS`, `HTTP`, `SMB`)
* Familiarity with `Windows` `Active Directory` concepts (domains, users, group policy)
* Basic scripting skills (Bash, `Python`, or `PowerShell`)
* Understanding of common network services and their ports
* Prior exposure to security concepts (e.g., `CompTIA Security+` level knowledge)
* Access to a dedicated lab environment (provided or self-built with virtual machines)

## Objectives
* Apply a structured penetration testing methodology aligned with `PTES` and `OWASP Testing Guide`
* Conduct passive and active reconnaissance using `OSINT` frameworks and network scanning tools
* Perform comprehensive network enumeration with `Nmap`, `Netcat`, and service-specific tools
* Use `Nessus` and `OpenVAS` to identify and prioritize vulnerabilities in network targets
* Exploit vulnerabilities against `Windows` and `Linux` targets using `Metasploit Framework`
* Execute password attacks using `Hashcat`, `John the Ripper`, and credential stuffing techniques
* Perform `ARP` poisoning, `SSL` stripping, and other man-in-the-middle attack techniques
* Attack common wireless network configurations using `Aircrack-ng` and `Wifite`
* Pivot through network segments using tunneling and port-forwarding techniques
* Establish post-exploitation persistence and perform privilege escalation
* Produce professional penetration testing reports suitable for executive and technical audiences
* Operate within legal and ethical boundaries, understanding scope, authorization, and liability

## Outline
<!-- chapter: penetration-testing-methodology, duration: 2h -->
* Penetration Testing Methodology
    * Penetration testing vs vulnerability assessment vs red teaming
    * The Penetration Testing Execution Standard (`PTES`) phases
    * Rules of engagement: scope definition, authorization, and legal agreements
    * Types of engagement: black box, grey box, and white box testing
    * Lab environment setup: `Kali Linux`, `Parrot OS`, virtual machines, and network simulation
    * Note-taking, evidence collection, and chain-of-custody practices
    * Overview of the kill chain and `MITRE ATT&CK` framework for network attacks

<!-- chapter: reconnaissance-and-osint, duration: 3h -->
* Reconnaissance and `OSINT`
    * Passive vs active reconnaissance: risks and use cases
    * `OSINT` framework: sources, tools, and structured intelligence gathering
    * `DNS` reconnaissance: dig, `nslookup`, `dnsrecon`, zone transfers
    * `WHOIS`, `ARIN`, and network ownership investigation
    * `Shodan`, `Censys`, and `Fofa` for internet-facing asset discovery
    * `Google` dorking and advanced search operators
    * Email harvesting with `theHarvester` and `Hunter.io`
    * Social engineering target profiling and `LinkedIn` `OSINT`
    * Compiling a target profile and attack surface map

<!-- chapter: network-scanning-and-enumeration, duration: 3h -->
* Network Scanning and Enumeration
    * Host discovery: `ARP` scanning, `ICMP` probing, and `TCP`/`UDP` ping sweeps with `Nmap`
    * `Nmap` port scanning techniques: SYN, `TCP`, `UDP`, FIN, XMAS, and `NULL` scans
    * Service version detection and `OS` fingerprinting with `Nmap`
    * `NSE` (`Nmap` Scripting Engine): enumeration and vulnerability detection scripts
    * `SMB` enumeration: enum4linux, smbclient, `CrackMapExec`
    * `SNMP` enumeration and community string exploitation
    * `LDAP` and `Active Directory` enumeration with ldapsearch and `BloodHound`
    * `NFS`, `FTP`, `SSH`, RDP, and `VNC` service enumeration
    * Building a network topology map from scan results

<!-- chapter: vulnerability-scanning-with-nessus-and-openvas, duration: 2h -->
* Vulnerability Scanning with `Nessus` and `OpenVAS`
    * How vulnerability scanners work: plugin-based and signature-based detection
    * `Nessus Essentials` setup, policy configuration, and scan execution
    * `OpenVAS` (`Greenbone`) setup and scan management
    * Interpreting `CVSS` scores and prioritizing findings by exploitability and impact
    * Authenticated vs unauthenticated scanning: differences in coverage
    * Reducing false positives: manual validation of scanner findings
    * Correlating scanner output with `Metasploit` module availability

<!-- chapter: exploitation-frameworks-metasploit, duration: 4h -->
* Exploitation Frameworks — `Metasploit`
    * `Metasploit Framework` architecture: exploits, payloads, encoders, and auxiliaries
    * `Metasploit` console (`msfconsole`) navigation and workflow
    * Selecting and configuring exploits: `RHOSTS`, LHOST, `LPORT`, and payload options
    * Staged vs stageless payloads: `meterpreter` and shell payloads
    * Exploiting `Windows` vulnerabilities: `EternalBlue` (`MS17-010`), `PrintNightmare`
    * Exploiting `Linux` services: vulnerable `SSH`, `Samba`, web application exploits
    * `Meterpreter` post-exploitation commands: file system, process, network
    * `MSFvenom` for custom payload generation and encoding
    * Automating exploitation workflows with `resource scripts`

<!-- chapter: password-attacks-and-credential-theft, duration: 3h -->
* Password Attacks and Credential Theft
    * Password attack taxonomy: online vs offline, brute force, dictionary, rule-based
    * Wordlist generation with `CeWL`, crunch, and `SecLists`
    * `Hashcat` `GPU`-accelerated cracking: hash identification, attack modes, rules
    * `John the Ripper` for diverse hash formats and rule application
    * Credential stuffing and password spraying to avoid account lockout
    * `Windows` credential extraction: `Mimikatz`, secretsdump, `lsass` dumping
    * Pass-the-hash and pass-the-ticket attacks in `Windows` environments
    * Responder for `LLMNR`/`NBT-NS` poisoning and `NTLMv2` hash capture

<!-- chapter: man-in-the-middle-attacks, duration: 2h -->
* Man-in-the-Middle Attacks
    * `ARP` cache poisoning fundamentals and `ARP` spoofing with arpspoof and `Ettercap`
    * `Bettercap` for modern MITM attacks, `HTTP`/`HTTPS` interception
    * `SSL` stripping attacks against `HSTS`-unprotected sites
    * `DNS` spoofing and `DNS` cache poisoning
    * Capturing and analyzing intercepted traffic with `Wireshark`
    * Attacking `IPv6` networks: `SLAAC` abuse and `Router Advertisement` spoofing
    * Mitigations: `DNSSEC`, `HSTS`, DAI (Dynamic `ARP` Inspection), port security

<!-- chapter: wireless-network-attacks, duration: 3h -->
* Wireless Network Attacks
    * `802.11` protocol fundamentals: management frames, association, authentication
    * Wireless adapter setup for monitor mode and packet injection on `Kali Linux`
    * Network discovery and client enumeration with `airodump-ng`
    * `WEP` cracking with `aircrack-ng` (historical context and legacy targets)
    * `WPA2`-PSK four-way handshake capture and offline cracking
    * `PMKID` attack for agentless `WPA2` cracking
    * `WPA3` and its protections against dictionary attacks
    * Evil twin attacks and rogue access point creation with `hostapd-wpe`
    * `WPA2-Enterprise` (`802.1X`) attacks and `RADIUS` credential capture

<!-- chapter: pivoting-and-lateral-movement, duration: 3h -->
* Pivoting and Lateral Movement
    * Why pivoting matters: reaching segmented internal networks
    * `SSH` tunneling: local, remote, and dynamic port forwarding
    * `Metasploit` route pivoting and the `autoroute` module
    * `SOCKS` proxies with proxychains and `chisel`
    * `Ligolo-ng` for advanced tunnel management
    * Lateral movement techniques: `PsExec`, WMI, RDP, `SMB` shares
    * `BloodHound` and `SharpHound` for `Active Directory` attack path analysis
    * Kerberoasting and `AS-REP` roasting for service account credential theft

<!-- chapter: post-exploitation-and-persistence, duration: 3h -->
* Post-Exploitation and Persistence
    * Post-exploitation goals: data exfiltration, persistence, privilege escalation
    * Local privilege escalation on `Linux`: SUID/SGID binaries, `sudo` misconfigurations, kernel exploits
    * Local privilege escalation on `Windows`: token impersonation, unquoted service paths
    * Establishing persistence: registry run keys, scheduled tasks, `cron` jobs, `systemd` services
    * `Meterpreter` persistence modules and encrypted staging
    * Living-off-the-land techniques: abusing `LOLBins` to evade detection
    * Data staging and exfiltration methods
    * Covering tracks: log clearing, timestomping, and artifact removal

<!-- chapter: report-writing, duration: 2h -->
* Report Writing
    * Why a high-quality report is the core deliverable of a penetration test
    * Structure of a professional penetration testing report
    * Executive summary: communicating risk in business terms
    * Technical findings format: description, evidence, impact, `CVSS` score, remediation
    * Writing actionable remediation recommendations
    * Evidence capture best practices: screenshots, tool output, and reproduction steps
    * Walkthrough of sample reports and common writing pitfalls

<!-- chapter: legal-and-ethical-considerations, duration: 2h -->
* Legal and Ethical Considerations
    * Computer crime laws: `CFAA` (USA), `Computer Misuse Act` (UK), and equivalents
    * The importance of written authorization and scope agreements
    * Handling discovered sensitive data: `PII`, credentials, and confidential documents
    * Responsible disclosure vs coordinated vulnerability disclosure
    * Bug bounty programs: platforms, rules of engagement, and safe `harbor` provisions
    * Ethical dilemmas in offensive security: dual-use tools and knowledge
    * Professional certifications and codes of conduct: `CREST`, `OSCP`, `CEH`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
