# Spectral Dynamics of Time Series

Research repository for **causal spectral reliability and spectral admissibility in time-series models**, with emphasis on local Koopman/EDMD operators, slow invariant subspaces, non-normality, finite-sample operator uncertainty, and the limits of causal source attribution.

## Scientific question

When a local data-driven spectrum changes, becomes unstable, or ceases to define the intended slow spectral object, what can be inferred from **past data only**?

The project began with adaptive history-window selection and evolved into two more fundamental questions:

1. **Spectral reliability/admissibility:** is the selected slow spectral object statistically trustworthy and does it remain well defined under finite estimation error?
2. **Source identifiability:** if the estimate moves, can the motion be attributed to finite-sample instability rather than genuine dynamical evolution?

Current evidence shows that reliability can remain predictable even when the source of the instability is not identifiable from the tested causal observables.

## Research trajectory

The project has undergone several falsification-driven pivots:

1. **Adaptive history windows.** Study the statistical-error/nonstationarity trade-off and causal window selection.
2. **Slow-subspace preservation.** Replace fragile mode-wise comparisons with invariant-subspace geometry.
3. **Spectral reliability.** Reject nested-window disagreement as a direct drift proxy and test it instead as an error/reliability signal.
4. **Cluster admissibility and non-normality.** Show that the intended spectral object can disappear through pair-cut complexification before survivor subspace error becomes large.
5. **Boundary-specific geometry.** Refute global eigenvector conditioning and a single fixed boundary-resolvent norm as sufficient transportable risk variables.
6. **Probabilistic spectral-cut theory.** Derive and freshly validate an exact projected boundary-complexification law; identify theorem-certified safe regimes and joint certificate/boundary geometry.
7. **Theory-to-data bridge.** Show that finite-sample OLS/linear-EDMD sampling laws can calibrate spectral-failure probability when spectral center geometry is known, then expose nonregular center uncertainty near the admissibility boundary.
8. **Risk intervals instead of unstable point risk.** Demonstrate calibrated uncertainty intervals in a controlled local-to-boundary matrix family.
9. **Limits of causal source attribution.** Show in a frozen matched-overlap benchmark that scale/time/operator/gap diagnostics do not reliably distinguish estimation instability from smooth true drift in the tested family.

## Selected results

### Cross-scale reliability works in a controlled regular-gap regime

E8 showed that cross-scale disagreement predicts slow-subspace estimation error in a stationary regular-gap linear-EDMD family (Spearman ≈ `0.51`, AUROC ≈ `0.79`). E9b strengthened this by using a two-dimensional invariant spectral cluster under a fixed outer gap (AUROC ≈ `0.83` in the hardest primary condition).

These are controlled-regime results, not universal uncertainty quantification claims.

### Invariant clusters are more robust than individual modes

E3 showed why mode-wise matching is fragile: a mode swap can leave the Grassmann distance essentially zero while individual-vector overlap changes strongly.

E9 then demonstrated the operational consequence. Under inner-gap collapse, the `r=1` object became poorly defined while the `r=2` invariant cluster remained useful. E9b removed the main gap confound by fixing the true outer cluster gap and passed all frozen cluster-reliability gates.

### Non-normality changes the failure mode

E10–E11 showed that non-normality can primarily reduce the probability that the intended real/conjugation-closed `r=2` spectral object exists at all. Conditional Grassmann error among surviving objects did not necessarily increase.

This shifted the target from survivor error alone to **spectral admissibility**.

### Global conditioning and one scalar resolvent are insufficient

E12 showed that a conditioning-normalized perturbation scale can rank admissibility risk but does not supply a universal calibrated law in the tested family.

E14a then constructed matched-conditioning counterexamples: relocating non-normal coupling across the retained/excluded spectral boundary changed pair-cut failure probability even with global conditioning, eigenvalues, gaps, and perturbation scale matched.

E15 froze a boundary-resolvent scalar in a fresh four-dimensional family. After correcting a reporting-orientation error, the larger resolvent had the predicted risk direction when nuisance geometry was matched, but matched resolvent values still permitted large risk differences when other geometry changed.

> **E15 verdict: the single-point boundary-resolvent norm is refuted as a standalone transportable admissibility-risk variable.**

### Exact projected boundary law survives fresh falsification

For the selected `2|3` spectral boundary, the project derived

\[
[g+\varepsilon(E_{22}-E_{33})]^2+4\varepsilon^2E_{23}E_{32}.
\]

The associated finite-epsilon projected-complexification probability was reduced to a low-dimensional angular/radial law under Frobenius-isotropic perturbations.

In the fresh T6 operator family, theory versus simulation over 252 cells gave approximately:

- MAE `0.00225`;
- RMSE `0.00325`;
- maximum absolute error `0.0119`;
- `98.8%` of cells inside exact 99% binomial intervals.

> **T5 survives fresh operator-family falsification for the projected `2×2` boundary event.**

### Theorem-certified perturbative regime is useful, but not a global predictor

A second-order boundary approximation failed strongly as a global finite-epsilon predictor (T7), and an empirical global validity threshold was not supported (T8).

A classical Riccati/Sylvester sufficient certificate performed differently: in a fresh controlled family it selected a subset where the second-order model reduced conditional probability error by about `42%` relative to the first-order boundary model (T9).

A conservative probabilistic pre-certificate and an exact shared-radial joint representation were then validated in fresh families (T10–T11). These results use classical perturbation-theory ingredients; novelty is not claimed for the underlying Riccati/Sylvester or pseudospectral machinery.

### Data bridge: sampling law is learnable, spectral center is the hard part

T12-A1 showed that a one-sample plug-in OLS sampling law can accurately calibrate full `r=2` failure probability **when the true spectral center/geometry is supplied** (MAE ≈ `0.0070`, RMSE ≈ `0.0095`, Spearman ≈ `0.876`).

Removing the oracle center caused substantial degradation. Increasing sample size alone did not reliably repair the point-centered risk estimator. A fresh local-to-boundary test (A2c2) showed that the matrix estimator itself can converge while the point-centered spectral-risk functional remains nonconcentrated under an `O(N^{-1/2})` approach to the pair-cut boundary.

A subsequent center-uncertainty risk interval achieved nominal-90% pooled coverage about `0.936` in a fresh controlled local matrix family. A high-N Riesz-chart test then produced strong theory-log evidence for risk-interval transport across six fresh non-normal embeddings, while one separate chart-support gate remained marginally design-limited.

**Provenance note:** the A4b numerical interpretation is retained in the structured scientific record, but a later recovery audit could not fully authenticate the original executable/configuration. A4b is therefore **theory-log / provenance-limited evidence**, not a source-reproducible run in this repository. The later correlated-trajectory B1 numerical result is more severe: it is **provenance-invalidated / not claim-ready**. See `theory/T12_provenance_status.md`.

### Source attribution can fail even when reliability prediction survives

EXP-009 Gate 1 used 4,000 fresh trajectories in a frozen matched-overlap design. Held-out AUROCs for cross-scale, temporal, operator-change, spectral-gap, and joint diagnostics remained near chance.

> **Gate-1 verdict: strong decomposition of finite-sample estimation instability versus smooth true drift is not identifiable from the tested causal diagnostics in this controlled family.**

However, cross-scale instability still correlated with actual slow-subspace estimation error at Spearman ≈ `0.51`.

The project therefore distinguishes **reliability prediction** from **source attribution**.

## Parallel branches

### Branch A — spectral admissibility theory

Operator-level perturbation geometry, projected boundary laws, invariant-graph certificates, nonregular risk near spectral boundaries, and the theory-to-data bridge.

See [`docs/branch_A_spectral_admissibility.md`](docs/branch_A_spectral_admissibility.md) and [`theory/README.md`](theory/README.md).

### Branch B — causal spectral reliability

Data-level calibration of local spectral error/risk, source-identifiability limits, and eventual reliability-aware adaptive history selection.

See [`docs/branch_B_causal_reliability.md`](docs/branch_B_causal_reliability.md).

The branches are kept separate: an operator-level mechanism is not automatically a causal data-level result.

## Repository map

```text
README.md

docs/
    current_state.md
    research_story.md
    experiment_ledger.md
    branch_A_spectral_admissibility.md
    branch_B_causal_reliability.md
    methodology_and_audits.md
    novelty_positioning.md
    roadmap.md
    reproducibility_status.md
    artifact_migration_status.md

experiments/
    README.md
    E1_local_edmd_bias_variance/
    E2_causal_lepski_selector/
    E3_grassmann_mode_swap_sanity/
    E4_adaptive_spectral_window_benchmark/
    E5_smooth_drift_benchmark/
    E6_noise_change_controls/
    EXP007_broad_online_spectral_benchmark/
    EXP008_nested_disagreement_vs_true_drift/
    E7_null_calibrated_directional/
    E8_cross_scale_reliability/
    E9_cluster_reliability/
    E9b_fixed_outer_gap/
    E10_nonnormal_reliability/
    E11_matched_nonnormal_perturbation/
    E12_conditioning_scaling/
    E13_causal_admissibility_guard/
    E13a_latent_risk_reanalysis/
    E14a_matched_conditioning_geometry/
    E14aR_boundary_mechanism_audit/
    E15_frozen_boundary_resolvent/
    EXP009_gate1_identifiability/

theory/
    README.md
    T4_T6_boundary_probability.md
    T7_T11_certified_geometry.md
    T12_theory_to_data.md
    T12_provenance_status.md
```

Some early packages are historical scientific records because their original byte-level archive has not yet been located. They are explicitly labeled as such and are not presented as fully reproducible runs.

Large simulation tables and checkpoints remain in the external project archive; GitHub stores compact source/configuration/provenance material where it can be transferred and verified safely.

## Historical naming

Two numbering conventions coexist in the research history:

- early `EXP-007` is the broad online benchmark, while later `E7` is the directional diagnostic;
- early `EXP-008` falsifies nested disagreement as a direct drift proxy, while later `E8` tests cross-scale disagreement as an estimation-error predictor.

The labels are preserved instead of being silently renumbered.

## Research principles

- Preserve negative, inconclusive, design-limited, provenance-limited, and provenance-invalidated results.
- Freeze confirmatory designs before target outcomes.
- Use oracle information for evaluation only, unless a result is explicitly labeled oracle/mechanistic.
- Label post-hoc analyses exploratory.
- Keep implementation corrections visible when they change interpretation.
- Check spectral-object support before reporting conditional survivor error.
- Do not promote historical numerical evidence to claim-ready status when executable provenance is missing.
- State claims only at the level supported by the tested operator family and data-generating process.
- Prefer a reliable negative result to a post-hoc rescued positive claim.

## Current priority

The next high-value Branch-A experiment is **`T12-B1R` — a reconstructed, re-frozen stationary correlated-trajectory Riesz risk-interval test that explicitly carries spectral-center uncertainty**. It must preserve executable source, configuration, exact event/support definitions, seed namespaces, manifests, hashes, and integrity tests before outcomes.

Adaptive history selection remains downstream until the stationary trajectory/data-reliability layer is established.
