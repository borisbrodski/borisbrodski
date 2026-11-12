---
title: Programming languages & DSLs
lead: A full language built from parser to IDE, two decades of Xtext, and domain-specific languages that became the primary specification artefact of a national tax platform. Screencasts on all of it at xtextcasts.org.
description: Boris Brodski — language engineer; designer of IDScript (parser, bytecode VM, IDE), Xtext and Langium expert since 2006, model-driven development, author of xtextcasts.org.
pitch:
  - "**Built a language.** IDScript: syntax, high-performance parser, bytecode compiler and VM, standard library, C bridge, OLE automation, Eclipse RCP IDE — four years, in production."
  - "**Xtext since 1.0, Langium now.** DSLs at the core of a public-sector platform for over a decade; talks at XtextCON and EclipseCon; [xtextcasts.org](https://xtextcasts.org)."
  - "**Model-driven for real.** Layered DSLs generating persistence, services and UI — designed, built and maintained, not slide-ware."
  - "**Parser toolbox.** JavaCC, Yacc/Bison, ANTLR, hand-written; Haskell for the ideas."
---
## IDScript

Between 2002 and 2007 I designed and implemented a new version of a company's scripting language for customer-specific processes: rule sets, workflows, document generation, PDF form evaluation. Everything a language needs — syntax, a high-performance parser, bytecode compiler, virtual machine, standard library, a bidirectional C ↔ script bridge, generic OLE automation of Word and Excel, a plugin interface, bytecode encryption, a converter from the old syntax, an Eclipse RCP IDE and a LaTeX manual. It shipped to banks and real-estate companies.

## Xtext and model-driven development

Xtext came in 2006 with version 1.0, first in a model-driven RAD framework that generated persistence, server and client layers from two layered DSLs, then in a ten-page web form generated from a DSL. Since 2012 it is at the heart of the KONSENS backend component I architect: text models as the primary artefact, maintained and evolved for over a decade by a team of 15+. That story was the XtextCON 2014 talk "Pay your taxes with Xtext". Newer work uses Langium.

## Teaching it

xtextcasts.org holds the screencasts; the Eclipse DemoCamp and EclipseCon talks covered embedded DSLs for testing enterprise applications, which also became an Eclipse Magazin article.

## What I do for clients

- Language and DSL design: syntax, semantics, tooling, migration from legacy formats.
- Xtext and Langium projects — new, or rescuing ones that grew without a plan.
- Model-driven architectures that generate code worth maintaining.
- Training and coaching for teams adopting DSLs.
