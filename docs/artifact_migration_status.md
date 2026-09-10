# Artifact and memory synchronization status

## Current status

The project archive has been consolidated into one canonical external research tree, and the public GitHub repository is now treated as a curated, compact mirror of the scientific record rather than a second source of truth.

The canonical archive is organized as:

```text
Koopman_Spectral_Research/
├── 00_Project_memory/
│   ├── Core_memory/
│   ├── Ledgers/
│   ├── Audits/
│   └── Manifests/
├── 01_Theory/
├── 02_Experiments/
├── 03_Results/
├── 04_Manuscript/
└── 99_Archive/
```

The public repository contains only material that can be safely represented as scientific documentation, compact source/configuration, provenance records, and selected results.

## Experiment coverage

The consolidated archive contains the main experiment packages for:

- E9 / E9b cluster reliability;
- E10 non-normal reliability transport;
- E11 matched non-normal perturbations;
- E12 conditioning scaling;
- E13 causal admissibility guard;
- E13a latent-risk reanalysis;
- E14a matched-conditioning geometry;
- E14a-R boundary mechanism audit;
- E15 frozen boundary resolvent;
- E15-R mechanism audit;
- EXP-009 pilot, identifiability, and confirmatory branches.

Earlier E1-E8 stages are retained as historical scientific records when complete byte-level run packages are unavailable. Their status must not be silently upgraded to fully reproducible execution.

## Theory coverage

The repository mirrors the structured theory branch through T12, including:

- T4-T6 boundary probability geometry;
- T7-T11 finite-epsilon falsification and certified regimes;
- T12 finite-data bridge, local nonregularity, risk intervals, and Riesz-chart formulation.

## Provenance correction retained

A later recovery audit established an important distinction in the T12 sequence:

- **T12-A4b:** the numerical/theory-log result is retained, but authentic original executable/configuration provenance was not fully recoverable. It must therefore not be described as source-reproducible merely because the numerical summary is known.
- **T12-B1:** the historical correlated-trajectory numerical result is **provenance-invalidated / not claim-ready**.

A future correlated-trajectory replication must use a new frozen identifier, `T12-B1R`, with executable source, configuration, exact event definitions, seed namespaces, manifests, hashes, and integrity tests preserved before outcomes.

## Migration policy

- Negative, inconclusive, design-limited, and implementation-corrected results are preserved.
- Large trajectory tables, checkpoints, and full simulation archives remain outside Git history unless a compact reproducer requires them.
- Source-level reproducibility and scientific-history coverage are reported separately.
- Public files exclude internal workflow/tool attribution that is irrelevant to the scientific record.

## Synchronization rule

When the external structured memory and GitHub differ, the structured project memory, ledgers, audits, and archived experiment packages determine the scientific status. GitHub should then be updated conservatively without promoting a result beyond its recorded claim or provenance ceiling.
