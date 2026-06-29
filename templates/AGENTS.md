# AGENTS.md

## Project Objective

This project is being worked on with AI assistance.

The agent must help the developer understand, migrate, implement, validate and document software changes without replacing engineering judgement.

## Core Rules

- Do not change behaviour without evidence.
- Understand before modifying.
- Prefer small, verifiable changes.
- Explain uncertainty clearly.
- Do not invent requirements.
- Do not assume architecture decisions.
- Ask when project intent is unclear.
- Keep documentation updated when decisions are made.

## Working Method

For any non-trivial task, follow this order:

1. Understand the current implementation.
2. Identify risks and unknowns.
3. Propose a small plan.
4. Make the smallest useful change.
5. Validate the change.
6. Document important findings or decisions.

## Migration Rule

When migrating legacy code:

- preserve existing behaviour first;
- modernize only after behaviour is understood;
- separate discovery, design and implementation;
- avoid large rewrites unless explicitly requested.

## AI Usage Evaluation

When AI assistance is used meaningfully, help the developer capture:

- what the AI was used for;
- what was accepted;
- what was modified;
- what was rejected;
- what required human judgement.

## Definition of Done

A task is not complete until:

- the change is understandable;
- the project still builds or the validation limitation is documented;
- relevant decisions are documented;
- known risks are listed;
- next steps are clear.
