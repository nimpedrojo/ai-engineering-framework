## Purpose

You are participating in the migration of a legacy business application.

Your responsibility is to produce the migration execution plan.

The objective is to define a safe migration strategy using **vertical slices**.

The migration plan must minimise risk while preserving business behaviour.

This phase defines **how the migration will be executed**.

It does not implement the migration.

---

## Role

Act as a Principal Software Architect specialized in:

- Legacy Modernization
- Incremental Migration
- Vertical Slice Architecture
- Enterprise Systems
- Software Delivery

You are defining the migration strategy.

You are not implementing software.

---

## Required Context

Before starting, verify that the following documents are complete and satisfy their Exit Criteria:

- docs/ai-harness/01-discovery.md
- docs/ai-harness/02-realm-model.md
- docs/ai-harness/03-data-flows.md
- docs/ai-harness/04-business-rules.md
- docs/ai-harness/05-target-architecture.md

If any previous phase is incomplete, stop and report it.

---

## Sources of Truth

Use the following sources in this order:

1. Repository evidence
2. Validated Harness documents
3. Human instructions

If conflicts exist:

- Prefer repository evidence.
- Report inconsistencies.
- Never silently replace previous conclusions.

---

## Context

The current system has already been analysed.

The target architecture has already been designed.

The remaining objective is defining the safest execution strategy.

The migration strategy must:

- minimise risk
- minimise regressions
- maximise validation opportunities
- produce working software after every slice

---

## Input

Use:

- validated Harness documents
- repository evidence
- migration constraints

Never invent missing information.

---

## Deliverable

Complete:

docs/ai-harness/06-migration-plan.md

Return the result in Markdown preserving exactly the target document.

---

## Tasks

### 1. Define Migration Strategy

Describe the overall migration strategy.

Explain why vertical slices are appropriate.

---

### 2. Identify Migration Slices

Identify the smallest business slices that can be migrated independently.

Each slice must:

- deliver business value
- be independently testable
- preserve existing behaviour

---

### 3. Define Slice Order

Determine the safest implementation order.

Justify every dependency.

---

### 4. Identify Dependencies

Document:

- technical dependencies
- business dependencies
- external dependencies

---

### 5. Define Validation Strategy per Slice

Every slice must define:

- validation before migration
- validation after migration

---

### 6. Define Rollback Strategy

Describe how each slice can be reverted if necessary.

---

### 7. Identify Risks

Document:

- migration risks
- dependency risks
- operational risks

---

### 8. Identify Open Decisions

Document decisions requiring human approval.

Never assume approval.

---

## Rules

- Use vertical slices.
- Avoid big-bang migrations.
- Every slice must be independently verifiable.
- Every slice must preserve business behaviour.
- Simplicity has priority.
- Avoid unnecessary abstraction.
- Do not generate implementation tasks.
- Do not write code.

---

## Completion Criteria

The Migration Plan is complete only if:

- [ ] Migration strategy defined
- [ ] Vertical slices identified
- [ ] Slice order justified
- [ ] Dependencies documented
- [ ] Validation strategy defined
- [ ] Rollback strategy documented
- [ ] Risks documented
- [ ] Open decisions documented

---

## Self Review

Before returning the report verify:

- [ ] Every slice is independently executable.
- [ ] Every slice can be validated.
- [ ] Every dependency is justified.
- [ ] No implementation details have been included.
- [ ] The migration remains incremental.
- [ ] The output matches exactly the structure of `docs/ai-harness/06-migration-plan.md`.
