# E14a — Matched-conditioning geometry falsification

## Scientific role

E14a is the controlled operator-level falsification that broke the project's earlier interpretation of **global eigenvector conditioning** as a sufficient description of spectral-admissibility risk.

The experiment asks a narrow question:

> If eigenvalues, raw gaps, perturbation distribution and magnitude, global eigenvector conditioning, and overall departure from the diagonal reference are matched, does relocating the same non-normal coupling relative to the selected `r=2` spectral boundary change the probability that the selected spectral object ceases to be admissible?

The answer in this controlled family is **yes**.

## Frozen construction

The unperturbed spectrum is

`Lambda = diag(0.70, 0.60, 0.50)`

and the selected object is the top-2 spectral cluster. Three one-shear geometries were studied:

- `12`: non-normal coupling within the retained side;
- `23`: non-normal coupling across the retained/excluded boundary;
- `13`: secondary long-range control.

The primary matched comparison is `12` versus `23` for

`s ∈ {0.5, 1, 2, 4, 6}`.

For every `s`, the primary pair exactly matched target eigenvalues, raw gaps, spectral radius, normalized global condition number, and `||A - Lambda||_F` within the frozen tolerances.

The perturbation grid was

`epsilon ∈ {0.005, 0.01, 0.02, 0.04, 0.08, 0.12, 0.16}`

with 10,000 shared Frobenius-normalized Gaussian perturbation directions per cell and 20,000 paired-bootstrap replicates. The same direction bank was used across the matched geometries.

## Primary result

**E14a GLOBAL KAPPA SUFFICIENCY REFUTED.**

Across informative cells, moving the non-normal coupling from geometry `12` to the boundary-crossing geometry `23` increased the probability that the selected `r=2` object became non-admissible, despite matched global conditioning.

The largest observed paired effect occurred at `s=6`, `epsilon=0.04`:

- failure probability `p12 = 0.0569`;
- failure probability `p23 = 0.3855`;
- paired difference `p23 - p12 = 0.3286`;
- paired-bootstrap 95% interval `[0.3180, 0.3391]`.

The positive boundary direction was also supported under the frozen mechanism gate.

## Why this matters

The experiment separates two statements that had previously been conflated:

1. global conditioning can correlate with fragility inside a restricted family;
2. global conditioning is sufficient to determine fragility across different placements of non-normal geometry.

E14a rejects the second statement.

The spectral boundary itself matters. A scalar global condition number discards information about **where** non-normal coupling sits relative to the retained/excluded cut.

## Secondary diagnostics

Boundary-local quantities changed even when global conditioning was matched. For example, at `s=6`:

| geometry | global kappa | projector norm r=2 | true Schur separation | boundary resolvent norm |
|---|---:|---:|---:|---:|
| 12 | 12.082763 | 1.000000 | 0.031272 | 82.715452 |
| 23 | 12.082763 | 6.082763 | 0.100000 | 241.655251 |
| 13 | 12.082763 | 6.082763 | 0.100000 | 161.380798 |

These quantities were **secondary diagnostics**, not pre-established replacements for global conditioning.

Conditional error among surviving spectral objects is also reported in the archived run, but survivor error does not override the failure-based admissibility verdict.

## Interpretation ceiling

Supported:

> In this controlled finite-dimensional operator family, matched global eigenvector conditioning does not imply matched `r=2` spectral-admissibility risk when non-normal geometry is relocated relative to the selected cluster boundary.

Not established:

- a universal Koopman/EDMD uncertainty law;
- a universal non-normal perturbation theorem;
- a practical data-level diagnostic;
- a new Schur, resolvent, or pseudospectral method;
- a nonstationary or adaptive-history result.

## Consequence for the project

E14a stopped the planned attempt to confirm a global-kappa law at the data level. The next step became a **boundary-specific mechanism audit**, E14a-R, with the explicit rule that any candidate found there would remain post-hoc and would require fresh falsification in a new operator family.

## Reproducibility

The original executable source and frozen configuration are included in this package. The archived source SHA256 is:

`ec2fdbeb7e84aa2cfea01e3a2210d17b1832c4b421ed7eac4cc8230c141462a5`

The exact source copied here was checked against that hash before migration.