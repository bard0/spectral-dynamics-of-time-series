# Portfolio summary

## Causal spectral reliability and admissibility in local Koopman/EDMD models

I started this project with a fairly ordinary practical problem: a local model of a nonstationary time series needs a history length. Too little data gives a noisy operator estimate; too much data mixes dynamics from different times.

The first calculation made that trade-off explicit. In a regular regime, the leading error bound has the form

\[
U(n,t)\approx \frac{A}{n}+CL_t^2n^2,
\]

which gives

\[
n^*_{UB}(t)=O(L_t^{-2/3})
\]

for the minimizer of the bound. Numerical tests recovered both component scalings and an empirical exponent close to \(-2/3\).

That result did not solve the main practical problem, because the local drift rate is not known online. I therefore tried a Lepski-style causal selector based on nested estimates and finite-sample radii. The bounds behaved correctly, but the selector was too conservative: many windows looked compatible and it often kept the longest history.

That failure changed the direction of the project.

Instead of asking for a generic "best window", I switched to the slow spectral structure itself. For metastable or multiscale systems, this is often more relevant than the full operator matrix. I also stopped comparing individual eigenvectors whenever an invariant subspace was the natural object. A mode-swap sanity test made the reason concrete: the relevant Grassmann distance stayed essentially zero while individual-vector overlap changed strongly.

The next hypothesis was that disagreement between nested slow subspaces,

\[
d_G(E_H,E_{2H}),
\]

might measure how much the true dynamics had changed. Controlled experiments did not support that interpretation. The quantity mixed several effects and correlated poorly with known true drift.

It was still useful, just for a different task.

In stationary regular-gap experiments, cross-scale disagreement carried information about actual slow-subspace estimation error. E8 gave Spearman correlation around 0.51 and AUROC around 0.79. E9b moved to a two-dimensional invariant cluster with a fixed outer gap; in the hardest primary condition, AUROC was about 0.83 and support was close to one.

The next surprise came from non-normal systems. The main problem was not always that the estimated subspace became less accurate. Sometimes the spectral object I was trying to estimate stopped being well defined under the perturbation: a real/conjugation-closed cluster could break across the selected spectral boundary.

From that point on, the project was no longer mainly about window selection. It became a study of **spectral admissibility** and finite-data reliability.

I tested several simple risk summaries. Global eigenvector conditioning helped rank difficult cases but was not sufficient. Matched-conditioning counterexamples showed that moving the non-normal coupling relative to the selected boundary could change failure probability substantially. A fixed boundary-resolvent norm also had the right direction in carefully matched comparisons, but matched resolvent values could still correspond to very different risks.

This suggested that the geometry near the selected boundary mattered more than one global scalar.

For a controlled 2|3 boundary, the projected complexification event reduces to

\[
[g+\varepsilon(E_{22}-E_{33})]^2
+4\varepsilon^2E_{23}E_{32}<0.
\]

Under Frobenius-isotropic perturbations, the resulting probability can be reduced to a low-dimensional angular/radial calculation. In a fresh test over 252 cells, the theoretical probability agreed closely with simulation: MAE was about 0.00225, RMSE about 0.00325, and 98.8% of cells were inside exact 99% binomial intervals.

The theory-to-data step was harder. A pilot OLS sampling law gave accurate failure-risk calibration when the true spectral center was supplied. Once the center itself had to be estimated from finite data, the point-risk estimate became unstable near the admissibility boundary. A local-to-boundary sequence showed a nonregular situation: the matrix estimate contracted with sample size, but the induced risk functional did not concentrate in the same way.

Replacing a single point-risk number with a center-uncertainty interval worked better. In the controlled local family, nominal 90% pooled coverage was about 0.936.

The last major question was whether causal observables could distinguish two sources of spectral motion: finite-sample estimation instability and smooth true drift. In a frozen matched-overlap benchmark with 4,000 new trajectories, the tested scale, temporal, operator-change, gap, and joint diagnostics all stayed near chance for this classification problem.

That negative result is important because it separates two questions that are easy to conflate:

\[
\text{How unreliable is the estimate?}
\]

and

\[
\text{Why did the estimate move?}
\]

The first can be informative even when the second is not identifiable from the same data.

## Results I would stand behind

The initial bias–nonstationarity calculation and its numerical scaling checks are solid for the derived upper bound. Invariant-subspace comparisons are clearly preferable to mode-wise matching in the tested swap scenario. Cross-scale disagreement is useful as a reliability signal in controlled regular-gap families, but not as a general drift detector. Non-normality can create an object-existence problem rather than only a larger conditional error. The projected boundary-complexification law works very well in the controlled perturbation family. Near the spectral boundary, uncertainty in the estimated center matters enough that interval-valued risk is more stable than a naive plug-in point estimate.

I would **not** present the work as a new general adaptive-window algorithm or as a universal Koopman uncertainty method.

## Negative results that stayed in the project

Several attractive ideas did not survive:

- the first Lepski-style selector was too conservative;
- no adaptive-history rule dominated robustly across the broad benchmark suite;
- nested subspace disagreement was not a direct measure of true drift;
- global conditioning was not a sufficient risk variable;
- a single boundary-resolvent value was not sufficient either;
- a second-order predictor failed when used globally outside a certified regime;
- causal source attribution failed in the matched-overlap benchmark.

Keeping these results made the final question much narrower, but also much clearer.

## Reproducibility

The repository distinguishes between results with migrated source, results whose source hash was verified externally, historical records, and provenance-limited results. I did not try to make the archive look cleaner by pretending that every old run was fully recoverable.

The later workflow also became stricter: frozen designs, explicit seeds, manifests, hashes, checkpoint rules, and separate correctness/statistical/claim audits.

See [reproducibility_status.md](reproducibility_status.md) for the experiment-by-experiment status.

## Where to look

Start with [research_story.md](research_story.md) for the chronological development of the project. [current_state.md](current_state.md) contains the detailed scientific position and limitations. [experiment_ledger.md](experiment_ledger.md) is the experiment record, and [../theory/README.md](../theory/README.md) indexes the theory branch.

The project is complete enough for a portfolio in its present form. The next scientifically useful step would be a provenance-clean stationary correlated-trajectory replication, followed — only if that works — by another attempt at a reliability-aware adaptive history rule.
