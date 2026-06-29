# Discovery Prompt

## Objective

Analyze the project before making any code changes.

The goal is to understand the current system, identify risks, and produce enough knowledge to plan the migration.

Do **not** modify any code during this phase.

---

## Instructions

Analyze the complete repository and produce a structured engineering report.

Focus on understanding the existing system rather than proposing improvements.

For every conclusion:

- indicate the evidence supporting it;
- distinguish facts from assumptions;
- identify uncertainties.

Do not invent missing information.

If something cannot be determined from the repository, explicitly state it.

---

## Produce the following sections

### 1. Executive Summary

Explain in a few paragraphs:

- what the application does;
- its main responsibilities;
- the overall architecture.

---

### 2. Technology Stack

Identify:

- languages;
- frameworks;
- persistence technologies;
- external dependencies;
- build system;
- testing framework;
- deployment-related components.

---

### 3. Project Structure

Describe the major modules and their responsibilities.

---

### 4. Data Flow

Explain:

- where data comes from;
- how it is transformed;
- where it is stored;
- how it is consumed.

---

### 5. Domain Model

Identify the main business entities and their relationships.

---

### 6. External Integrations

List all external systems, APIs, databases or services.

---

### 7. Risks

Identify technical risks such as:

- obsolete dependencies;
- tightly coupled components;
- missing tests;
- unclear behaviour;
- hidden assumptions.

---

### 8. Migration Considerations

Identify what should be preserved during migration.

Highlight components that may require redesign.

Do not redesign them yet.

---

### 9. Questions

List every important question that cannot be answered from the repository.

---

## Expected Output

Produce a concise engineering report suitable for software architects.

Avoid unnecessary detail.

Prioritize clarity, evidence and traceability.
