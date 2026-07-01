# Data Flow Analysis

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

Understand how data moves through the application from acquisition to final consumption.

The goal is to identify every transformation applied to the data before designing the target architecture.

Do **not** redesign the flow in this document.

---

# High-Level Flow

Describe the complete application flow.

```
Source

↓

Acquisition

↓

Validation

↓

Normalization

↓

Business Rules

↓

Persistence

↓

Consumption

↓

Output
```

---

# Data Sources

| Source | Type | Frequency | Critical | Notes |
| ------ | ---- | --------- | -------- | ----- |
|        |      |           |          |       |

---

# Data Acquisition

| Component | Source | Responsibility | Notes |
| --------- | ------ | -------------- | ----- |
|           |        |                |       |

---

# Validation

Describe all validation performed before data is accepted.

| Validation | Location | Purpose |
| ---------- | -------- | ------- |
|            |          |         |

---

# Normalization

Describe every normalization step.

| Input | Output | Rule | Notes |
| ----- | ------ | ---- | ----- |
|       |        |      |       |

---

# Business Processing

Describe the business logic applied to the data.

| Process | Description | Inputs | Outputs |
| ------- | ----------- | ------ | ------- |
|         |             |        |         |

---

# Calculations

List every important calculation.

| Calculation | Purpose | Inputs | Outputs |
| ----------- | ------- | ------ | ------- |
|             |         |        |         |

---

# Persistence Flow

Describe how processed data is persisted.

| Component | Writes | Reads | Notes |
| --------- | ------ | ----- | ----- |
|           |        |       |       |

---

# Data Consumers

Who consumes the stored data?

| Consumer | Purpose | Notes |
| -------- | ------- | ----- |
|          |         |       |

---

# Error Handling

Describe what happens when a step fails.

| Step | Behaviour | Recovery |
| ---- | --------- | -------- |
|      |           |          |

---

# Sequence Overview

Describe the execution order.

1.

2.

3.

4.

5.

---

# Bottlenecks

| Area | Cause | Impact |
| ---- | ----- | ------ |
|      |       |        |

---

# Migration Considerations

List observations that may affect the migration.

- ***

# Unknowns

- [ ]

- [ ]

- [ ]

---

# Discovery Checklist

- [ ] All data sources identified

- [ ] Acquisition process understood

- [ ] Validation documented

- [ ] Normalization documented

- [ ] Business rules identified

- [ ] Calculations documented

- [ ] Persistence flow understood

- [ ] Consumers identified

- [ ] Failure scenarios documented

- [ ] Migration considerations recorded

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
