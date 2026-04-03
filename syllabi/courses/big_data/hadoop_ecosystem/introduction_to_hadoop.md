---
tags:
  - tools:hadoop
  - data-and-ai:big-data
  - data-and-ai:hdfs
  - data-and-ai:mapreduce
level: beginner
category: big-data
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-engineers
  - audiences:sysadmins
---
<!-- course: introduction_to_hadoop -->
# Introduction to `Hadoop`

## Description
`Apache Hadoop` is the foundational framework for distributed storage and processing of large datasets across clusters of commodity hardware. This course introduces the core components of the `Hadoop` ecosystem including `HDFS`, `YARN`, and `MapReduce`, along with an overview of the broader ecosystem tools. Students will understand how `Hadoop` solves big data challenges and gain hands-on experience with cluster setup and basic data processing.

## Duration
16 hours / 2 days

## Intended Audience
* Developers entering the big data field
* Data engineers looking to understand `Hadoop` fundamentals
* System administrators managing or planning `Hadoop` clusters

## Prerequisites
* Basic `Linux` command-line skills
* Familiarity with any programming language

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand big data concepts and the challenges `Hadoop` addresses
* Describe `HDFS` architecture and data storage mechanisms
* Explain the `YARN` resource management framework
* Write and run basic `MapReduce` programs
* Identify the role of key `Hadoop` ecosystem components
* Set up a basic `Hadoop` cluster

## Outline
<!-- chapter: big-data-fundamentals, duration: 2h -->
* Big Data Fundamentals
    * What is big data (volume, velocity, variety, veracity)
    * Challenges of traditional data processing
    * Distributed computing concepts
    * History and evolution of `Hadoop`
    * `Hadoop` distributions (`Apache`, Cloudera, Hortonworks)
<!-- chapter: hdfs-hadoop-distributed-file-system, duration: 3h -->
* `HDFS` (`Hadoop` Distributed `File` System)
    * `HDFS` architecture overview
    * NameNode and its responsibilities
    * DataNode and block storage
    * Data replication and fault tolerance
    * Rack awareness
    * `HDFS` command-line interface
    * `File` read and write operations
    * NameNode high availability
    * Secondary NameNode vs standby NameNode
<!-- chapter: yarn-yet-another-resource-negotiator, duration: 3h -->
* `YARN` (Yet Another Resource Negotiator)
    * `YARN` architecture
    * ResourceManager components
    * NodeManager responsibilities
    * Application lifecycle
    * Container allocation
    * Capacity scheduler and fair scheduler
    * `YARN` command-line tools
<!-- chapter: mapreduce-programming-model, duration: 3h -->
* `MapReduce` Programming Model
    * `MapReduce` concepts and data flow
    * Map phase
    * Shuffle and sort phase
    * Reduce phase
    * Combiners and partitioners
    * Input and output formats
    * Writing a `MapReduce` program in `Java`
    * `Hadoop` Streaming for `Python` and other languages
    * Counters and job monitoring
<!-- chapter: hadoop-ecosystem-overview, duration: 3h -->
* `Hadoop` Ecosystem Overview
    * `Hive` (`SQL`-on-`Hadoop`)
    * `Pig` (data flow scripting)
    * `HBase` (`NoSQL` column-family store)
    * `Sqoop` (relational database import/export)
    * `Flume` (log and event data collection)
    * `Oozie` (workflow scheduling)
    * `ZooKeeper` (coordination service)
<!-- chapter: cluster-setup-and-administration-basics, duration: 2h -->
* Cluster Setup and Administration Basics
    * Single-node and pseudo-distributed setup
    * Multi-node cluster planning
    * Configuration files (core-site.`xml`, `hdfs`-site.`xml`, `yarn`-site.`xml`, mapred-site.`xml`)
    * Starting and stopping services
    * Web UIs for monitoring
    * Basic troubleshooting

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
