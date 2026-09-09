# E15 — Frozen Boundary-Resolvent Transport Falsification

## Purpose

Test a **single frozen intrinsic candidate** on a fresh four-dimensional non-normal operator family:

\[
R_b(A)=\|(0.55I-A)^{-1}\|_2.
\]

The candidate was nominated only after the exploratory E14a-R mechanism audit. E15 did not allow candidate switching after outcomes.

## Frozen family

The tested operators used

\[
\Lambda=\operatorname{diag}(0.70,0.60,0.50,0.40),
\]

with a unit upper-triangular similarity family containing independently variable within-cluster, boundary, excluded-block, and bypass couplings.

The selected spectral cut was `r=2`, with boundary between modes 2 and 3 and fixed evaluation point `z_b=0.55`.

A fresh shared bank of 5,000 normalized Gaussian `4x4` perturbation directions was used over

```text
epsilon = [0.005, 0.01, 0.02, 0.04, 0.08, 0.12, 0.16]
```

with paired bootstrap inference across shared directions.

## Panel A

**Design:** nuisance-matched / resolvent-separated operator pairs.

The prediction was that the operator with larger `R_b` would have larger integrated probability of losing the intended `r=2` conjugation-closed object.

### Audit correction

The archived reporting code stored the pair in `(low_R, high_R)` order but later labeled the first member as high-R when reporting the contrast. This reversed the sign of an already-correct underlying contrast.

Correcting only this orientation, without changing operators, perturbations, bootstrap samples, or thresholds, gives:

- `8/8` Panel-A pairs support the predicted direction;
- corrected high-minus-low integrated-risk differences are approximately `+0.1068` to `+0.1219`;
- representative pair 1: delta approximately `+0.1117`, paired 95% interval approximately `[0.0999, 0.1235]`.

**Correct Panel-A interpretation:** the fixed boundary resolvent carries directional risk information when nuisance geometry is closely matched.

## Panel B

**Design:** resolvent-matched / nuisance-separated pairs.

The prediction was that if `R_b` were a sufficient transportable scalar, tightly matched resolvent values should imply practically equivalent integrated admissibility risk despite nuisance differences.

Panel B was unaffected by the orientation bug.

All eight archived pair comparisons had nearly identical resolvent values, approximately

```text
256.509 vs 256.281
ratio ≈ 1.00089
```

but integrated failure-risk differences were approximately `0.154–0.171`, with paired intervals far outside the frozen equivalence region.

Representative pair 1:

```text
risk AUC ≈ 0.1903 vs 0.3550
delta ≈ 0.1647
95% CI ≈ [0.1551, 0.1746]
```

**Panel-B verdict:** decisive failure of resolvent sufficiency.

## Final verdict

> **E15 FROZEN BOUNDARY RESOLVENT REFUTED AS A STANDALONE TRANSPORTABLE ADMISSIBILITY-RISK SCALAR.**

This does **not** mean resolvent information is useless. The experiment supports a narrower statement:

> In this fresh controlled 4D family, a larger fixed boundary-resolvent norm predicts higher risk when nuisance geometry is closely matched, but matching that scalar does not determine `r=2` admissibility risk when other non-normal geometry changes.

## Secondary observations

Across the 40 selected operators, secondary rank correlation between the scalar resolvent and risk was only moderate (Spearman about `0.538`).

The matched-resolvent counterexamples differed strongly in boundary-pair and global eigenvector geometry, motivating the later E15-R mechanism audit.

## Reproducibility/provenance

The archived scientific source is a 573-line Python program.

```text
source file: E15_COLAB_PROGRAM.py
SHA256: d37783041d1442499a8c4152f91af5c6835179b9dc4db22e5ff8a4feae870ce4
master perturbation seed: 15031501
bootstrap seed: 15031502
perturbation directions: 5000
bootstrap replicates: 10000
```

Archived integrity checks reported:

- 1,400,000 raw outcome rows = 40 operators × 7 epsilon values × 5,000 seeds;
- no duplicate `(operator, epsilon, seed)` keys;
- no missing binary primary fields;
- `failure = 1 - r2_defined` exactly;
- rotation-equivariance sanity `1600/1600`;
- perturbation-bank SHA256 `31e068e137db6ac1790c4338193605a028401efd309524b6d857afe1c056ced8`;
- all 280 operator×epsilon outcome checkpoints were valid hits in the archived final resume run.

The original executable source is preserved in the Drive archive and has been syntax-checked during repository migration. The repository record above contains the **corrected scientific interpretation** rather than silently reproducing the original sign-labeling error.

## Claim ceiling

E15 is an operator-level controlled falsification. It does not establish a universal Koopman uncertainty law, a practical data-only estimator, or a new resolvent/pseudospectral theory.