# Business Rules Catalogue

## Status

☐ Not Started

☐ In Progress

☐ Completed

**Owner**

- **Last Updated**

- **Reviewed**

- **Confidence**

High / Medium / Low

---

## Objective

Identify, document and validate every business rule implemented by the current application.

The purpose of this document is to preserve business behaviour during the migration.

This document describes **what the system does**, not **how it is implemented**.

---

# Business Domains

List the functional areas of the application.

| Domain | Description | Critical |
| ------ | ----------- | -------- |
|        |             |          |

---

# Business Rule Inventory

| Rule ID | Domain | Name | Critical |
| ------- | ------ | ---- | -------- |
| BR-001  |        |      | High     |

---

# Business Rule

## Rule ID

BR-

## Name

-

## Domain

-

## Description

Describe the rule using business language.

Avoid implementation details.

---

## Business Purpose

Why does this rule exist?

- ***

## Trigger

When is this rule executed?

- ***

## Inputs

| Input | Source |
| ----- | ------ |
|       |        |

---

## Outputs

| Output | Destination |
| ------ | ----------- |
|        |             |

---

## Preconditions

Conditions that must be true before execution.

- ***

## Postconditions

Conditions that must be be true after execution.

- ***

## Processing Logic

Describe the functional behaviour.

Do not describe source code.

- ***

## Exceptions

Describe situations where the rule behaves differently.

| Condition | Behaviour |
| --------- | --------- |
|           |           |

---

## Dependencies

What does this rule depend on?

- External systems
- Configuration
- Database values
- Other business rules

- ***

## Persistence Impact

Does this rule create, update or delete information?

- ***

## Validation Strategy

How can this rule be validated after migration?

- ***

## Migration Notes

Observations for the migration team.

- ***

## Source Location

Files or modules implementing this rule.

- ***

## AI Analysis

Was the rule initially identified by AI?

Yes / No

Was it validated by a human?

Yes / No

Corrections required

-

Confidence

High / Medium / Low

---

# Rule Dependencies

Describe relationships between business rules.

| Parent Rule | Child Rule | Relationship |
| ----------- | ---------- | ------------ |
|             |            |              |

---

# Critical Rules

List the rules that **must** behave exactly the same after migration.

| Rule | Reason |
| ---- | ------ |
|      |        |

---

# Potential Hidden Rules

Rules suspected to exist but not yet fully understood.

| Observation | Investigation Required |
| ----------- | ---------------------- |
|             |                        |

---

# Open Questions

- [ ]

- [ ]

- [ ]

---

# Discovery Checklist

- [ ] Functional domains identified

- [ ] Business rules catalogued

- [ ] Critical rules identified

- [ ] Dependencies documented

- [ ] Validation strategy defined

- [ ] Hidden rules investigated

- [ ] Migration risks identified

---

# AI Usage

## AI assistants used

- [ ] ChatGPT
- [ ] Codex
- [ ] Copilot

## AI contribution

Summary

-

Human validation

-

Corrections required

-

Confidence

High / Medium / Low
