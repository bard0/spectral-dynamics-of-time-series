# Current Scientific State

## Central question

The active problem is **causal spectral reliability for local Koopman/EDMD models of nonstationary time series**.

The project asks two distinct questions that must not be conflated:

1. **Reliability:** how accurately does the currently estimated slow spectral object represent the underlying local dynamics?
2. **Source attribution:** if the estimate is unstable, is that instability caused by finite-sample estimation error or by genuine evolution of the dynamics?

The experiments show that the first problem can be tractable in controlled regimes even when the second is not identifiable from the same causal observables.

## Core diagnostics

For a history horizon `H` and current time `t`, the project has used quantities such as

\[
S_{scale}(H,t)=d_G(E_H(t),E_{2H}(t)),
\]

where `E_H(t)` is a slow invariant subspace estimated from the most recent `H` observations, and

\[
S_{time}(H,t)=d_G(E_H(t),E_H(t-\Delta)),
\]

as well as temporal operator change

\[
D_K(H,t)=\|K_H(t)-K_H(t-\Delta)\|_F.
\]

A central correction established by the project is that `S_scale` must not automatically be called statistical uncertainty or true drift. It mixes finite-sample error, estimator instability, spectral separation, non-normal sensitivity, model mismatch, and nonstationarity.

## Confirmed or strongly supported results

### Invariant-subspace comparisons are preferable to raw eigenvector comparisons

A controlled mode-swap sanity check produced Grassmann distance on the order of `1e-14` while individual-vector overlap could fall to about `0.13`. This motivated cluster/subspace-based evaluation throughout the later reliability branch.

### Cross-scale disagreement can predict error in regular-gap stationary systems

E8 established useful predictive information in a controlled stationary regular-gap linear-EDMD regime:

- Spearman correlation with actual spectral error approximately `0.51`;
- AUROC approximately `0.79`;
- high/low error quartile ratio approximately `2.34`;
- isotonic calibration reduced MAE by roughly `21%`.

The claim is deliberately narrow: this does not establish universal calibration.

### Cluster reliability is more robust than individual-mode reliability

E9b used an invariant two-dimensional spectral cluster with fixed outer spectral separation. In the hardest primary condition:

- support was about `99.8%`;
- Spearman approximately `0.574`;
- AUROC approximately `0.831`;
- median predicted/actual error approximately `0.992`;
- calibration improved MAE by about `26%`.

Complex leading eigenpairs occurred frequently while the invariant two-dimensional subspace remained well defined.

### Non-normality primarily creates an object-existence failure mode

E10 showed that normal-regime reliability calibration did not transport unchanged across non-normal systems. E11 then used matched operator perturbations to isolate the mechanism:

- the probability that the intended `r=2` real/conjugation-closed spectral object remained defined fell strongly with non-normality;
- conditional Grassmann error among surviving objects did not increase and often decreased;
- the dominant mechanism was perturbation-induced complexification and pair-cut across the selected cluster boundary.

This shifted the target from survivor error alone to **spectral admissibility**.

### Global conditioning is a useful proxy in one family but not a sufficient variable

E13a found a strong exploratory condition-level relationship between estimated eigenvector conditioning and latent admissibility risk in a triangular non-normal VAR family. For median `kappa_2H`, held-out condition-level Spearman correlations were approximately `0.84`, `0.87`, and `0.90` across the cross-fitted summaries, with large calibration gains after aggregation.

E14a then falsified sufficiency. At matched eigenvalues, gaps, perturbation scale, and global conditioning, moving non-normal coupling across the `2|3` retained/excluded boundary changed pair-cut failure probability substantially.

Thus global conditioning is a coarse aggregate and cannot determine admissibility risk by itself.

### A fixed boundary-resolvent scalar is informative but not transportably sufficient

E15 froze

\[
R_b=\|(0.55I-A)^{-1}\|_2
\]

before fresh outcomes in a new four-dimensional family.

After correcting a Panel-A orientation error:

- nuisance-matched, resolvent-separated pairs supported the predicted direction;
- all eight corrected Panel-A comparisons supported higher risk for the larger resolvent, with high-minus-low integrated-risk effects around `0.107–0.122`;
- however, Panel B provided decisive counterexamples: operators with nearly identical `R_b` had integrated failure-risk differences around `0.154–0.171` when other non-normal geometry differed.

Therefore:

> `R_b` is informative but is **not sufficient and not transportable as a standalone admissibility-risk variable**.

The E15-R mechanism audit further showed that a projected `2x2` boundary discriminant tracks much of the high-risk failure geometry, but the counterexample family contains co-varying mechanisms and does not isolate a unique replacement variable.

## Strong negative results

### Nested disagreement is not a direct drift proxy

E8's predecessor and the broader adaptive-horizon tests established that

\[
d_G(E_H,E_{2H})
\]

correlates poorly with true dynamical drift in controlled nonstationary systems. The original interpretation of a direct "coherence horizon" was therefore abandoned.

### Generic adaptive-horizon superiority was not established

Across fixed-window, Lepski-like, prediction-loss, forgetting, gap-based, Grassmann-based, and related causal selectors, no method showed a robust general advantage across all tested systems. This caused the project to move away from generic adaptive-window claims.

### A simple conditioning-normalized law is not universally calibrated

E12 tested a score of the form `kappa * epsilon / gap`. It ranked held-out failure relatively well, with AUROC around `0.83`, but failed the frozen calibration/log-loss criterion. The result does not support a universal calibrated law.

### Single-replicate data-only admissibility prediction was design-limited

E13 attempted to predict whether an independent validation realization would lose the spectral object. Because probe and validation noise were independent conditional on the underlying condition, even a condition-propensity oracle could not reach the preregistered success gates. E13 is therefore retained as a design-limited negative rather than a branch-stopping refutation of latent risk predictability.

### Strong source decomposition failed in EXP-009 Gate 1

After a pilot redesign achieved overlap in total observable instability, the frozen confirmatory test used 4,000 fresh trajectories and 3,982 supported rows. Support was `0.9955` in both regimes.

Held-out AUROC values were near chance:

- `S_scale`: `0.484`;
- `S_time`: `0.467`;
- temporal operator difference: `0.513`;
- spectral gap: `0.482`;
- joint scale-time model: `0.467`;
- full joint model: `0.470`.

The joint scale-time model did not improve over the best individual scale/time diagnostic; bootstrap confidence intervals included no positive added value.

Frozen verdict:

> **Strong decomposition of finite-sample estimation instability versus smooth true drift is not identifiable from the tested diagnostics in this controlled family.**

At the same time, `S_scale` retained Spearman correlation around `0.51` with true slow-subspace estimation error. This separates **error prediction** from **source attribution**.

## Current working interpretation

The evidence currently supports the following hierarchy:

1. Spectral error can sometimes be predicted from causal cross-scale information.
2. Reliability calibration is conditional on spectral separation and operator geometry.
3. Non-normality can destroy the identity of the selected spectral object rather than simply increase survivor error.
4. Global scalar conditioning and a single resolvent norm discard important boundary-local and directional information.
5. Observable instability magnitude does not uniquely encode whether the underlying cause is estimation noise or dynamical drift.
6. Adaptive history selection should remain downstream until a causal reliability diagnostic has survived transport across operator families and nonstationary settings.

## Claim ceiling

The project does **not** currently claim:

- a universal uncertainty estimator for Koopman/EDMD spectra;
- a universal non-normal spectral-risk law;
- a new general adaptive-window algorithm;
- general identifiability of estimation noise versus dynamical drift;
- a new resolvent or pseudospectral theory.

The strongest current niche is the study of **causal, data-driven reliability and admissibility of selected slow spectral objects**, including explicit characterization of failure mechanisms and identifiability limits.