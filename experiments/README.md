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

For large raw artifacts — checkpoint banks, multi-megabyte CSV tables, compressed mechanism rows, simulation dumps, large plot collections, and archived ZIP files — the experiment `MANIFEST.md` contains:

- a direct link to the corresponding Google Drive experiment folder;
- links to important individual archived files when useful;
- SHA256 values from the original artifact manifest;
- a note describing whether the Drive item is required for byte-level reproduction.

GitHub keeps the compact scientific/reproducibility layer whenever available:

- experiment README;
- frozen configuration;
- executable source when reasonably sized and provenance-valid;
- corrected reports/audit notes;
- compact primary tables;
- provenance manifest.

Drive remains the byte-level source of truth for heavy archived outputs. Access to a Drive link depends on that item's sharing permissions.

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
| E14a | matched-conditioning geometry falsification | migrated |
| E14a-R | boundary-specific mechanism audit with corrected screen | migrated |
| E13 / E13a | data-only admissibility prediction limits | **next** |
| E12 | conditioning scaling calibration limits | next |
| E11 | non-normal perturbation mechanism | next |
| E10 | transport failure of regular-regime calibration | next |

### Phase 3 — Positive controlled regimes

| Experiment | Scientific role | Status |
|---|---|---|
| E9/E9b | cluster reliability | next |
| E8 | cross-scale reliability | next |
| E3 | Grassmann mode-swap sanity | next |

## Recommended package structure

```
experiment_name/
├── README.md
├── config/
├── src/
├── reports/
├── tables/
└── MANIFEST.md
```

`figures/`, raw tables, checkpoints, and complete ZIP archives may remain on Drive when they are large; their locations and hashes belong in `MANIFEST.md`.

## Provenance rule

A historical result may be scientifically discussed without being presented as reproducible evidence. If executable source, configuration, or seed provenance is missing, the repository labels the result as historical/design documentation only.

## Next migration target

The next packages are E13 and E13a. Together they document the distinction between predicting a **single independent admissibility realization** and estimating a **latent condition-level risk**, including the design-limited negative E13 result and the later exploratory reanalysis.