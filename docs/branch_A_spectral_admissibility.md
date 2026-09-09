# Branch A — Theory of Spectral Admissibility

## Goal

Develop a mathematical description of when a **preselected slow spectral cut or invariant spectral object** remains admissible under finite perturbations of an estimated operator.

This branch arose after the reliability experiments showed that non-normality can destroy the identity of the selected spectral object before conditional survivor subspace error becomes large.

The branch is operator-level. Its results do not automatically imply a causal data-level diagnostic.

## Starting point

Let

\[
A=V\Lambda V^{-1}, \qquad A_\varepsilon=A+\varepsilon D,
\]

and express the perturbation in the eigenbasis,

\[
E=V^{-1}DV.
\]

For a selected `r=2` cut, the critical retained/excluded boundary is the pair `(2,3)`.

Define

\[
Y=E_{23}=w_2^T D v_3,
\qquad
Z=E_{32}=w_3^T D v_2.
\]

The central question is not merely how far the invariant subspace rotates, but whether the selected spectral object stays well defined under the perturbation.

---

# T4 — Dangerous-sign probability

For isotropic Gaussian perturbation directions before radial normalization,

\[
\rho_{23}=\operatorname{Corr}(Y,Z)
=\frac{(w_2^T w_3)(v_3^T v_2)}{\|w_2\|\,\|w_3\|\,\|v_2\|\,\|v_3\|}.
\]

The sign event is invariant to positive radial normalization, giving

\[
P(E_{23}E_{32}<0)=\frac{\arccos(\rho_{23})}{\pi}.
\]

This law exactly explained the approximately `0.50` versus `0.87` dangerous-sign fractions observed in the canonical matched-resolvent counterexample from E15-R.

**Interpretation.** Directional correlation across the selected boundary contains information that a global conditioning scalar discards.

---

# T5 — Exact projected boundary-complexification law

For the projected `2x2` boundary block, define

\[
\operatorname{Disc}_\varepsilon
=
[g+\varepsilon(E_{22}-E_{33})]^2
+4\varepsilon^2E_{23}E_{32},
\]

where `g=lambda_2-lambda_3`.

Projected complexification occurs when

\[
\operatorname{Disc}_\varepsilon<0.
\]

The perturbation coordinates can be reduced to a spherical-angular variable and an independent Beta-distributed radial variable. This yields an exact finite-dimensional population expression for the projected boundary-complexification probability under Frobenius-isotropic fixed-norm perturbation directions.

## Frozen-data numerical falsification

Against the already archived E15/E15-R perturbation bank:

- MAE about `0.00325`;
- RMSE about `0.00474`;
- maximum absolute discrepancy about `0.0170`;
- `269/280 = 96.1%` of theoretical probabilities lay inside cellwise exact 95% binomial intervals.

Because the same perturbation bank was reused across cells, the interval coverage is descriptive rather than an independent coverage test.

## T6 fresh falsification

A fresh operator family and fresh perturbation banks were then used.

Across 36 selected operators:

- T4 dangerous-sign law: MAE about `0.00311`, maximum discrepancy about `0.00976`;
- T5 over `36 x 7 = 252` operator/epsilon cells: MAE `0.002247`, RMSE `0.003246`, maximum error `0.011883`;
- `249/252 = 98.81%` of theoretical T5 probabilities lay inside exact 99% binomial intervals.

**Verdict.** T5 **survived fresh operator-family falsification for the projected `2x2` boundary event**.

A secondary hypothesis that the residual full failure beyond T5 could be summarized by total external modal susceptibility was inconclusive. Five of six pair effects had the expected sign, but the median effect missed the frozen support threshold and one pair was a decisive reverse. Aggregate external amplitude is therefore not an adequate explanation.

---

# T7 — Second-order external-mode correction

A near-identity block-diagonalization gives a second-order effective boundary block. Static numerical unit tests showed the boundary-eigenvalue approximation error scaling approximately as `O(epsilon^3)`, consistent with the algebraic expansion.

The important question was whether the second-order effective discriminant improves prediction of **full top-2 admissibility failure** beyond T5.

## T7-F fresh falsification

Six operator pairs were selected before outcomes so that T5 risk was closely matched while T7 predicted substantially different risk.

Fresh results, high-T7 minus low-T7 full-risk AUC:

- pair 1: `-0.04065` — decisive reverse;
- pair 2: `-0.06545` — decisive reverse;
- pair 3: `+0.00057` — ambiguous;
- pair 4: `-0.04986` — decisive reverse;
- pair 5: `-0.07250` — decisive reverse;
- pair 6: `-0.02067` — ambiguous under the frozen threshold.

Support count: `0/6`. Decisive reverses: `4/6`.

Secondary model audit:

- T7 improved absolute AUC error in `0/12` operators;
- cellwise MAE to full risk: T5 `0.02892` vs T7 `0.10901`;
- cellwise RMSE: T5 `0.03848` vs T7 `0.14297`.

T7 was better than T5 only at the smallest perturbations and deteriorated strongly at moderate/larger epsilon.

**Verdict.** **T7-F FAIL.** The second-order expansion is asymptotically meaningful but is falsified as a global finite-epsilon predictor of full top-2 admissibility.

---

# T8 — Empirical validity-regime hypothesis

The next hypothesis introduced

\[
\eta_{mix}(D,\varepsilon)=\varepsilon\|K_1(D)\|_2
\]

and an operator-level median coordinate `eta50` to identify a perturbative regime.

The frozen low-regime threshold required a substantial T7 improvement; the high-regime threshold predicted systematic T7 breakdown.

Fresh result:

- LOW regime: T7 was directionally better in `19/26 = 73.08%` of evaluable cells, but MAE ratio was `0.7898`, failing the required `<=0.70` gate;
- HIGH regime: T7 was worse in `39/39` evaluable cells; MAE ratio was about `6.03`;
- descriptive Spearman between `eta50` and T7-minus-T5 error was about `0.8405`.

**Verdict.** **T8 VALIDITY REGIME NOT SUPPORTED.** The proposed universal threshold was not validated, although the coordinate remained descriptively related to breakdown severity.

---

# T9 — Riccati/Sylvester certified regime

Rather than tune another empirical threshold, the project moved to a theorem-backed sufficient condition for a nearby invariant graph.

Partition the eigenbasis into boundary block `B={2,3}` and external block `O={1,4}`. Let `sep_F` be the smallest singular value of the Sylvester operator, and let `b,c` measure cross-block perturbation magnitudes.

The frozen sufficient certificate was

\[
\operatorname{CERT}=1
\quad\Longleftrightarrow\quad
\operatorname{sep}_F^2>4bc.
\]

In fresh data, 34 certified cells were evaluable:

- T7 had smaller conditional probability error than T5 in `26/34 = 76.47%`;
- conditional MAE: T5 `0.0128457`, T7 `0.00744569`;
- MAE ratio `0.5796`, roughly a `42%` reduction.

All frozen gates passed.

**Verdict.** **T9 CERTIFIED-REGIME SUPPORTED** in the controlled fresh family.

The certificate pass fraction shrank automatically with epsilon, from about `0.975` at `0.0025` to about `0.080` at `0.04`.

**Important ceiling.** The Riccati/Sylvester certificate is classical. The result is not a novelty claim for invariant-subspace perturbation theory; it shows that a classical sufficient condition identifies a subset where the second-order boundary approximation is empirically useful for the continued boundary-cluster event.

---

# T10 — Probabilistic pre-certificate

A stronger but epsilon-separable sufficient event was derived from the unperturbed Sylvester separation `s0`:

\[
\varepsilon Z(D)<s_0,
\qquad
Z(D)=d(D)+2\sqrt{b_0(D)c_0(D)}.
\]

This defines

\[
q_0(\varepsilon)=P[Z<s_0/\varepsilon].
\]

## Fresh result

- zero implication violations of the pre-certificate into the exact T9 certificate;
- 94 cells with exact certificate probability at least `0.20`;
- median `q0/q_cert = 0.7451`;
- fraction with `q0/q_cert >= 0.40`: `0.7766`.

**Verdict.** The pre-certificate was **useful in this fresh family**, although increasingly conservative as epsilon grew.

## Independence approximation falsified

The approximation

\[
P(C_0\cap B_5)\approx q_0 p_5
\]

failed decisively:

- MAE `0.03126`;
- RMSE `0.03727`;
- maximum error `0.08228`;
- `26.32%` of active cells had error above `0.05`.

Moreover, `p_joint - p_prod` was negative in every active cell, and the median ratio

\[
P(B_5\mid C_0)/P(B_5)
\]

was only about `0.045`.

**Consequence.** The certificate and dangerous boundary event share geometry and cannot be modeled as independent marginal probabilities.

---

# T11 — Joint certificate/boundary geometry

T11 derived a shared-radial representation of the joint event under Frobenius-isotropic perturbations. A scalar identity component can be separated, leaving a traceless angular direction and a Beta-distributed radial factor.

Two structural results matter:

1. the radial variable can be integrated analytically in the joint `C0 ∩ B5` probability;
2. the certificate susceptibility is **not generically determined by the three T5 boundary variables alone**, so an exact universal three-variable reduction is impossible without additional structure.

A theorem-backed safe event was also derived that excludes projected boundary complexification.

## T11-F fresh result

Fresh geometry varied both the boundary gap and the external Sylvester separation independently.

Primary shared-radial test:

- active cells: `75/384`;
- MAE `0.0005527`;
- RMSE `0.0007317`;
- maximum absolute error `0.0022223`.

All frozen support gates passed.

Safe-core transport:

- 240 cells with `q0 >= 0.20`;
- median `P(S_safe | C0) = 0.8982`;
- `90.42%` of eligible cells had safe fraction at least `0.35`.

**Verdicts.**

- **T11 SHARED-RADIAL LAW SUPPORTED IN THE FRESH FAMILY.**
- **SAFE-CORE PRACTICALLY USEFUL IN THE FRESH FAMILY.**

The safe fraction depended strongly on the ratio of boundary gap to external separation, as expected from the theorem.

---

# T12 — Theory-to-data bridge

After the operator-level theory became coherent enough, the project asked whether finite-sample EDMD/OLS estimation error distributions can be learned well enough from data to calibrate spectral-admissibility risk.

## T12-A1 — Sampling law with oracle spectral center

One iid transition dataset per condition was used to estimate the OLS sampling law, while the true operator supplied the spectral center/event geometry.

Across 36 active conditions:

- FULL_FAIL probability MAE `0.00701`;
- RMSE `0.00950`;
- Spearman `0.8757`;
- mean bias `+0.00037`.

All frozen gates passed.

Projected T5 risk was also well calibrated descriptively: MAE about `0.0107`, Spearman about `0.9465`.

**Verdict.** **T12-A1 SUPPORTED** for full `r=2` failure probability in the controlled iid linear-EDMD family when the true spectral center/geometry is supplied.

**Critical limitation.** T9/T10 safe certificates were essentially inactive at `N <= 128`; what passed was the sampling-distribution-to-full-risk bridge, not practical certificate coverage.

## T12-A2 — Fully data-centered plug-in risk

The true spectral center was removed. Risk was predicted around the pilot estimate `Ahat` using only the estimated sampling law.

Across 36 conditions:

- MAE `0.09361`;
- RMSE `0.11491`;
- Spearman `0.4538`;
- mean bias `-0.02484`.

The support gates were not met, but the severe-failure gates were also not crossed.

**Verdict.** **T12-A2 INCONCLUSIVE.**

The oracle-center control using the same estimated covariance law was excellent, showing that most degradation came from **uncertainty in the spectral center/geometry**, not from estimating the covariance law itself.

## T12-A2b — Does larger N fix the point-centered estimator?

With fresh geometries and sample sizes from `64` to `1024`, only `2/10` geometries improved from the smallest to largest N. Median absolute calibration error increased from `0.0850` to `0.1383`, while matrix estimation error itself decreased strongly.

**Verdict.** **CENTER-CONVERGENCE REFUTED** over the tested range. Better matrix estimation did not automatically repair the point-centered spectral-risk functional.

## T12-A2c / A2c2 — Local-to-boundary nonregularity

The first local-to-boundary design was inconclusive because the chosen local grid became too degenerate at the largest N.

A fresh, narrower, predeclared grid then kept all target risks nondegenerate.

At `N=4096`:

- pooled median point-centered risk error was larger than at `N=128` rather than smaller;
- the IQR of predicted risk across pilots remained large for every local coordinate;
- meanwhile median `||Ahat-A||_F` contracted strongly with N.

**Verdict.** **T12-A2c2 LOCAL NONREGULARITY SUPPORTED.**

This provides a controlled matrix example in which the ordinary matrix estimator is consistent while the point-centered spectral-risk functional remains nonconcentrated under an `O(N^{-1/2})` approach to the pair-cut boundary.

This is a local matrix analogue of classical nonregular estimation phenomena, not a claim of a new general impossibility principle.

## T12-A3 — Risk interval carrying center uncertainty

Rather than insist on a single point risk estimate, the next test propagated center uncertainty into a risk interval.

Across 4,000 fresh pilot intervals:

- nominal 90% pooled coverage `0.93625`;
- coverage by N: approximately `0.957`, `0.938`, `0.930`, `0.920`;
- at `N=4096`, every local-coordinate coverage exceeded `0.89`.

The local Gaussian chart was also well calibrated (`z` mean near zero, SD near one).

**Verdict.** **T12-A3 RISK-INTERVAL SUPPORTED.**

The scientific lesson is that near a spectral-admissibility boundary, an honest uncertainty set may remain informative even when a point-centered risk estimate cannot concentrate uniformly.

## T12-A4 / A4b — Nonnormal Riesz-chart transport

The first transport design used a fixed contour around the boundary pair embedded through non-normal similarities. Chart support was insufficient at the planned sample sizes, so the experiment stopped as **DESIGN-LIMITED**, not as a falsification.

A high-N extension was then run on fresh non-normal embeddings while retaining the same contour and event definitions. Its role is to test transport of the isolated local pair-cut chart once the fixed neighborhood is actually entered; it does not cover interacting spectral-boundary strata or nonlinear EDMD.

## T12-B1 historical correlated-trajectory test

A stationary correlated-VAR risk-interval experiment produced encouraging historical numerical coverage, but a later provenance audit found that the original executable source, configuration, and exact event definitions were not recoverable from the archived artifacts.

**Current status.** Historical numerical result is **NOT CLAIM-READY / provenance-invalidated**. It must not support a paper claim until a fully reconstructed, re-frozen experiment is executed with complete provenance.

---

# Current Branch-A interpretation

The branch has ruled out several tempting scalar shortcuts while retaining a narrower mathematical structure:

- global conditioning is insufficient;
- one fixed resolvent value is insufficient;
- a second-order boundary model is not a global finite-epsilon predictor;
- an empirical perturbative threshold is not validated;
- a classical Riccati/Sylvester certificate does isolate a regime where the second-order model is useful;
- the projected `2x2` boundary probability admits an accurate exact finite-dimensional law under isotropic perturbations;
- certificate and boundary-complexification events are strongly dependent;
- near a spectral-admissibility boundary, point-centered data-level risk estimation is nonregular, while uncertainty intervals can remain calibrated.

The remaining bridge to practical time-series analysis is to estimate the required geometry and sampling uncertainty from causal data without relying on oracle spectral centers and without losing calibration near the boundary.