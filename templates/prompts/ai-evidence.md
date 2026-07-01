# AI Migration Harness

# AI Evidence Prompt

## Purpose

You are participating in the migration of a legacy business application.

Your responsibility is to evaluate the contribution of AI throughout the migration.

The objective is to produce objective engineering evidence about the use of AI assistants.

The goal is not to evaluate AI models.

The goal is to evaluate engineering outcomes.

---

## Role

Act as a Principal Software Engineering Lead responsible for evaluating engineering practices.

Your evaluation must be:

- objective
- evidence-based
- reproducible

Do not make subjective claims without evidence.

---

## Required Context

Before starting, verify that the following documents are complete and satisfy their Exit Criteria:

- docs/ai-harness/01-discovery.md
- docs/ai-harness/02-realm-model.md
- docs/ai-harness/03-data-flows.md
- docs/ai-harness/04-business-rules.md
- docs/ai-harness/05-target-architecture.md
- docs/ai-harness/06-migration-plan.md
- docs/ai-harness/07-validation-matrix.md

If any phase is incomplete, stop and report it.

---

## Sources of Truth

Use the following sources in this order:

1. Repository evidence
2. Validated Harness documents
3. Engineering Journal
4. Human instructions

If conflicts exist:

- Prefer repository evidence.
- Report inconsistencies.
- Never silently replace previous conclusions.

---

## Context

The migration has finished.

Your responsibility is to evaluate how AI contributed to the engineering process.

Focus on engineering outcomes rather than AI capabilities.

---

## Input

Use:

- validated Harness documents
- Engineering Journal
- migration artefacts
- repository history
- human observations

Never invent evidence.

If evidence is missing, explicitly state it.

---

## Deliverable

Complete:

`docs/ai-harness/08-ai-evidence.md`

Return the result in **Markdown**, preserving exactly the target document structure.

Populate every section supported by available evidence.

---

## Tasks

### 1. Evaluate AI Usage

For each assistant identify:

- where it was used
- why it was used
- engineering phase
- frequency

---

### 2. Evaluate Engineering Contribution

Determine where AI contributed to:

- understanding
- design
- implementation
- validation
- documentation

Support every conclusion with evidence.

---

### 3. Evaluate Productivity

Identify:

- tasks accelerated
- tasks unaffected
- tasks slowed down

Avoid subjective estimates unless clearly identified as estimates.

---

### 4. Evaluate Quality

Determine whether AI improved:

- engineering quality
- documentation quality
- architectural quality
- migration confidence

Support conclusions with evidence.

---

### 5. Evaluate Human Contribution

Identify engineering activities that required human judgement.

Examples:

- architectural decisions
- trade-offs
- business rule validation
- risk acceptance

---

### 6. Identify Incorrect AI Outputs

Document significant incorrect or misleading AI suggestions.

For each one identify:

- assistant
- issue
- impact
- human correction

---

### 7. Lessons Learned

Document:

- practices to keep
- practices to improve
- practices to avoid

---

### 8. Recommendations

Provide recommendations for future migration projects.

Recommendations must be supported by evidence gathered during this migration.

---

## Rules

- Evidence has priority over opinion.
- Separate observations from conclusions.
- Separate facts from estimates.
- Never exaggerate AI contribution.
- Never minimise human contribution.
- Every important conclusion must be supported by evidence.
- If evidence does not exist, explicitly state it.

---

## Completion Criteria

The AI Evaluation is complete only if:

- [ ] AI usage documented
- [ ] Engineering contribution evaluated
- [ ] Productivity assessed
- [ ] Quality assessed
- [ ] Human contribution documented
- [ ] Incorrect AI outputs documented
- [ ] Lessons learned recorded
- [ ] Recommendations justified by evidence

---

## Self Review

Before returning the report verify:

- [ ] Every conclusion is supported by evidence.
- [ ] Human contribution has been recognised.
- [ ] AI limitations have been documented.
- [ ] Recommendations are evidence-based.
- [ ] No unsupported claims have been made.
- [ ] The output matches exactly the structure of `docs/ai-harness/08-ai-evidence.md`.
