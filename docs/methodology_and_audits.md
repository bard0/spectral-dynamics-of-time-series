# Methodology, Falsification, and Audit Rules

This project is organized around **falsification-first experimental design**. The repository preserves design failures, negative results, post-hoc analyses, and implementation corrections because they materially determine which claims are defensible.

## 1. Causality rule

Any method described as causal or online must use only information available at or before the current time.

Oracle quantities may be used for:

- evaluation;
- synthetic ground-truth comparisons;
- mechanism audits explicitly labeled as oracle/post-hoc.

Oracle quantities must not enter:

- online selection;
- causal predictors;
- thresholds fitted on held-out outcomes;
- model inputs for data-level claims.

## 2. Freeze before outcomes

When an experiment is confirmatory or a fresh falsification, the following should be frozen before target outcomes are generated or inspected:

- data-generating family;
- parameter grid;
- operator selection rules;
- train/development/test split;
- perturbation or trajectory seed namespace;
- primary metric;
- support/evaluability rules;
- success, failure, and inconclusive thresholds;
- candidate diagnostic being tested.

A failed frozen candidate is not replaced post hoc by the best-performing alternative from the same outcomes.

## 3. Design failure is not scientific refutation

A design can fail before it meaningfully tests the hypothesis.

Examples in this project include:

- insufficient overlap between estimation-instability and drift regimes in the first EXP-009 Gate-1 pilot;
- insufficient Riesz-chart support in the first T12-A4 design;
- an overly broad local-to-boundary grid in T12-A2c that violated the predeclared target-nondegeneracy condition.

Such experiments are recorded as **DESIGN-LIMITED / INCONCLUSIVE**, not as evidence against the scientific mechanism.

## 4. Post-hoc analysis discipline

Post-hoc analyses are allowed for:

- diagnosing why a frozen experiment failed;
- identifying candidate mechanisms;
- auditing bugs or metric definitions;
- deciding what should be frozen in a genuinely fresh next experiment.

They are labeled **EXPLORATORY** and cannot become confirmatory evidence until retested on fresh data or a fresh operator family.

Examples:

- E13a latent-risk analysis after the design-limited E13 target;
- E14a-R boundary-mechanism analysis;
- E15-R analysis of matched-resolvent counterexamples.

## 5. Bug corrections remain visible

Implementation errors are not silently overwritten when they affect interpretation.

Important examples:

### E12 separation label

A quantity reported as a separation diagnostic in one stage was in fact a raw eigenvalue gap rather than the intended Schur/Stewart–Sun separation. Claims relying on that stronger interpretation were withdrawn.

### E14a-R informative-epsilon flag

A bug marked all epsilon cells as non-informative, invalidating the automated candidate-nomination verdict. The scientific report was corrected and the candidate was only promoted to a fresh falsification after the audit.

### E15 Panel-A orientation

The frozen pair construction stored one panel in low/high order while a later reporting layer treated it as high/low. This flipped the sign of already-computed pair effects. Correcting orientation changed Panel A from an apparent reversal to `8/8` support for the directional resolvent prediction.

The overall E15 verdict did **not** change because the independent Panel-B sufficiency test still failed decisively.

### E15-R structural replication count

Symmetry-related pairs were initially overcounted as distinct structural replications. The corrected interpretation treats the central matched-resolvent counterexample conservatively as one unordered structural comparison up to sign/symmetry.

## 6. Object support before conditional error

A spectral-error analysis must distinguish:

1. whether the intended spectral object is defined/admissible;
2. conditional error among surviving objects.

Dropping undefined objects and analyzing only survivors can hide the main failure mechanism. E10–E11 showed that non-normality can strongly reduce object support without increasing conditional survivor Grassmann error.

## 7. Invariant subspaces over raw eigenvectors

Raw eigenvectors are sensitive to:

- sign;
- ordering;
- mode swaps;
- rotations inside nearly degenerate clusters.

Whenever the scientific target is a slow invariant object, comparisons should use:

- invariant subspaces;
- spectral clusters;
- Schur subspaces;
- projector-based quantities;

rather than individual eigenvector identity alone.

## 8. Identifiability and spectral separation

Small spectral separation changes the meaning of subspace error. Gap, Schur separation, non-normal conditioning, and support must be tracked explicitly.

A large Grassmann motion near an ill-conditioned spectral boundary cannot automatically be interpreted as physical drift.

## 9. Observation noise is not process drift

Changes in measurement noise do not necessarily change the latent Koopman operator. In some cases more historical data may become more useful, not less.

Observation-noise controls and process-noise/dynamical-drift controls are therefore treated separately.

## 10. Reliability is distinct from source attribution

The EXP-009 Gate-1 result is a standing methodological constraint:

- cross-scale disagreement can correlate with actual estimation error;
- the same causal observable may fail to identify whether that error arose from finite-sample instability or true smooth drift.

A method may therefore be useful as a reliability diagnostic without being a valid drift-source classifier.

## 11. Point risk versus uncertainty interval near a boundary

The T12 data bridge showed that estimating the sampling covariance law is not the main difficulty near a spectral-admissibility boundary. Conditioning the risk calculation on one noisy estimated center can remain unstable even as the matrix estimator itself converges.

For local `O(N^{-1/2})` approaches to the pair-cut boundary, the point-centered risk estimate can remain nonconcentrated. A risk interval carrying center uncertainty performed substantially better in the controlled T12-A3 experiment.

This is consistent with classical nonregular inference near parameter-space boundaries. The project does not claim that the general nonregularity principle is new.

## 12. Provenance rule

A historical numerical result is not claim-ready unless the repository can identify enough information to reconstruct what was executed, including where applicable:

- executable source;
- configuration;
- exact event definitions;
- seed namespace;
- frozen design or split;
- artifact manifest/checksums;
- primary outputs.

A historical correlated-trajectory result in the theory-to-data branch was later marked **provenance-invalidated for claim purposes** because its original executable/configuration/event definitions could not be authenticated from the archived artifacts. The numerical story is preserved as history but is not used as confirmatory evidence.

## 13. Reproducibility expectations for migrated experiment code

When code is added to this repository, the preferred package should contain:

- a runnable scientific program;
- a machine-readable configuration;
- deterministic or explicitly recorded random seeds;
- checkpoints for long runs where appropriate;
- explicit logs;
- integrity checks;
- scientific report and primary tables;
- artifact manifest/checksums;
- resume logic whose behavior is actually tested when claimed.

## 14. Claim hierarchy

Every result should be phrased at the narrowest level supported by the evidence:

- **operator-level mechanism** is not a data-level estimator;
- **stationary linear EDMD/OLS** is not nonlinear Koopman validity;
- **iid transitions** are not one correlated trajectory;
- **stationary trajectories** are not nonstationary causal online inference;
- **projected boundary complexification** is not full top-by-modulus admissibility;
- **one controlled operator family** is not a universal theorem.

## 15. Current research rule

Before a new experiment, ask:

> What is the cheapest decisive test that could show the proposed claim is wrong?

A robust negative result is preferable to a post-hoc rescued positive claim.