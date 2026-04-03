---
tags:
  - infrastructure:linux
  - infrastructure:storage
  - infrastructure:filesystems
  - infrastructure:lvm
  - infrastructure:raid
  - infrastructure:nfs
  - security:encryption
level: advanced
category: operating-systems
duration_hours: 40
audience:
  - audiences:sysadmins
  - audiences:security-professionals
  - audiences:devops
---
<!-- course: advanced_linux_files_and_storage_management -->
# Advanced `Linux` Files and Storage Management

## Description
This advanced course is designed for experienced `Linux` system administrators, `DevOps` engineers, and security professionals with `solid` foundational knowledge of `Linux`. The course covers comprehensive `file` system architecture, advanced storage technologies, logical volume management, networked storage solutions, and performance optimization. Students will gain expertise in enterprise-level storage management, troubleshooting, and security practices.

## Duration
40 hours / 5 days

## Intended Audience
* Experienced `Linux` system administrators
* `DevOps` engineers
* Security professionals with `solid` foundational knowledge of `Linux`

## Prerequisites
* Strong foundational knowledge of `Linux` operating system
* Experience with basic `Linux` `file` system operations
* Understanding of storage concepts and hardware
* Familiarity with command-line tools and system administration

## Objectives
* Understand and implement advanced `Linux` `file` system architectures and concepts
* Perform complex `file` system operations including creation, management, and repair
* Configure and manage advanced storage technologies including `LVM` and `RAID`
* Set up and optimize networked and distributed storage solutions
* Monitor, tune, and troubleshoot storage performance issues
* Implement storage security measures including encryption and access controls
* Apply best practices for enterprise `Linux` storage management

## Outline
<!-- chapter: linux-file-system-architecture-and-concepts, duration: 5h -->
* `Linux` `File` System Architecture and Concepts
    * Overview of `Linux` `file` system hierarchy and standards (FHS)
    * Extended `file` attributes and access control lists (`ACLs`)
    * Understanding inodes, superblocks, and journaling
    * `File` system types and characteristics
        * `ext4`
        * `XFS`
        * `Btrfs`
        * `ZFS`
    * Mounting, unmounting, and `bind` mounts
<!-- chapter: advanced-file-system-operations, duration: 12h -->
* Advanced `File` System Operations
    * `File` system creation and management
        * mkfs
        * tune2fs
        * xfs_admin
        * zpool
    * Resizing and migrating `file` systems
        * `resize2fs`
        * `xfs_growfs`
        * `Btrfs` snapshots
    * `File` system integrity checking and repair
        * `fsck`
        * e2fsck
        * `xfs_repair`
    * Working with symbolic and hard links in complex environments
    * Advanced `file` search and manipulation
        * `find`
        * locate
        * stat
        * `lsof`
<!-- chapter: storage-technologies-and-logical-volume-management-lvm, duration: 6h -->
* Storage Technologies and Logical Volume Management (`LVM`)
    * Disk partitioning with `GPT` and MBR
        * `fdisk`
        * parted
        * gdisk
    * `RAID` concepts and implementation (mdadm)
    * `LVM` concepts: physical volumes, volume groups, logical volumes
    * Advanced `LVM` features
        * Snapshots
        * Resizing
        * Thin provisioning
    * Device mapper and multipath storage configuration
<!-- chapter: networked-and-distributed-storage, duration: 5h -->
* Networked and Distributed Storage
    * `NFS` and `SMB`/`CIFS` configuration and optimization
    * `iSCSI` target and initiator setup
    * Working with Fibre Channel storage (overview and configuration)
    * Introduction to distributed storage solutions
        * Ceph
        * GlusterFS
        * Other distributed storage solutions
    * Managing mounts with autofs and `systemd` automount
<!-- chapter: performance-security-and-troubleshooting, duration: 12h -->
* Performance, Security, and Troubleshooting
    * Monitoring `file` system and storage performance
        * iostat
        * vmstat
        * dstat
    * Tuning `file` systems and storage for performance
        * Mount options
        * sysctl
    * Disk quotas and resource limits
        * edquota
        * prlimit
    * Storage encryption and secure erasure techniques
        * LUKS
        * cryptsetup
        * Secure erasure techniques
    * Troubleshooting storage issues and recovering data
    * Review and best practices for enterprise `Linux` storage management

## References
* [`Linux` `File` System Hierarchy Standard](`https`://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.`pdf`)
* [`LVM` HOWTO](`https`://tldp.org/HOWTO/`LVM`-HOWTO/)
* [mdadm Manual](`https`://`linux`.die.net/man/8/mdadm)
* [`NFS` Documentation](`https`://`nfs`.sourceforge.net/)
* [Ceph Documentation](`https`://docs.ceph.com/)
* [GlusterFS Documentation](`https`://docs.gluster.org/)
* [LUKS Disk Encryption](`https`://`gitlab`.com/cryptsetup/cryptsetup/-/wikis/home)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
