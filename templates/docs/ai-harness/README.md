# AI Migration Harness

## Purpose

This harness provides a structured engineering process for migrating legacy business applications while preserving business behaviour and generating objective evidence of AI usage.

The harness guides the migration from initial analysis to final validation.

---

# Workflow

Complete each phase in order.

Do not skip phases.

A phase may only begin when the previous phase satisfies its Exit Criteria.

```
Discovery
        ↓
Realm Analysis
        ↓
Data Flow Analysis
        ↓
Business Rules Analysis
        ↓
Target Architecture
        ↓
Migration Plan
        ↓
Migration Slices
        ↓
Validation
        ↓
AI Evidence
```

---

# Documents

| Phase               | Deliverable               |
| ------------------- | ------------------------- |
| Discovery           | 01-discovery.md           |
| Realm Analysis      | 02-realm-model.md         |
| Data Flow Analysis  | 03-data-flows.md          |
| Business Rules      | 04-business-rules.md      |
| Target Architecture | 05-target-architecture.md |
| Migration Plan      | 06-migration-plan.md      |
| Validation          | 07-validation-matrix.md   |
| AI Evidence         | 08-ai-evidence.md         |

Migration slices:

```
docs/ai-harness/slices/
```

Engineering decisions:

```
docs/ai-harness/decisions/
```

---

# Prompts

Use exactly one prompt for each phase.

| Phase               | Prompt                         |
| ------------------- | ------------------------------ |
| Discovery           | prompts/discovery.md           |
| Realm Analysis      | prompts/realm-analysis.md      |
| Data Flow Analysis  | prompts/data-flow-analysis.md  |
| Business Rules      | prompts/business-rules.md      |
| Target Architecture | prompts/target-architecture.md |
| Migration Plan      | prompts/migration-plan.md      |
| Migration Slice     | prompts/migration-slice.md     |
| Validation          | prompts/validation.md          |
| AI Evidence         | prompts/ai-evidence.md         |

---

# Daily Workflow

1. Open `CURRENT_STATE.md`.
2. Continue the current phase or migration slice.
3. Use the corresponding prompt.
4. Update the deliverable.
5. Record important work in `ENGINEERING_JOURNAL.md`.
6. Record important engineering decisions if required.
7. Update `CURRENT_STATE.md`.

---

# Engineering Principles

- Preserve business behaviour.
- Repository evidence has priority.
- Human validation is mandatory.
- Complete one phase before starting the next.
- Complete one slice before starting the next.
- Avoid overengineering.
- Keep architecture as simple as possible.
- Document engineering decisions.
- Validate behaviour instead of implementation.

---

# Definition of Done

The migration is complete only when:

- Every phase has been completed.
- Every migration slice has been validated.
- Critical business rules have been preserved.
- Engineering decisions have been documented.
- AI contribution has been evaluated.
- Remaining risks are explicitly documented.

---

# Version

Harness Version

1.0

## Harness Information

Version: 1.0.0

Created:
YYYY-MM-DD

Last Updated:
YYYY-MM-DD
