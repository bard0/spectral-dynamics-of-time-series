# EXP-008 — Nested disagreement versus true dynamical drift

## Naming note

This is the **early EXP-008 drift-proxy falsification**. It is distinct from the later `E8` cross-scale reliability experiment in the reliability branch.

The original project labels are preserved because the scientific meaning changed between these stages.

## Scientific question

Does the nested-window Grassmann disagreement

`d_G(E_H(t), E_2H(t))`

measure the amount of true dynamical drift?

This question was central to the original "coherence horizon" interpretation: if older history became dynamically invalid, disagreement across history scales was expected to increase in a way that tracked true evolution of the underlying system.

## Result

The nested disagreement correlated poorly with oracle true dynamical drift in controlled nonstationary experiments.

Instead, it behaved mainly as a signal of estimator/scale instability and finite-data inconsistency.

## Verdict

**REFUTED — nested-window disagreement is not a direct drift proxy.**

## Scientific consequence

This was a major pivot point for the project.

The original interpretation

> cross-scale disagreement ≈ how far back the dynamics remain valid

was abandoned.

The same observable can mix:

- finite-sample estimation error;
- estimator variance;
- poor spectral separation;
- non-normal sensitivity;
- model mismatch;
- genuine nonstationarity.

Therefore it cannot be called true drift without additional evidence.

## What survived the negative result

The observable itself was not discarded. The question was changed.

Instead of asking whether cross-scale disagreement **measures drift**, the later E8 experiment asked whether it can **predict spectral estimation error** in a controlled stationary regime. That narrower reliability hypothesis passed.

This distinction is fundamental to the current project framing:

- EXP-008 refuted a source interpretation;
- E8 supported an error-prediction interpretation under restricted conditions.

## Provenance status

This result is grounded in the authoritative project experiment ledger and project-state history. A separate byte-level EXP-008 archive has not yet been identified during the current migration.