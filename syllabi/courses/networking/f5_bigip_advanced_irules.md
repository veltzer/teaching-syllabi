---
tags:
  - networking:http
  - networking:web
  - networking:security
  - networking:troubleshooting
  - architecture:load-balancing
  - practices:scripting
  - practices:performance
  - security:web-security
level: advanced
category: networking
duration_hours: 16
audience:
  - audiences:security-engineers
  - audiences:network-engineers
  - audiences:devops
  - audiences:sysadmins
---

<!-- course: f5_bigip_advanced_irules -->
# `F5` `BIG-IP` Advanced iRules

## Description
iRules are the scripting layer of the `F5` `BIG-IP` application delivery controller. They are small `Tcl`
programs attached to a virtual server which run inside the traffic management microkernel at well defined
points of a connection's life, and they let an engineer inspect, rewrite, route, reject and log traffic in
ways that no static configuration can express. For a security infrastructure team they are the fastest way
to close a gap at the edge: block a dangerous `HTTP` method, strip a header that leaks information, add a
missing security header, or virtual patch a vulnerable application before the application team can ship a fix.

This two day course takes engineers who already administer `BIG-IP` and makes them fluent iRule authors.
It starts with the `Tcl` foundations that every iRule depends on (events, commands, variables, strings and
quoting), moves on to the `HTTP` command set used to read and manipulate requests and responses, and then
covers the two subjects that separate a working iRule from a production grade one: troubleshooting and
runtime efficiency. The last chapter applies everything to web application defense, where each mitigation
is built and tested against a real attack.

The course is hands on. Every chapter is practiced on a lab `BIG-IP` with real backend servers, and the
iRules written during the course form a small library that students can take back to their own environment.

## Duration
16 hours / 2 days

## Intended Audience
* security infrastructure engineers who own `BIG-IP` as part of the perimeter and need to respond to threats with iRules
* network engineers administering `BIG-IP` `LTM` who want to go beyond the built in profiles and policies
* `DevOps` engineers and system administrators responsible for application delivery on `BIG-IP`
* anyone who has inherited a set of iRules and has to understand, fix and improve them

## Prerequisites
* hands on experience administering `BIG-IP` `LTM`: virtual servers, pools, nodes, monitors and profiles
* solid understanding of `HTTP`: methods, headers, status codes, cookies and redirects
* familiarity with `TCP/IP` and `SSL/TLS` termination on a load balancer
* some scripting experience in any language is helpful. No prior knowledge of `Tcl` is required

## Objectives
* understand where iRules run in the `BIG-IP` traffic flow and which events fire when
* write correct `Tcl` code for iRules, including variables, operators, conditionals, loops and quoting rules
* parse and transform numbers and strings using the `Tcl` and iRule string commands
* inspect and manipulate `HTTP` headers, `URI` components, cookies and payload
* develop, test and troubleshoot iRules methodically using logging, `Fiddler`, `curl` and `tcpdump`
* measure the runtime cost of an iRule and restructure it for efficiency
* apply best practices for readable, maintainable and modular iRules
* implement iRule based mitigations for common web application attacks and harden `HTTP` responses

## Exercises
The course is lab driven. Each student gets a `BIG-IP` Virtual Edition with a set of backend web servers
and works on iRules that grow from a one line redirect to a complete web application defense rule.

## Outline
<!-- chapter: introducing-the-big-ip-system, duration: 1h -->
* Introducing the `BIG-IP` system
    * The `BIG-IP` platform and the traffic management microkernel (`TMM`)
    * Full proxy architecture: client side and server side connections
    * Virtual servers, pools, nodes, profiles and where iRules fit in
    * Initially setting up the `BIG-IP` system
    * Archiving the `BIG-IP` configuration (`UCS` and `SCF`)
    * Leveraging `F5` support resources and tools (`AskF5`, `iHealth`, `qkview`)
<!-- chapter: getting-started-with-irules, duration: 1h -->
* Getting started with iRules
    * Customizing application delivery with iRules
    * What iRules can do that profiles and local traffic policies cannot
    * Triggering an iRule: assigning iRules to a virtual server and ordering
    * Leveraging the `DevCentral` ecosystem: code share, wiki and community
    * Creating and deploying iRules from the configuration utility and from `tmsh`
    * Your first iRule: redirecting `HTTP` to `HTTPS`
<!-- chapter: exploring-irule-elements, duration: 3h -->
* Exploring iRule elements
    * Introducing iRule constructs: `Tcl` syntax as used in iRules
    * Understanding iRule events and event context
        * Client side and server side events
        * The event lifecycle of a `TCP` and an `HTTP` connection
        * Event priority and multiple iRules on one virtual server
    * Working with iRule commands
        * Query, action and utility commands
        * Command namespaces (`HTTP::`, `TCP::`, `IP::`, `SSL::`, `LB::`)
    * Logging from an iRule using `syslog-ng` (the log command)
    * Working with user defined variables
        * Local variables and their lifetime within a connection
        * Static and global variables and why to avoid them
    * Working with operators and data types
    * Working with conditional control structures (if and switch)
    * Working with looping control structures (while, for and foreach)
    * Incorporating best practices in iRules
        * Naming, comments and structure
        * Return early, fail closed
        * Keeping iRules out of the hot path when a profile will do
<!-- chapter: working-with-numbers-and-strings, duration: 2h -->
* Working with numbers and strings
    * Understanding number forms and notation
    * Arithmetic and comparison with the expr command
    * Mastering whitespace and special symbols
    * Grouping strings: braces, double quotes and substitution
    * Working with strings (the string and scan commands)
    * Combining strings (adjacent variables, the concat and append commands)
    * Using iRule string parsing functions (the findstr, getfield and substr commands)
    * Pattern matching: glob and regular expressions and the cost of each
    * Working with lists
<!-- chapter: processing-the-http-payload, duration: 3h -->
* Processing the `HTTP` payload
    * Reviewing `HTTP` headers and commands
    * Introducing iRule `HTTP` header commands
    * Accessing and manipulating `HTTP` headers (the `HTTP::header` commands)
    * Other `HTTP` commands
        * `HTTP::host`, `HTTP::method`, `HTTP::version`, `HTTP::status`
        * `HTTP::is_keepalive`
        * `HTTP::redirect` and `HTTP::respond`
        * `HTTP::uri`
    * Parsing the `HTTP` `URI` (`URI::path`, `URI::basename`, `URI::query`)
        * Decoding and normalizing the `URI` before making decisions
    * Parsing cookies with `HTTP::cookie`
    * Collecting and inspecting the request and response body (`HTTP::collect`, `HTTP::payload`)
    * Selectively compressing `HTTP` data (the `COMPRESS` command)
<!-- chapter: developing-and-troubleshooting-irules, duration: 1h -->
* Developing and troubleshooting iRules
    * Developing and troubleshooting tips
        * Reading `/var/log/ltm` and `Tcl` runtime error messages
        * Catching errors with the catch command
        * Testing in stages: log first, act later
    * Using `Fiddler` to test and troubleshoot iRules
    * Using `curl` and `tcpdump` to test and troubleshoot iRules
    * Common iRule failure modes and how to spot them
<!-- chapter: optimizing-irule-execution, duration: 2h -->
* Optimizing iRule execution
    * Understanding the need for efficiency: every iRule runs in the data plane
    * Measuring iRule runtime efficiency using timing statistics
    * Modularizing iRules for administrative efficiency
    * Using procedures to modularize code
    * Optimizing logging
    * Using high speed logging (`HSL`) commands in an iRule
    * Implementing other efficiencies
        * Data groups (the class command) instead of long switch statements
        * Preferring switch and glob matching over regular expressions
        * Avoiding unnecessary variables and string copies
        * Choosing the earliest event that has the data you need
<!-- chapter: securing-web-applications-with-irules, duration: 3h -->
* Securing web applications with iRules
    * Integrating iRules into web application defense
        * Where iRules fit next to `WAF` policies and local traffic policies
        * Virtual patching at the edge
    * Mitigating `HTTP` version attacks
    * Mitigating path traversal attacks
    * Using iRules to defend against `CSRF`
    * Mitigating `HTTP` method vulnerabilities
    * Securing `HTTP` cookies with iRules (`Secure`, `HttpOnly` and `SameSite` attributes)
    * Adding `HTTP` security headers
    * Removing undesirable `HTTP` headers
    * Building and testing a complete defense iRule against a live attack

## Installations
Each student needs access to a lab environment with:

* A `BIG-IP` Virtual Edition (trial or lab license) with `LTM` provisioned, reachable over the management
interface and with at least one virtual server that can be modified freely
* Two or more backend `HTTP` servers behind the `BIG-IP`, real or virtual, that the student can send traffic to
* A workstation with a modern browser, `Fiddler` (or another intercepting proxy) and `curl`
* `SSH` access to the `BIG-IP` for `tmsh`, `tcpdump` and reading the logs

The lab environment can be provided by the training organization or built by the customer in advance.
The instructor will assist with setup on the first morning.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
