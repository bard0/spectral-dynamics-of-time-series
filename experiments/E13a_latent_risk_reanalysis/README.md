# E13a — Latent spectral-admissibility risk reanalysis

## Scientific role

E13a is a **post-hoc exploratory reanalysis** of the saved E13 dataset. It generated no new VAR simulations.

E13 had asked whether probe features could predict the binary failure of an **independent validation realization**. A later design audit showed that this target has a low intrinsic predictability ceiling because probe and validation randomness are independent conditional on the latent system condition.

E13a therefore changed the estimand:

> from predicting one independent Bernoulli failure realization to estimating the **condition-level failure propensity** `p_fail(condition)`.

This is a different scientific question and does not replace the original E13 verdict.

## Data reuse and cross-fitting

The analysis reused the 25,200 saved E13 rows.

Probe summaries were aggregated within conditions and cross-fitted against opposite-parity validation outcomes so that the latent-risk target and the feature summaries were separated across replicate groups.

The primary interest was whether causal observable quantities rank or calibrate the latent probability that the selected `r=2` spectral object becomes non-admissible under the condition.

## Main exploratory result

**E13a STRONG LATENT PRE-FAILURE ASSOCIATION OBSERVED — EXPLORATORY.**

Standalone eigenvector conditioning, especially median `kappa_2H`, strongly ranked latent admissibility risk across unseen conditions:

- fold A Spearman ≈ `0.839`;
- fold B Spearman ≈ `0.869`;
- pooled Spearman ≈ `0.897`;
- pooled bootstrap 95% interval ≈ `[0.785, 0.947]`.

A frozen development-to-test isotonic calibration of median `kappa_2H` reduced condition-level MSE by approximately `71.9%`.

## Aggregation ladder

The result depended strongly on averaging multiple noisy probe estimates.

A single `kappa_2H` probe already gave median held-out Spearman around `0.611` and MSE improvement around `31.8%`. Performance improved as more independent probe estimates were aggregated.

This is consistent with a substantial within-condition noise component: the condition-level signal becomes clearer after aggregation.

## Important negative structure

At the condition level:

- conditioning was strongly positively associated with latent failure propensity;
- `D_K`, `S2`, and the separation-style ratio were negatively associated with latent failure propensity in this family;
- the earlier composite score mixing operator discrepancy, conditioning and gap did not dominate standalone conditioning.

This pattern is consistent with the project-level interpretation that the relevant event can be **loss of spectral-object admissibility** rather than a simple monotone increase in survivor subspace error.

## Why this remains exploratory

E13a is not confirmatory for several reasons:

1. the latent-risk target was introduced after inspection of the E13 design limitation;
2. the analysis reused the same underlying experiment family;
3. aggregation and calibration choices were evaluated on an existing dataset rather than a completely fresh operator/data family;
4. the strong condition-level association does not prove a practical single-trajectory causal predictor;
5. later E14a showed that global conditioning is not a sufficient transportable risk variable when non-normal geometry is relocated relative to the selected spectral boundary.

Therefore the result must be read as:

> **strong exploratory evidence that conditioning carries condition-level admissibility-risk information in the E13 family**, not as a universal calibrated law.

## Relationship to later experiments

E13a created an important tension:

- conditioning looked highly informative after condition-level aggregation;
- but it was unclear whether the signal reflected a genuine intrinsic risk variable or a family-specific proxy for boundary geometry.

E14a directly tested that possibility by matching global conditioning while moving non-normal coupling across the selected spectral boundary. E14a refuted global-conditioning sufficiency.

Thus the sequence is:

`E13 negative single-realization target → E13a strong latent-risk association → E14a matched-conditioning counterexample`.

This progression is central to the project's shift from global scalar reliability scores toward boundary-specific spectral admissibility.

## Claim ceiling

Allowed:

> In the E13 family, aggregated eigenvector conditioning strongly ranked cross-fitted latent condition-level admissibility risk.

Not allowed:

- confirmation of E13;
- a universal conditioning-based failure law;
- a practical online causal guard;
- transport beyond the tested family;
- a new general perturbation-theory result.