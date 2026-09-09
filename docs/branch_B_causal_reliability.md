# Branch B — Causal Reliability and Adaptive History Horizons

## Goal

Develop a causal, data-level framework for deciding whether an observed local spectral estimate is trustworthy enough to interpret and, eventually, whether historical data remain dynamically compatible with the current slow structure.

This is the main applied time-series branch.

Adaptive history selection is **downstream**. The branch does not currently claim a new generic adaptive-window algorithm.

## Required decomposition

For a local estimator built from the most recent history horizon `H`, distinguish

\[
\widehat K_H(t)-K_t^*
=
[\widehat K_H(t)-K_H^\circ(t)]
+
[K_H^\circ(t)-K_t^*]
+
\text{regularization bias}
+
\text{misspecification}.
\]

The first bracket is finite-sample estimator error. The second is history/window bias caused by averaging over nonstationary dynamics.

These are different scientific objects and must not be merged into a generic "uncertainty" term.

## Main causal observables

### Cross-scale instability

\[
S_{scale}(H,t)=d_G(E_H(t),E_{2H}(t)).
\]

This compares spectral subspaces estimated from two amounts of past data.

### Temporal spectral instability

\[
S_{time}(H,t)=d_G(E_H(t),E_H(t-\Delta)).
\]

### Temporal operator motion

\[
D_K(H,t)=\|\widehat K_H(t)-\widehat K_H(t-\Delta)\|_F.
\]

### Reliability / identifiability variables

Additional quantities include:

- spectral gap;
- Schur separation;
- eigenvector or cluster conditioning;
- support/defined-state of the intended spectral object;
- admissibility safeguards suggested by Branch A.

## Established facts governing this branch

### Cross-scale disagreement is not a direct drift proxy

Controlled experiments showed that `S_scale` correlates poorly with true dynamical drift. It is a mixed signal of finite-data error, scale inconsistency, spectral separation, operator geometry, nonstationarity, and model mismatch.

### Reliability can still be useful

E8 and E9b showed that cross-scale or cluster disagreement can predict actual spectral estimation error in controlled stationary regular-gap settings.

### Spectral object existence must be checked before interpreting motion

E10–E15 showed that under non-normal geometry the selected slow object can become non-admissible through pair-cut complexification. A large or erratic Grassmann motion is not interpretable if the object itself is poorly defined.

### Source attribution is harder than error prediction

EXP-009 Gate 1 directly tested whether causal observables could distinguish finite-sample spectral instability from smooth true dynamical drift after matching total observable instability magnitude.

They could not in the tested family.

This does not imply that reliability prediction is impossible; `S_scale` still retained substantial association with actual slow-subspace error.

---

# EXP-009 Gate 1 — Identifiability test

## Pilot v1 — design failure, not scientific failure

The first pilot attempted to match stationary estimation-instability conditions against smooth-drift conditions at the same history horizon.

Support was high, but total observable instability

\[
M_{ST}=\sqrt{S_{scale}^2+S_{time}^2}
\]

was systematically larger in the drift conditions. No qualifying matched pairs existed under the frozen overlap gate.

The experiment stopped before confirmatory trajectories, classifiers, or bootstrap inference were generated.

**Status.** DESIGN-LIMITED INCONCLUSIVE.

## Pilot v2 — overlap calibration

The data-generating grids were recalibrated with fresh pilot seeds only. The matching principle and downstream scientific gates were not changed.

The new pilot produced the required ten disjoint matched condition pairs with:

- high overall support (~`0.992`);
- matched `M_ST` median ratios roughly `1.003–1.286`;
- representation across all four history horizons;
- raw `M_ST` alone near chance for regime discrimination in the selected pilot conditions.

The confirmatory design and development/test split were then frozen before fresh outcomes.

## Frozen confirmatory result

Fresh confirmatory data:

- 4,000 independent trajectories;
- 3,982 primary-supported rows;
- support `0.9955` in both regimes.

The held-out amplitude-overlap gate passed, so the source-classification test was not trivially driven by total instability magnitude.

Held-out AUROC:

| Diagnostic | AUROC |
|---|---:|
| Cross-scale `S_scale` | 0.484 |
| Temporal `S_time` | 0.467 |
| Temporal operator difference | 0.513 |
| Spectral gap | 0.482 |
| Joint scale + time | 0.467 |
| Full joint model | 0.470 |

The joint scale-time model minus the best individual scale/time diagnostic was approximately

\[
-0.0167,
\]

with hierarchical-bootstrap 95% interval approximately

\[
[-0.0698,\;0.0023].
\]

It was at least as good as the best single scale/time diagnostic in only `2/5` held-out condition pairs.

**Frozen verdict.**

> **Strong decomposition of finite-sample estimation instability versus smooth true drift is not identifiable from the tested causal diagnostics in this matched-overlap family.**

This is a branch-stopping result for the simple source-decomposition hypothesis represented by the frozen feature set. It should not be rescued by post-hoc feature search or rematching.

## Positive residue

Source attribution failed, but error prediction remained informative.

Held-out Spearman correlation with true slow-subspace estimation error was approximately:

- `S_scale`: `0.508`;
- `S_time`: `0.286`;
- `D_K`: `0.175`;
- gap: `-0.237`.

Thus the practical distinction is:

> **A causal observable may predict that a spectral estimate is unreliable without identifying why it is unreliable.**

---

# Current endpoint

A future causal system should not immediately output a window length. A more defensible sequence is:

1. **Is the intended spectral object identifiable/admissible?**
2. **How large is the estimated spectral error or reliability risk?**
3. **Is an observed temporal change large relative to that reliability envelope?**
4. **Only then:** decide whether changing the history horizon is justified.

A possible operational output could distinguish:

- reliable spectral estimate;
- estimate too unreliable to interpret;
- observed change exceeds a calibrated reliability envelope and is compatible with genuine dynamics;
- insufficient evidence to identify the source of instability.

## Relationship to Branch A

Branch A supplies operator-level mechanisms and sufficient conditions describing how perturbations can destroy a selected spectral boundary.

Those results may become safeguards or priors in Branch B only if the required quantities can be estimated from data and their calibration survives data-level tests.

An operator-level theorem does not by itself validate a causal time-series diagnostic.

## Current open questions

1. Can actual spectral estimation error be calibrated online more robustly than source attribution?
2. Which admissibility/conditioning quantities are estimable stably from one causal trajectory?
3. Can a risk interval or reliability envelope be estimated near nonregular spectral boundaries without conditioning on one noisy spectral center?
4. Can a data-level method distinguish "object not identifiable" from "reliable object undergoing genuine motion"?
5. How does the framework behave under observation noise with fixed latent dynamics?
6. How does it behave when the spectral gap collapses without true system drift?
7. Only after the above: can reliability-aware history adaptation improve slow-subspace recovery, implied timescales, or metastable-state recovery over fixed windows, prediction loss, forgetting, and standard change-detection baselines?

## Claim ceiling

The branch currently supports:

- controlled reliability/error-prediction results;
- explicit negative identifiability results;
- careful separation of finite-sample error and history bias;
- the requirement to treat spectral admissibility before interpreting subspace motion.

It does **not** currently support:

- a universal drift detector;
- a universal Koopman uncertainty estimator;
- a solved adaptive-horizon method;
- general identifiability of true drift from one time series without additional assumptions.