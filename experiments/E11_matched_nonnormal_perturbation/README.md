# E11 — Matched non-normal operator perturbations

## Scientific role

E11 was a mechanism falsification experiment designed to explain the transport failure observed in E10.

Instead of simulating trajectories or fitting EDMD models, E11 works directly at the operator level. The same normalized Gaussian perturbation directions are applied to a controlled `3×3` family while non-normality is varied through the parameter `c`.

This removes finite-sample estimation and trajectory covariance as competing explanations.

## Frozen question

Under identical finite operator perturbations, does increasing non-normality cause:

1. a larger probability that the intended `r=2` spectral object ceases to exist; and/or
2. larger conditional Grassmann error among realizations where that object still exists?

## Design

Base family:

```text
A(c) = [[0.7, 0,       0],
        [0,   0.6, -0.1c],
        [0,   0,     0.5]]
```

with `c ∈ {0,2,4,6}`.

The eigenvalues and the selected spectral gaps are fixed while non-normality increases with `c`.

For every frozen perturbation amplitude, the **same 5,000 normalized Gaussian perturbation directions** are reused across all `c` values. This matched-direction construction isolates operator geometry.

The selected `r=2` object is admissible when the two leading modes are either both real or form a complete complex-conjugate pair. A pair cut that retains only one member of a complex pair is counted as loss of object identity.

## Result

**E11 PURE NONNORMAL SPECTRAL-SENSITIVITY MECHANISM SUPPORTED.**

The key result is asymmetric:

- the probability that the `r=2` object remained defined decreased strongly as non-normality increased;
- conditional Grassmann error among the realizations where the object survived did **not** show the hypothesized generic amplification and often decreased.

Therefore the important failure mode was not simply

> non-normality → larger subspace error.

It was instead

> non-normality → perturbation-induced complexification / pair cut → loss of the selected spectral object's identity.

The conditional-error-amplification hypothesis was therefore **refuted**, while the object-existence mechanism was supported.

## Why this mattered

E10 had shown that a reliability calibration learned in a regular normal regime failed to transport into a non-normal family. E11 identifies a concrete mechanism for that failure: the target object itself can disappear before survivor error becomes large.

This forced a change in the scientific target. Reliability could no longer be evaluated only conditionally on a spectral object having survived. The probability of **spectral admissibility** had to become an explicit object of study.

That shift directly motivated E12–E15 and the later spectral-admissibility theory branch.

## What E11 establishes

For this controlled `3×3` operator family under matched finite perturbations:

- non-normal geometry changes the probability of retaining a conjugation-closed `r=2` object;
- pair-cut complexification is a dominant observed mechanism;
- survivor subspace error is not a sufficient summary of spectral reliability.

## What E11 does not establish

E11 does not establish:

- a universal theorem for arbitrary non-normal operators;
- a complete explanation of every E10 failure;
- a practical data-only reliability score;
- a drift-versus-uncertainty decomposition;
- novelty of Schur, eigenvector-conditioning, or pseudospectral perturbation theory.

## Reproducibility

The archived experiment includes:

- full executable one-cell source;
- frozen configuration;
- matched-direction raw checkpoints for each epsilon;
- aggregated outcomes;
- paired bootstrap summaries;
- preregistered gates;
- figures and audit reports.

Verified source SHA256:

`0f13104ac089e5a2c9c55e08ce8a6098d4101641a9a8ac6eb5c737aafdaa78fd`

The source passed the public-release screening for internal workflow references.