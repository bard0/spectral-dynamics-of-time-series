# E14a provenance manifest

This file records the archival provenance used for the public repository migration.

## Drive source

- experiment folder ID: `1NY7vbDjEzCWbOQS_ttcZ3aidYadFYpUz`
- scientific report ID: `1SMuSVPQ0pToPu2Aw4FBsjW_GEHdIUo4L`
- original artifact manifest ID: `10-wklYcmiuu13jNDAfdKgdMRnGtkooMM`
- frozen configuration ID: `1H4FnE03ZmFk7UlS4rtbJhMUeVgGMrBPT`
- source ID: `14Bi_eOyrYJR2wve6L_d2X46RziuvFr7d`

## Core checksums

- `src/E14a_experiment.py` SHA256: `ec2fdbeb7e84aa2cfea01e3a2210d17b1832c4b421ed7eac4cc8230c141462a5`
- `config/config.json` SHA256: `72fb9bf56f1242408db7c8fcbf13846d642bb8cf645c14315de5c64a462d61a3`

The source and configuration copied into this repository were checked against these hashes before migration.

## Archived perturbation bank

The original Drive package contains a persisted `perturbation_directions.npy` bank and its SHA256 record. The binary bank is not duplicated in this source repository because it is deterministically generated from the frozen master seed and because the raw archive remains the byte-level source of truth.

Frozen master seed: `14031401`.

## Large archived outputs

The original package contains per-cell raw checkpoints of several megabytes each, paired-bootstrap checkpoints, CSV summaries, figures, reports, and the full artifact manifest. These are not blindly duplicated here. The repository preserves the executable source, frozen configuration, scientific result, and the hashes/identifiers needed to audit the archived run.

## Scientific integrity note

The E14a primary verdict is not inferred from later experiments. It is the frozen E14a result itself: global conditioning sufficiency is refuted in the controlled matched-geometry family. Later E14a-R and E15 results are stored separately and do not retroactively alter the E14a outcome.