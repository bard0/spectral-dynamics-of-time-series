# E13a provenance manifest

## External archive

The full E13a reanalysis archive remains on Google Drive:

- experiment folder: https://drive.google.com/drive/folders/1DvbQkuoOBK_e1OzgdLE0cL-_89zhkLna
- scientific report: https://drive.google.com/file/d/1W6untiS8PbkWUwhf-4IgRggmB1272SMB/view
- original artifact manifest: https://drive.google.com/file/d/1w-MQ4oWmtVFmOgIETWcOy8vCYHMYKeLp/view

Access depends on the permissions of the corresponding Drive items.

## Archived contents

The Drive archive contains compact tables for:

- condition-level latent risk;
- cross-fitted condition features;
- rank metrics;
- calibration metrics;
- bootstrap summaries;
- aggregation ladder;
- variance decomposition;
- support diagnostics;
- original-target oracle ceiling;
- frozen reanalysis criteria;
- regenerated plots and audit reports;
- a recovery/finalization source file.

## Reanalysis status

E13a is not a fresh simulation experiment. It reused saved E13/E13a outputs and finalized a post-hoc condition-level reanalysis.

The archived scientific report explicitly states that the recovery did **not** recompute bootstrap, aggregation-ladder, simulation, or original E13 input. The full numerical results are carried by the saved CSV checkpoints.

For byte-level verification of those CSVs and regenerated figures, use the Drive folder above.

## Scientific relationship to E13

E13a changes the estimand. It estimates latent condition-level failure propensity rather than the specific Bernoulli outcome of an independent validation realization.

Consequently:

- E13 remains negative/design-limited;
- E13a remains post-hoc/exploratory;
- the two records are intentionally kept in separate GitHub packages.

## Large-file policy

The CSV and plot archive is not duplicated wholesale in GitHub. The repository preserves the concise scientific interpretation and points to Drive for the complete numerical record.