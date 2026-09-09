# Consolidated Results

This directory is a compact index of the project's main empirical and theoretical outcomes.

The detailed scientific history remains in `docs/experiment_ledger.md`, while experiment-specific provenance is stored under `experiments/` and the theory program under `theory/`.

## Result classes

The repository uses the following distinctions:

- **SUPPORTED / CONFIRMED** — passed a frozen or otherwise defensible controlled test;
- **REFUTED / NEGATIVE** — the tested hypothesis failed;
- **INCONCLUSIVE** — evidence did not pass support or failure thresholds;
- **DESIGN-LIMITED** — the experiment could not answer the intended question because a prerequisite/gate failed;
- **EXPLORATORY** — useful post-hoc or screening evidence, not claim-ready confirmation;
- **PROVENANCE-INVALIDATED** — numerical history retained, but executable provenance is insufficient for a reproducible scientific claim.

## Main scientific chain

| Stage | Main result | Status |
|---|---|---|
| E1 | local EDMD upper-bound minimizer scales approximately as `L^-2/3` | confirmed upper-bound sanity |
| E2 | statistically valid Lepski-style radii were too conservative for practical selection | refuted in tested setup |
| EXP-008 | nested spectral disagreement is not a direct true-drift proxy | refuted |
| E8 | cross-scale disagreement predicts estimation error in a regular stationary regime | supported in controlled regime |
| E9/E9b | invariant-cluster reliability survives internal mode ambiguity better than individual-mode reliability | supported |
| E10 | normal-regime calibration does not transport unchanged under non-normality | negative transport result |
| E11 | non-normality primarily increases spectral-object loss through pair cut/complexification | mechanism supported |
| E12 | `kappa*epsilon/gap` ranks risk but does not provide a universal calibrated law | calibration hypothesis not supported |
| E13 | independent-realization failure is not predictable from tested cheap observables at preregistered level | negative, design-limited |
| E13a | aggregated conditioning strongly ranks latent condition-level risk | exploratory |
| E14a | matched global conditioning does not imply matched admissibility risk | refuted sufficiency |
| E14a-R | boundary resolvent nominated after corrected post-hoc screen | exploratory nomination |
| E15 | fixed single-point boundary resolvent is not a sufficient transportable risk variable | refuted |
| T5/T6 | exact projected boundary-complexification law matches fresh simulations | supported |
| T7 | second-order correction fails as a global finite-epsilon full-risk predictor | refuted globally |
| T9 | Riccati/Sylvester certified subset makes the second-order model useful | supported in certified subset |
| T10 | conservative pre-certificate useful; independence factorization fails | mixed: useful + refuted simplification |
| T11 | shared-radial joint law and safe-core geometry survive fresh test | supported |
| T12-A1 | plug-in OLS sampling law predicts risk with oracle spectral center | supported |
| T12-A2b | larger N alone does not repair point-centered spectral-risk estimation near the tested boundary | refuted |
| T12-A2c2 | local point-risk nonregularity persists under `N^-1/2` boundary approach | supported in controlled matrix family |
| T12-A3 | center-uncertainty spectral-risk intervals attain high nominal coverage | supported |
| T12-A4b | Riesz risk-interval transport across fresh non-normal embeddings | supported; separate chart gate marginally design-limited |
| T12-B1 | correlated-trajectory historical result | provenance-invalidated |
| EXP-009 | source attribution between estimation instability and smooth drift from tested causal observables | strong negative |

## Interpretation

The project does not end with a single successful scalar diagnostic. Its main result is a progressively sharper description of **where spectral reliability is identifiable and where it is not**.

The strongest recurring pattern is:

1. invariant-cluster reliability can be calibrated in regular regimes;
2. non-normal geometry introduces an object-existence problem;
3. global scalar sensitivity summaries are too coarse;
4. boundary-local probability laws can be derived and validated;
5. point risk becomes statistically nonregular near the admissibility boundary;
6. uncertainty intervals can remain well calibrated even when a point-risk estimate cannot concentrate;
7. knowing that an estimate is unreliable is easier than identifying the physical/statistical source of that unreliability.