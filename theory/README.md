# Spectral-Admissibility Theory Program

This directory records the parallel theory branch that grew out of the E10–E15 mechanism studies.

Its scientific goal is to describe when a **preselected spectral cut or slow spectral object** remains admissible under finite perturbations of an estimated Koopman/EDMD operator.

## Boundary condition

This theory program does **not** rescue E15. The frozen E15 result remains:

> a fixed single-point boundary resolvent norm is refuted as a standalone transportable admissibility-risk scalar.

The theory branch instead asks what richer boundary geometry is required.

## Path into the theory branch

```text
E10: reliability calibration fails to transport under non-normality
  ↓
E11: non-normality increases loss of spectral-object identity
  ↓
E12: global conditioning ranks risk but does not give a calibrated law
  ↓
E14a: matched global conditioning can have very different admissibility risk
  ↓
E15: one fixed boundary-resolvent scalar is still insufficient
  ↓
T4–T12: boundary-local probability laws, certified regimes, and theory-to-data transport
```

## Main theory sequence

| Stage | Question | Status |
|---|---|---|
| T4 | dangerous-sign probability for the boundary modal pair | analytic working result |
| T5 | exact finite-epsilon projected 2×2 boundary-complexification probability | supported on frozen + fresh families |
| T6 | fresh transport of T4/T5; external-amplitude residual explanation | T5 supported; simple external-amplitude explanation inconclusive |
| T7 | second-order external-mode correction as a finite-epsilon full-failure predictor | strongly refuted globally |
| T8 | empirical perturbative validity regime for T7 via `eta_mix` | not supported under frozen thresholds |
| T9 | classical Riccati/Sylvester certified regime | supported in certified subset |
| T10 | epsilon-separable pre-certificate probability | useful; independence factorization refuted |
| T11 | exact shared-radial joint certificate/boundary law and safe core | supported in fresh family |
| T12-A1 | finite-sample OLS sampling-law → spectral-risk bridge with oracle spectral center | supported |
| T12-A2 | fully data-centered point risk | inconclusive |
| T12-A2b | repair by increasing sample size alone | refuted |
| T12-A2c | first local-to-boundary test | design-limited |
| T12-A2c2 | local nonregularity under `N^-1/2` approach to pair-cut boundary | supported |
| T12-A3 | center-uncertainty risk interval | supported |
| T12-A4 | coordinate-free Riesz-chart transport | design-limited due to chart support |
| T12-A4b | high-N Riesz transport | scientific/theory-log result retained; Gate A marginally design-limited; source provenance incomplete |
| T12-B1 | correlated-trajectory extension | provenance-invalidated / not claim-ready |
| T12-B1R | reconstructed correlated-trajectory replication | required future re-frozen experiment; not yet run |

The A4b/B1 distinction is important: A4b retains its structured-theory-log scientific interpretation but is **not source-reproducible from the recovered archive**, whereas B1 loses claim-ready status entirely. See `T12_provenance_status.md`.

## Current theoretical picture

The accumulated evidence supports a layered view:

1. A selected spectral cut can fail through a boundary-local complexification mechanism.
2. The probability of the projected 2×2 boundary event can be derived exactly under Frobenius-isotropic fixed-norm perturbations.
3. Low-order perturbation expansions are only useful in a certified perturbative regime; they should not be treated as global finite-epsilon predictors.
4. Classical Riccati/Sylvester separation certificates can isolate a subset where the second-order model is much more accurate.
5. Certificate probability and boundary-failure probability are strongly dependent; multiplying marginal probabilities is invalid.
6. Near a regular pair-cut boundary, point-centered spectral-risk estimation is locally nonregular even while the operator estimator itself is consistent.
7. Carrying uncertainty in the spectral center yields calibrated **risk intervals** in the tested local matrix families.
8. A Riesz-projector boundary functional provides a coordinate-free formulation for an isolated two-eigenvalue cluster.

## Claim ceiling

This theory program does not claim novelty for:

- random matrix perturbations;
- pseudospectra;
- Riccati/Sylvester invariant-subspace bounds;
- spherical/Beta decompositions;
- local asymptotic minimax theory;
- bootstrap nonregularity at parameter-space boundaries;
- Riesz projectors themselves.

Potential project-specific content is narrower: the assembly of these established ingredients around **probabilistic admissibility of a preselected slow spectral cut** and its connection to finite-data Koopman/EDMD reliability.

## Files

- `T4_T6_boundary_probability.md` — boundary modal sign law and exact projected-complexification probability.
- `T7_T11_certified_geometry.md` — global failure of the second-order correction, certified perturbative recovery, pre-certificate and shared-radial joint geometry.
- `T12_theory_to_data.md` — finite-data OLS bridge, local nonregularity, risk intervals and Riesz-chart transport.
- `T12_provenance_status.md` — explicit record of the A4b/B1 provenance correction and the required B1R reconstruction rule.
