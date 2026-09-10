# T12 — Theory-to-data bridge, local nonregularity, and spectral-risk intervals

T12 asks whether operator-level spectral-admissibility theory can be connected to finite-data Koopman/EDMD estimation.

The sequence is deliberately staged. Each extension is allowed only after the previous, easier assumption has been tested.

---

## T12-A1 — Oracle-geometry sampling-law bridge

### Question

From **one iid transition-pair training sample**, can a plug-in finite-sample OLS error law estimate the probability that a fresh same-budget linear-EDMD estimate loses the selected `r=2` spectral object?

A1 estimates the sampling law from data but still evaluates spectral events around the **true operator geometry**. This is an explicit oracle limitation.

### Exact OLS sampling model

For iid Gaussian design,

- `S = X X^T ~ Wishart(Sigma,N)`;
- conditional on `S`, `Ahat-A` is matrix normal with covariance determined by `Q` and `S^-1`.

The oracle target uses true `(Sigma,Q)`. The plug-in prediction uses one pilot's `(Sigma_hat,Q_hat)`.

### Result

All 36 conditions were active and supported.

FULL_FAIL probability calibration:

- MAE `0.0070125`;
- RMSE `0.0095004`;
- Spearman `0.87568`;
- mean bias `+0.000368`.

All frozen support gates passed.

**Verdict: T12-A1 ORACLE-GEOMETRY SAMPLING-LAW BRIDGE SUPPORTED in this iid linear-EDMD family.**

Projected boundary-event calibration was also strong:

- MAE `0.01073`;
- RMSE `0.01389`;
- Spearman `0.9465`.

### Critical practical limitation

The theorem-backed safe certificates were almost inactive at these finite-sample budgets (`N<=128`). The T10 pre-certificate probability was zero in all 36 oracle and predicted conditions, while the exact T9 certificate had mean oracle pass probability only about `1.1e-4`.

Thus A1 validates the **sampling-distribution-to-full-spectral-risk bridge**, not practical certificate coverage.

---

## T12-A2 — Fully data-centered iid risk

A2 removes the oracle spectral center. Prediction uses only

`(Ahat, Sigma_hat, Q_hat, N)`

and evaluates failure of `Ahat + Delta_star` under the plug-in OLS law. True `A` enters only the independent oracle target.

### Result

All 36 conditions were active.

- MAE `0.093606`;
- RMSE `0.114907`;
- Spearman `0.45380`;
- bias `-0.024844`;
- maximum absolute error `0.24125`.

The support criteria did not pass, but none of the frozen severe-failure thresholds was crossed.

**Verdict: T12-A2 FULLY DATA-CENTERED IID BRIDGE INCONCLUSIVE.**

### Mechanism control

Using the same plug-in covariance law but centering at true `A` gave:

- MAE `0.009692`;
- RMSE `0.012745`;
- Spearman `0.82728`;
- bias `-0.001286`.

Therefore the dominant A2 degradation was **spectral-center/geometry uncertainty**, not covariance-law estimation.

A descriptive signed-error association with the estimated `2|3` magnitude gap was strong (Spearman about `-0.788`).

---

## T12-A2b — Does larger N repair the point-centered risk estimate?

A2b changed only sample size, using fresh geometries and nested pilot prefixes

`N={64,128,256,512,1024}`.

No new correction, shrinkage, recentering, or recalibration was allowed.

### Result

All 10 geometries were paired-active at both `N=64` and `N=1024`.

- only `2/10` geometries improved from N=64 to N=1024;
- median absolute error increased from `0.08503` to `0.13830`;
- error ratio `1.626`;
- at N=1024 MAE `0.15240`;
- RMSE `0.17488`;
- bias `-0.05708`.

**Verdict: T12-A2b CENTER-CONVERGENCE REFUTED.**

Ordinary matrix estimation still converged: median `||Ahat-A||_F` decreased approximately

`0.4196 -> 0.2632 -> 0.1937 -> 0.1310 -> 0.0870`.

Thus matrix-center convergence did not translate into convergence of the point-centered spectral-risk functional over this range.

---

## Local-to-boundary nonregularity hypothesis

The working explanation is not a universal topological impossibility theorem. It is more specific.

Near a regular spectral-admissibility boundary, if the signed boundary distance is on the same `N^-1/2` scale as estimator fluctuations, then a point-centered estimate of a fresh-estimate failure probability can remain random even though the operator estimator itself is consistent.

Scalar analogy:

- admissibility coordinate `theta>0`;
- fresh estimator `theta_hat' = theta + sigma Z'/sqrt(N)`;
- target risk `p_N(theta)=Phi(-sqrt(N) theta/sigma)`;
- point-centered plug-in `p_hat=Phi(-sqrt(N) theta_hat/sigma)`.

For local alternatives `theta=c/sqrt(N)`, the target converges to `Phi(-c/sigma)` but the point-centered plug-in retains `O(1)` randomness.

The general nonregular-statistics ingredients are classical; the project-specific target is spectral-cut admissibility.

---

## T12-A2c — First local-to-boundary test

A controlled 4D block family was constructed with a pair-cut discriminant coordinate `phi(delta)=0.4 delta` and local alternatives

`phi(A_{N,c}) = c sigma_phi / sqrt(N)`.

Frozen grid:

- `c={-2,-1,0,1,2}`;
- `N={128,256,512,1024,2048,4096}`.

### Result

Implementation sanity passed, but at N=4096 only `3/5` c-values satisfied the frozen target-nondegeneracy requirement.

**Formal verdict: T12-A2c DESIGN-LIMITED INCONCLUSIVE.**

The central local regimes nevertheless showed strong descriptive nonconcentration, but this was not promoted to a confirmatory claim.

The fixed-distance control showed pointwise recovery, suggesting that the problem is specifically local to the spectral boundary rather than a generic OLS implementation failure.

---

## T12-A2c2 — Fresh local-to-boundary design extension

A2c2 preserved the same scientific hypothesis and frozen verdict gates, but used the narrower theory-motivated grid

`c={-1,-0.5,0,0.5,1}`

with fresh pilots, prediction banks, and target banks.

### Result

All five c-values remained target-nondegenerate at N=4096.

- pooled median absolute point-risk error at N=128: `0.118525`;
- at N=4096: `0.172225`;
- ratio `1.4531`;
- N=4096 IQR of point predictions across pilots: approximately
  `{0.3601,0.3715,0.4170,0.3901,0.2986}`;
- all `5/5` exceeded the frozen `0.10` nonconcentration threshold.

Direct-refit sanity passed.

**Verdict: T12-A2c2 LOCAL NONREGULARITY SUPPORTED.**

Meanwhile median `||Ahat-A||_F` contracted strongly with N:

`0.2908, 0.2056, 0.1434, 0.1000, 0.0702, 0.0508`.

This is a controlled matrix example where the operator estimate is consistent while the point-centered spectral-risk functional remains nonconcentrated under `O(N^-1/2)` approach to the pair-cut boundary.

It is not a universal theorem for all spectral boundary strata.

---

## T12-A3 — Center-uncertainty risk interval

A3 asked whether the appropriate local object is an **interval/distribution for spectral risk**, rather than another point estimate.

For a fresh boundary family, define the normalized local coordinate `c_hat`. Three summaries were reported:

1. naive point `Phi(-c_hat)`;
2. center-integrated point `Phi(-c_hat/sqrt(2))`;
3. a nominal 90% center-uncertainty risk interval obtained by mapping a Gaussian interval for the local center coordinate through the monotone risk map.

### Result

All 20 target cells were active.

Risk-interval coverage:

- pooled across 4000 pilot intervals: `0.93625`;
- by N = 512,1024,2048,4096: `0.957, 0.938, 0.930, 0.920`;
- at N=4096 c-specific coverages: `0.915,0.920,0.930,0.890,0.945`.

All frozen gates passed.

**Verdict: T12-A3 RISK-INTERVAL SUPPORTED.**

At N=4096, the normalized local coordinate had empirical mean about `0.0366` and SD about `0.9747`.

### Nonvanishing uncertainty

Median 90% risk-interval width remained about `0.796` at N=4096. This is expected in the local regime and is consistent with a local minimax barrier.

The center-integrated point reduced overall MAE from about `0.2074` to `0.1784`, but both point errors remained `O(1)`.

---

## Coordinate-free local boundary functional

For an isolated algebraic-multiplicity-two cluster with Riesz projector `P(A)`, define

`phi_R(A) = 2 tr(A^2 P(A)) - [tr(A P(A))]^2`.

For the two cluster eigenvalues this equals

`(lambda_a-lambda_b)^2`.

Hence locally:

- `phi_R>0`: two real eigenvalues;
- `phi_R<0`: complex conjugate pair;
- `phi_R=0`: repeated pair-cut boundary.

The derivative is

`D phi_R(A)[H] = 4 tr(P A H) - 2 tr(A P) tr(P H)`.

This formulation is similarity invariant and avoids differentiating individual eigenvalues at a defective point, provided the same isolated algebraic cluster remains defined.

---

## T12-A4 — First Riesz-chart transport test

A4 embedded the pair-cut boundary into six fresh non-normal 4D similarities and used a fixed contour to define the isolated cluster.

The frozen chart-support requirement was `>=0.995` in every cell.

At the tested N values, actual chart support was only about `0.61–0.76` at N=1024 and `0.89–0.94` at N=4096 in representative boundary cells.

**Verdict: DESIGN-LIMITED / CHART SUPPORT INSUFFICIENT.**

The contour was not retuned.

This is not a refutation of the Riesz functional or the local nonregularity theory.

---

## T12-A4b — High-N Riesz-chart transport

A4b kept the same scientific functional, contour, event definitions, and gates, while moving to

`N={16384,32768,65536}`

with fresh non-normal embeddings and sampling banks.

### Gate A — local event equivalence

The chart-support precondition was missed in exactly one cell:

- minimum support `0.99455`;
- frozen requirement `>=0.995`.

No rounding or threshold change was permitted.

**Gate A: formally DESIGN-LIMITED / MARGINALLY INCONCLUSIVE.**

Conditional/event-equivalence evidence was nevertheless extremely strong descriptively:

- MAE `|p_full-p_phi| = 0.000075`;
- maximum difference `0.00145`;
- all `90/90` cells within `0.02`.

### Gate B — risk-interval transport

All 90 cells were active.

- pooled coverage `0.90222`;
- mean coverage by geometry approximately
  `[0.9006,0.9067,0.9011,0.9133,0.8944,0.8972]`;
- at N=65536 all `6/6` geometries had pooled-over-c coverage above `0.80`.

**Recorded scientific verdict: A4b RIESZ RISK-INTERVAL TRANSPORT SUPPORTED ACROSS FRESH NONNORMAL EMBEDDINGS.**

Do not promote Gate A to PASS: one frozen support cell missed the threshold by `0.00045`.

### Provenance ceiling

A later independent recovery audit could not fully authenticate the original executable source/configuration and all exact source-dependent event/support implementations for the A4b/B1 extension sequence.

Therefore the A4b numerical interpretation is retained as **THEORY-LOG / PROVENANCE-LIMITED EVIDENCE**. It must not be presented as source-reproducible from the recovered archive. This provenance limitation does not by itself convert the recorded numerical result into a scientific refutation.

See `T12_provenance_status.md` for the exact distinction between A4b and the more severe T12-B1 provenance failure.

---

## Working local Riesz-boundary proposition

The evidence motivates, but does not yet fully prove, the following structure.

At a regular isolated pair-cut boundary stratum:

1. the Riesz cluster functional `phi_R` is a smooth signed local coordinate with nonzero derivative;
2. under a LAN estimator and `N^-1/2` local alternatives, the normalized estimated coordinate converges to a Gaussian shift experiment;
3. the fresh same-budget spectral-failure risk converges to a monotone Gaussian risk map;
4. no scalar point estimator can be uniformly consistent over a nontrivial compact local parameter set;
5. a valid confidence interval for the local coordinate maps to an asymptotically valid spectral-risk interval whose width need not vanish.

The statistical ingredients are classical. A publication-level proof still needs explicit uniformity conditions and control of leaving the isolated Riesz neighborhood / entering external ordering strata.

## T12 conclusion

The T12 sequence changes the interpretation of "spectral uncertainty" substantially:

- estimating the **sampling covariance** can be easy;
- estimating a **single point spectral-risk probability** can still be nonregular near the admissibility boundary;
- explicitly representing uncertainty in the spectral center can produce calibrated **risk intervals**;
- a coordinate-free Riesz boundary chart transports this picture across the tested non-normal embeddings in the structured numerical record when the isolated cluster remains supported, but the A4b executable provenance ceiling must remain explicit.

The remaining challenge is to extend this carefully beyond isolated linear pair-cut strata without losing provenance, identifiability, or claim discipline.
