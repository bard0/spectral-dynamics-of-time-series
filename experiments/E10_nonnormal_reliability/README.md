# E10 — Frozen reliability calibration under stationary non-normality

## Scientific role

E10 is the transport falsification that forced the project to move from ordinary cross-scale error calibration toward explicit **spectral admissibility**.

E8/E9b had shown that cross-scale disagreement can carry useful reliability information in controlled stationary systems when spectral separation is regular. E10 asked whether a calibration learned in the normal regime still works when the spectrum and stationary covariance are held fixed but operator geometry becomes increasingly non-normal.

## Frozen question

Does a normal-regime mapping from cross-scale subspace disagreement `S2` to actual slow-subspace error `e2` transport across a covariance-neutral non-normal family?

## What was held fixed

- eigenvalues: `(0.70, 0.60, 0.50)`;
- inner and outer spectral gaps: `0.10`;
- target slow subspace `span(e1,e2)`;
- stationary covariance `I`;
- history sizes and estimator convention;
- normal-regime isotonic calibration after it was frozen.

## What changed

Non-normal operator geometry was varied through

```text
B(c) = [[0.7, 0,       0],
        [0,   0.6, -0.1c],
        [0,   0,     0.5]]
```

for `c = 0,2,4,6`.

The process-noise covariance `Q(c)=I-B(c)B(c)^T` necessarily changes to preserve stationary covariance `I`. This is part of the controlled design and is not hidden.

## Baseline replication

The normal test condition reproduced a useful reliability signal:

- `r2_defined_rate ≈ 0.77`;
- Spearman `≈ 0.461`, 95% CI approximately `[0.368, 0.546]`;
- AUROC `≈ 0.773`;
- isotonic MAE improvement `≈ 14.4%`;
- median predicted/actual error ratio `≈ 1.042`.

Thus the transport test was not simply failing because the baseline calibration was already useless.

## Frozen non-normal transport result

**E10 NONNORMAL TRANSPORT FAIL.**

**RANKING ALSO FAILS** under the frozen hardest-condition criterion.

Selected summary values:

| c | true `kappa(V)` | defined rate | Spearman | median predicted/actual | MAE improvement |
|---:|---:|---:|---:|---:|---:|
| 2 | 4.236 | 0.518 | 0.406 | 1.170 | 0.153 |
| 4 | 8.123 | 0.430 | 0.207 | 1.227 | 0.201 |
| 6 | 12.08 | 0.416 | 0.284 | 1.278 | 0.348 |

At `c=6`, the frozen gates failed because:

- the selected `r=2` object existed in only about `41.6%` of realizations, far below the required support;
- held-out ranking dropped below the frozen threshold;
- calibration ratio moved outside the frozen acceptable interval.

The high apparent MAE improvement among surviving rows does not rescue the experiment: the target object itself disappears too often, so conditional survivor calibration is no longer an adequate reliability statement.

## Scientific interpretation

E10 showed that a calibration learned in a normal, regular regime does **not** transport unchanged through this tested non-normal family, even though eigenvalues, nominal gaps, target subspace, and stationary covariance are controlled.

The most important observation was the collapse in object existence. This suggested that non-normality may change the problem qualitatively:

> the selected spectral object can cease to be admissible rather than merely become noisier.

That observation motivated E11, which removed trajectories and estimation effects and applied identical operator perturbations directly. E11 then supported pair-cut/complexification as a mechanism for the object-existence collapse.

## Alternative explanations retained after E10

E10 alone could not uniquely attribute transport failure to pure operator geometry because finite-sample estimation remained present. Relevant possibilities included:

- changing process-noise covariance needed for covariance neutrality;
- finite-sample excitation and Gram conditioning;
- shared dependence between nested estimates;
- surrogate-reference effects;
- support shift;
- non-normal/pseudospectral sensitivity.

This is why E11 was necessary.

## Claim ceiling

E10 supports only a controlled transport-failure statement. It does **not** establish:

- a universal theorem about non-normality;
- failure of Koopman uncertainty quantification in general;
- a new pseudospectral correction;
- drift-versus-estimation decomposition;
- nonlinear Koopman/VAMP results;
- nonstationary validation;
- a universal adaptive-history rule.

## Reproducibility

The archived package contains full executable source, frozen calibration/configuration, all 2,500 trajectory-level rows split across the development/normal/non-normal conditions, frozen gate outputs, audit tables, and figures.

Verified source SHA256:

`52537ac03793b690b542910c6002d535175543771ff44be885f18ba66fab2d8d`

The source passed public-release screening for internal workflow references.