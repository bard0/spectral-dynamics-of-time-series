# EXP-007 — Broad causal online spectral benchmark

## Naming note

This is the **early broad online benchmark** recorded as `EXP-007` in the project ledger. It is distinct from the later `E7` null-calibrated directional diagnostic, which belongs to the subsequent reliability branch.

The two experiments are kept under separate directories to preserve the historical record rather than renumbering them retrospectively.

## Scientific role

EXP-007 compared a broad set of causal history-selection and spectral-stability ideas in an online nonstationary setting.

## Methods considered

- fixed short/medium/long windows;
- prediction-loss selection;
- Lepski-like nested-estimator selection;
- forgetting-factor EDMD;
- Grassmann-only criteria;
- spectral-gap-only criteria;
- VAMP-inspired lag stability;
- threshold/coherence-style horizons.

## Evaluation

The benchmark considered quantities such as oracle regret, tracking behavior, transition/regime detection, and spectral errors.

## Result

No robust evidence was obtained for a generally superior spectral history-horizon selector across the tested systems.

## Verdict

**INCONCLUSIVE / supports reframing away from generic adaptive-window claims.**

## Scientific consequence

EXP-007 was one of the experiments that made the original project framing untenable. The evidence did not support presenting the work as a new generic adaptive-window algorithm.

The project subsequently shifted toward the narrower question of **spectral reliability**: whether causal spectral diagnostics predict when a local estimate is inaccurate or poorly identifiable.

## Provenance status

This record is grounded in the authoritative experiment ledger. A byte-level archive for this early broad benchmark has not yet been identified during the current migration.