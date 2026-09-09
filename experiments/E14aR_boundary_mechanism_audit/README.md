# E14a-R — Boundary-specific mechanism audit

## Scientific role

E14a-R is a **post-hoc exploratory mechanism audit** of the already completed E14a operator family. It generated no new perturbation outcomes.

E14a had established that matched global eigenvector conditioning does not imply matched `r=2` spectral-admissibility risk when non-normal geometry is moved relative to the selected spectral boundary. E14a-R asked which boundary-local quantities might explain that ordering well enough to justify one fresh, preregistered falsification experiment.

The analysis considered a deliberately small theory-motivated candidate set, including:

- boundary-pair angle/cosine;
- boundary-pair conditioning;
- boundary eigenvalue conditioning;
- retained-cluster projector norm;
- true Schur separation;
- a fixed-boundary resolvent norm;
- modal perturbation susceptibility;
- an oracle projected `2×2` boundary discriminant.

No candidate discovered here was allowed to become a claim-ready metric without a fresh experiment.

## Important implementation correction

The original package automatically reported:

> `NO INTRINSIC BOUNDARY CANDIDATE NOMINATED`

That automated verdict is **invalid**.

A subsequent audit found that the per-epsilon analysis reused the first epsilon row for each `s` instead of filtering by the current epsilon. This caused every epsilon to be marked non-informative and forced the stability screen to fail for every candidate.

The saved E14a outputs show that the frozen informativeness rule is actually satisfied for

`epsilon = {0.02, 0.04, 0.08, 0.12, 0.16}`.

Therefore the public scientific record uses the corrected screen, not the erroneous automatic package verdict.

## Corrected result

**E14a-R ONE CANDIDATE FAMILY NOMINATED FOR FRESH FALSIFICATION — `boundary_resolvent_norm`.**

This result is strictly:

**POST-HOC / EXPLORATORY / NOT CLAIM-READY.**

For the frozen boundary point `z_b = 0.55`, the boundary-resolvent candidate showed:

- geometry ordering `A23 > A12` and `A23 > A13` in `5/5` values of `s`;
- integrated-risk Spearman correlation `rho = 0.9393`;
- block-bootstrap 95% interval approximately `[0.8869, 0.9964]`;
- informative-epsilon Spearman values approximately
  `[0.8356, 0.9442, 0.9393, 0.8679, 0.7500]` for
  `epsilon = [0.02, 0.04, 0.08, 0.12, 0.16]`;
- leave-one-`s`-out Spearman values remaining positive and high, approximately `0.902–0.965`.

The candidate was not practically redundant with the other tested intrinsic quantities under the frozen redundancy rule.

## Mechanistic oracle result

The projected boundary discriminant

`[g + epsilon(E22 - E33)]^2 + 4 epsilon^2 E23 E32`

was evaluated in the true eigenbasis using the realized perturbation direction. It therefore serves as an **oracle mechanistic diagnostic**, not as a causal data-only predictor.

Using the saved mechanism rows, pooled performance was strong for the principal boundary-crossing geometry:

- `A23`: sensitivity ≈ `0.9154`, specificity ≈ `0.9793`, balanced accuracy ≈ `0.9474`, MCC ≈ `0.8925`;
- pooled `A12 + A23`: sensitivity ≈ `0.8768`, specificity ≈ `0.9780`, balanced accuracy ≈ `0.9274`, MCC ≈ `0.8457`.

The `A13` control had lower sensitivity, approximately `0.679`, consistent with additional interactions not captured by an isolated boundary `2×2` block.

## Why this did not establish the resolvent candidate

E14a-R reused the E14a family and outcomes. The resolvent nomination was therefore a **screening result**, not confirmation.

The only legitimate next step was to freeze that one candidate and test it on a new family designed to separate resolvent sensitivity from global conditioning, boundary-pair conditioning, projector norm, and other nuisance geometry.

That fresh experiment is E15.

E15 subsequently refuted the single fixed-boundary resolvent norm as a standalone transportable admissibility-risk variable. E14a-R is retained because it documents why that candidate was selected for falsification, not because it survived.

## Reproducibility caveats

The original E14a-R package has important archival defects:

- the source file stored inside the original package contains only the tail of the executed program rather than the full executable source;
- several audit markdown files are placeholders rather than substantive audits;
- one confusion table contains cell-level summaries although the report describes pooled behavior;
- the original per-epsilon nomination screen contains the implementation bug described above.

A complete source was subsequently available for static inspection and confirmed the exact per-epsilon bug, but the original package itself does not satisfy the standard required for a fully self-contained reproducibility archive.

For this reason, GitHub presents E14a-R as an **audited historical mechanism package with a corrected scientific record**, not as an independently reproducible confirmatory run.

## Claim ceiling

Allowed:

> In the E14a operator family, boundary-local geometry explains variation in admissibility risk that matched global conditioning misses, and a fixed-boundary resolvent was sufficiently promising under a corrected post-hoc screen to justify one fresh falsification experiment.

Not allowed:

- a universal resolvent risk law;
- a new pseudospectral or resolvent theory;
- a practical Koopman/EDMD uncertainty estimator;
- a data-level or causal validation claim;
- treating the E14a-R nomination as confirmation.