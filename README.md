# AI Engineering Framework

A lightweight framework for AI-assisted software engineering.

Its purpose is to provide a simple, repeatable way to use AI assistants during software development without changing the team's existing engineering practices.

The framework focuses on three goals:

- Give AI assistants the right context.
- Define a repeatable engineering workflow.
- Capture enough evidence to evaluate the real value of AI assistance.

---

## Why this framework exists

Modern software development increasingly involves AI assistants such as:

- GitHub Copilot
- Codex
- ChatGPT
- Claude
- Gemini

Each tool is good at different tasks, but projects rarely define:

- how they should be used;
- what context they need;
- how decisions should be documented;
- how to evaluate whether AI actually helped.

This framework provides that structure.

---

## What the framework provides

- A standard project structure for AI-assisted development.
- Instructions for AI assistants.
- A repeatable engineering workflow.
- Documentation templates.
- A lightweight methodology for evaluating AI usage.

---

## What the framework is NOT

This framework is **not**:

- a replacement for Git;
- a replacement for Azure DevOps, Jira or GitHub Issues;
- a coding standard;
- an AI assistant.

It complements existing development processes instead of replacing them.

---

## Current scope

The first real-world use case is the migration of a legacy macOS desktop application to a modern .NET architecture.

The framework will be refined during that migration and then generalized so it can be reused in any software project.

---

## Repository structure

```
docs/
```

Framework documentation.

```
templates/
```

Reusable files that can be copied into any project.

---

## Design principles

The framework follows a few simple principles:

- Keep it lightweight.
- Avoid unnecessary complexity.
- Reuse before creating.
- Prefer methodology over tooling.
- Automate only after the manual process is proven.

---

## Roadmap

Version 0.1 focuses on defining the methodology.

Automation, integrations and tooling will be added only when they solve a proven need.
