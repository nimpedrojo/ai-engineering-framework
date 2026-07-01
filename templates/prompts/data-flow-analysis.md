# AI Migration Harness

# Data Flow Analysis Prompt

## Required Context

Before starting this phase, review:

- docs/ai-harness/01-discovery.md
- docs/ai-harness/02-realm-model.md

## Purpose

You are participating in the migration of a legacy business application.

Your responsibility is to perform the **Data Flow Analysis** phase.

The objective is to understand how information moves through the application from acquisition to final consumption.

Accuracy is more important than completeness.

Never invent information.

---

## Role

Act as a Senior Software Architect specialized in:

- Reverse Engineering
- Data Pipelines
- Business Applications
- Legacy Systems
- Software Migration

You are not redesigning the application.

You are documenting how information flows through the existing system.

---

## Context

Business applications rarely fail because of persistence.

They fail because data is transformed incorrectly.

Your responsibility is to understand every significant transformation performed on the data.

Do not redesign anything.

Do not optimize anything.

---

## Input

Use the repository as the single source of truth.

You may inspect:

- Services
- Managers
- Controllers
- Workers
- Jobs
- Repository classes
- Data transformations
- Calculations
- Validation logic
- Configuration
- Scheduled tasks

Never infer facts that cannot be demonstrated.

Whenever evidence is insufficient, explicitly state it.

---

## Deliverable

Complete the following document:

`docs/ai-harness/03-data-flows.md`

Return the result in **Markdown**, preserving **exactly** the structure of the target document.

Do not create additional sections.

Do not remove existing sections.

Populate every section where repository evidence exists.

---

## Tasks

Perform the following analysis.

### 1. Identify Data Sources

Document every origin of business data.

Examples:

- APIs
- Files
- Databases
- User input
- Scheduled imports
- External systems

---

### 2. Trace Data Acquisition

For every source identify:

- acquisition component
- acquisition frequency
- acquisition mechanism
- initial validation

---

### 3. Trace Validation

Document every validation step.

Identify:

- validation rules
- validation components
- rejected data
- validation failures

---

### 4. Trace Normalization

Identify every transformation applied to incoming data.

Document:

- original format
- normalized format
- transformation rules
- business purpose

---

### 5. Trace Business Processing

Describe every business process that modifies the information.

Focus on behaviour rather than implementation.

---

### 6. Trace Calculations

Identify every relevant calculation.

For every calculation document:

- inputs
- outputs
- dependencies
- business meaning

---

### 7. Trace Persistence

Describe:

- when data is stored
- what data is stored
- which components perform persistence

Do not analyse Realm internals.

That belongs to the Realm Analysis phase.

---

### 8. Trace Data Consumption

Identify every consumer of persisted information.

Examples:

- UI
- Reports
- APIs
- Export processes
- Synchronization
- Background jobs

---

### 9. Trace Error Handling

Document how failures affect the data flow.

Examples:

- retries
- partial failures
- rollback
- ignored errors
- logging

---

### 10. Identify Bottlenecks

Document:

- duplicated processing
- expensive calculations
- sequential operations
- unnecessary persistence
- synchronization delays

---

### 11. Migration Considerations

Identify observations that may affect the migration.

Do not propose solutions.

Only document them.

---

### 12. Unknowns

Document every unanswered question.

Never guess.

---

## Rules

- Repository evidence always has priority.
- Clearly distinguish facts from assumptions.
- Follow the data, not the source code hierarchy.
- Reference files whenever possible.
- Do not redesign the flow.
- Do not optimise.
- Do not propose implementation changes.
- Do not discuss .NET architecture.
- Do not discuss SQL.

---

## Completion Criteria

The Data Flow Analysis phase is complete only if:

- [ ] Every data source identified
- [ ] Acquisition flow documented
- [ ] Validation documented
- [ ] Normalization documented
- [ ] Business processing documented
- [ ] Calculations documented
- [ ] Persistence flow documented
- [ ] Data consumers documented
- [ ] Error handling documented
- [ ] Bottlenecks identified
- [ ] Migration considerations documented
- [ ] Unknowns documented

---

## Self Review

Before returning the report verify:

- [ ] Every conclusion is supported by repository evidence or explicitly marked as an assumption.
- [ ] Facts and assumptions are clearly separated.
- [ ] The analysis follows the data flow instead of the project structure.
- [ ] No migration decisions have been proposed.
- [ ] No implementation recommendations have been included.
- [ ] Every important unknown has been documented.
- [ ] The output matches exactly the structure of `docs/ai-harness/03-data-flows.md`.
