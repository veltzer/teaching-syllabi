---
tags:
  - infrastructure:android
  - hardware-and-embedded:ndk
  - tools:jni
  - infrastructure:kernel
  - hardware-and-embedded:embedded
level: advanced
category: operating-systems
duration_hours: 16
audience:
  - audiences:developers
  - audiences:embedded-engineers
---
# `Android` Advanced

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course provides an in-depth exploration of the `Android` platform across all its layers: the `Java` SDK layer, the native NDK layer, and the `Linux` kernel layer. Participants will learn to develop and deliver applications at each layer, use `JNI` to bridge `Java` and native code, write kernel modules, and understand the `Android` boot process and power management framework.

## Duration
16 hours / 2 days

## Intended Audience
* mobile application developers
* software engineers interested in Android development

## Prerequisites
* working experience with android`
* experience with Java programming
* familiarity with object-oriented programming

## Objectives
* understand the core concepts and principles of Android` Advanced
* gain practical knowledge of Android` platform overview
* gain practical knowledge of Exploring your `Android` device
* gain practical knowledge of The `Java` layer (basics): assumes knowledge of `Java

## Outline
* `Android` platform overview
    * The `Java` layer (`SDK`).
    * The native layer (NDK).
    * The kernel layer (`Linux` basically).
    * The power management framework.
    * Building the platform.
* Exploring your `Android` device
    * remote login and ssh.
    * ssh tunneling on android.
    * gaining root on the device for fun and profit.
    * changing stuff and rebooting (watch out!).
* The `Java` layer (basics): assumes knowledge of `Java`
    * overview
    * Activities
    * Services
    * Broadcast Receiver
    * Content Provider
    * Intents and Permissions
    * Context
    * developing `Java` applications (tools).
    * delivering `Java` applications (tools).
    * Power management `APIs`.
    * exercise: writing a `Java` application and delivering it.
* The `Java` layer (advanced)
    * Interprocess communication mechanisms.
        * the android.os package.
        * ConditionVariable
        * Debug
        * FileObserver
        * DropBoxManager
        * Looper
        * MemoryFile
        * MessageQueue
        * Parcel
        * Process
        * RecoverySystem
        * PowerManager
    * managing threads in the `Java` layer.
    * managing data storage.
        * files.
        * database like.
* `JNI` (interlude): assumes knowledge of `Linux` native development
    * how to write `JNI` code
        * manually
        * using native access libraries
        * using swig
    * converting arguments
    * local and global references.
    * memory management
    * accessing classes, methods and more and caching them.
    * locking and unlocking.
    * handling exceptions from `Java` code called.
    * throwing exceptions from the `JNI` layer.
    * encoding and internationalization.
    * issues with creating native threads.
    * coding in C++.
    * exercise: writing a program in `Java` that uses your own `JNI` code.
* The NDK (basics)
    * developing and delivering native applications.
        * the .mk files
    * exercise: creating a native library.
    * exercise: creating a native executable.
    * exercise: creating a native android activity.
    * exercise: creating a native android service.
* The NDK (advanced)
    * list of `APIs` of the NDK.
    * list of libraries usually found on android devices.
        * bionic libc.
            * differences from gnu libc.
            * properties
            * logging.
        * webkit
        * media libraries.
            * adding codecs in software.
            * adding codecs in hardware.
        * SQLite.
        * surface flinger.
        * audio flinger.
        * OpenGL ES for 2d and 3d.
        * hardware abstraction libraries.
        * exercises
            * writing a native application playing sound.
            * writing a new device driver in user space (hardware abstraction layer exercise).
            * writing a native application that uses wakelocks.
    * services (applications running) usually found on android devices.
    * debugging native applications.
    * checking CPU and features at runtime.
    * security, users, files, layout and permissions.
    * interprocess communication mechanisms.
* The android kernel: assumes knowledge of the `Linux` kernel
    * difference between android and stock `Linux` kernel.
        * alarm.
        * `ashmem` (shared memory driver).
        * IPC binder.
        * power management.
        * low memory killer.
        * kernel debugger.
        * logger.
* Writing kernel modules for android
    * how to setup a development environment.
    * writing and running your first android kernel module.
    * exercise: writing and running your first android kernel module.
    * writing framebuffer modules.
    * writing audio modules.
    * writing keyboard modules.
    * writing sensor modules.
    * power management in kernel modules
        * wakelocks.
        * responding to power management events.
* The boot process
    * a description of the boot process.
    * adding your own service to the android init process.
    * exercise: writing your own native service and adding it to the android platform.

## Notes
* I am not sure that all of these topics are necessary. Remove any you do not really need.
I think that you guys will be most interested in the HAL layer but I really don't know.
* The course has 3 parts: `Java`, native and kernel each with it's own pre-requisites.
* The overall purpose of this course is: To provide the participants, who are kernel and
user space C programmers, with intimate knowledge of the various layers of the android
platform. Participants will code modules for the android kernel, write native code in
user space that uses those modules, and write `Java` applications that uses the user space
code.
* This is not a final result but rather a result of a few days research and my own
personal knowledge. Some topics I already know and some I will have to research and
write the materials for. The topics themselves are, however, relevant. They may be
too specific at times since I really don't know what the client is after.
* I also do not have a time estimate for this course: nor for the time it will take me
to develop all of the materials nor for how long it would take to deliver such a course.
I will have a better estimate once I start actually building the exercises and writing the
missing slides.
* I am also not sure of the depth that we should cover each topic in. If all topics are
covered in great depth then this could be a very long course indeed. Maybe drop some
of the exercises? Maybe some topics should only be overview ? The subject is huge.
* In the beginning I though about doing this course in "reverse" to what you are seeing
in this document. First do the kernel and have people code some module in it.
Then using that code from a user space native application or android native service and
then finally writing a UI on top of that in `Java`. The problem with this approach is that
the students will not "see" results till the last stage and that is also why I think I
will stick with this structure instead of the reverse: students will code an application with
UI (very easy at first). Then they will code native libraries which they will use from
the previous application. And finally they will write a kernel module which will be
used from the native library (and therefor from the UI application).

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
