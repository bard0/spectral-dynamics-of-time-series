# Experiment Archive Index

This directory will contain the reproducible scientific packages migrated from the project archive.

The documentation in `docs/experiment_ledger.md` is the authoritative scientific history; this directory is the implementation/artifact layer.

## Migration policy

An experiment package is migrated only after checking:

1. the package belongs to the time-series / Koopman / EDMD project;
2. source and configuration correspond to the scientific result described in the ledger;
3. internal workflow notes are removed when they are not part of the scientific method;
4. known implementation corrections are documented next to the original code rather than silently changing the historical result;
5. large raw outputs are summarized or referenced by manifest/checksum when they are impractical for a normal source repository;
6. provenance-invalidated historical runs are not presented as reproducible confirmatory evidence.

## Experiment map

| Experiment | Scientific role | Status | Migration priority |
|---|---|---|---|
| E1 | local EDMD bias–variance | confirmed upper-bound sanity | medium |
| E2 | causal Lepski selector | negative | medium |
| E3 | Grassmann/mode-swap sanity | confirmed | medium |
| E4–E7 | adaptive-history benchmarks | exploratory/inconclusive/negative | medium |
| E8 | cross-scale reliability | controlled positive | high |
| E9/E9b | cluster reliability | controlled positive | high |
| E10 | non-normal transport | negative / pivot | high |
| E11 | matched perturbation mechanism | mechanism supported | high |
| E12 | conditioning scaling | calibrated-law negative | high |
| E13 | data-only admissibility target | design-limited negative | high |
| E13a | latent-risk reanalysis | exploratory | high |
| E14a | matched-conditioning geometry | global-conditioning sufficiency refuted | high |
| E14a-R | mechanism audit | exploratory + corrected | high |
| E15 | frozen boundary resolvent | standalone scalar refuted | **highest** |
| E15-R | matched-resolvent mechanism audit | exploratory | high |
| EXP-009 Gate 1 | source identifiability | strong negative | **highest** |

## Drive archive folders identified

The project archive contains dedicated folders for at least:

- `koopman_E9_cluster_reliability`
- `koopman_E9b_fixed_outer_gap`
- `koopman_E10_nonnormal_reliability`
- `koopman_E11_matched_nonnormal_perturbation`
- `koopman_E12_conditioning_scaling`
- `koopman_E13_causal_admissibility_guard`
- `koopman_E13a_latent_risk_reanalysis`
- `koopman_E14a_matched_conditioning_geometry`
- `koopman_E14aR_boundary_mechanism_audit`
- `koopman_E15_frozen_boundary_resolvent`
- `koopman_E15R_resolvent_mechanism_audit`
- `koopman_EXP009_gate1_identifiability`
- `koopman_EXP009_gate1_v2_pilot_overlap`
- `koopman_EXP009_gate1_confirmatory_clean_v2`

The source repository will not blindly mirror every checkpoint or multi-gigabyte simulation table. The goal is to preserve enough code, frozen design information, primary tables, reports, and manifests to make each scientific claim auditable and reproducible.

## First migrated package

`E15_frozen_boundary_resolvent/` is the first package being migrated because it is a central falsification with a complete executable source and a well-documented correction to the interpretation.