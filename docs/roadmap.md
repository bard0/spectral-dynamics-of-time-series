# Research Roadmap

The roadmap is deliberately conditional. A failed gate should stop or redirect a branch rather than trigger post-hoc metric replacement.

## Two parallel branches

### Branch A — spectral admissibility theory

Goal: understand when finite operator-estimation error destroys a preselected slow spectral cut, and translate that understanding into calibrated uncertainty statements.

### Branch B — causal spectral reliability

Goal: estimate from past time-series data whether a local slow spectral object is trustworthy, while acknowledging that the source of instability may be non-identifiable.

The intended bridge is:

```text
operator perturbation geometry
        ↓
spectral admissibility / failure probability
        ↓
data-estimated sampling uncertainty
        ↓
causal reliability envelope
        ↓
interpretation of observed spectral motion
        ↓
adaptive history horizon, only if justified
```

---

# Priority 1 — Complete provenance-clean theory-to-data transport

## Motivation

The theory branch now has a coherent sequence:

- exact projected boundary law T5 survives fresh falsification;
- global second-order prediction T7 fails;
- a classical Riccati/Sylvester certificate identifies a useful perturbative subset (T9);
- the certificate probability admits a useful conservative CDF reduction (T10);
- joint certificate/boundary probability requires shared geometry and is accurately represented by the T11 shared-radial law;
- iid OLS sampling-law calibration works very well when the true spectral center is supplied (T12-A1);
- one-center fully data-centered point risk is unstable near the spectral boundary (A2/A2b/A2c2);
- explicit center-uncertainty risk intervals are calibrated in the controlled iid local model (A3).

The next bridge must therefore preserve center uncertainty rather than condition on a single noisy spectral estimate.

## Next experiment: reconstructed stationary correlated-trajectory interval

A previous stationary-trajectory result cannot be used for claims because its executable provenance is incomplete. The next valid version must be a **new, re-frozen experiment identifier** with:

- complete executable source;
- exact event definitions;
- configuration;
- seed namespaces;
- frozen contour/chart definition;
- artifact manifest and hashes;
- all primary outputs;
- reproducible code audit.

### Primary question

Does the center-uncertainty / local-risk interval remain calibrated when the estimator is based on **one stationary correlated VAR trajectory** rather than iid transition pairs?

### Stop condition

If the interval is poorly calibrated even in a stationary Gaussian VAR with controlled mixing and isolated spectral boundary, do not proceed to nonstationary online data.

---

# Priority 2 — Calibrated data-level reliability, not source classification

EXP-009 Gate 1 showed that the tested causal observables cannot reliably identify whether instability came from finite-sample error or smooth true drift after total instability magnitude was matched.

The next Branch-B target should therefore be narrower:

> Can a causal procedure estimate the magnitude/probability of spectral estimation failure without claiming to identify its source?

Candidate evaluation targets:

- slow-subspace error;
- probability that the selected spectral object is non-admissible;
- implied-timescale error;
- support probability for the intended spectral cluster;
- calibrated risk interval rather than point risk near a boundary.

### Required baselines

At minimum compare against:

- fixed history lengths;
- raw cross-scale disagreement;
- spectral-gap-only diagnostics;
- bootstrap/subsampling uncertainty where appropriate;
- parametric linear-model uncertainty in controlled VAR tests;
- simple condition-number / resolvent summaries as known insufficient scalar controls.

### Stop condition

If the calibrated reliability estimate does not outperform simple raw disagreement or standard resampling uncertainty on fresh held-out operator families, do not promote a new reliability method.

---

# Priority 3 — Stationary trajectory before nonstationarity

Before returning to genuinely time-varying systems, establish that the reliability target can be estimated from one correlated stationary trajectory.

Progression:

1. iid transition pairs — controlled benchmark;
2. one stationary Gaussian VAR trajectory;
3. stationary non-normal trajectory with varied mixing time;
4. observation-noise corruption with fixed latent dynamics;
5. only then smooth nonstationarity.

This ordering separates correlation/mixing failures from genuine nonstationarity failures.

---

# Priority 4 — Explicit observation-noise and process-drift controls

The project already established that observation noise must not be conflated with operator drift.

A future causal reliability benchmark should include at least:

### A. Stationary latent dynamics + changing observation noise

Expected behavior: the latent operator has not changed. A method should not automatically report genuine dynamical drift or shorten the history merely because measurements become noisier.

### B. Smooth latent operator drift

Expected behavior: the local population operator genuinely changes.

### C. Gap collapse with little/no true drift

Expected behavior: spectral interpretation becomes unreliable because identifiability fails, not because the dynamical source necessarily changed.

### D. Non-normal admissibility failure

Expected behavior: the spectral object can become undefined before survivor error becomes large.

The purpose is not to force a multiclass source classifier. The purpose is to test whether the reliability state and its limitations are scientifically interpretable across qualitatively different failure mechanisms.

---

# Priority 5 — Nonstationary reliability envelope

Only after stationary trajectory calibration survives should the project return to online local estimates.

For each current time `t` and causal horizon `H`, estimate:

- spectral object support/admissibility;
- uncertainty/risk interval for slow-subspace quantities;
- cross-scale discrepancy;
- observed temporal motion.

The key test is then:

> Is the observed temporal motion large relative to the calibrated estimation-reliability envelope?

This does **not** guarantee identification of the physical source of the change. It may only justify statements such as:

- motion is explainable by estimator variability;
- motion exceeds the calibrated estimator envelope;
- spectral object is too poorly identified for either statement.

---

# Priority 6 — Adaptive history horizon as a downstream application

Only if the reliability layer is calibrated should adaptive history selection be revisited.

The candidate decision is no longer

> choose a window because nested estimates disagree.

Instead it should be closer to

> choose the longest causal history for which the current spectral object remains supported and the estimated history bias is acceptable relative to the reliability envelope.

## Evaluation

Do not evaluate only "window regret" against an oracle window. Use independent downstream metrics:

- slow-subspace Grassmann error;
- implied-timescale error;
- metastable-state recovery;
- transition-rate error;
- prequential prediction as a secondary generic metric;
- frequency of forced decisions when the correct output should be uncertain.

## Baselines

Compare against:

- fixed short/medium/long histories;
- prediction-loss selection;
- forgetting-factor estimation;
- Lepski-like nested selection;
- standard concept-drift/change-point methods where relevant.

## Success criterion

The reliability-aware horizon must improve a downstream dynamical target on fresh nonstationary systems, not merely select a window similar to an oracle defined with the same spectral metric.

---

# Theory work that can proceed in parallel

The following questions remain mathematically useful but should not become an endless scalar-feature search:

1. characterize full spectral-cut failure beyond the isolated `2x2` boundary event;
2. separate pair-cut complexification from ordering changes and external-mode collisions;
3. express admissibility conditions in basis-invariant projector/Schur/Riesz language;
4. characterize local asymptotic risk near intersections of spectral-boundary strata;
5. determine when honest risk intervals have useful width rather than merely correct coverage.

Any new proposed scalar must be justified by theory and frozen before fresh outcomes.

---

# Paper-level milestone

A defensible main paper would need a coherent chain such as:

1. **problem:** local Koopman/EDMD spectral estimates can fail in ways not captured by ordinary error magnitude;
2. **controlled mechanism:** admissibility of a selected spectral cut depends on boundary-local geometry;
3. **theory:** exact/projected probability and theorem-backed safe regime for controlled perturbations;
4. **data bridge:** calibrated uncertainty for spectral-admissibility risk from finite data, including center uncertainty;
5. **trajectory transport:** reproducible stationary correlated-trajectory validation;
6. **nonstationary demonstration:** reliability envelope used causally without overclaiming source identification;
7. **optional application:** reliability-aware adaptive history if it improves an independent downstream dynamical target.

If the trajectory/data bridge fails, the theoretical branch can still stand as a controlled spectral-perturbation study, but claims about practical online time-series reliability must be reduced accordingly.