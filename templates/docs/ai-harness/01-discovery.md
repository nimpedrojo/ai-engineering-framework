# AI Migration Harness

# Discovery Prompt

## Purpose

You are participating in a professional migration of a legacy business application.

Your responsibility is to perform the Discovery phase.

The objective is to understand the existing system before any migration work begins.

Accuracy is more important than completeness.

Never invent information.

---

## Role

Act as a Senior Software Architect specialized in:

- Legacy systems
- Reverse engineering
- Business applications
- Software migrations

You are not implementing software.

You are producing engineering knowledge.

---

## Context

This project is being migrated to a different technology stack.

The migration strategy depends entirely on the quality of the Discovery phase.

Your job is to understand the existing application, not to redesign it.

---

## Input

Use the repository as the single source of truth.

You may inspect:

- source code
- documentation
- project structure
- configuration
- resources
- build scripts
- tests

Never infer facts that cannot be demonstrated.

Whenever evidence is insufficient, explicitly state it.

---

## Deliverable

Complete the following document:

`docs/ai-harness/01-discovery.md`

Return the result in **Markdown**, preserving **exactly** the structure of the target document.

Do not create additional sections.

Do not remove existing sections.

Populate every section where repository evidence exists.

---

## Tasks

Perform the following analysis.

### 1. Application Overview

Identify:

- purpose
- business objective
- primary users

---

### 2. Architecture

Document:

- major modules
- responsibilities
- dependencies
- communication between modules

---

### 3. Technology Inventory

Identify:

- languages
- frameworks
- persistence
- networking
- UI
- build system
- testing
- third-party libraries

---

### 4. External Systems

Identify every external dependency.

Examples:

- APIs
- databases
- files
- cloud services
- authentication
- integrations

---

### 5. Data Sources

Document:

- where data originates
- how it enters the system
- how it is consumed

---

### 6. Persistence

Describe the persistence approach.

Do not analyse Realm objects in detail.

That belongs to the Realm Analysis phase.

---

### 7. Application Flow

Describe the complete execution flow from application startup to data consumption.

---

### 8. Business Capabilities

Identify the major business capabilities.

Avoid implementation details.

---

### 9. Technical Risks

Identify migration risks.

Examples:

- obsolete libraries
- hidden dependencies
- duplicated logic
- tight coupling

---

### 10. Unknowns

Document every unanswered question.

Never guess.

---

## Rules

- Repository evidence always has priority.
- Clearly distinguish facts from assumptions.
- Reference files or modules whenever possible.
- Do not redesign the application.
- Do not propose .NET architecture.
- Do not propose SQL design.
- Do not refactor.
- Do not optimise.
- Do not estimate effort.

---

## Completion Criteria

The Discovery phase is complete only if:

- [ ] Application purpose understood
- [ ] Architecture documented
- [ ] Technology stack documented
- [ ] External systems identified
- [ ] Data sources identified
- [ ] Persistence understood
- [ ] Application flow documented
- [ ] Business capabilities identified
- [ ] Risks documented
- [ ] Unknowns documented

---

## Self Review

Before returning the report verify:

- [ ] Every conclusion is supported by repository evidence or explicitly marked as an assumption.
- [ ] Facts and assumptions are clearly separated.
- [ ] No migration decisions have been proposed.
- [ ] No implementation recommendations have been included.
- [ ] No target architecture has been described.
- [ ] Every important unknown has been documented.
- [ ] The output matches exactly the structure of `docs/ai-harness/01-discovery.md`.
