# E13 — Causal data-only spectral-admissibility guard

## Scientific question

Can cheap **causal, data-only observables** computed from nested local operator estimates predict whether an independent validation realization will lose the intended `r=2` spectral object?

This experiment followed E10–E12, where non-normality and conditioning were found to affect spectral-object admissibility. E13 asked whether those mechanisms could be turned into an operational predictor without oracle access to the true operator.

## Primary target

The target was a binary event:

> Does an **independent validation trajectory**, generated under the same underlying condition and data budget, fail to produce an admissible `r=2` spectral object?

The probe and validation realizations were independent conditional on the underlying system condition.

Candidate causal features included:

- temporal/operator discrepancy `D_K`;
- nested/subspace discrepancy `S2`;
- raw spectral-gap ratio;
- conditioning-based ratio;
- separation-style ratio;
- a frozen joint model.

## Frozen held-out result

**E13 DATA-ONLY SPECTRAL-ADMISSIBILITY PREDICTION NOT SUPPORTED.**

Held-out metrics from the archived scientific report:

| method | AUROC | PR-AUC | Brier | log loss |
|---|---:|---:|---:|---:|
| constant | 0.5000 | 0.3069 | 0.2128 | 0.6168 |
| D_K | 0.4997 | 0.3069 | 0.2129 | 0.6206 |
| S2 | 0.5008 | 0.3077 | 0.2127 | 0.6166 |
| gap ratio | 0.5016 | 0.3081 | 0.2128 | 0.6204 |
| conditioning ratio | 0.5327 | 0.3278 | 0.2122 | 0.6154 |
| separation-style ratio | 0.4960 | 0.3052 | 0.2129 | 0.6209 |
| joint | 0.5233 | 0.3146 | 0.2124 | 0.6158 |

The preregistered support, signal, and joint-added-value gates failed.

## Post-run design audit

The negative numerical result is real, but its interpretation requires an important design qualification.

The probe features and the target validation failure are based on **independent realizations** of the same latent condition. Therefore probe features can at best estimate the condition-level failure propensity

`p_fail(condition)`

rather than deterministically predict the Bernoulli outcome of another realization.

A condition-level oracle ceiling was itself below the preregistered positive gates:

- held-out oracle AUROC ≈ `0.650`;
- Brier improvement ≈ `6.8%`.

Thus the original positive gate was effectively unattainable for the chosen single-realization target.

For this reason the final scientific status is:

> **INCONCLUSIVE / DESIGN-LIMITED NEGATIVE**, while the original preregistered verdict remains unchanged.

E13 must not be rewritten as a success.

## What E13 still establishes

Within this controlled stationary VAR setting:

- `D_K`, `S2`, gap-based and separation-style scores had little single-row predictive value for an independent validation failure;
- conditioning showed only a weak single-row exploratory signal;
- the distinction between **predicting a realization** and **estimating a latent failure propensity** is scientifically essential.

This distinction motivated E13a.

## Relation to E13a

E13a did **not** rerun E13 or replace its target. It reused the saved E13 rows and changed the estimand from the independent Bernoulli outcome to a cross-fitted **condition-level latent admissibility risk**.

Therefore:

- E13 remains a negative/design-limited experiment;
- E13a is a separate post-hoc exploratory reanalysis;
- E13a cannot retroactively turn E13 into a positive confirmatory result.

## Claim ceiling

E13 does not establish:

- a universal data-only uncertainty estimator;
- a universal non-normality diagnostic;
- a drift detector;
- an adaptive-history method;
- a new Schur or pseudospectral method;
- general impossibility of spectral-admissibility prediction.

Its strongest lesson is methodological: **the statistical target must match what causal observables can identify.**