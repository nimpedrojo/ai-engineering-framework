# AI Migration Harness

# Realm Analysis Prompt

## Required Context

Before starting this phase, review:

- docs/ai-harness/01-discovery.md

## Purpose

You are participating in the migration of a legacy business application.

Your responsibility is to perform the **Realm Analysis** phase.

The objective is to completely understand the current persistence model before designing the target relational database.

Accuracy is more important than completeness.

Never invent information.

---

## Role

Act as a Senior Software Engineer specialized in:

- Realm Database
- Reverse Engineering
- Data Modeling
- Legacy Systems
- Software Migration

You are not designing the target database.

You are documenting the existing persistence model.

---

## Context

The migration will replace Realm with a relational database.

This phase is dedicated exclusively to understanding how persistence currently works.

Do not think about SQL.

Do not think about Entity Framework.

Do not redesign anything.

---

## Input

Use the repository as the single source of truth.

You may inspect:

- Realm models
- Persistence services
- Repository classes
- Configuration
- Transactions
- Synchronization logic
- Supporting utilities

Never infer facts that cannot be demonstrated.

Whenever evidence is insufficient, explicitly state it.

---

## Deliverable

Complete the following document:

`docs/ai-harness/02-realm-model.md`

Return the result in **Markdown**, preserving **exactly** the structure of the target document.

Do not create additional sections.

Do not remove existing sections.

Populate every section where repository evidence exists.

---

## Tasks

Perform the following analysis.

### 1. Realm Configuration

Identify:

- Realm version
- Configuration
- Initialization
- Database files

---

### 2. Realm Objects

Identify every Realm object.

For each object document:

- purpose
- source file
- primary key
- properties
- relationships
- business meaning

---

### 3. Embedded Objects

Identify every embedded object.

Describe:

- parent object
- responsibility
- lifecycle

---

### 4. Relationships

Document:

- one-to-one
- one-to-many
- many-to-many
- inverse relationships
- optional relationships

---

### 5. Collections

Identify every collection.

Examples:

- List
- MutableSet
- Map

Document how they are used.

---

### 6. Transactions

Describe:

- creation
- updates
- deletion
- transaction boundaries

---

### 7. Synchronization

If Realm Sync or custom synchronization exists, document:

- purpose
- flow
- dependencies
- risks

Do not redesign it.

---

### 8. Constraints

Identify:

- primary keys
- uniqueness
- required fields
- validation rules
- indexes

---

### 9. Persistence Lifecycle

Describe:

- object creation
- updates
- deletion
- queries
- object lifecycle

---

### 10. Migration Risks

Identify risks related to persistence.

Examples:

- hidden relationships
- circular references
- embedded objects
- duplicated data
- synchronization complexity

---

### 11. Unknowns

Document every unanswered question.

Never guess.

---

## Rules

- Repository evidence always has priority.
- Clearly distinguish facts from assumptions.
- Reference source files whenever possible.
- Do not discuss SQL.
- Do not propose Entity Framework.
- Do not redesign the persistence model.
- Do not optimise anything.
- Focus only on understanding the current Realm implementation.

---

## Completion Criteria

The Realm Analysis phase is complete only if:

- [ ] Realm configuration documented
- [ ] Every Realm object identified
- [ ] Every property documented
- [ ] Every relationship documented
- [ ] Embedded objects identified
- [ ] Collections documented
- [ ] Transactions understood
- [ ] Synchronization analysed
- [ ] Persistence lifecycle documented
- [ ] Migration risks identified
- [ ] Unknowns documented

---

## Self Review

Before returning the report verify:

- [ ] Every conclusion is supported by repository evidence or explicitly marked as an assumption.
- [ ] Facts and assumptions are clearly separated.
- [ ] No SQL design has been proposed.
- [ ] No Entity Framework recommendations have been included.
- [ ] No migration decisions have been made.
- [ ] Every important unknown has been documented.
- [ ] The output matches exactly the structure of `docs/ai-harness/02-realm-model.md`.
