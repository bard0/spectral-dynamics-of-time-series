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

## Historical naming note

The project contains two numbering conventions from different stages. In particular:

- early `EXP-007` is the broad online spectral benchmark;
- later `E7` is the null-calibrated directional diagnostic;
- early `EXP-008` is the falsification of nested disagreement as a direct true-drift proxy;
- later `E8` is the positive regular-gap cross-scale reliability benchmark.

The original labels are preserved instead of being silently renumbered.

## Migration status

### Early adaptive-history branch

| Experiment | Scientific role | Status |
|---|---|---|
| E1 | local EDMD bias–variance upper-bound sanity | historical record migrated |
| E2 | causal Lepski-style selector | historical negative migrated |
| E3 | Grassmann/mode-swap sanity | historical record migrated |
| E4 | adaptive spectral window/oracle benchmark | historical exploratory negative migrated |
| E5 | smooth-drift benchmark | historical inconclusive migrated |
| E6 | observation/process-noise control correction | historical audit migrated |
| EXP-007 | broad causal online spectral benchmark | historical inconclusive migrated |
| EXP-008 | nested disagreement vs true dynamical drift | historical decisive negative migrated |

### Reliability branch / positive and negative controls

| Experiment | Scientific role | Status |
|---|---|---|
| E7 | null-calibrated directional added-value test | historical negative migrated |
| E8 | regular-gap cross-scale reliability | historical positive record migrated; byte-level archive not currently located |
| E9 | individual mode vs invariant cluster mechanism | scientific layer migrated; ZIP/source hashes verified |
| E9b | fixed-outer-gap cluster reliability confirmation | migrated; source provenance verified |

### Spectral-admissibility mechanism chain

| Experiment | Scientific role | Status |
|---|---|---|
| E10 | non-normal transport failure | migrated + source |
| E11 | matched non-normal perturbation mechanism | migrated + source |
| E12 | conditioning-scaling calibration limits | migrated + source |
| E13 | independent-realization admissibility prediction | migrated + source |
| E13a | latent condition-level risk reanalysis | migrated + recovery source + audit |
| E14a | matched-conditioning geometry falsification | migrated |
| E14a-R | boundary-specific mechanism audit with corrected screen | migrated |
| E15 | boundary-resolvent sufficiency falsification | migrated |

### Causal source-attribution branch

| Experiment | Scientific role | Status |
|---|---|---|
| EXP-009 Gate 1 | finite-sample instability vs smooth true drift identifiability | migrated; strong negative |

## Scientific chain represented in GitHub

```text
E1–E7: generic adaptive-history selection is not robustly established
       ↓
EXP-008: nested spectral disagreement is not a direct true-drift proxy
       ↓
E8: the same kind of cross-scale signal can predict estimation error in a regular regime
       ↓
E9/E9b: invariant spectral-cluster reliability survives internal mode ambiguity when outer separation is controlled
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
       ↓
EXP-009: source attribution between finite-sample instability and smooth drift is not identifiable from the tested causal observables
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

The next major layer is the parallel spectral-admissibility theory program (`T4–T12`) and selected compact tables/figures from the core E9b–E15 packages. Theory entries must preserve their formal status: supported, refuted, inconclusive, design-limited, or provenance-invalidated.