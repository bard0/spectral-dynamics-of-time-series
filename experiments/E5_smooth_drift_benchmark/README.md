# E5 — Smooth-drift benchmark

## Scientific role

E5 tested adaptive history selection under smooth nonstationarity, a regime that is harder for abrupt change-point logic and therefore more relevant to a continuously evolving local Koopman/EDMD model.

## Result

Some adaptive methods improved over the largest fixed history window in parts of the benchmark, but the advantage was not stable across scenarios.

The project archive records representative behavior where Lepski-like or spectral adaptive rules could improve over the largest fixed window under smooth drift, while other settings showed no robust advantage.

## Verdict

**INCONCLUSIVE for a general adaptive-selector claim.**

## Scientific consequence

E5 showed that smooth drift can create a genuine bias–variance trade-off in which using all available history is suboptimal. However, it did not identify a causal spectral selector that was reliably best across systems.

This distinction is important: evidence that an adaptive horizon could be useful does not imply that the tested diagnostic correctly identifies that horizon.

## Relation to later work

The inconsistency in E5 contributed to the later decision to stop optimizing a generic history selector directly and instead ask whether observable spectral instability can first be calibrated against actual estimation error.

## Provenance status

This record is grounded in the authoritative project experiment ledger. The original detailed E5 numerical archive has not yet been identified during the current migration, so no additional metrics are promoted here beyond what the project history supports.