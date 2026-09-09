# EXP-009 Gate 1 — Causal Source-Identifiability Test

## Question

Can observable causal spectral diagnostics distinguish

1. **finite-sample estimation instability**, from
2. **smooth true dynamical drift**,

when the two regimes are deliberately matched in total observable spectral-instability magnitude?

This experiment belongs to the causal reliability branch. It does not test adaptive-history performance directly.

## Why matching was necessary

Without matching, a classifier could separate regimes merely because one produces larger overall spectral motion.

The total observable magnitude used for matching was

\[
M_{ST}=\sqrt{S_{scale}^2+S_{time}^2}.
\]

The scientific target was whether the **structure** of the diagnostics contains source information after overall magnitude is controlled.

---

# Pilot v1 — stopped before scientific evaluation

The first frozen pilot had high spectral support but failed the overlap design gate. At every common history horizon, drift conditions had systematically larger `M_ST` than estimation-instability conditions.

Best same-history median ratio was about `1.59`, above the frozen maximum `1.40`, and no qualifying matched pairs existed.

No confirmatory trajectories, classifiers, or bootstrap inference were generated.

**Status:** DESIGN-LIMITED INCONCLUSIVE.

The pilot was preserved rather than retroactively retuned.

---

# Pilot v2 — overlap calibration

A new pilot-only design extension used fresh seeds and adjusted only the data-generating parameter grids.

Frozen history horizons:

```text
H = [96, 128, 160, 192]
```

Stationary estimation-instability controls varied a finite-sample instability parameter; smooth-drift controls varied rotation rate while preserving the same population spectrum and gap.

The deterministic matching rule used only same-history pilot median `M_ST` and support.

Result:

- overall support approximately `0.9917`;
- first successful matching level produced 10 disjoint condition pairs;
- matched `M_ST` median ratios approximately `1.003–1.286`;
- all four history horizons represented;
- pilot-only raw `M_ST` regime AUROC approximately `0.519`.

The confirmatory design and a deterministic five-pair development / five-pair held-out split were frozen before evaluation outcomes.

Frozen design SHA256:

```text
9e55fe9a3f91932b9c1cd0918beaafd8b65f65f8598743c134da8441f0852335
```

Frozen split SHA256:

```text
e9c0d3cb424cf4d89db5c7f8ea332e858f2d988e1e6c5cb9030e1fb2c2d10f3d
```

Development pairs: `[4, 5, 6, 7, 8]`  
Held-out pairs: `[1, 2, 3, 9, 10]`

---

# Frozen confirmatory test

Fresh data:

- raw rows: `4000`;
- supported rows: `3982`;
- support in estimation regime: `0.9955`;
- support in drift regime: `0.9955`.

The held-out amplitude-overlap gate passed:

```text
median M_ST estimation = 0.127270
median M_ST drift      = 0.119206
median ratio           = 1.06765
raw amplitude AUROC    = 0.46578
AUC information        = 0.53422
```

Thus the confirmatory source-classification result was not explained by trivial magnitude separation.

## Held-out discrimination

| Model | Features | AUROC | PR-AUC |
|---|---|---:|---:|
| SCALE | cross-scale instability | 0.48398 | 0.47825 |
| TIME | temporal subspace instability | 0.46707 | 0.46815 |
| OPERATOR_TIME | temporal operator difference | 0.51332 | 0.52414 |
| GAP | spectral gap | 0.48160 | 0.48946 |
| JOINT_ST | scale + time | 0.46733 | 0.46829 |
| JOINT_FULL | scale + time + operator + gap | 0.46989 | 0.46620 |

Joint scale-time added value relative to the better individual scale/time diagnostic:

```text
delta AUROC = -0.01665
hierarchical bootstrap 95% CI = [-0.06981, 0.00231]
pairwise consistency = 2 / 5 held-out pairs
```

The full joint secondary gate also failed.

## Frozen verdict

> **EXP-009 GATE 1 — STRONG DECOMPOSITION NOT IDENTIFIABLE IN THE TESTED FAMILY.**

After controlling total observable instability magnitude, the frozen cross-scale, temporal, operator-motion, and gap diagnostics did not provide a stable transportable mapping from observed spectral instability to its source.

This is a strong negative for the tested simple source-decomposition hypothesis.

It does not prove impossibility under every possible assumption or diagnostic.

## Important positive residue

On the same held-out supported rows, the diagnostics still contained information about **actual spectral estimation error**:

```text
Spearman(S_scale, true subspace error) ≈  0.5083
Spearman(S_time,  true subspace error) ≈  0.2863
Spearman(D_K,     true subspace error) ≈  0.1753
Spearman(gap,     true subspace error) ≈ -0.2370
```

The central lesson is therefore:

> Reliability prediction can survive even when source attribution fails.

## Consequence for the project

Do not proceed as though this experiment validated a drift classifier.

The causal branch was reframed toward:

- calibrated spectral error/risk prediction;
- explicit limits of source identifiability;
- spectral-object admissibility checks;
- adaptive history only as a downstream application.

## Claim ceiling

This experiment supports only the stated result in the frozen matched-overlap controlled family. It does not prove general non-identifiability for every nonstationary process and does not validate or refute an adaptive-history algorithm.