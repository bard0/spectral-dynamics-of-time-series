# E12 archive manifest

## Archived source package

The original Drive archive contains:

- full `E12_COLAB_ONE_CELL.py` source;
- configuration and environment capture;
- Part-A exact-discriminant rows and aggregates;
- Part-B matched-direction raw rows and aggregates;
- held-out logistic-model metrics and frozen gates;
- plots and audit reports;
- full ZIP archive retained externally because it is large.

Verified executable-source SHA256:

`39121d0cb4222e70fd3580c199bcf3743ff5a0f91bfd3aa6e0eff3e22669f7e9`

## Public-release audit note

The implementation variable named `sep` equals the raw eigenvalue gap `g` in the archived source. It must not be described as true Schur/Stewart–Sun separation.

## Large-file policy

The original ZIP is approximately 219 MB and is not duplicated in this source repository. The external archive remains the byte-level source of truth for raw matched-direction data and generated figures.