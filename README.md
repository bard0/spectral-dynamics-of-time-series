# Spectral Dynamics of Time Series

Research repository for **causal spectral reliability in nonstationary time-series models**, with emphasis on local Koopman/EDMD operators, slow spectral subspaces, non-normality, spectral admissibility, and the limits of causal source attribution.

## Scientific question

When a local data-driven spectrum changes, becomes unstable, or ceases to define the intended slow spectral object, what can be inferred from **past data only**?

The project started from adaptive history-window selection and evolved into a more fundamental reliability problem:

> Can observable spectral diagnostics tell us whether a local Koopman/EDMD spectral object is trustworthy, and under what geometric conditions does that object cease to be admissible?

A separate but related question is whether observed instability can be attributed to finite-sample estimation error or to genuine dynamical drift. Current evidence shows that this attribution can fail even when spectral error itself remains predictable.

## Research trajectory

The project has undergone several deliberate falsification-driven pivots:

1. **Adaptive history windows.** Initial work studied the statistical-error/nonstationarity trade-off and causal window selection.
2. **Slow-subspace preservation.** Mode-wise comparisons were replaced by invariant-subspace geometry because individual eigenvectors are fragile under sign, ordering, and mode swaps.
3. **Spectral reliability.** Nested-window disagreement was found not to be a direct drift proxy. The focus moved from selecting a window to determining when a spectral estimate is reliable.
4. **Cluster admissibility and non-normality.** Controlled experiments showed that reliability can work in regular-gap stationary systems but can fail to transport through non-normal families because the selected spectral object may disappear through pair-cut complexification.
5. **Boundary-specific geometry.** Global eigenvector conditioning was shown to be insufficient. A single fixed boundary-resolvent norm was also refuted as a standalone transportable risk variable.
6. **Limits of source attribution.** A frozen matched-overlap test found that scale, temporal, operator-change, and gap diagnostics could not reliably distinguish finite-sample instability from smooth true drift after observable instability magnitude was controlled.

## Strongest current results

### 1. Cross-scale reliability can be informative in controlled regular-gap systems

In the E8 stationary regular-gap benchmark, cross-scale disagreement predicted slow-subspace estimation error with moderate ranking power. In E9b, moving from individual modes to a two-dimensional spectral cluster produced substantially stronger reliability under a fixed outer gap, including AUROC around 0.83 in the hardest primary condition.

This is a **controlled-regime result**, not a universal uncertainty quantification claim.

### 2. Non-normality changes the failure mode

E10 showed that a reliability calibration learned in a normal regime did not transport unchanged to non-normal systems. E11 isolated the mechanism: increasing non-normality primarily increased the probability that the intended real/conjugation-closed `r=2` spectral object ceased to exist, while conditional Grassmann error among surviving objects did not increase and often decreased.

Thus the important failure event is sometimes **loss of spectral-object identity**, not merely increased subspace error.

### 3. Global conditioning is not sufficient

E13a found a strong exploratory association between estimated eigenvector conditioning and latent admissibility risk within one triangular non-normal VAR family. E14a then constructed matched-conditioning counterexamples. With global conditioning, eigenvalues, gaps, and perturbation scale matched, relocating non-normal coupling across the retained/excluded spectral boundary substantially changed pair-cut failure probability.

The relevant geometry is therefore boundary-specific rather than captured by a single global conditioning number.

### 4. A fixed boundary resolvent is informative but not sufficient

E15 tested a frozen scalar candidate in a fresh four-dimensional operator family. After correcting an orientation error in one panel, larger boundary-resolvent norm had the predicted risk direction when nuisance geometry was closely matched. However, operators with nearly identical fixed-point boundary resolvent could have very different admissibility risks when other non-normal geometry changed.

Final E15 verdict:

> **The single-point boundary-resolvent norm is refuted as a standalone transportable admissibility-risk variable.**

### 5. Strong source decomposition is not identifiable in the tested Gate-1 family

EXP-009 Gate 1 constructed fresh held-out pairs with matched total observable instability magnitude. Classifiers based on cross-scale instability, temporal instability, temporal operator difference, spectral gap, and their combinations remained near chance. The frozen joint scale-time diagnostic did not outperform the individual diagnostics.

Final Gate-1 verdict:

> **Strong decomposition of finite-sample estimation instability versus smooth true drift is not identifiable from the tested causal diagnostics in this controlled family.**

Importantly, cross-scale instability still correlated with true slow-subspace estimation error. Reliability prediction can therefore remain useful even when the *source* of the error is not identifiable.

## Current interpretation

The project no longer claims a generic new adaptive-window method. Adaptive history selection is treated as a downstream application that should only be revisited after a reliable causal diagnostic has survived transport tests.

The current scientific picture is:

- cross-scale disagreement can contain real information about spectral estimation error;
- it is not a direct measure of dynamical drift;
- spectral gap and non-normal geometry control identifiability;
- the intended spectral object can fail to exist before survivor error becomes large;
- global conditioning and a single scalar resolvent are too coarse to determine admissibility risk across geometries;
- source attribution from causal scale/time diagnostics can be non-identifiable even when reliability prediction remains possible.

## Repository structure

```text
docs/
    current_state.md
    research_story.md
    experiment_ledger.md
    roadmap.md
    methodology_and_audits.md
experiments/
    README.md
```

Experiment code, reports, tables, and figures are being added from the archived project runs after provenance and reproducibility checks.

## Research principles

- Negative results are preserved rather than rewritten as successful experiments.
- Every new hypothesis should first face the cheapest decisive falsification test.
- Oracle information may be used for evaluation but not for causal selection or prediction.
- Post-hoc analyses are explicitly labeled exploratory.
- Implementation corrections that change interpretation are retained in the scientific history.
- A result is stated only at the level supported by the tested operator family, data-generating process, and evaluation protocol.

## Status

Active research project. The current priority is **calibrated spectral reliability and the geometry of spectral admissibility**, together with a precise characterization of where causal source attribution is impossible.