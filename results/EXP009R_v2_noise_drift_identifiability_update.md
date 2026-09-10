# EXP-009R v2 — Noise-to-Drift Identifiability Audit

## Status

EXP-009 Gate 1 verdict remains:

**STRONG DECOMPOSITION NOT IDENTIFIABLE IN TESTED FAMILY**

EXP-009R v2 was a post-hoc mechanism audit using only existing frozen confirmatory data. No new simulations were generated.

## Main question

Can source attribution failure be explained by a ratio between true spectral drift and intrinsic estimation uncertainty?

\[
R = \frac{D_{true}}{U_E}
\]

where:

- `D_true` is true slow-subspace drift from the known VAR dynamics;
- `U_E` is a first-order spectral estimation uncertainty proxy.

## Result

The noise-to-drift ratio did not provide a clean identifiability boundary in the tested family.

Observed regime:

- true drift was generally smaller than the estimated uncertainty floor;
- therefore source attribution remained unresolved.

The result does not rescue Gate 1, but it refines the interpretation:

> spectral instability can indicate that a Koopman/EDMD estimate is unreliable, while the reason for unreliability may remain non-identifiable when dynamical drift is below the estimator uncertainty floor.

## Scientific interpretation

Positive:

- reliability signal survives;
- spectral error prediction remains possible.

Negative:

- source attribution from simple spectral instability diagnostics is not robust.

## Next direction

The next natural experiment is an identifiability phase diagram:

vary drift strength and measure the transition between:

- uncertainty-dominated regime;
- transition regime;
- drift-dominated regime.

The target hypothesis is a noise-limited identifiability boundary rather than a new classifier.

## Branch status

PRIMARY BRANCH: B

BRANCH A STATUS: UNCHANGED
