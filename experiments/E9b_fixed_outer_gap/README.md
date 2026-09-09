# E9b — Fixed-outer-gap cluster reliability confirmation

## Scientific role

E9b is the strongest controlled positive reliability experiment in the early branch of the project.

E9 had suggested that an invariant `r=2` spectral cluster is more reliable than tracking individual modes, but its stress test changed the inner and outer spectral gaps together. E9b removed that confound by holding the **true outer gap fixed at 0.27** while collapsing only the inner gap inside the selected two-dimensional cluster.

## Scientific question

Does a frozen cross-scale calibration

`S2 -> e2`

remain informative when the two leading modes become nearly degenerate, provided the selected two-dimensional cluster remains separated from the excluded spectrum?

Here:

- `S2` is the causal cross-scale Grassmann disagreement between the `H=256` and `2H=512` slow spectral clusters;
- `e2` is the oracle Grassmann error of the `H` cluster against the true slow two-dimensional subspace and is used only for evaluation.

Complex leading eigenpairs are represented by the invariant real span `span(Re(v), Im(v))`, so mode rotations and complexification inside the cluster do not by themselves destroy the target object.

## Design

All systems are stationary, diagonal, normal linear systems with stationary covariance `I`.

The true outer gap is fixed at `0.27` in every test condition. The inner gap is varied through:

- regular replication: `0.16`;
- stress conditions: `0.08`, `0.03`, `0.01`.

Only the untouched development-regular seeds were used to fit the isotonic calibration. No refitting occurred on the stress conditions.

## Untouched regular-gap replication

The independent regular condition reproduced the expected reliability signal:

- defined rate `0.996`;
- Spearman `0.505` with 95% CI approximately `[0.434, 0.573]`;
- AUROC `0.791`;
- quartile error ratio `2.224`;
- isotonic MAE improvement `18.3%`;
- median predicted/actual error `1.005`.

## Fixed-outer-gap stress results

| inner gap | defined rate | complex-pair rate | Spearman | AUROC | MAE improvement | median pred/actual |
|---:|---:|---:|---:|---:|---:|---:|
| 0.08 | 1.000 | 0.032 | 0.464 | 0.755 | 0.138 | 1.018 |
| 0.03 | 1.000 | 0.214 | 0.539 | 0.813 | 0.210 | 1.009 |
| 0.01 | 1.000 | 0.406 | 0.574 | 0.831 | 0.264 | 0.992 |

At the hardest `inner_gap=0.01` condition, the frozen gates were:

- B1 object existence: `1.0 >= 0.99` — pass;
- B2 association: Spearman `0.574`, lower CI `0.508` — pass;
- B3 calibration scale: median predicted/actual `0.992` within `[0.80,1.25]` — pass;
- B4 MAE improvement: `0.264 > 0.10` — pass;
- B5 calibration-domain support: `0.998 >= 0.90` — pass;
- numerical validity — pass.

## Verdict

**E9b CONFIRMATORY PASS.**

Within this stationary normal linear-EDMD family, a frozen cluster-level cross-scale reliability calibration remains informative even when the internal eigenvalue gap collapses, as long as the true outer cluster gap is preserved.

This is an important distinction: reliability of an invariant cluster need not deteriorate when individual modes inside that cluster become difficult to identify separately.

## Why this result matters

E9b established the positive control needed for the later falsification sequence:

1. cluster-level cross-scale reliability can work in a regular stationary setting;
2. inner-cluster mode ambiguity alone is not fatal when the cluster remains isolated;
3. E10 can therefore be interpreted as a genuine transport failure under non-normal geometry rather than as evidence that the basic reliability idea never worked.

The sequence `E9b -> E10 -> E11` is central:

- E9b: cluster reliability survives inner-gap collapse at fixed outer separation;
- E10: the same broad reliability picture does not transport unchanged under non-normality;
- E11: non-normality can destroy the selected spectral object's admissibility through pair cut/complexification.

## Alternative explanations retained

The positive result does not prove a universal uncertainty law. Shared dependence on the `H` estimate, finite-sample geometry, estimated-gap variability, surrogate-reference effects, and score-domain support can still influence calibration.

## Claim ceiling

E9b does **not** establish:

- a universal Koopman/EDMD uncertainty estimator;
- a new perturbation theorem;
- drift detection or drift/noise separation;
- non-normal or nonstationary transport;
- VAMP/nonlinear results;
- a universal adaptive-history rule.

## Reproducibility

The archived package contains full executable source, frozen calibration/configuration, development and untouched test rows, fixed-outer-gap stress rows, bootstrap summaries, frozen gates, plots, and audit reports.

Verified source SHA256:

`683c989136c2784b2e14990ff8a8916d649f3284026db2f112d61fc299d86e7f`

The source passed public-release screening for internal workflow references.