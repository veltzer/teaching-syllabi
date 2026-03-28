---
tags:
  - infrastructure:linux
  - infrastructure:unix
  - languages:shell
  - practices:command-line
  - audiences:sysadmin
level: beginner
category: operating-systems
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - practices:devops
---
# `Linux` fundamentals

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course is about the `Linux` as a `UNIX` operating systems structure. It deals with how the system
is build together, from what components, how basic security works etc. Because this subject
is very theoretical, and because in practice people who deal with `UNIX` need knowledge of
the command line, this course also introduces the shell interface to the `UNIX` system and
teaches how to use this command line effectively. This command line knowledge enables
both day to day working with the system and to better explore and understand in practice
the theoretical aspects of the underlying operating system.

This course is not a development course. It does not deal with the `C`/`C++` programming `APIs`. Just with the command line.
If you are in need of such a course consider some `UNIX` (systems) programming course. Take note that such a course is
usually better undertaken with the knowledge of this course already internalized.

## Duration
24 hours / 3 days

## Intended Audience
* people who are new to working with the `UNIX` operating system.
* people who want to find their way around the command line.
* programmers who are unfamiliar with the basics of `UNIX` or the command line.
* quality assurance, monitoring, profiling and debugging people who want to familiarize themselves with `UNIX` and it's command line usage.
* anyone interested in fundamentals of the `UNIX` operating system.

## Prerequisites
* No special requirements for this course.

## Objectives
* understand the core concepts and principles of Linux` fundamentals
* gain practical knowledge of Introduction to `UNIX
* gain practical knowledge of The basics
* gain practical knowledge of File system

## Outline
* Introduction to `UNIX`
    * What is `UNIX`
    * History of `UNIX`
    * Operating system core structure
    * The process tree
        * Why is it important?
        * Adoption by init
        * Zombies
    * What are system calls?
    * Basic security
        * file system security
        * processes as separate boxes
    * The root user
        * Not different from regular user
        * System calls do not get refused
* The basics
    * Logging in/out
    * Changing your password
    * Command structure
    * Simple commands
    * Control characters
* File system
    * Basic structure
    * Paths (relative and absolute)
    * Home directories
    * Moving around commands (cd, PWD, pushd, popd)
* Shells
    * Why a shell?
    * The two main families of shells (csh/tcsh, sh/ksh/bash)
    * defining shell variables (csh/tcsh and sh/ksh/bash).
    * exporting as environment variables (csh/tcsh and sh/ksh/bash).
    * command line substitution (csh/tcsh and sh/ksh/bash).
    * glob patterns on the command line (csh/tcsh and sh/ksh/bash).
    * redirection of input, output and errors. (csh/tcsh and sh/ksh/bash).
    * aliases (csh/tcsh and sh/ksh/bash).
    * pipes (csh/tcsh and sh/ksh/bash).
    * command history (csh/tcsh and sh/ksh/bash).
    * session initialization files (csh/tcsh and sh/ksh/bash)
* Manipulating files, folders, and whole disks
    * `ls`
    * `cat, more`
    * `head, tail`
    * `tee`
    * `wc, diff`
    * `touch`
    * `mkdir, rmdir`
    * `mv, cp`
    * `df, du`
    * `tr, cut`
    * `uniq, sort`
    * `xargs, find`
    * `grep`
    * `sed, awk`
    * What are power tools good for?
    * Exercise with power tools.
* Files in details
    * File types in `UNIX` (all 7 types).
    * The INODE concept
    * ls and INODES
    * Symbolic links (ln -s)
    * Hard links (ln)
* Security in practice
    * `UNIX` accounts.
    * The `/etc/passwd` and `/etc/shadow` files.
    * File ownership.
    * Directory and file access modes.
    * How File and Directory access is determined.
    * Changing modes and ownership (`chmod`, `chown`) in symbolic and octal forms.
    * `umask`
The `vi` text editor
    * Introduction to `vi`
    * The `vi` command
    * `vi` modes
    * insert mode
    * moving around
    * command mode
    * command commands
    * search and replace
* Process management
    * The ps command
    * Finding the pid of a process
    * Sending a signal to a process (kill).
    * Monitoring processes with top.
    * Dealing with zombies in practice.
    * The shell and jobs.
* Networking basics
    * The client/server model.
    * `ifconfig`, `ifup`, `ifdown`
    * `netstat`, `ssh`
    * `telnet`, `rlogin`, `rcp`, `rsh`, `trust`
* Shell scripting introduction (in sh/ksh/bash family of shells)
    * Writing your first shell script
    * Variables
    * Command line arguments
    * Mathematical operations
    * Exit status and error handling
    * Expressions, operators and conditions
    * Flow control (test, if, elif, case)
    * Loops (for while until)
* The `Linux` boot system (`systemd`)
    How the `Linux` system boots
    * old `SysV` init system
    * new `systemd`
    * `rc.local` and adding your own initialization code
    * writing your own `/etc/init.d` script

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
