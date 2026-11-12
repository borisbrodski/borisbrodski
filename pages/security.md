---
title: Security & AI security
lead: Twenty-eight years of asking what still holds when a component is hostile — from DOS viruses in an isolated lab to cryptographic design, reverse engineering, hardened public-sector architectures, and now the security of AI models and the agents built on them.
description: Boris Brodski — security architect with a degree focused on security and verification, cryptographic design, reverse engineering (x86, OllyDbg, Java bytecode), and current work on AI security, trojaned open-weight models and secure agent runtimes.
pitch:
  - "**Degree in security.** Diplom-Informatiker at TU Dortmund, focus area *Sicherheit und Verifikation*, grade 1.5."
  - "**Built the primitives.** Cryptographic file layer (2001), hardware-bound copy protection (2006), PKI and network security, bytecode encryption for a shipped language."
  - "**Thinks like the attacker.** Virus lab and antivirus at 18, x86 reverse engineering with OllyDbg, Java bytecode analysis and injection."
  - "**Applies it to AI.** One-hour public talk on AI security; hands-on analysis of models that phone home; Torhaus, a secure host for untrusted agents."
---
## The thread

It started in 1998 with proof-of-concept DOS viruses written in an isolated lab — to understand infection, stealth and self-modifying code — and the antivirus that caught them. The degree that followed had security and verification as its focus area. The first professional project was a transparent encryption layer for banking software; the next ones were a copy-protection scheme with hardware-bound licences and the bytecode encryption of a scripting language I had designed.

The reverse-engineering side kept pace: assembler-level debugging and x86 disassembly with OllyDbg through the 2000s, Java bytecode analysis and injection from 2010 on. Knowing how a protection is broken is the only reliable way to design one.

Since 2012 that background has been applied at scale: chief architect of a backend component for KONSENS, the software programme of Germany's tax administrations — where data protection, auditability and dozens of external interfaces are hard constraints, and where a design has to survive a decade of change.

## AI security

The same question now applies to models and agents. In 2026 the community documented open-weight models reaching for their vendor's cloud storage from inside sandboxes, LoRA-tuned models that exfiltrate secrets over DNS on their first turn, and pretraining poisoning that plants remote-code-execution backdoors in coding agents. A reasoning trace is not a security boundary; only deterministic code outside the model is.

That is the premise of my one-hour public talk on AI security, of the hands-on reproduction work on self-hosted models, and of **Torhaus** — a framework that runs any agent harness in kernel-enforced compartments with default-deny egress, a credential broker and a tamper-evident audit log, and ships a trojaned-model red-team suite that has to fail to exfiltrate in CI.

## What I do for clients

- Threat modelling and architecture review for systems that handle sensitive data — including systems that embed LLMs or agents.
- Secure deployment of self-hosted models and agent harnesses: compartmentalisation, egress control, secrets handling, auditability.
- Cryptographic design review, licensing and protection schemes, reverse-engineering assessments.
- Talks and workshops on AI security for engineering teams.
