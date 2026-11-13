---
title: AI & machine learning
lead: Models built from zero to production — own datasets, own training, own inference, shipped as an application the customer actually uses. Since 2025 also open-weight LLMs on own hardware, LoRA fine-tuning, and the agent harnesses around them.
description: Boris Brodski — machine-learning engineer and architect; vision models from data collection to a customer-facing app, custom trading models, LoRA fine-tuning and local agent harnesses on self-hosted hardware.
pitch:
  - "**Zero to hero, alone.** Mask detector: dataset collected and labelled, model designed and trained in TensorFlow, real-time OpenCV inference, Gtk app and web monitoring delivered to the customer."
  - "**Custom models, not just fine-tuning.** Trading models on market data with proper walk-forward evaluation; CUDA, Numba, Colab."
  - "**Local LLMs end to end.** Self-hosted inference, LoRA fine-tuning, agent harnesses, skills and MCP tools, multi-agent orchestration."
  - "**Mathematical footing.** Deep Learning Specialization, reinforcement learning, MIT statistics — and a physics minor."
---
## Vision models from data collection to a customer app

The COVID mask detector is the project I point to first because it is the whole loop in one pair of hands. There was no dataset, so I collected and labelled one. The model was designed and trained from scratch in TensorFlow and had to run in real time on commodity hardware, so inference went through OpenCV. The customer needed to configure and watch it, so it shipped with a Gtk configuration application and web monitoring. From first photo to deployed product in a few months, as a one-person project.

## Custom models for hard signals

The trading work was the opposite kind of problem: data in abundance, signal scarce. Feature pipelines in PostgreSQL, TensorFlow training on CUDA and Colab, and the evaluation discipline — walk-forward testing, leakage checks — that decides whether a model is real.

## Local LLMs, LoRA and agents

Since 2025 the focus is open-weight language models on own GPU hardware: serving with llama.cpp and vLLM, LoRA fine-tuning for domain tasks, and the agent harnesses on top — writing skills, wiring tools and MCP servers, orchestrating several agents over Matrix. The security of that stack is its own topic; see [Security & AI security](/security/). For a general-audience introduction to what these systems are and why controlling them is hard, there is my one-hour lecture *AI: a giant leap — into heaven or hell?* ([Russian](https://youtu.be/OMsONFIx_p8) · [English](https://youtu.be/e-0_39vcfgY)).

## What I do for clients

- Feasibility and data strategy: is there enough signal, and what would it take to collect it?
- Model design, training and evaluation — with the honest number at the end.
- Productisation: inference services, desktop or web front ends, monitoring.
- Self-hosted LLM deployments: model selection, serving, fine-tuning, agent integration — on hardware you control.
