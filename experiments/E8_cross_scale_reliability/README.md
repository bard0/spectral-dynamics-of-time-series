# E8 — Cross-scale spectral reliability in a regular-gap stationary regime

## Scientific role

E8 is the first controlled positive experiment showing that causal cross-scale spectral disagreement can carry information about **actual spectral estimation error**.

It came immediately after the project abandoned the interpretation of nested-window disagreement as a direct measure of true dynamical drift. The scientific target changed from

> "does disagreement measure drift?"

to

> "does disagreement predict whether the current spectral estimate is inaccurate?"

## Scientific question

In a stationary linear-EDMD regime with regular spectral separation, is the cross-scale disagreement between nested estimates informative about true spectral/subspace estimation error?

## Result

**PASS in the tested regular-gap stationary linear-EDMD regime only.**

Authoritative experiment-ledger metrics:

- Spearman correlation ≈ `0.5098`, 95% interval ≈ `[0.4404, 0.5767]`;
- AUROC ≈ `0.7883`, interval ≈ `[0.7393, 0.8339]`;
- high/low error quartile ratio ≈ `2.340`, interval ≈ `[2.043, 2.686]`;
- isotonic calibration MAE improvement ≈ `20.8%`, interval ≈ `[15.2%, 26.3%]`.

## Interpretation

The safe conclusion is narrow:

> Cross-scale reliability carried meaningful predictive information about spectral estimation error in the tested stationary regular-gap setting.

This is **not** the same as saying that cross-scale disagreement is true dynamical drift or a general statistical confidence radius.

## Transport limitation

When spectral-gap conditions changed, transport degraded. Complex modes and systematic underprediction appeared as failure mechanisms.

This limitation motivated the move from individual-mode reliability toward invariant spectral clusters in E9/E9b.

## Relation to later experiments

- E8: cross-scale error prediction works in one regular regime.
- E9: individual modes become fragile under inner-gap collapse while a two-dimensional cluster remains more stable.
- E9b: cluster reliability survives inner-gap collapse when the outer cluster gap is fixed.
- E10: the regular-regime calibration does not transport unchanged into a non-normal family.

Thus E8 is a positive control, not the final reliability claim.

## What E8 does not establish

E8 does not establish:

- direct measurement of true dynamical drift;
- a universal uncertainty estimator;
- a universal calibrated risk law;
- transport across arbitrary spectral gaps;
- non-normal or nonstationary validity;
- a general adaptive-history rule.

## Provenance status

The experiment is recorded in the authoritative project experiment ledger with the metrics above. The original package is named in project history as:

`koopman_E8_cross_scale_reliability.zip`

The byte-level archive is **not currently locatable through the connected Drive metadata search**, so this GitHub directory is intentionally labeled as a historical scientific record rather than a fully migrated reproducibility package.

No source code or artifact hashes are invented here. They should be added only if the original archive is recovered.