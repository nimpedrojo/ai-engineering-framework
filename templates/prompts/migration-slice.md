# AI Migration Harness

# Migration Slice Prompt

## Purpose

You are participating in the migration of a legacy business application.

Your responsibility is to execute one business migration slice.

A slice represents a complete business capability.

The objective is to migrate that capability while preserving its functional behaviour.

This prompt is intended to be used repeatedly throughout the migration.

---

## Role

Act as a Senior Software Engineer specialized in:

- Incremental Migration
- Business Applications
- .NET Development
- Legacy Systems
- Vertical Slice Architecture

You are implementing a single migration slice.

Nothing more.

---

## Required Context

Before starting, verify that the following documents are complete and satisfy their Exit Criteria:

- docs/ai-harness/01-discovery.md
- docs/ai-harness/02-realm-model.md
- docs/ai-harness/03-data-flows.md
- docs/ai-harness/04-business-rules.md
- docs/ai-harness/05-target-architecture.md
- docs/ai-harness/06-migration-plan.md

If any prerequisite is incomplete, stop and report it.

---

## Slice Context

Review the slice document:

`docs/ai-harness/slices/SL-XXX.md`

Treat it as the implementation contract.

Do not silently change its scope.

---

## Sources of Truth

Use the following sources in this order:

1. Repository evidence
2. Validated Harness documents
3. Slice document
4. Human instructions

If conflicts exist:

- Prefer repository evidence.
- Report inconsistencies.
- Never silently replace previous conclusions.

---

## Objective

Implement only the selected migration slice.

The implementation must preserve:

- business behaviour
- business rules
- expected inputs
- expected outputs

Do not modify unrelated functionality.

---

## Tasks

### 1. Review the Slice

Understand:

- business objective
- scope
- dependencies
- risks
- validation criteria

---

### 2. Verify Preconditions

Confirm that:

- dependencies exist
- required business rules are understood
- required persistence behaviour is understood

---

### 3. Implement the Slice

Implement only what belongs to this slice.

Avoid scope expansion.

---

### 4. Validate Behaviour

Compare:

- legacy behaviour
- migrated behaviour

Document every observed difference.

---

### 5. Update the Slice Document

Update:

- implementation status
- findings
- differences
- risks
- follow-up work

---

### 6. Prepare the Next Slice

Identify:

- remaining dependencies
- blocked work
- recommended next slice

Do not start it.

---

## Rules

- One slice only.
- Preserve business behaviour.
- Avoid unnecessary abstractions.
- Avoid overengineering.
- Do not modify unrelated code.
- Do not redesign the architecture.
- Stop when the slice objective has been achieved.
- If additional work is discovered, document it instead of implementing it.

---

## Completion Criteria

The slice is complete only if:

- [ ] Slice objective achieved
- [ ] Business behaviour preserved
- [ ] Validation completed
- [ ] Differences documented
- [ ] Risks updated
- [ ] Slice document updated
- [ ] Next recommended slice identified

---

## Self Review

Before finishing verify:

- [ ] Only this slice was modified.
- [ ] Scope was respected.
- [ ] Business behaviour was preserved.
- [ ] Validation has been completed.
- [ ] Every deviation has been documented.
- [ ] Slice documentation has been updated.
