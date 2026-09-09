# E14a provenance manifest

This file records the archival provenance used for the public repository migration.

## External archive

Large raw artifacts remain in the project archive on Google Drive:

- experiment folder: https://drive.google.com/drive/folders/1NY7vbDjEzCWbOQS_ttcZ3aidYadFYpUz
- scientific report: https://drive.google.com/file/d/1SMuSVPQ0pToPu2Aw4FBsjW_GEHdIUo4L/view
- original artifact manifest: https://drive.google.com/file/d/10-wklYcmiuu13jNDAfdKgdMRnGtkooMM/view
- frozen configuration: https://drive.google.com/file/d/1H4FnE03ZmFk7UlS4rtbJhMUeVgGMrBPT/view
- original executable source: https://drive.google.com/file/d/14Bi_eOyrYJR2wve6L_d2X46RziuvFr7d/view

Access to these links depends on the permissions of the corresponding Drive items. The links are retained even when the underlying archive is not publicly shared, because Drive remains the byte-level source of truth for the original run.

## Core checksums

- original executable source SHA256: `ec2fdbeb7e84aa2cfea01e3a2210d17b1832c4b421ed7eac4cc8230c141462a5`
- frozen `config.json` SHA256: `72fb9bf56f1242408db7c8fcbf13846d642bb8cf645c14315de5c64a462d61a3`

The frozen configuration copied into this repository was checked against the archived file before migration. The original executable source is linked above and may also be mirrored into `src/` because it is small enough for the source repository.

## Archived perturbation bank

The original Drive package contains a persisted `perturbation_directions.npy` bank and its SHA256 record. The binary bank is not duplicated in this repository because it is deterministically generated from the frozen master seed and because the raw archive remains the byte-level source of truth.

Frozen master seed: `14031401`.

## Large archived outputs

The original package contains per-cell raw checkpoints of several megabytes each, paired-bootstrap checkpoints, CSV summaries, figures, reports, and the full artifact manifest. These are not blindly duplicated here. The GitHub package preserves the scientific result, frozen design, concise reproducibility metadata, checksums, and direct archive links.

## Scientific integrity note

The E14a primary verdict is not inferred from later experiments. It is the frozen E14a result itself: global conditioning sufficiency is refuted in the controlled matched-geometry family. Later E14a-R and E15 results are stored separately and do not retroactively alter the E14a outcome.