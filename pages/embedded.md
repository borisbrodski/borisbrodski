---
title: Microcontrollers & IoT
lead: PIC microcontrollers since 1997 — assembler first, XC8 C++ later — plus Arduino, a Bluetooth LE device, and a home-grown simulator so firmware can be tested before the hardware exists.
description: Boris Brodski — microcontroller and IoT developer; PIC assembler and XC8 C++ since 1997, Arduino, Bluetooth 5.0 (Toshiba PAN1762), firmware simulation, bare-metal x86.
pitch:
  - "**Assembler native.** PIC assembler since 1997, x86 protected-mode assembler, an operating-system kernel written at 19."
  - "**C++ on small targets.** XC8 C++ firmware, Arduino, careful about every byte and every interrupt."
  - "**Radio and IoT.** A Bluetooth 5.0 device on the Toshiba PAN1762 module."
  - "**Testable firmware.** An own simulator so logic can be verified without the board."
---
## Hardware the software has to respect

Microcontrollers are where I learned that the hardware is part of the design. PIC assembler from 1997, later XC8 C++ and Arduino where it fits. The IoT project around the Toshiba PAN1762 Bluetooth 5.0 module added the radio side; the simulator I wrote for firmware testing added the discipline of verifying logic before touching the board.

The same instincts come from the other direction: the Unix-like kernel written in 386 assembler and Watcom C in 1999 — memory management, scheduler, boot drivers — and the cross-platform C++ work described under [Systems & C/C++](/systems/).

## What I do for clients

- Firmware for PIC and similar 8/16-bit targets in assembler or C++.
- Prototypes with Arduino and Bluetooth LE modules.
- Test strategies for embedded code: simulators, hardware-in-the-loop, continuous builds.
