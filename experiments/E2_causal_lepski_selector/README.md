# E2 — Causal Lepski-style history selector

## Scientific question

Can theoretically valid uncertainty radii for nested local EDMD estimates be converted into a practically useful causal rule for choosing history length?

## Approach

The experiment compared local operator/spectral estimates across nested history windows using a Lepski-style compatibility logic. The intended idea was to choose the largest history horizon still statistically compatible with shorter-horizon estimates.

## Result

The statistically valid confidence radii were too conservative in the tested setup:

- most or all candidate history windows were declared mutually compatible;
- the selector therefore frequently chose the largest available window;
- the rule did not react usefully enough to the bias–variance trade-off identified in E1.

## Verdict

**REFUTED as a practically effective causal selector in the tested setup.**

## Scientific consequence

E2 exposed a gap between two different goals:

1. obtaining a finite-sample bound that is statistically defensible;
2. obtaining a scale-selection rule that is sharp enough to be useful online.

A conservative theoretical confidence set can be valid while still being practically uninformative for adaptive history selection.

## Relation to later work

This negative result was one reason the project moved away from treating adaptive-window selection itself as the primary contribution. Later work focused on diagnosing spectral reliability and identifiability before attempting any downstream horizon-selection rule.

## What E2 does not establish

E2 does not show that Lepski methods are generally ineffective. It only shows that the particular statistically valid radii and EDMD setup used here were too conservative to produce a useful selector.

## Provenance status

This record is grounded in the authoritative project experiment ledger. A byte-level E2 archive has not yet been identified during the current migration, so this directory is a historical scientific record rather than a fully reproducible package.