# E4 — Adaptive spectral window / oracle benchmark

## Scientific role

E4 broadened the initial adaptive-history idea into a controlled benchmark against several simple and spectral baselines.

## Systems

The benchmark used controlled nonstationary AR/VAR/Markov-style systems.

## Methods explored

- fixed history windows;
- Lepski-like selection;
- drift-only criteria;
- spectral-gap criteria;
- Grassmann/subspace criteria;
- oracle comparisons.

## Result

Adaptive spectral heuristics did **not** consistently outperform simple fixed windows. Some selectors were overly conservative, while others were unstable or selected inappropriate horizons in parts of the benchmark.

## Verdict

**EXPLORATORY / negative for the broad superiority claim.**

The experiment did not justify a claim that a generic spectral adaptive-window rule was better than simple fixed-history baselines across nonstationary systems.

## Scientific consequence

E4 reinforced the need to separate two questions:

1. which history length minimizes a particular downstream error;
2. whether the spectral estimate at a chosen history length is itself identifiable and reliable.

The project later moved toward the second question.

## Evaluation caveat

Early oracle comparisons were themselves audited because using the same Grassmann-style target for both selection and evaluation can create circularity. Later work therefore emphasized independent evaluation targets and explicit spectral-gap/identifiability checks.

## Provenance status

This record is grounded in the authoritative project experiment ledger and project-state audit history. A byte-level E4 archive has not yet been identified in the current migration.