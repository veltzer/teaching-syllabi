---
tags:
  - practices:methodology
  - practices:build-systems
  - practices:testing
  - infrastructure:configuration-management
level: intermediate
category: methodology
duration_days: 1
audience:
  - audiences:developers
  - audiences:managers
  - audiences:testers
---
# Modern Development

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course discusses some of the leading topics of development from the experience
of professional developers: Configuration management, Build systems, Modern QA and Team leading.
It discusses when some of these tools and/or ideas help you do more and when and why they sometimes
fail.

## Duration
8 hours / 1 day

## Intended Audience
* Anyone doing development
* Programmers, QA people, team leaders, managers.

## Prerequisites
* Some development background

## Objectives
* understand the core concepts and principles of Modern Development
* gain practical knowledge of Configuration management
* gain practical knowledge of Build system
* gain practical knowledge of Modern QA

## Outline
* Configuration management
    * comparing various tools (git, ClearCase, aegis, CVS, BitKeeper, subversion).
    * the most important principles of configuration management.
    * the most common mistakes that companies do when managing configuration.
    * free commit via reviewed commit.
    * size of development team and delegation of power.
* Build system
    * comparing various tools (make, cook, cmake, SCONS, maven).
    * treating your build system as a product.
    * making it possible to deliver the build system to a client.
    * holistic build systems.
    * easy to build -> easy to live.
    * build is NECESSARY for commit.
    * TEST is NECESSARY for build.
    * all parts of the build system to be committed to configuration.
* Modern QA
    * is a separate QA team necessary ?
    * when to bring in a separate QA team ?
    * QA within the code
        * automatic testing.
        * peer and management review.
        * tools for automatic review.
        * tools for test coverage.
        * UI testing.
        * web testing.
        * ALL systems can be automatically tested.
* Team leading
    * **punishing** bad commits.
    * review.
    * deciding on technologies.
        * keeping the number of technologies down.
        * playing switch on technologies.
        * automating the insertion of new technologies.
        * agility in inserting new technologies.
    * deciding on order of commits.
    * cleaning changes.
        * how often to do them.
        * how to live with the drawbacks.
    * splitting the product.
    * sharing as much as possible between products.
    * not inventing the wheel.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
