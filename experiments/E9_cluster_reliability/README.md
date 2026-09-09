# E9 — Individual-mode versus spectral-cluster reliability

## Scientific role

E9 tested whether cross-scale reliability should be formulated for **individual eigenmodes** or for an **invariant spectral cluster**.

The experiment was motivated by a basic spectral-identifiability issue: when two leading eigenvalues approach each other, individual eigenvectors can rotate, swap, or become a complex conjugate pair even while the two-dimensional slow invariant subspace remains meaningful.

## Scientific question

Does collapse of the inner spectral gap break `r=1` reliability while the isolated `r=2` slow cluster remains calibratable?

## Design

- stationary normal linear VAR(1);
- no dynamical drift;
- no changing observation-noise regime;
- no non-normal true operator;
- causal estimates at `t=512` using only `x_0,...,x_512`;
- cross-scale disagreement calibrated on a separate regular-gap development set;
- complex leading pairs invalidate the chosen real `r=1` object but are retained as a valid real `r=2` invariant span `span(Re(v), Im(v))`.

## Regular-gap replication

Both objects showed useful reliability information in the regular regime.

| object | defined rate | Spearman | AUROC | MAE improvement | median pred/actual |
|---|---:|---:|---:|---:|---:|
| r=1 | 1.000 | 0.548 | 0.822 | 0.247 | 1.010 |
| r=2 | 1.000 | 0.469 | 0.847 | 0.138 | 1.013 |

## Inner-gap collapse

As the second eigenvalue approached the leading one, the individual-mode object became progressively less identifiable:

- at `lambda_2=0.90`, `r=1` defined rate ≈ `0.964`;
- at `lambda_2=0.95`, `r=1` defined rate ≈ `0.772`;
- at `lambda_2=0.97`, `r=1` defined rate ≈ `0.646`.

At the hardest condition, `r=1` Spearman fell to about `0.248` and the median predicted/actual error ratio fell to about `0.618`.

The `r=2` invariant cluster behaved very differently. Across the same conditions its defined rate remained `1.0`, while ranking and calibration remained useful. At the hardest condition:

- Spearman ≈ `0.514`;
- AUROC ≈ `0.848`;
- quartile error ratio ≈ `2.182`;
- MAE improvement ≈ `17.9%`;
- median predicted/actual ≈ `1.196`;
- score-domain support ≈ `0.994`.

## Verdict

**E9 MECHANISM PASS.**

The frozen individual-mode breakdown and all cluster gates passed.

The safe interpretation is:

> Under inner-gap collapse in this controlled stationary normal family, individual-mode reliability degrades because the mode itself becomes poorly identifiable, while the two-dimensional invariant slow cluster remains a substantially more stable reliability target.

## Important limitation that motivated E9b

E9 varied the inner and outer gaps together. Therefore E9 alone could not establish whether the positive `r=2` result came from genuine cluster robustness or from the accompanying outer-gap geometry.

E9b was designed specifically to remove that confound by fixing the true outer gap at `0.27` while collapsing only the inner gap. E9b subsequently passed all confirmatory gates.

## What E9 does not establish

E9 does not establish:

- a universal spectral perturbation theorem;
- a universal uncertainty estimator;
- drift detection or drift/estimation separation;
- non-normal transport;
- nonlinear Koopman or VAMP results;
- universal calibration;
- an adaptive-history result.

## Provenance

Original ZIP SHA256:

`0652b0013b205f69dea30bb38942a00447cfeeca1a7d34a83fbb9444521d0f70`

Archived executable source:

`code/E9_COLAB_ONE_CELL.py`

Verified source SHA256:

`a5155f95f88219f00926f7a22b551978584f8150849cf0bef84b7707939099b8`

The source passed public-release screening for internal workflow references.