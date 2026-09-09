# E13 provenance manifest

## External archive

The full archived experiment remains on Google Drive:

- experiment folder: https://drive.google.com/drive/folders/1siQZe4zMVC9-KXExHtF_0GWKDjboka-C
- scientific report: https://drive.google.com/file/d/1xKAfTnPsVuEzeBXqN5ft8g70IDAAE17i/view
- original artifact manifest: https://drive.google.com/file/d/1E7l6S8gN6ZAMD8ub1Z1nUtIV2oP7eIv5/view

Access depends on the permissions of the corresponding Drive items.

## Archived contents

The original package contains:

- `csv/raw_rows.csv`;
- held-out metrics, calibration, bootstrap and condition summaries;
- survivorship summaries;
- plots for probe support, ROC/PR, calibration, gap/conditioning/separation diagnostics and hard conditions;
- causality, correctness, statistical, spectral-geometry and reproducibility audits;
- frozen configuration/environment;
- executable experiment source;
- multiple multi-megabyte checkpoint files at the experiment root.

The checkpoint CSVs are intentionally not duplicated in GitHub. The Drive folder above is the byte-level archive for those heavy files.

## Public GitHub record

The GitHub package preserves the scientifically relevant distinction between:

1. the frozen negative held-out result; and
2. the later design audit showing that the independent-realization target had a low oracle ceiling.

The public interpretation is therefore `INCONCLUSIVE / DESIGN-LIMITED NEGATIVE`, while the preregistered verdict `DATA-ONLY SPECTRAL-ADMISSIBILITY PREDICTION NOT SUPPORTED` remains unchanged.

## Relationship to E13a

E13a is stored separately because it changes the estimand from a single independent validation outcome to latent condition-level risk. No E13a result should be used to overwrite the original E13 experiment.