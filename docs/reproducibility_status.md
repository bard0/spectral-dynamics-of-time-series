# Reproducibility and Provenance Status

This file distinguishes scientific-history coverage from executable reproducibility.

A result can be scientifically important while still lacking a fully migrated byte-level archive. The repository does not promote such a result to reproducible status merely because its numerical summary is known.

## Status classes

- **SOURCE MIGRATED** — executable source is present in GitHub and linked to the archived result.
- **SOURCE VERIFIED / HASH RECORDED** — source exists in the external archive and its SHA256 has been verified, but the exact source file is not yet stored in GitHub.
- **THEORY-LOG / PROVENANCE-LIMITED** — a structured theory log records the design/result, but authentic source-level reproduction is not established from the recovered archive.
- **HISTORICAL RECORD** — the authoritative project ledger supports the scientific result, but a complete executable archive has not yet been located.
- **PROVENANCE-INVALIDATED** — a historical numerical result exists but its original execution provenance is insufficient for a claim-ready reproducible result.

## Experiment map

| Experiment | Status | Notes |
|---|---|---|
| E1 | historical record | upper-bound/numerical result preserved in ledger |
| E2 | historical record | practical negative preserved in ledger |
| E3 | historical record | mode-swap sanity result preserved in ledger |
| E4 | historical record | broad adaptive-window benchmark |
| E5 | historical record | smooth-drift benchmark |
| E6 | historical record | noise-control methodological correction |
| EXP-007 | historical record | broad online benchmark |
| EXP-008 | historical record | direct drift-proxy falsification |
| E7 | historical record | later directional-diagnostic negative result |
| E8 | historical record | package name known; byte-level archive not currently located |
| E9 | source verified / hash recorded | original ZIP and source recovered; source SHA `a5155f95f88219f00926f7a22b551978584f8150849cf0bef84b7707939099b8` |
| E9b | source verified / hash recorded | source SHA `683c989136c2784b2e14990ff8a8916d649f3284026db2f112d61fc299d86e7f` |
| E10 | source migrated | source SHA `52537ac03793b690b542910c6002d535175543771ff44be885f18ba66fab2d8d` |
| E11 | source migrated | source SHA `0f13104ac089e5a2c9c55e08ce8a6098d4101641a9a8ac6eb5c737aafdaa78fd` |
| E12 | source migrated | source SHA `39121d0cb4222e70fd3580c199bcf3743ff5a0f91bfd3aa6e0eff3e22669f7e9` |
| E13 | source migrated | source SHA `58522864293f10b03fec18af0e5e9abb1091880047aba487c8e7c3fbcdda0b0c` |
| E13a | recovery source migrated | recovery SHA `e788384325352f664468c4e1d086b0b755607f3c5b442f5c79649649f2ce1143`; exploratory result |
| E14a | source verified / hash recorded | archived source SHA `ec2fdbeb7e84aa2cfea01e3a2210d17b1832c4b421ed7eac4cc8230c141462a5` |
| E14a-R | audited historical mechanism package | original archive had source-capture/reporting defects; corrected scientific result documented |
| E15 | source verified / hash recorded | archived program SHA `d37783041d1442499a8c4152f91af5c6835179b9dc4db22e5ff8a4feae870ce4` |
| EXP-009 | migrated scientific package | frozen design/result documented |
| T4-T11 | theory-log provenance | derivations and frozen numerical summaries migrated from the structured theory log |
| T12-A1-A3 | theory-log provenance | iid/data-centered/local-boundary sequence documented; source-level status must be read stage by stage |
| T12-A4 | theory-log provenance | design-limited Riesz-chart transport stage |
| T12-A4b | theory-log / provenance-limited | high-N numerical interpretation retained, but authentic original executable/configuration provenance was not fully recoverable |
| T12-B1 | provenance-invalidated | historical correlated-trajectory numerical outcome retained, claim status removed |
| T12-B1R | not yet run | required future reconstructed/re-frozen correlated-trajectory replication |

## Byte-faithful source policy

A source file is not committed when the available transfer path cannot be verified byte-for-byte. In that case the external source SHA256 is retained and the source stays in the project archive.

This is intentionally stricter than copying a visually similar or truncated program into the public repository.

## Large artifacts

The following normally remain outside GitHub unless needed for a compact reproducer:

- multi-megabyte trajectory-level CSV files;
- checkpoint banks;
- large compressed mechanism tables;
- complete plot collections;
- simulation ZIP archives.

Their names and checksums are retained in experiment manifests where available.

## Required standard for future confirmatory experiments

A claim-ready future package should freeze and preserve before target outcomes:

1. complete executable source;
2. full configuration;
3. exact event/metric definitions;
4. random-seed namespaces;
5. checkpoint/resume rules;
6. environment information;
7. artifact manifest;
8. SHA256 checksums;
9. substantive correctness/statistical/claim audits.

The T12 provenance correction is the reason this standard is explicit. In particular, the next stationary correlated-trajectory test must use a new identifier (`T12-B1R`) rather than silently rerunning the provenance-invalidated B1 record.
