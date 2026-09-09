# Experiment Ledger

This ledger preserves positive, negative, inconclusive, exploratory, and implementation-corrected results. Later experiments do not erase earlier failures.

Status vocabulary:

- **CONFIRMED** — replicated or robust within the stated tested regime.
- **SUPPORTED** — primary hypothesis supported in the stated controlled setting.
- **REFUTED** — frozen hypothesis or claimed mechanism failed.
- **INCONCLUSIVE** — evidence insufficient or design did not test the intended hypothesis cleanly.
- **EXPLORATORY** — informative post-hoc result, not claim-ready.
- **AUDIT/FIX** — implementation or methodology correction that must be retained with the result.

## E1 — Local EDMD bias–variance analysis

**Question.** How does local estimation error trade off against nonstationarity bias as history length grows?

**Result.** Derived leading upper-bound structure approximately `A/n + C L^2 n^2`. Numerical checks supported an `n^-1` statistical term, an `n^2` drift term, and upper-bound minimizer scaling near `L^(-2/3)` with fitted exponent about `-0.6675`.

**Status.** CONFIRMED as an upper-bound/numerical sanity result.

**Limitation.** The scaling is for the minimizer of the derived bound, not a theorem for the true expected-risk minimizer.

---

## E2 — Causal Lepski-style selector

**Question.** Can finite-sample confidence radii support useful causal history selection?

**Result.** The radii were too conservative; most candidate windows were compatible and the selector often chose the largest window.

**Status.** REFUTED as a practically effective selector in the tested setup.

---

## E3 — Mode-swap / Grassmann sanity check

**Question.** Can invariant-subspace geometry avoid false changes caused by eigenvector sign/order swaps?

**Result.** Maximum Grassmann distance under a mode swap was about `1.1e-14`, while individual-vector overlap could fall to about `0.13`.

**Status.** CONFIRMED.

**Consequence.** Prefer invariant subspaces or spectral clusters over raw eigenvector identities.

---

## E4 — Adaptive spectral window / oracle benchmark

**Systems.** Controlled AR/VAR/Markov-style nonstationary systems.

**Methods.** Fixed windows, Lepski-like rules, drift-only criteria, Grassmann criteria, spectral-gap criteria, oracle comparisons.

**Result.** Adaptive heuristics did not consistently beat simple fixed windows; several criteria were conservative or unstable.

**Status.** EXPLORATORY / negative for a broad superiority claim.

---

## E5 — Smooth-drift benchmark

**Question.** Do adaptive spectral rules help in smooth nonstationarity where abrupt change-point methods are less natural?

**Result.** Some adaptive methods improved over the largest fixed window in parts of the benchmark, but behavior was inconsistent across scenarios.

**Status.** INCONCLUSIVE for a general selector claim.

---

## E6 — Noise-change controls

**Issue.** The original interpretation conflated observation-noise changes with changes in latent dynamics.

**Correction.** Observation noise and process noise were separated conceptually and experimentally.

**Status.** AUDIT/FIX.

**Rule retained.** Increased observation noise does not imply a changed Koopman operator and can make longer histories preferable.

---

## E7 — Broad causal online spectral benchmark

**Methods.** Fixed windows, prediction-loss adaptation, Lepski-like selection, forgetting EDMD, Grassmann-only, gap-only, VAMP-inspired lag stability, threshold/coherence-style horizons.

**Result.** No robust general advantage of a spectral horizon selector was established.

**Status.** INCONCLUSIVE / supports reframing away from generic adaptive-window claims.

---

## E7 directional branch — Null-calibrated directional diagnostic

**Question.** Does directional information add predictive value beyond instability magnitude?

**Result.** Directional added value was approximately `-0.098` with a wide confidence interval crossing zero; AUROC was about `0.454`, and a key support gate failed.

**Status.** REFUTED / branch-stopping for the tested directional-added-value hypothesis.

---

## E8 — Cross-scale reliability in a stationary regular-gap family

**Question.** Does nested cross-scale disagreement predict actual slow-subspace estimation error?

**Result.** Spearman approximately `0.510`, AUROC approximately `0.788`, high/low error quartile ratio approximately `2.34`, and isotonic calibration MAE improvement approximately `20.8%`.

**Status.** SUPPORTED in the tested regular-gap stationary linear-EDMD regime.

**Limitation.** Calibration degraded across changing-gap conditions and complex-mode cases.

---

## E9 — Cluster reliability precursor

**Purpose.** Move from fragile individual-mode reliability to invariant spectral-cluster/subspace reliability.

**Status.** COMPLETED precursor; not the final confirmatory result.

---

## E9b — Fixed-outer-gap cluster reliability

**Question.** Does `r=2` cluster reliability survive complex leading modes when the outer gap is controlled?

**Hardest primary condition.** Support approximately `99.8%`; Spearman approximately `0.574`; AUROC approximately `0.831`; high/low quartile ratio approximately `2.30`; median predicted/actual approximately `0.992`; MAE improvement approximately `26.4%`.

**Status.** SUPPORTED in the tested covariance-neutral stationary family with fixed outer gap.

**Limitation.** No claim for arbitrary covariance structure, nonstationarity, nonlinear dictionaries, or general Koopman operators.

---

## E10 — Non-normal reliability transport

**Question.** Does normal-regime `r=2` cross-scale reliability calibration transport to stationary non-normal systems at fixed eigenvalues and gaps?

**Result.** FAIL. At high non-normality the selected object became undefined much more often, ranking degraded, and calibration did not transport.

**Status.** REFUTED as an unchanged transport claim.

**Consequence.** Object-existence failure became a primary target.

---

## E11 — Matched non-normal operator perturbations

**Question.** Under identical finite perturbations, does increasing non-normality amplify survivor subspace error or primarily change object existence?

**Result.** Defined-rate decreased strongly with non-normality. Conditional Grassmann error among surviving objects did not increase and often decreased. The dominant mechanism was pair-cut complexification across the retained/excluded spectral boundary.

**Status.** Mechanism SUPPORTED; conditional-error-amplification hypothesis REFUTED.

---

## E12 — Conditioning/gap scaling

**Question.** Can a simple score such as `kappa * epsilon / gap` provide a transportable calibrated failure law?

**Result.** Ranking was comparatively strong (AUROC about `0.829`) but the frozen calibration/log-loss gate failed.

**Status.** REFUTED as a universal calibrated law.

**Audit correction.** One reported separation variable was the raw eigenvalue gap rather than the intended Schur/Stewart–Sun separation. Claims involving true Schur separation from that stage are invalid.

---

## E13 — Causal data-only spectral-admissibility prediction

**Question.** Can features from causal nested estimates predict whether an independent same-budget validation estimate loses the `r=2` object?

**Official result.** Prediction not supported.

**Design audit.** Probe and validation realization noise were independent conditional on the operator condition, so single-row prediction targeted an independent Bernoulli outcome. A condition-propensity oracle itself could not reach the preregistered gates.

**Status.** INCONCLUSIVE / DESIGN-LIMITED NEGATIVE.

---

## E13a — Latent admissibility-risk reanalysis

**Type.** Post-hoc reanalysis; no new simulations.

**Question.** Are causal spectral summaries associated with latent condition-level failure propensity?

**Result.** Strong exploratory association for estimated eigenvector conditioning. Median `kappa_2H` achieved held-out condition-level Spearman values around `0.84`, `0.87`, and `0.90` across cross-fitted summaries, with large calibration gains after aggregation.

**Status.** STRONG EXPLORATORY / NOT CLAIM-READY.

**Consequence.** Fresh families were required to test whether conditioning was causal/transportable or merely a family-specific proxy.

---

## E14a — Matched-conditioning geometry falsification

**Question.** Is global eigenvector conditioning sufficient to determine `r=2` admissibility risk?

**Design.** Matched eigenvalues, raw gaps, perturbation norm/distribution, and global conditioning while relocating non-normal coupling relative to the selected `2|3` spectral boundary.

**Result.** Boundary-crossing coupling produced substantially higher pair-cut failure than matched within-cluster coupling. The largest reported matched effect was approximately `0.329` in failure probability with a narrow paired-bootstrap interval.

**Status.** GLOBAL CONDITIONING SUFFICIENCY REFUTED; boundary-coupling direction SUPPORTED in the controlled family.

---

## E14a-R — Boundary-specific mechanism audit

**Type.** Post-hoc mechanism analysis using the existing E14a outcomes.

**Initial implementation issue.** An informative-epsilon flag bug invalidated the automated candidate-nomination result.

**Corrected interpretation.** A fixed boundary-resolvent norm was nominated only as a candidate for fresh falsification, not as an established method.

**Status.** EXPLORATORY / IMPLEMENTATION-CORRECTED.

---

## E15 — Frozen boundary-resolvent transport falsification

**Frozen candidate.** `R_b = ||(0.55 I - A)^(-1)||_2` in a fresh four-dimensional `r=2` operator family.

**Primary correction.** A Panel-A orientation bug reversed the reported sign of already-computed contrasts. After correcting orientation, all eight nuisance-matched/resolvent-separated pairs supported the predicted direction, with high-minus-low integrated-risk effects approximately `+0.107` to `+0.122`.

**Decisive failure.** Panel B was unaffected by the bug. Operators with nearly identical frozen `R_b` (ratio approximately `1.00089`) had integrated admissibility-risk differences approximately `0.154–0.171`, with paired intervals far outside the equivalence region.

**Status.** `R_b` REFUTED as a standalone transportable admissibility-risk scalar.

**Safe interpretation.** The scalar carries directional information under nuisance matching but is not sufficient across non-normal geometries.

---

## E15-R — Mechanism audit of matched-resolvent counterexamples

**Type.** Post-hoc mechanism reanalysis; E15 verdict fixed.

**Result.** A projected `2x2` boundary discriminant explained much of the high-risk structural type, with strong sensitivity/specificity in the canonical counterexample. Off-boundary modal mixing plausibly explained residual failures in the lower-risk type.

**Audit limitation.** The eight Panel-B pairs reduce to one unordered structural comparison up to sign/symmetry, and several candidate mechanisms co-vary. A unique replacement mechanism is therefore not isolated.

**Status.** EXPLORATORY MECHANISM RESULT; no new scalar nominated.

---

## EXP-009 Gate 1 — Causal source identifiability

### Pilot v1

**Goal.** Compare finite-sample estimation instability against smooth true dynamical drift at matched observable instability magnitude.

**Result.** Pilot stopped before confirmatory evaluation because the regimes did not overlap sufficiently in `M_ST = sqrt(S_scale^2 + S_time^2)`.

**Status.** INCONCLUSIVE DESIGN / preserved as pilot failure.

### Pilot v2

The data-generating grids were recalibrated using fresh pilot seeds only. Same-history matching yielded the required ten disjoint condition pairs with adequate `M_ST` overlap and high support.

**Status.** DESIGN READY; no scientific confirmatory claim from pilot data.

### Frozen confirmatory test

**Fresh data.** 4,000 independent trajectories; 3,982 supported rows; support `0.9955` in both regimes. The held-out amplitude-overlap gate passed.

**Held-out AUROC.** `S_scale=0.484`, `S_time=0.467`, temporal operator difference `=0.513`, gap `=0.482`, joint scale-time `=0.467`, full joint model `=0.470`.

**Added value.** Joint scale-time minus best individual scale/time diagnostic approximately `-0.0167`, bootstrap 95% CI approximately `[-0.0698, 0.0023]`.

**Status.** STRONG NEGATIVE.

**Frozen verdict.** Strong decomposition of finite-sample estimation instability versus smooth true drift is not identifiable from the tested causal diagnostics in this controlled family.

**Positive residue.** `S_scale` still correlated with actual slow-subspace estimation error at approximately `0.51`, supporting reliability prediction even when source attribution failed.

---

# Methodology corrections retained across the project

1. An early objective of the form `D(H,t) - lambda/H` had the wrong incentive and favored small histories; it was abandoned.
2. Spectral-gap/identifiability checks were added explicitly.
3. An explicit uncertain state was introduced rather than forcing a decision when the spectral object was poorly identified.
4. Per-time diagnostic exports were added for causal auditing.
5. Observation-noise and process-noise controls were separated.
6. Direct future leakage was audited and excluded from the causal logic.
7. Post-hoc analyses are labeled exploratory and are not promoted to confirmatory claims without fresh data.
8. Implementation bugs that alter interpretation are recorded with the affected experiment rather than silently overwritten.