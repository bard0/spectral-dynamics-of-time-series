# Experiment Archive Index

This directory contains scientific packages migrated from the project archive.

The documentation in `docs/experiment_ledger.md` is the authoritative scientific history; this directory is the implementation/artifact layer.

## Migration policy

An experiment package is migrated only after checking:

1. the package belongs to the time-series / Koopman / EDMD project;
2. source and configuration correspond to the scientific result described in the ledger;
3. internal workflow notes are removed when they are not part of the scientific method;
4. known implementation corrections are documented rather than silently rewriting the historical result;
5. provenance-invalidated historical runs are not presented as reproducible confirmatory evidence.

### Large-file policy

GitHub is **not** used as a blind mirror of the full numerical archive.

Large raw artifacts — checkpoint banks, multi-megabyte CSV tables, compressed mechanism rows, simulation dumps, plot collections, and archived ZIP files — remain in the external project archive when duplicating them would make the source repository unwieldy.

GitHub keeps the compact scientific/reproducibility layer whenever possible:

- experiment README;
- frozen configuration;
- executable source when provenance-valid and transferable without truncation;
- corrected reports/audit notes;
- compact primary tables;
- provenance manifest and SHA256 values.

## Migration status

### Core falsification / current story

| Experiment | Scientific role | Status |
|---|---|---|
| E15 | boundary-resolvent sufficiency falsification | migrated |
| EXP-009 Gate 1 | source-attribution identifiability | migrated |

### Spectral-admissibility mechanism chain

| Experiment | Scientific role | Status |
|---|---|---|
| E14a | matched-conditioning geometry falsification | migrated |
| E14a-R | boundary-specific mechanism audit with corrected screen | migrated |
| E13 | independent-realization admissibility prediction | migrated + source |
| E13a | latent condition-level risk reanalysis | migrated + recovery source + audit |
| E12 | conditioning-scaling calibration limits | migrated + source |
| E11 | matched non-normal perturbation mechanism | migrated + source |
| E10 | non-normal transport failure | migrated + source |

### Positive controlled reliability regimes

| Experiment | Scientific role | Status |
|---|---|---|
| E9b | fixed-outer-gap cluster reliability confirmation | migrated; source provenance verified |
| E9 | first cluster-reliability experiment | pending archive migration |
| E8 | cross-scale reliability | pending archive location / migration |
| E3 | Grassmann mode-swap sanity | pending compact reconstruction |

## Scientific chain now represented in GitHub

```text
E8/E9/E9b: cross-scale / cluster reliability can work in controlled regular regimes
       ↓
E10: calibration does not transport unchanged under non-normality
       ↓
E11: non-normality can destroy the selected r=2 spectral object through pair cut
       ↓
E12: global conditioning-normalized scalar ranks risk but fails universal calibration
       ↓
E13: independent-realization failure prediction is negative and design-limited
       ↓
E13a: aggregated conditioning strongly ranks latent condition-level risk, exploratory
       ↓
E14a: matched global conditioning does not imply matched admissibility risk
       ↓
E14a-R: boundary-local candidate screen, corrected after implementation audit
       ↓
E15: fixed single-point boundary resolvent is refuted as a standalone transportable scalar
```

## Recommended package structure

```text
experiment_name/
├── README.md
├── config/
├── src/
├── reports/
├── tables/
└── MANIFEST.md
```

## Provenance rule

A historical result may be scientifically discussed without being presented as reproducible evidence. If executable source, configuration, or seed provenance is missing, the repository labels the result as historical/design documentation only.

A source file is not copied into GitHub if the available transfer path would truncate or rewrite it. In that case the repository records the verified SHA256 and archive manifest until byte-faithful transfer is possible.

## Next migration target

Next: recover the original E9 archive and the E8 cross-scale-reliability package, then add the compact E3 mode-swap sanity experiment. These three packages complete the positive-control side of the research history.