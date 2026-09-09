# T4–T6 — Boundary sign geometry and exact projected-complexification probability

## Setup

Let

`A = V Lambda V^{-1}`

and perturb

`A_epsilon = A + epsilon D`.

In the eigenbasis define

`E = V^{-1} D V`.

For the selected boundary pair `(2,3)`:

- `Y = E_23 = w_2^T D v_3`;
- `Z = E_32 = w_3^T D v_2`.

Under Frobenius-isotropic Gaussian perturbation directions, `(Y,Z)` is jointly Gaussian before positive radial normalization.

## T4 — Dangerous-sign law

The modal correlation is

`rho_23 = ((w_2^T w_3)(v_3^T v_2)) / (||w_2|| ||w_3|| ||v_2|| ||v_3||)`.

Therefore

`P(E_23 E_32 < 0) = arccos(rho_23) / pi`.

For the projected `2×2` boundary block,

`Disc_epsilon = [g + epsilon(E_22-E_33)]^2 + 4 epsilon^2 E_23 E_32`,

where `g=lambda_2-lambda_3`.

Complexification requires `Disc_epsilon<0`, so `E_23 E_32<0` is necessary and

`P(boundary complexification) <= arccos(rho_23)/pi`.

This law explained the approximately `0.50` versus `0.87` dangerous-sign fractions in the canonical matched-resolvent counterexample family.

## T5 — Exact finite-epsilon law

Define

- `X=E_22-E_33`;
- `Y=E_23`;
- `Z=E_32`;
- coefficient matrices `C_X,C_Y,C_Z`;
- Gram matrix `H=C^T C`.

For `d=n^2`, with `u=vec(D)` uniform on `S^(d-1)`, the three-dimensional projection can be represented as

`q=(X,Y,Z)^T = H^(1/2)(R s)`,

where

- `s` is uniform on `S^2`;
- `R^2 ~ Beta(3/2,(d-3)/2)`;
- `R` and `s` are independent.

For fixed angular direction, write `H^(1/2)s=(a,b,c)`. The discriminant condition becomes the radial quadratic

`F_s(r)=g^2 + 2g epsilon a r + epsilon^2(a^2+4bc)r^2 < 0`, `0<=r<=1`.

Thus the exact population probability reduces to a two-dimensional angular integral over `S^2` of Beta-CDF radial mass over the intervals where `F_s(r)<0`.

### Frozen-data falsification

Against the already frozen E15/E15-R projected-complexification outcomes:

- 40 operators × 7 epsilon values = 280 cells;
- MAE ≈ `0.00325`;
- RMSE ≈ `0.00474`;
- maximum absolute difference ≈ `0.0170`;
- `269/280 = 96.1%` of theoretical probabilities lay inside cellwise exact 95% binomial intervals.

The cellwise coverage is descriptive because E15 reused the same perturbation bank across cells.

### T5 interpretation

T5 gives an exact finite-epsilon population law for the **projected two-dimensional boundary-complexification event** under Frobenius-isotropic fixed-norm perturbation directions.

It does not equal full `r=2` top-by-modulus admissibility failure in dimensions larger than two because off-boundary modes and ordering changes can create additional failures.

## T6 — Fresh operator-family falsification

T6 tested T4/T5 on 36 fresh selected operators from a new 4D family and used independent pair-specific perturbation banks.

### T4 result

Across 36 selected operators:

- MAE between empirical dangerous-sign fraction and `arccos(rho_23)/pi` ≈ `0.00311`;
- maximum absolute discrepancy ≈ `0.00976`;
- maximum standardized discrepancy ≈ `2.14` binomial standard errors.

No evident falsification was observed.

### T5 result

Across `36×7=252` cells:

- MAE ≈ `0.002247`;
- RMSE ≈ `0.003246`;
- maximum absolute error ≈ `0.011883`;
- `249/252 = 98.81%` of theoretical probabilities lay inside exact 99% binomial intervals.

All frozen T5 gates passed.

**Verdict: T5 survives fresh operator-family falsification for the projected 2×2 boundary event.**

## External-mode residual test

T6 also asked whether the difference

`p_full - p_T5`

could be explained by a simple scalar external-modal susceptibility.

For the six pre-matched external-susceptibility pairs, residual-AUC differences were approximately

`[+0.00399,+0.06356,+0.02468,+0.03539,+0.01472,-0.00662]`.

Five of six were positive, but the median was `0.01970`, narrowly below the preregistered `0.020` support threshold; one pair was decisively reversed.

**Frozen verdict: INCONCLUSIVE.**

The aggregate external-amplitude scalar was therefore not promoted as an explanation or predictor.

## Scientific conclusion

T4/T5 identify a robust boundary-local component of admissibility risk. The residual full spectral-cut failure contains additional structured information that is not captured by total off-boundary amplitude alone.

This led to T7, which attempted an analytic second-order correction for external modes.