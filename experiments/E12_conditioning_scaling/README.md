# E12 — Conditioning/gap scaling

## Scientific role

E12 tested whether a simple one-dimensional perturbation scale based on eigenvector conditioning could provide a **transportable calibrated law** for `r=2` spectral-admissibility failure.

The preregistered primary score was effectively

`kappa * epsilon / g`,

where `kappa` summarizes eigenvector conditioning, `epsilon` is perturbation magnitude, and `g` is the selected spectral gap.

The experiment followed E11, where non-normality was shown to increase loss of spectral-object identity under matched perturbations.

## Final scientific verdict

**E12 CONDITIONING-SCALING HYPOTHESIS NOT SUPPORTED.**

The conditioning-normalized score ranked held-out failure relatively well, with AUROC about `0.829`, but the frozen calibration/log-loss criterion failed. The negative verdict persisted after audit of the class-weighted logistic calibration analysis.

Therefore the defensible statement is:

> `kappa * epsilon / g` carries useful ranking information in the tested family, but it is not established as a universal calibrated admissibility-risk law.

## Important audit correction

The implementation contains a crucial naming/interpretation issue:

```python
sep = g
```

and the preregistered `M6_sep_normalized` model uses

```python
epsilon / sep
```

Thus E12's `sep` variable is the **raw eigenvalue gap `g`**, not a true Schur/Stewart–Sun separation quantity.

Any interpretation claiming that E12 compared the primary score against true invariant-subspace separation is invalid.

This correction does not change the main negative E12 verdict.

## Additional result

Finite-`epsilon` failure probability was non-monotone in many operator cells. This limits the usefulness of a first-order scalar scaling law outside the small-perturbation regime.

## Experimental design

E12 contained two controlled parts:

### Part A — exact 2x2 discriminant

A two-dimensional boundary model used the exact discriminant to study perturbation-induced complexification as a function of gap, shear/non-normality, and perturbation magnitude.

### Part B — matched-direction 3x3 operator experiment

A stationary triangular operator family was perturbed using shared normalized Gaussian directions. Whole `(g,c)` condition cells were split into development and held-out sets.

The primary outcome was whether the intended `r=2` spectral object remained conjugation-closed / admissible.

Simple frozen logistic scores compared different perturbation normalizations. `M5 = kappa * epsilon / g` was preregistered as the primary candidate.

## What E12 establishes

Within the tested operator family:

- conditioning strongly affects admissibility risk;
- conditioning-normalized perturbation magnitude can rank failure probability;
- ranking quality does not imply calibrated probability transport;
- a one-dimensional first-order scaling law is too coarse across the full finite-perturbation grid.

## What E12 does not establish

E12 does not establish:

- a universal non-normal spectral-risk law;
- a universal Koopman/EDMD uncertainty estimator;
- a calibrated probability law from `kappa * epsilon / gap`;
- any result involving true Schur separation under the mislabeled `sep` score;
- a data-level causal diagnostic.

## Relation to later experiments

E12 left open whether global conditioning was merely a useful proxy for more specific spectral geometry.

E13a later found a strong exploratory condition-level association between estimated conditioning and latent admissibility risk. E14a then directly falsified **global-conditioning sufficiency** by matching global `kappa` while moving non-normal coupling relative to the selected spectral boundary.

This makes E12 an important intermediate result: conditioning matters, but scalar global conditioning is not enough.

## Reproducibility

The archived package contains a full standalone source, matched-direction raw outputs, held-out model metrics, plots, and reports.

Verified source SHA256:

`39121d0cb4222e70fd3580c199bcf3743ff5a0f91bfd3aa6e0eff3e22669f7e9`

No internal workflow-tool references were found in the source during public-release screening.