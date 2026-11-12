---
title: Systems & C/C++
lead: From an operating-system kernel written at 19 to a JNI library compiled for six platform/architecture combinations and used worldwide — C and C++ where it has to be correct, portable and fast.
description: Boris Brodski — systems programmer; C/C++ since 1999, JNI (7-Zip-JBinding), cross-platform CMake builds, Python–C++ bridges, interpreters and bytecode VMs, x86 kernel work.
pitch:
  - "**Kernel to library.** Unix-like RTOS kernel in 386 assembler and C (1999); 7-Zip-JBinding, a JNI library in production since 2007."
  - "**Portable by construction.** Linux, macOS, Windows, 32/64 bit, ARM — CMake, CTest, GCC, MinGW, one test suite everywhere."
  - "**Language runtimes.** Interpreter and bytecode VM for IDScript; C ↔ script and Python ↔ C++ bridges."
  - "**Modern C++.** Template metaprogramming where it buys safety, plain C where it buys clarity."
---
## 7-Zip-JBinding

The flagship: a JNI-conformant C++ library around the 7-Zip algorithms with an archive-format-independent Java API, password-protected and multi-part archives, built for Windows, Linux and macOS in 32 and 64 bit plus ARM, with a test suite that runs on every target. Founded in 2007, maintained since, around ten thousand downloads a month on Maven Central. Heavy C++ metaprogramming inside; a simple API outside.

## Bridges and ports

A Python ↔ C++ bridge for a CAD manufacturer across several interpreter versions and architectures; a Qt application moved from Windows to Linux with a new CMake build; the C ↔ script bridge and bytecode VM of IDScript; a stdio-like encryption layer in C.

## Where it started

A Unix-like real-time kernel in 386 assembler and Watcom C in 1999 — boot, protected-mode memory management, scheduler, drivers — written to find out what an operating system is.

## What I do for clients

- Native libraries and bindings: JNI, Python extensions, C APIs.
- Cross-platform build systems and CI for C/C++.
- Porting, performance work, and the occasional rescue of a build nobody understands any more.
