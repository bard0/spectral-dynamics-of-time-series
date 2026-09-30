# Spectral Dynamics of Time Series

This repository grew out of a practical question: when a Koopman/EDMD model is fitted locally to a changing time series, how much of the past is still useful?

I first treated this as an adaptive-window problem. That turned out to be too broad. Several natural selectors were either too conservative or worked only in restricted regimes, and a direct interpretation of nested-window disagreement as dynamical drift did not survive controlled tests.

The project therefore moved toward a narrower question: **when can a slow spectral object estimated from finite data be trusted, and when does that object stop being well defined at all?**

The current repository records that whole development, including the ideas that failed.

For a shorter overview, see [docs/portfolio_summary.md](docs/portfolio_summary.md).

## Main results

The first part of the project studied the usual bias–variance trade-off for a local EDMD estimate. In a regular regime, the leading upper bound has the form

\[
U(n,t)\approx \frac{A}{n}+C L_t^2 n^2,
\]

so the minimizer of this bound scales as

\[
n^*_{UB}(t)=O(L_t^{-2/3}).
\]

The numerical checks reproduced the expected \(n^{-1}\) statistical term, the \(n^2\) drift term, and an exponent close to \(-2/3\).

A Lepski-style causal selector was then tested. The finite-sample radii were valid but too conservative to be useful in the main synthetic setup: many windows remained mutually compatible and the selector often chose the largest one. I kept this as a negative result rather than tuning it away.

The next step was to work with invariant subspaces instead of individual eigenvectors. A simple mode-swap test showed why this matters: the Grassmann distance between the relevant subspaces stayed at roughly \(10^{-14}\), while individual-vector overlap could drop to about \(0.13\).

Cross-scale disagreement,

\[
S_{\mathrm{scale}}(H,t)=d_G(E_H(t),E_{2H}(t)),
\]

did **not** turn out to be a clean measure of true dynamical drift. It was more useful as a reliability signal. In a stationary regular-gap benchmark (E8), it reached Spearman correlation of about 0.51 with the actual spectral error and AUROC about 0.79. In the fixed-outer-gap cluster experiment E9b, AUROC was about 0.83 in the hardest primary condition.

The non-normal experiments changed the interpretation again. Increasing non-normality did not simply make the surviving subspace estimates worse. Instead, the intended real/conjugation-closed spectral cluster could cease to exist under finite perturbations. This led to the notion of **spectral admissibility**.

Several simple explanations were then tested and rejected. Global eigenvector conditioning was informative but insufficient. A single fixed boundary-resolvent norm was also informative in matched comparisons but not enough to determine admissibility risk across geometries.

For a selected 2|3 boundary, the projected complexification event can be written as

\[
[g+\varepsilon(E_{22}-E_{33})]^2
+4\varepsilon^2E_{23}E_{32}<0.
\]

In the controlled isotropic perturbation family, the corresponding probability law matched fresh simulations closely. Across 252 cells, MAE was about 0.00225, RMSE about 0.00325, and 98.8% of cells fell inside exact 99% binomial intervals.

The data-level part then showed where the real difficulty lies. The finite-sample OLS perturbation law can calibrate failure risk well when the spectral center is known. Near the admissibility boundary, however, estimating the center and then plugging it into a point-risk functional becomes nonregular: the matrix estimate can converge while the estimated risk remains unstable. Carrying center uncertainty through to a risk interval worked much better in the controlled local family; nominal 90% pooled coverage was about 0.936.

A separate causal benchmark asked whether one can tell estimation instability from smooth true drift using only scale, time, operator-change, gap, and joint diagnostics. In the tested matched-overlap family, the answer was negative: held-out AUROCs stayed close to chance. At the same time, cross-scale instability still contained information about the size of the spectral estimation error.

So one of the main conclusions of the project is simple:

> **Predicting whether a spectral estimate is reliable is easier than identifying why it moved.**

## What did not work

The repository deliberately keeps several negative results:

- generic adaptive-history methods did not show robust superiority over fixed histories;
- nested spectral disagreement was not a reliable direct proxy for true drift;
- a conditioning-normalized scalar did not give a universal calibrated risk law;
- a global second-order finite-perturbation predictor failed outside a certified regime;
- strong causal separation of finite-sample instability from smooth drift failed in the tested family.

These failures shaped the later theory and are part of the project rather than discarded intermediate work.

## Scope

The results here are mainly controlled linear or finite-dimensional operator experiments. I do not claim a universal Koopman uncertainty estimator, a general adaptive-window algorithm, or general identifiability of drift versus estimation noise.

Classical ingredients such as Grassmann geometry, resolvents, pseudospectra, Riccati/Sylvester theory, and nonregular inference are used as tools rather than presented as new theory.

The most defensible contribution of the project is the combination of:

- a concrete spectral-admissibility target for selected slow Koopman/EDMD objects;
- controlled boundary-local failure mechanisms under non-normal perturbations;
- a finite-data calibration problem that explicitly includes uncertainty in the spectral center;
- and a careful separation between reliability estimation and source attribution.

## Repository structure

~~~text
docs/
    portfolio_summary.md
    research_story.md
    current_state.md
    experiment_ledger.md
    novelty_positioning.md
    reproducibility_status.md
    branch_A_spectral_admissibility.md
    branch_B_causal_reliability.md

experiments/
    E1 ... E15
    EXP007 ...
    EXP009 ...

theory/
    README.md
    T4_T6_boundary_probability.md
    T7_T11_certified_geometry.md
    T12_theory_to_data.md
    T12_provenance_status.md
~~~

The [experiment ledger](docs/experiment_ledger.md) gives the chronological record. The [research story](docs/research_story.md) explains how the question changed after each falsification. The [reproducibility page](docs/reproducibility_status.md) separates fully migrated source from historical or provenance-limited results.

## Reproducibility

Later experiments have source files, frozen configurations, hashes, manifests, and explicit audit notes where they could be transferred reliably. Some early numerical packages survive only as historical records, and a few later results have a stated provenance limit. Those cases are marked rather than silently promoted to fully reproducible evidence.

Large simulation tables, checkpoints, and ZIP archives are kept outside GitHub; the repository contains the compact scientific record and the source material that could be verified safely.

## Status

I consider the project complete as a portfolio research case study in its current form. There is still an obvious research continuation — especially a clean stationary correlated-trajectory replication before returning to nonstationary adaptive-history selection — but that is a next project stage rather than something needed to make the present work coherent.
