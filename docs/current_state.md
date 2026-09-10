# Current Scientific State

## Central question

The active project is **causal spectral reliability and spectral admissibility for local Koopman/EDMD models of time series**.

Three questions are now kept separate:

1. **Reliability:** how inaccurate or fragile is the currently estimated slow spectral object?
2. **Admissibility:** does the intended selected spectral object remain well defined under finite estimation/operator perturbations?
3. **Source attribution:** if the estimate moves, can that motion be attributed to finite-sample estimation error rather than genuine evolution of the dynamics?

The experiments show that reliability/admissibility can be tractable in controlled regimes even when source attribution is not identifiable from the same causal observables.

## Core causal diagnostics

For a history horizon `H` and current time `t`, the data-level branch has used

\[
S_{scale}(H,t)=d_G(E_H(t),E_{2H}(t)),
\]

\[
S_{time}(H,t)=d_G(E_H(t),E_H(t-\Delta)),
\]

and

\[
D_K(H,t)=\|K_H(t)-K_H(t-\Delta)\|_F.
\]

`S_scale` must not automatically be called statistical uncertainty or true drift. It mixes finite-sample error, scale inconsistency, spectral separation, non-normal sensitivity, model mismatch, and nonstationarity.

---

# Confirmed or strongly supported results

## Invariant-subspace comparisons are preferable to raw eigenvectors

A mode-swap sanity check produced Grassmann distance on the order of `1e-14` while individual-vector overlap could fall to about `0.13`. This motivated cluster/subspace-based evaluation throughout the later reliability branch.

## Cross-scale disagreement predicts error in a controlled regular-gap regime

E8 stationary regular-gap linear-EDMD benchmark:

- Spearman with actual spectral error ≈ `0.51`;
- AUROC ≈ `0.79`;
- high/low error quartile ratio ≈ `2.34`;
- isotonic calibration reduced MAE by roughly `21%`.

This is a controlled-regime result, not universal calibration.

## Cluster reliability is more robust than individual-mode reliability

E9b used an invariant two-dimensional spectral cluster with fixed outer separation. In the hardest primary condition:

- support ≈ `99.8%`;
- Spearman ≈ `0.574`;
- AUROC ≈ `0.831`;
- median predicted/actual error ≈ `0.992`;
- MAE improvement ≈ `26%`.

Complex leading eigenpairs occurred frequently while the invariant two-dimensional subspace remained well defined.

## Non-normality creates an object-existence failure mode

E10 showed that normal-regime reliability calibration did not transport unchanged across non-normal systems. E11 then isolated the mechanism:

- probability that the intended `r=2` real/conjugation-closed object remained defined fell strongly with non-normality;
- conditional Grassmann error among surviving objects did not increase and often decreased;
- the dominant failure mechanism was perturbation-induced pair-cut complexification across the selected cluster boundary.

This shifted the target from survivor error alone to **spectral admissibility**.

## Global conditioning is not sufficient

E13a found a strong exploratory condition-level relationship between estimated eigenvector conditioning and latent admissibility risk in one triangular non-normal VAR family.

E14a then falsified sufficiency: with eigenvalues, gaps, perturbation scale, and global conditioning matched, moving non-normal coupling across the retained/excluded `2|3` boundary changed pair-cut failure probability substantially.

## A fixed boundary-resolvent scalar is informative but not sufficient

E15 froze

\[
R_b=\|(0.55I-A)^{-1}\|_2
\]

in a fresh four-dimensional family.

After correcting a reporting-orientation error:

- nuisance-matched, resolvent-separated pairs supported the predicted risk direction in `8/8` comparisons;
- corrected high-minus-low integrated-risk effects were approximately `0.107–0.122`;
- but resolvent-matched pairs with ratio about `1.00089` still showed risk differences around `0.154–0.171` when other geometry differed.

Therefore:

> `R_b` carries information but is **not sufficient or transportable as a standalone admissibility-risk variable**.

## Exact projected boundary law survives fresh falsification

For the `2|3` projected boundary, define

\[
D_5=[g+\varepsilon(E_{22}-E_{33})]^2+4\varepsilon^2E_{23}E_{32}.
\]

Projected complexification is `D5 < 0`.

Under Frobenius-isotropic fixed-norm perturbations, the population probability can be reduced to a low-dimensional angular/radial law.

Fresh T6 validation over 252 cells:

- MAE `0.002247`;
- RMSE `0.003246`;
- max absolute error `0.011883`;
- `249/252 = 98.81%` of theoretical probabilities inside exact 99% binomial intervals.

**T5 survives fresh operator-family falsification for the projected `2x2` event.**

## Classical invariant-graph certificate identifies a useful regime

A second-order effective boundary model failed as a global finite-epsilon predictor (T7), and a fixed empirical validity threshold was not supported (T8).

T9 instead used a theorem-backed Riccati/Sylvester sufficient condition

\[
\mathrm{sep}_F^2>4bc.
\]

In 34 evaluable certified cells:

- T7 improved on T5 in `26/34 = 76.47%`;
- conditional MAE T5 `0.01285` vs T7 `0.00745`;
- ratio `0.5796`, about `42%` reduction.

**T9 certified-regime supported** in the controlled fresh family.

The certificate itself is classical and is not claimed as a new perturbation theorem.

## Probabilistic certificate geometry is useful but strongly dependent on boundary risk

T10 derived a conservative pre-certificate probability curve `q0(epsilon)` from a directionwise susceptibility CDF. It retained a substantial fraction of the exact T9 certificate probability in a fresh family, but the independence approximation `q0 * p5` was decisively refuted.

T11 then derived an exact shared-radial representation of the joint certificate/boundary event. Fresh test:

- 75 active cells;
- MAE `0.000553`;
- RMSE `0.000732`;
- maximum error `0.00222`.

The theorem-backed safe core also transported:

- 240 eligible cells;
- median `P(S_safe|C0) ≈ 0.898`;
- `90.42%` of eligible cells had safe fraction at least `0.35`.

Thus the joint geometry is structured and tractable in the controlled isotropic setting, but it is not reducible to the three projected boundary variables alone in general.

## OLS sampling law can calibrate spectral failure when the center is known

T12-A1 tested an iid linear-EDMD/OLS theory-to-data bridge. One pilot dataset estimated the finite-sample OLS perturbation law, while the true operator supplied the spectral center/geometry.

Across 36 active conditions:

- FULL_FAIL MAE `0.00701`;
- RMSE `0.00950`;
- Spearman `0.8757`;
- mean bias `+0.00037`.

**T12-A1 supported** for the stated controlled iid family.

The practical limitation is that the theorem-backed safe certificates had essentially zero coverage at `N<=128`; what passed was the sampling-distribution-to-full-risk bridge, not certificate practicality.

## Local-to-boundary point risk is nonregular in the controlled matrix family

A fully data-centered one-center plug-in risk estimate was inconclusive at moderate N (A2), and a larger-N extension refuted the hypothesis that merely increasing N to `1024` repairs it (A2b), despite ordinary matrix-center convergence.

A fresh local-to-boundary design A2c2 then kept risks nondegenerate under an `O(N^{-1/2})` approach to the pair-cut boundary.

Results:

- matrix estimation error contracted strongly with N;
- point-centered spectral-risk error did not contract;
- predicted-risk dispersion across pilots remained large at `N=4096`.

**A2c2 local nonregularity supported** in this controlled matrix setting.

## Carrying center uncertainty yields calibrated risk intervals

T12-A3 replaced the unstable point-risk target by a center-uncertainty risk interval.

Across 4,000 fresh intervals:

- nominal 90% pooled coverage `0.93625`;
- coverage by N approximately `0.957`, `0.938`, `0.930`, `0.920`;
- all local-coordinate coverages at `N=4096` were at least `0.89`.

**T12-A3 risk interval supported** in the controlled local matrix family.

## Riesz-chart transport: scientific result retained, source provenance limited

The structured theory log records a high-N A4b test across six fresh non-normal embeddings. One of 90 cells marginally missed the frozen chart-support requirement (`0.99455` versus `0.995`), so the chart/event gate is formally design-limited. The independent risk-interval gate had pooled coverage about `0.902` with geometry-level coverage roughly `0.894–0.913`.

A later recovery audit could not fully authenticate the original executable source/configuration and exact source-dependent event/support implementations for the A4b/B1 extension sequence.

Therefore A4b is retained as **theory-log / provenance-limited evidence**, not as a source-reproducible run. T12-B1 is more severe and is **provenance-invalidated / not claim-ready**. The next valid stationary correlated-trajectory replication must use the new identifier `T12-B1R` and freeze complete executable provenance before outcomes.

---

# Strong negative / limiting results

## Nested disagreement is not a direct drift proxy

\[
d_G(E_H,E_{2H})
\]

correlates poorly with true dynamical drift in controlled nonstationary systems. The original direct "coherence horizon" interpretation was abandoned.

## Generic adaptive-horizon superiority was not established

Across fixed-window, Lepski-like, prediction-loss, forgetting, gap-based, Grassmann-based, and related causal selectors, no method showed robust general superiority across the tested systems.

## A simple conditioning-normalized law is not universally calibrated

E12 score `kappa * epsilon / gap` ranked held-out failure relatively well (AUROC around `0.83`) but failed the frozen calibration/log-loss criterion.

## E13 single-replicate target was design-limited

Predicting an independent validation Bernoulli outcome from a probe estimate had an oracle ceiling below the preregistered success gates. E13 is therefore a design-limited negative, not a branch-stopping refutation of latent risk prediction.

## T7 global second-order predictor failed strongly

When T5 curves were matched but T7 predicted large risk differences, fresh full admissibility outcomes produced `0/6` supporting pairs and `4/6` decisive reverses. T7 was substantially worse than T5 at moderate/larger perturbations.

## Strong source decomposition failed in EXP-009 Gate 1

After pilot redesign achieved matched observable-instability magnitude, the frozen confirmatory test used 4,000 fresh trajectories and 3,982 supported rows.

Held-out AUROCs:

- `S_scale`: `0.484`;
- `S_time`: `0.467`;
- temporal operator difference: `0.513`;
- gap: `0.482`;
- joint scale-time: `0.467`;
- full joint: `0.470`.

Joint scale-time added value was approximately `-0.0167` with bootstrap 95% interval `[-0.0698, 0.0023]`.

Frozen verdict:

> **Strong decomposition of finite-sample estimation instability versus smooth true drift is not identifiable from the tested causal diagnostics in this controlled matched-overlap family.**

At the same time, `S_scale` retained Spearman correlation around `0.51` with true slow-subspace estimation error.

This separates **error prediction** from **source attribution**.

---

# Current branch structure

## Branch A — spectral admissibility theory

Current focus:

- exact/projected boundary failure laws;
- theorem-backed invariant-graph safe regimes;
- finite-sample sampling distributions;
- nonregular center uncertainty near the spectral boundary;
- calibrated risk intervals;
- provenance-clean transport from iid transitions to one correlated trajectory.

The next trajectory experiment is `T12-B1R`, a reconstructed/re-frozen stationary correlated-trajectory Riesz risk-interval test.

See `branch_A_spectral_admissibility.md`.

## Branch B — causal reliability

Current focus:

- calibrated spectral error/risk prediction rather than source classification;
- data-estimable admissibility/support diagnostics;
- reliability envelopes for temporal spectral motion;
- explicit limits of causal source attribution;
- adaptive history only after reliability calibration survives.

See `branch_B_causal_reliability.md`.

---

# Current working interpretation

The evidence supports the following hierarchy:

1. spectral error can sometimes be predicted from causal cross-scale information;
2. reliability calibration depends on spectral separation and operator geometry;
3. non-normality can destroy spectral-object identity rather than simply increase survivor error;
4. global conditioning and one scalar resolvent discard important boundary-local information;
5. the projected boundary-complexification event has a strong exact probabilistic structure in controlled perturbation families;
6. finite-order approximations need theorem-backed validity regimes rather than empirical global thresholds;
7. learning the finite-sample perturbation law is easier than handling uncertainty in the spectral center itself;
8. near a spectral boundary, honest uncertainty intervals can be more appropriate than one-center point risk;
9. observable instability magnitude does not uniquely encode whether the underlying cause is estimation noise or genuine drift;
10. adaptive history selection remains downstream.

## Claim ceiling

The project does **not** currently claim:

- a universal Koopman/EDMD uncertainty estimator;
- a universal non-normal spectral-risk law;
- a new generic adaptive-window algorithm;
- general identifiability of estimation noise versus dynamical drift;
- novelty of classical Riccati/Sylvester, resolvent, pseudospectral, or nonregular-inference theory;
- nonlinear or general nonstationary validity of the controlled linear results;
- source-level reproducibility for provenance-limited T12-A4b;
- claim-ready correlated-trajectory evidence from provenance-invalidated T12-B1.

The strongest current niche is **causal/data-driven reliability and admissibility of selected slow spectral objects, together with explicit mechanisms, provenance ceilings, and identifiability limits**.
