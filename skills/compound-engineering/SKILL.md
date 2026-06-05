---
name: compound-engineering
description: Implementation reference library for compound engineering workflows. For workflow orchestration, use slash commands under `commands/workflows/` (constitution, plan, work, review, compound). This skill provides stack-specific fix recipes those workflows consume.
version: 1.0.0
tags: [reference, fixes, typescript, react, nextjs, wagmi, automation]
triggers:
  - stack-specific breakage
  - migration fix
  - runtime type mismatch
  - TS triage
  - dashboard testing
model: inherit
---

# Compound Engineering — Implementation Reference

Actionable fix recipes for recurring breakages. Use alongside `aegntic/compound-engineering` workflow commands.

## Usage

Invoke from workflow steps when a fix recipe applies:

```
# From /workflows:work
"Consult skills/compound-engineering for the wagmi v7 migration recipe."
```

## References

- `references/wagmi-v7-migration.md` — upgrade patterns, ABI tuples, balance API changes
- `references/typescript-strict-patterns.md` — empty-array inference, framer-motion ease, never[] fixes
- `references/dashboard-testing.md` — multi-tab verification, lazy-load console checks
- `references/nextjs-build-stability.md` — stale chunks, Turbopack recovery, production build fallback
- `references/verification-fallback-chain.md` — playwright → urllib → curl selection rules
- `references/runtime-type-mismatches.md` — API response shape bugs, empty-state crashes
- `references/frontend-design-system.md` — UI layer recipes for design-first features

## Maintenance

Add new references when a stack-specific fix proves recurrent. Delete references once the pattern is obsolete or upstream has fixed it.
