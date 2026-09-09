# T12 trajectory-extension provenance status

## Why this file exists

The theory log contains a historical correlated-trajectory experiment labeled `T12-B1` with a detailed frozen design and a numerical result. A later independent recovery audit found that the original executable provenance was incomplete.

The repository therefore separates **historical narrative evidence** from **claim-ready reproducible evidence**.

## Historical T12-B1 design

The intended experiment extended the local Riesz risk interval from iid transition-pair sampling to a stationary correlated linear VAR trajectory.

The frozen design used:

- two fresh non-normal embeddings;
- local `c={-1,-0.5,0,0.5,1}`;
- trajectory lengths `T={4096,8192}`;
- stationary Gaussian initialization;
- OLS on all causal transition pairs;
- 1200 oracle trajectories per cell;
- 200 pilot trajectories per cell;
- the same Riesz boundary functional and nominal-90% center-uncertainty risk interval used in the iid theory branch.

The historical log reports:

- fixed-contour Gate 1 design-limited at minimum support `0.9583` for T=4096;
- descriptive event mismatch MAE `0.00675`, maximum `0.025`, all 20/20 cells within `0.03`;
- risk-interval pooled coverage `0.91625`;
- coverage by geometry `0.9330` and `0.8995`;
- coverage by T `0.9090` at T=4096 and `0.9235` at T=8192.

If provenance had remained valid, the frozen narrative verdict would have been support for the stationary correlated-trajectory risk interval.

## Provenance correction

A subsequent independent recovery audit found that the following authentic run components could not be recovered from the archived executable provenance:

- original `M(delta)` implementation;
- exact FULL_FAIL implementation;
- exact PHI_FAIL implementation;
- Riesz-support implementation;
- failure-category implementation;
- original run configuration;
- authenticated original executable source.

Authentic-source-dependent unit tests therefore could not be independently rerun.

## Claim status

The historical T12-B1 numerical result is consequently:

**PROVENANCE-INVALIDATED / NOT CLAIM-READY.**

It must not be used as reproducible confirmatory evidence in a paper or repository summary.

The detailed frozen specification remains useful as design documentation, but a narrative specification is not a substitute for executable provenance.

## Required reconstruction rule

The old identifier must not simply be rerun and presented as the same experiment.

Any future correlated-trajectory replication must use a new identifier, for example:

`T12-B1R — reconstructed/re-frozen correlated-trajectory Riesz risk interval`

and must freeze **before outcomes**:

- full executable source;
- configuration;
- exact event definitions;
- seed namespaces;
- artifact manifest;
- SHA256 checksums;
- numerical integrity tests.

Only the reconstructed fresh result may become claim-ready.

## Repository policy illustrated by B1

This project preserves provenance failures rather than deleting them. A scientifically plausible numerical result can still lose claim status when the execution path cannot be independently authenticated.