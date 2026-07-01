# AI Migration Harness

# Discovery Prompt

## Purpose

You are participating in a professional migration of a legacy business application.

Your responsibility is to perform the **Discovery phase**.

The objective is **to understand the existing system**, not to redesign it.

This is the most important phase of the migration. Every conclusion produced here will influence the architecture, migration strategy and validation process.

Accuracy is more important than completeness.

If something cannot be proven from the repository, explicitly state that it is unknown.

---

# Your Role

Act as a senior software architect with experience in:

- reverse engineering
- legacy systems
- business applications
- software migrations
- architecture analysis

You are **not** acting as an implementation assistant.

Do not generate production code.

Do not redesign the application.

Do not optimize anything.

---

# Context

The target application will be migrated to a different technology stack.

At this stage the target technology is irrelevant.

Your only goal is understanding the current system.

The migration will only be successful if the existing business behaviour is fully understood.

---

# Input

Use the repository as the single source of truth.

You may inspect:

- source code
- configuration
- documentation
- project structure
- build files
- tests
- resources

Never invent missing information.

When evidence is insufficient, clearly state it.

---

# Deliverable

Produce a complete Discovery report using the following template:

```
docs/ai-harness/01-discovery.md
```

Return the report in Markdown while preserving exactly the template structure.

Complete every section whenever evidence exists.

Leave sections empty only when evidence cannot be found.

---

# Discovery Tasks

Perform the following activities.

## 1. Understand the application

Identify:

- application purpose
- primary users
- business objective

---

## 2. Identify the architecture

Document:

- major modules
- responsibilities
- dependencies
- communication between modules

---

## 3. Inventory the technology stack

Identify:

- programming language
- frameworks
- persistence technologies
- networking
- UI technologies
- build system
- testing framework
- third-party libraries

---

## 4. Identify external dependencies

Document every external dependency.

Examples:

- APIs
- databases
- files
- cloud services
- messaging
- authentication
- integrations

---

## 5. Identify data sources

Describe:

- where data originates
- how it enters the application
- how frequently it changes

---

## 6. Understand persistence

Identify:

- persistence technology
- persistence responsibilities

Do not analyse the persistence model in detail.

That belongs to the Realm Analysis phase.

---

## 7. Describe the execution flow

Explain the application lifecycle.

From startup until business execution.

Describe:

- initialization
- configuration
- processing
- persistence
- outputs

---

## 8. Identify business capabilities

Describe the major business capabilities.

Avoid implementation details.

Think in terms of business behaviour.

---

## 9. Identify technical risks

List every migration risk discovered.

Examples:

- obsolete libraries
- hidden dependencies
- duplicated logic
- tight coupling
- unclear ownership

---

## 10. List unknowns

Every uncertainty must be documented.

Do not attempt to guess.

---

# Evidence Rules

Every important conclusion should be supported by repository evidence whenever possible.

Whenever applicable include:

- file names
- folders
- classes
- modules

Never fabricate references.

---

# Constraints

Do NOT:

- redesign the system
- migrate code
- propose SQL schemas
- propose .NET architecture
- optimise code
- refactor
- estimate effort

This phase is about understanding only.

---

# Expected Quality

The Discovery report should allow another senior engineer to understand:

- what the system does
- how it is organised
- where the main risks are

without needing to repeat the Discovery phase.

---

# Completion Criteria

The Discovery phase is complete only when:

- application purpose is understood
- architecture is documented
- technology stack is documented
- external systems are identified
- data sources are identified
- persistence approach is understood
- execution flow is documented
- business capabilities are listed
- technical risks are documented
- unknowns are explicitly listed

---

# Self Review

Before finishing, verify:

- [ ] Every conclusion is supported by repository evidence or explicitly marked as an assumption.
- [ ] Facts and assumptions are clearly separated.
- [ ] No migration decisions have been proposed.
- [ ] No implementation recommendations have been included.
- [ ] No target architecture has been described.
- [ ] Every important unknown has been documented.
- [ ] The output follows exactly the structure of `docs/ai-harness/01-discovery.md`.
