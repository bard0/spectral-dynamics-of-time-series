# E3 — Grassmann mode-swap sanity check

## Scientific role

E3 is a small but foundational sanity test that changed how all later spectral comparisons were performed.

Individual eigenvectors are not stable identifiers of a slow dynamical object: signs can flip, ordering can change, and two basis vectors can rotate or swap while spanning essentially the same invariant subspace.

## Result

**CONFIRMED.**

In the controlled mode-swap sanity test:

- maximum Grassmann distance between the subspaces was approximately `1.1e-14`;
- individual-vector overlap could fall to approximately `0.13`.

Thus a large apparent change in individual modes can coexist with essentially zero change in the invariant subspace.

## Rule inherited by later experiments

Whenever the scientific target is a multi-mode slow spectral object, prefer an invariant-subspace comparison over raw eigenvector matching.

This rule motivated the later use of projector/Grassmann geometry in E8–E15 and is especially important near mode crossings, nearly degenerate eigenvalues, and complex-pair formation.

## What this does not establish

E3 is a representation sanity check, not a reliability theorem. It does not establish:

- statistical consistency of EDMD;
- a universal metric for all spectral objects;
- robustness under spectral-gap collapse;
- a causal drift detector;
- a new Grassmannian method.

## Provenance status

The numerical result is preserved in the authoritative project experiment ledger. A separate byte-level experiment archive has not been identified during the current migration, so this directory records the scientific result and methodological rule only.