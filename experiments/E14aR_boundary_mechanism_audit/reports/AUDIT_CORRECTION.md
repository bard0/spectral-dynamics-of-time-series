# E14a-R audit correction

## Original automated failure

The archived package marked every epsilon as non-informative and therefore returned no nominated intrinsic candidate.

That conclusion was caused by an implementation bug in the per-epsilon loop.

Instead of filtering the risk table by the current epsilon value, the code reused the first available epsilon row for each `s`. As a consequence, every epsilon iteration saw effectively the same risk vector and the informativeness screen failed by construction.

## Frozen rule

The preregistered informativeness condition was:

- at least five distinct failure probabilities across the 15 operator conditions; and
- failure-probability range at least `0.05`.

Applying that rule correctly to the saved E14a outputs identifies the following informative epsilon values:

- `0.02`
- `0.04`
- `0.08`
- `0.12`
- `0.16`

## Corrected candidate screen

The corrected screen nominates one candidate family for fresh falsification:

`boundary_resolvent_norm = ||(0.55 I - A)^(-1)||_2`

Summary:

| quantity | corrected value |
|---|---:|
| integrated-risk Spearman | 0.9393 |
| block-bootstrap 95% CI | [0.8869, 0.9964] |
| median informative-epsilon Spearman | ~0.8679 |
| geometry-specific ordering A23>A12 and A23>A13 | 5/5 s values |
| leave-one-s-out Spearman | ~0.902–0.965 |

The informative-epsilon Spearman values were approximately:

| epsilon | Spearman |
|---:|---:|
| 0.02 | 0.8356 |
| 0.04 | 0.9442 |
| 0.08 | 0.9393 |
| 0.12 | 0.8679 |
| 0.16 | 0.7500 |

## Mechanism diagnostic

The projected `2×2` boundary discriminant remained an oracle diagnostic because it uses the true eigenbasis and realized perturbation matrix.

For geometry A23, pooled diagnostic performance reconstructed from the saved mechanism rows was approximately:

- sensitivity: `0.9154`;
- specificity: `0.9793`;
- balanced accuracy: `0.9474`;
- MCC: `0.8925`.

This supports the pair-cut mechanism but does not convert the discriminant into a causal estimator.

## Scientific status after correction

The corrected E14a-R conclusion is:

> One boundary-resolvent candidate family was nominated for **fresh falsification only**.

This is exploratory selection, not confirmation. The subsequent fresh E15 experiment refuted the fixed-point boundary-resolvent norm as a standalone transportable admissibility-risk variable.

The original erroneous automatic nomination verdict must not be used in scientific summaries.