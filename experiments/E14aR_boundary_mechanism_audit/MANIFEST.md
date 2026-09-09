# E14a-R provenance manifest

## External archive

The full archived package remains on Google Drive:

- experiment folder: https://drive.google.com/drive/folders/1T6asPBkf9Gm-RFs-KMjHUA_VVPlGD5GU
- scientific report: https://drive.google.com/file/d/1WCk1O5jVt_xRDbPg-gS5IZm7KzSD1hqd/view
- original artifact manifest: https://drive.google.com/file/d/130rXjpv-LRDI5GerCNiqJ9Qb8bnncGsZ/view

Access depends on the permissions of the corresponding Drive items.

## Important archive status

This package is **not** treated as a fully self-contained reproducibility archive.

The original archived source file was only 3,266 bytes and contains the tail of the executed program rather than the full executable source. A later source audit recovered the complete program sufficiently to identify the per-epsilon bug, but the original ZIP did not preserve that complete source.

Accordingly, the GitHub package preserves:

- corrected scientific interpretation;
- explicit implementation correction;
- original artifact hashes;
- direct links to the full archived result package;
- the relationship to the fresh E15 falsification.

It does not claim that the original E14a-R ZIP can independently reproduce the complete analysis from source.

## Selected archived checksums

From the original E14a-R manifest:

- archived source tail: `65244f5ac09a3bedbf991d98a43b44bd722cc75cd71fd0dc32629d477f75351b`
- `analysis_config.json`: `7625d68f6307fab4b9e7cb264a11f322927234aef08f74e0659f7a1cb1e75ddc`
- `candidate_rank_metrics.csv`: `3d571dd4b3f4b7fc5c5dff21854269c78b5494b214d354798853d08c1534f37f`
- `operator_boundary_metrics.csv`: `a4f785bbb1242f79f03854aba7ec44db750b9e9593cce2fa1618676e8c7a1b95`
- `operator_integrated_risk.csv`: `95384e975b90af1a6adfbe54005624d2ec10be92adf99b107eb628fce7ceb7e8`
- `projected_boundary_mechanism_rows.csv.gz` (~54.5 MB): `97dec4e49ea1fe90b77931ca033601560a5650e23436296dcd230eb78b839b3f`
- scientific report: `25aba33d07d1de70f548ad69326eecaa59eb6d175b5cc3d3d666aec6f33ac5fb`

## Large-file policy

The ~54.5 MB mechanism table, plots, raw CSVs, and other heavy outputs are intentionally not duplicated in GitHub. The Drive folder above is the archive location for those files.

For future migrated experiments, the same policy is used: GitHub contains compact reproducibility-critical material and scientific records; large raw artifacts remain on Drive with direct links and checksums.

## Scientific integrity

The original automatic verdict is preserved only as part of the historical audit trail and is explicitly superseded by the corrected screen documented in `reports/AUDIT_CORRECTION.md`.