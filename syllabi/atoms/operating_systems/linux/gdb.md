---
tags:
  - linux
  - gdb
  - debugging
  - c
  - c++
  - toolchain
level: intermediate
category: operating-systems
duration_days: 2
audience:
  - developers
---
# Gdb

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course is intended for `C`/`C++` developers who wish to learn how to better
use the `Linux` `gdb` debugger and get better at debugging in general.

## Duration
16 hours / 2 days

## Outline
* definitions
* `gdb` intro
* the toolchain and its tools
    * `GCC`
    * `ld`
    * `gas`
    * `readelf`
    * `nm`
    * `ldd`
    * `objcopy`
    * `objdump`
    * `LD_LIBRARY_PATH`
    * `dlopen`
    * `ar`
    * `ranlib`
    * `strip`
    * `gcore`
    * customizing core file names
* debug information problems
    * different debug information types
    * the problem of size
    * C++ templates and their problems
    * ways of solving the issues
* dynamic libraries
    * how do they work? `PLT`, `GOT`
    * versions
    * the dynamic library cache (ldconfig)
* static libraries
    * how do they work? `ar(1)`
    * speed and link time
* c++ name mangling
    * `c++filt`
    * mangling in your code
* `gdb`
    * running and stepping
    * listing and ordering your files
    * breakpoints (software and hardware)
    * remote debugging + debugging agent
    * remote debugging in eclipse
    * scripting
    * viewing variables
    * changing variables
    * calling functions
    * viewing memory
    * viewing registers
    * multi-thread debugging
    * handling core files
* GUI programs for `gdb`
    * `gdbtui`
    * `xxgdb`
    * eclipse+CDT

## Copyright
Mark Veltzer, © 2026
