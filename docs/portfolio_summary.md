# Portfolio Summary

## Causal Spectral Reliability and Admissibility in Local Koopman/EDMD Models

**Status:** completed exploratory research case study, portfolio release — September 2026.

## Research question

Local Koopman/EDMD models of nonstationary time series require choosing how much past data to use and deciding whether the resulting slow spectral structure is trustworthy.

The project began with a practical question:

> How much historical data remains dynamically relevant at the current time?

It then evolved into a more fundamental one:

> Can the reliability and even the existence of a selected slow spectral object be assessed from finite data, especially near non-normal spectral boundaries?

The final project therefore separates three tasks that initially looked similar:

1. **reliability** — how inaccurate or fragile is the estimated slow spectral object?
2. **admissibility** — does the intended spectral object remain well defined under finite perturbations?
3. **source attribution** — can observed spectral motion be identified as estimation noise rather than genuine dynamical change?

The experiments show that the first two can be tractable in controlled regimes even when the third is not identifiable from the tested causal diagnostics.

---

## Research trajectory

### 1. Local estimation under nonstationarity

For a local EDMD estimator based on a history window of length \(n\), the initial analysis produced the leading upper-bound structure

\[
U(n,t) \approx \frac{A}{n} + C L_t^2 n^2.
\]

The first term is statistical and decreases with the amount of data. The second accumulates bias from a time-varying operator.

The minimizer of this upper bound scales as

\[
n^*_{UB}(t) = O(L_t^{-2/3}).
\]

Controlled numerical tests recovered the expected \(n^{-1}\) and \(n^2\) scalings and an empirical exponent near \(-0.6675\).

This result established the bias–nonstationarity trade-off, but not a causal estimator of the unknown local drift rate.

### 2. A mathematically valid selector was practically too conservative

A Lepski-style nested-window selector was implemented using finite-sample confidence radii.

In the tested regime it often declared many windows mutually compatible and selected the largest history. This exposed a useful gap:

> a correct finite-sample upper bound need not be sharp enough to drive an informative online decision rule.

The negative result was retained rather than tuned away.

### 3. Invariant subspaces replaced individual eigenvectors

The project then moved from raw operator error and individual modes to slow invariant subspaces.

A mode-swap sanity test showed Grassmann distance on the order of \(10^{-14}\) while individual-vector overlap could fall to about \(0.13\). This motivated the use of invariant clusters/subspaces throughout the later work.

### 4. Adaptive-window superiority was not established

Broad causal benchmarks compared fixed histories, prediction-based rules, forgetting, Lepski-like selectors, gap-based criteria, Grassmann criteria, and related baselines.

No adaptive rule showed robust general superiority across all tested systems.

This falsified the broad project framing as a new generic adaptive-window method.

### 5. Cross-scale disagreement became a reliability signal, not a drift estimator

The nested quantity

\[
S_{scale}(H,t)=d_G(E_H(t),E_{2H}(t))
\]

was tested against known true dynamical drift.

It was not a reliable direct drift proxy.

However, in stationary regular-gap families it did contain information about actual slow-subspace estimation error. In E8, Spearman correlation was about \(0.51\) and AUROC about \(0.79\). In the fixed-outer-gap cluster experiment E9b, the hardest primary condition reached AUROC about \(0.83\) with support near one.

This led to a key distinction:

> cross-scale inconsistency can predict spectral reliability without identifying the physical source of the inconsistency.

### 6. Non-normality changed the type of failure

E10–E11 showed that increasing non-normality did not merely increase conditional subspace error. Instead, it could reduce the probability that the intended real/conjugation-closed spectral cluster existed at all.

The scientific target therefore shifted from conditional estimation error to **spectral admissibility**.

### 7. Simple global sensitivity scalars were insufficient

A conditioning-normalized perturbation score ranked some failure risks but failed universal calibration.

Matched-conditioning counterexamples then showed that the location of non-normal coupling relative to the selected spectral boundary mattered.

A frozen boundary-resolvent scalar was informative in nuisance-matched comparisons but was also insufficient as a standalone transportable risk variable.

The emerging lesson was that **boundary-local geometry** matters.

### 8. A projected boundary law survived fresh falsification

For a selected \(2|3\) boundary, projected complexification reduces to the sign of

\[
[g+\varepsilon(E_{22}-E_{33})]^2
+4\varepsilon^2 E_{23}E_{32}.
\]

Under controlled Frobenius-isotropic perturbations, the corresponding finite-\(\varepsilon\) failure probability was reduced to a low-dimensional law.

Fresh validation over 252 cells gave approximately:

- MAE: \(0.00225\);
- RMSE: \(0.00325\);
- maximum absolute error: \(0.0119\);
- \(98.8\%\) of cells inside exact 99% binomial intervals.

This is one of the strongest controlled positive results in the repository.

### 9. Finite-data calibration exposed spectral-center nonregularity

A one-sample OLS/linear-EDMD sampling law calibrated full spectral-failure probability accurately when the true spectral center was supplied.

Once the center also had to be estimated from data, performance degraded strongly near the admissibility boundary.

A local-to-boundary sequence showed that the matrix estimator itself could converge while a point-centered risk functional remained nonconcentrated.

Replacing unstable point risk by a center-uncertainty interval produced nominal-90% pooled coverage about \(0.936\) in the controlled local matrix family.

### 10. Source attribution remained non-identifiable

In a frozen matched-overlap benchmark with 4,000 fresh trajectories, scale, temporal, operator-change, gap, and joint diagnostics remained near chance for distinguishing finite-sample instability from smooth true drift.

At the same time, cross-scale instability still correlated with actual slow-subspace estimation error.

The final conceptual separation is therefore:

\[
\text{reliability prediction} \neq \text{source attribution}.
\]

---

## Main outcomes

| Outcome | Evidence | Status |
|---|---|---|
| Bias–nonstationarity trade-off | \(A/n + C L_t^2n^2\), numerical \(L^{-2/3}\) scaling | supported for derived upper bound |
| Raw eigenvector matching is fragile | mode-swap sanity test | supported |
| Generic causal adaptive-window superiority | broad benchmarks | **not established** |
| Nested spectral disagreement as true drift proxy | controlled nonstationary test | **refuted** |
| Cross-scale signal as reliability predictor | E8 / E9b | supported in controlled regular-gap regimes |
| Non-normality can destroy spectral-object identity | E10 / E11 | supported |
| Global conditioning as universal risk variable | E12 / E14a | **insufficient** |
| One fixed boundary-resolvent scalar | E15 | **insufficient standalone** |
| Projected boundary-complexification probability | T5 / T6 | strongly supported in controlled perturbation family |
| Data-level point risk near boundary | T12 local-to-boundary sequence | nonregular / unstable |
| Center-uncertainty risk intervals | T12-A3 | supported in controlled local family |
| Strong causal source decomposition | EXP-009 | **not identifiable in tested family** |

---

## What the project does not claim

The repository does not claim:

- a new generic adaptive-window method;
- a universal Koopman/EDMD uncertainty estimator;
- universal identification of true drift versus estimation noise;
- a universal non-normal spectral-risk law;
- novelty of classical Grassmann, resolvent, pseudospectral, Riccati/Sylvester, or nonregular-inference machinery;
- general nonlinear validity beyond the controlled systems that were actually tested;
- source-level reproducibility for results explicitly marked provenance-limited or provenance-invalidated.

These restrictions are part of the scientific result, not omitted caveats.

---

## Reproducibility and research practice

The project preserves positive, negative, inconclusive, design-limited, and provenance-limited results.

The repository includes:

- experiment and theory ledgers;
- separate Branch-A and Branch-B scientific narratives;
- reproducibility/provenance status for each major experiment;
- migrated source for a subset of later experiments;
- hashes or historical records when byte-faithful migration was not possible;
- explicit corrections when an implementation or reporting issue changed interpretation.

Large trajectory-level outputs and checkpoint archives are intentionally kept outside GitHub.

See [reproducibility_status.md](reproducibility_status.md).

---

## Skills demonstrated

This project exercises a complete research workflow rather than a single modeling technique:

- nonstationary time-series modeling;
- Koopman/EDMD operator estimation;
- spectral perturbation theory;
- invariant-subspace and Grassmann geometry;
- non-normal matrix analysis;
- finite-sample statistical reasoning;
- simulation design and falsification;
- calibration and uncertainty quantification;
- causal/online evaluation without future leakage;
- negative-result interpretation;
- reproducibility and provenance auditing;
- literature-based novelty narrowing.

---

## Recommended entry points

1. [../README.md](../README.md) — repository overview and selected results.
2. [research_story.md](research_story.md) — chronological falsification-driven development.
3. [current_state.md](current_state.md) — detailed scientific state and claim ceiling.
4. [novelty_positioning.md](novelty_positioning.md) — prior-art boundaries and defensible positioning.
5. [reproducibility_status.md](reproducibility_status.md) — source/provenance map.
6. [experiment_ledger.md](experiment_ledger.md) — experiment-by-experiment record.
7. [../theory/README.md](../theory/README.md) — theory branch index.

---

## Portfolio conclusion

The project is complete as an exploratory research case study because it contains the full scientific loop:

\[
\text{problem formulation}
\rightarrow
\text{mathematical model}
\rightarrow
\text{controlled experiment}
\rightarrow
\text{falsification}
\rightarrow
\text{reframing}
\rightarrow
\text{mechanistic theory}
\rightarrow
\text{finite-data limitations}.
\]

The strongest result is not a single universally successful algorithm. The value of the project is the progressively sharper characterization of **when slow spectral information is reliable, when the spectral object itself ceases to be admissible, and what finite data can and cannot identify**.

Further experiments are scientifically possible, but they are optional continuation rather than necessary work for the portfolio version.
