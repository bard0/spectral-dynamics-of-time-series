# Prior Art and Novelty Positioning

This document records the project's **claim ceiling**. Several early formulations were intentionally abandoned after comparison with established methods.

## What is not claimed as novel

The project does **not** claim novelty merely from any of the following combinations:

- adaptive/sliding history windows;
- concept-drift detection;
- nested-estimator comparison;
- local or moving-window Koopman/EDMD estimation;
- Grassmann distances between subspaces;
- slow Koopman/VAMP modes;
- lag/model selection by variational scores;
- online subspace tracking;
- spectral-gap safeguards;
- non-normal eigenvalue/eigenvector sensitivity;
- resolvent or pseudospectral sensitivity;
- Riccati/Sylvester invariant-subspace perturbation theory;
- generic bootstrap/nonregular inference near parameter boundaries.

These all have substantial established literature.

---

# 1. Adaptive windows / concept drift

## ADWIN

Albert Bifet and Ricard Gavaldà, **Learning from Time-Changing Data with Adaptive Windowing**, Proceedings of the 2007 SIAM International Conference on Data Mining, pp. 443–448.

DOI: `10.1137/1.9781611972771.42`

ADWIN already adapts a window online in response to statistical changes in a data stream. Therefore the broad claim

> "automatically choose how much recent history to keep under drift"

is not a novel problem statement.

## OPTWIN

Mauro Dalle Lucca Tosi and Martin Theobald, **OPTWIN: Drift Identification with Optimal Sub-Windows**, arXiv:2305.11942; later presented at ICDEW 2024.

OPTWIN detects drift by splitting a sliding window using statistically significant changes in error mean/variance.

### Consequence for this project

The repository should not be presented as a new generic adaptive-window or concept-drift method. A history horizon is only a downstream control variable here; the intended scientific target is reliability of a selected dynamical spectral object.

---

# 2. VAMP / slow dynamical modes / model selection

## Variational approach for Markov processes

Hao Wu and Frank Noé, **Variational Approach for Learning Markov Processes from Time Series Data**, Journal of Nonlinear Science 30, 23–66 (2020).

DOI: `10.1007/s00332-019-09567-y`

VAMP provides variational scores for finding slow singular components of the Koopman operator and for model/hyperparameter selection. It is valid beyond reversible equilibrium settings and explicitly addresses nonreversible/nonstationary realizations.

## VAMPnets

Andreas Mardt, Luca Pasquali, Hao Wu, and Frank Noé, **VAMPnets for deep learning of molecular kinetics**, Nature Communications 9, 5 (2018).

DOI: `10.1038/s41467-017-02388-1`

VAMPnets learn representations targeting slow kinetic information and metastable dynamics.

### Consequence for this project

The following are not novelty claims:

- learning slow modes;
- using Koopman/VAMP spectral structure as the object of interest;
- selecting lag/model parameters to preserve slow dynamics.

The project's distinct question is whether a **locally estimated selected slow spectral object is statistically admissible/reliable under finite data and nonstationarity**, and whether that risk can be estimated causally.

---

# 3. Time-dependent / moving-window Koopman estimation

Mengnan Li and Lijian Jiang, **Data-driven reduced-order modeling for nonautonomous dynamical systems in multiscale media**, Journal of Computational Physics 474, 111799 (2023).

DOI: `10.1016/j.jcp.2022.111799`

This work estimates time-dependent Koopman operators by decomposing data with moving time windows and applying EDMD locally.

### Consequence

Local `K_t` or moving-window EDMD is established. The project cannot claim novelty from simply making Koopman estimation local in time.

---

# 4. Verified spectral computation / ResDMD

Matthew J. Colbrook and Alex Townsend, **Rigorous data-driven computation of spectral properties of Koopman operators for dynamical systems** (2021/2023 line of work), introduced Residual Dynamic Mode Decomposition (ResDMD) for data-driven spectra/pseudospectra with verification and error control.

Related applied exposition:

Matthew J. Colbrook, Lorna J. Ayton, and Máté Szőke, **Residual dynamic mode decomposition: robust and verified Koopmanism**, Journal of Fluid Mechanics (2023).

### Consequence

"Verify whether a Koopman spectral approximation is trustworthy" is already a substantial research area. The present project must distinguish its target carefully.

The narrower target studied here is the **probability/admissibility of a preselected finite-dimensional slow spectral cut under operator-estimation uncertainty**, especially when non-normal geometry can destroy conjugation-closed object identity, followed by a causal finite-data bridge.

This is not the same as claiming the first verified Koopman spectral method.

---

# 5. Classical spectral perturbation theory

The theory branch uses ideas closely connected to classical work on:

- eigenvalue/eigenvector conditioning;
- spectral projectors;
- invariant subspaces;
- Sylvester equations and separation;
- Riccati graph transforms;
- pseudospectra and resolvents;
- perturbation of non-normal matrices.

These mechanisms are classical. In particular, the T9 invariant-graph certificate is treated explicitly as a classical sufficient condition, not a new theorem of perturbation theory.

### Consequence

The project cannot claim novelty for facts such as

> non-normal matrices are spectrally sensitive

or

> small separation makes invariant subspaces unstable.

The possible contribution must lie in the particular **spectral-admissibility target, falsification chain, probability construction, and data-driven calibration problem**.

---

# 6. Nonregular statistical inference

The T12 local-to-boundary results are conceptually close to classical nonregular inference:

- parameter-space boundary problems;
- non-Hadamard-smooth functionals;
- local Gaussian experiments;
- bootstrap inconsistency near nonregular boundaries;
- honest confidence/risk intervals with nonvanishing local width.

### Consequence

The project does not claim that generic local nonregularity is new.

The narrower contribution candidate is its manifestation for a **spectral-cut admissibility probability** arising from finite-data Koopman/EDMD operator estimation, together with a theory-to-data calibration pipeline.

---

# Current novelty hypothesis

The strongest potentially distinguishing direction is:

> **Causal finite-data reliability for a preselected slow Koopman/EDMD spectral object, formulated in terms of spectral admissibility/failure risk and explicitly accounting for boundary-local non-normal geometry and center uncertainty.**

This remains a hypothesis about positioning, not a completed novelty claim.

To justify it at paper level, the project still needs evidence that the proposed reliability target and its estimator add something not already supplied by standard residual, bootstrap, pseudospectral, or parametric uncertainty methods.

---

# What must be demonstrated before a strong novelty claim

1. **Fresh data-level transport.** The admissibility-risk framework must work when the spectral center and sampling uncertainty are both estimated from data.
2. **Trajectory validity.** A provenance-clean stationary correlated-trajectory test must succeed before nonstationary online claims.
3. **Comparison to standard UQ.** Benchmark against residual-based verification, bootstrap/subsampling, and parametric linear-model uncertainty in settings where those methods are applicable.
4. **Nonstationary value.** Show a task where calibrated admissibility/reliability changes what can be inferred from a changing time series.
5. **Independent downstream metric.** If adaptive history is revisited, improvement must be measured by slow-subspace/timescale/metastability recovery, not by an oracle defined using the same selection score.
6. **Theoretical statement at the right level.** Separate new problem formulation/results from classical perturbation and nonregular-inference ingredients.

## Current defensible positioning

A cautious paper-level description is:

> We study reliability of selected slow spectral objects in local data-driven dynamical models. Controlled experiments reveal a failure mode in which non-normal finite-sample perturbations destroy spectral-object admissibility rather than merely increasing conditional subspace error. We develop and falsify increasingly structured operator-level risk descriptions, identify a controlled projected boundary law and certified regime, and investigate the statistical difficulty of translating spectral-admissibility risk to finite-data estimates near nonregular spectral boundaries. In parallel, we show that causal error prediction can remain informative even when the source of observed spectral instability is not identifiable.

This positioning is intentionally narrower than "new adaptive windows", "new Koopman uncertainty", or "new perturbation theory".