# E1 — Local EDMD bias–variance analysis

## Scientific question

How does the useful history length trade finite-sample statistical error against nonstationarity bias in a local EDMD estimate?

## Analytic structure

The derived upper bound had leading form approximately

`U(n,t) ≈ A/n + C L_t^2 n^2`,

where the first term represents statistical error and the second represents local-drift bias.

The minimizer of this **derived upper bound** scales as

`n*_UB ~ L^(-2/3)`.

## Numerical sanity check

The numerical checks supported:

- statistical term approximately `n^-1`;
- drift-bias term approximately `n^2`;
- fitted exponent for the upper-bound minimizer approximately `-0.6675`, consistent with `-2/3`.

## Verdict

**CONFIRMED as an upper-bound / numerical sanity result.**

## Important limitation

This is not a theorem for the minimizer of the true expected EDMD estimation risk. It is a result about the minimizer of the particular analytic upper bound used in the study.

This limitation became important later because an asymptotically sensible bias–variance scaling does not automatically yield a practically useful online selector.

## Relation to E2

E2 tested whether statistically valid nested-estimator radii could convert this bias–variance intuition into a useful causal history selector. That attempt was too conservative.

## Provenance status

This record is grounded in the authoritative project experiment ledger. A byte-level E1 archive has not yet been identified in the current Drive migration, so no source/configuration hashes are asserted.