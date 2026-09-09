# Experiment Archive Index

This directory contains reproducible scientific packages migrated from the project archive.

The documentation in `docs/experiment_ledger.md` is the authoritative scientific history; this directory is the implementation/artifact layer.

## Migration policy

An experiment package is migrated only after checking:

1. the package belongs to the time-series / Koopman / EDMD project;
2. source and configuration correspond to the scientific result described in the ledger;
3. internal workflow notes are removed when they are not part of the scientific method;
4. known implementation corrections are documented next to the original code rather than silently changing the historical result;
5. large raw outputs are summarized or referenced by manifest/checksum when they are impractical for a normal source repository;
6. provenance-invalidated historical runs are not presented as reproducible confirmatory evidence.

## Migration order

The migration follows scientific importance rather than chronology.

### Phase 1 — Core falsification and current story

| Experiment | Scientific role | Status |
|---|---|---|
| E15 | boundary resolvent sufficiency falsification | migrated |
| EXP-009 Gate 1 | source attribution identifiability | migrated |

### Phase 2 — Mechanism chain

| Experiment | Scientific role | Status |
|---|---|---|
| E14a / E14a-R | global conditioning insufficiency and mechanism audit | next |
| E13 / E13a | data-only admissibility prediction limits | next |
| E12 | conditioning scaling calibration limits | next |
| E11 | non-normal perturbation mechanism | next |
| E10 | transport failure of regular-regime calibration | next |

### Phase 3 — Positive controlled regimes

| Experiment | Scientific role | Status |
|---|---|---|
| E9/E9b | cluster reliability | next |
| E8 | cross-scale reliability | next |
| E3 | Grassmann mode-swap sanity | next |

## Current package structure

Each experiment should contain:

```
experiment_name/
├── README.md
├── config/
├── src/
├── reports/
├── tables/
├── figures/
└── MANIFEST.md
```

Large checkpoints and raw simulation dumps should remain archived separately with checksums unless they are essential for reproduction.

## Provenance rule

A historical result may be scientifically discussed without being presented as reproducible evidence. If executable source, configuration, or seed provenance is missing, the repository must label the result as historical/design documentation only.

## Next migration target

The next packages to add are E14a-R and E13 because together they explain why global conditioning and single-trajectory admissibility prediction are insufficient, which is the conceptual bridge from early reliability calibration to the current spectral-admissibility framework.