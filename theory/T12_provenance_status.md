# T12 provenance status

## Why this file exists

The T12 theory-to-data sequence contains results with different levels of executable provenance. The repository therefore separates **scientific-history evidence**, **source-reproducible evidence**, and **provenance-invalidated numerical history**.

## T12-A4b — high-N Riesz-chart transport

The structured theory log records a high-N extension in which the Riesz-chart risk interval transported across six fresh non-normal embeddings. The scientific summary retained in the project memory is:

- one of 90 chart-support cells marginally missed the frozen support requirement (`0.99455` versus `0.995`), so the event-support gate is formally design-limited;
- conditional/event-equivalence evidence was numerically very close (`MAE ≈ 7.5e-5`, maximum difference `≈0.00145`);
- the independent nominal-90% risk-interval gate had pooled coverage about `0.902`, with geometry-level coverage approximately `0.894–0.913`.

The scientific interpretation is retained as **theory-log evidence supporting Riesz risk-interval transport in the tested high-N controlled family, with the separate chart-support gate marginally design-limited**.

### Provenance limitation

A later independent recovery audit could not fully recover and authenticate the original executable source/configuration used for the A4b/B1 trajectory-extension sequence, including all exact event/support implementations needed for a byte-faithful rerun.

Therefore A4b must **not** be labeled `SOURCE MIGRATED` or `SOURCE VERIFIED` solely from its numerical summary. Its current repository status is:

**THEORY-LOG / PROVENANCE-LIMITED EVIDENCE — scientific interpretation retained, source-level reproduction not established from the recovered archive.**

This is a reproducibility limitation, not an automatic reclassification of the recorded numerical verdict as a scientific refutation.

## T12-B1 — historical correlated-trajectory extension

The intended experiment extended the local Riesz risk interval from iid transition-pair sampling to one stationary correlated linear VAR trajectory.

The historical log reports a frozen design using:

- two fresh non-normal embeddings;
- local `c={-1,-0.5,0,0.5,1}`;
- trajectory lengths `T={4096,8192}`;
- stationary Gaussian initialization;
- OLS on causal transition pairs;
- oracle and pilot trajectory banks;
- the same Riesz boundary functional and nominal-90% center-uncertainty risk interval used in the iid theory branch.

The historical numerical narrative reported encouraging coverage. However, the later recovery audit could not authenticate enough of the original executable provenance to reproduce the exact event definitions and failure logic independently.

The following authentic run components were not sufficiently recoverable for claim-ready reproduction:

- original transition-covariance implementation details;
- exact full-failure event implementation;
- exact Riesz-chart failure/support implementation;
- failure-category logic;
- complete original run configuration;
- authenticated original executable source.

Authentic-source-dependent unit tests therefore could not be independently rerun.

## B1 claim status

The historical T12-B1 numerical result is consequently:

**PROVENANCE-INVALIDATED / NOT CLAIM-READY.**

It must not be used as reproducible confirmatory evidence in a paper or repository summary.

The frozen narrative specification remains useful as design documentation, but a narrative specification is not a substitute for executable provenance.

## Required reconstruction rule

The old B1 identifier must not simply be rerun and presented as the same experiment.

Any future correlated-trajectory replication must use a new identifier:

`T12-B1R — reconstructed/re-frozen correlated-trajectory Riesz risk interval`

and must freeze **before outcomes**:

- complete executable source;
- configuration;
- exact event and support definitions;
- seed namespaces;
- chart/contour specification;
- artifact manifest;
- SHA256 checksums;
- numerical integrity tests;
- substantive implementation and claim audits.

Only the reconstructed fresh result may become claim-ready.

## Repository policy illustrated by T12

A scientifically plausible or even numerically strong result is not promoted to source-reproducible status when the execution path cannot be independently authenticated. Numerical scientific history is preserved, but provenance ceilings remain explicit.
