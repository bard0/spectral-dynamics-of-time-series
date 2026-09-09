# E7 — Null-calibrated directional diagnostic

## Naming note

This is the **later reliability-branch experiment** recorded as `E7` in the project history. It is distinct from the earlier `EXP-007` broad online spectral benchmark.

The original labels are preserved to avoid rewriting the research chronology.

## Scientific question

After controlling for the overall magnitude of cross-scale inconsistency, does a directional spectral diagnostic provide additional information beyond magnitude alone?

## Result

**NEGATIVE / branch-stopping for the directional added-value hypothesis.**

Audited project-history metrics:

- directional added-value difference ≈ `-0.098`, 95% interval ≈ `[-0.368, 0.242]`;
- AUROC ≈ `0.454`, interval ≈ `[0.283, 0.629]`;
- clean same-`M=4` AUROC ≈ `0.478`;
- drift `M=16` support ≈ `69%`, below the predefined `90%` gate.

## Interpretation

The frozen directional calibration did not provide reliable added value beyond magnitude in the tested setting.

A substantial part of the apparent raw directional consistency could be explained by magnitude confounding rather than by an independently useful directional signal.

## Verdict discipline

This branch should not be revived by cosmetic parameter changes or a post-hoc reformulation of the same score. A future return would require a genuinely new mechanism or a theory-driven reason to expect a directional quantity to carry information not contained in magnitude.

## Relation to E8

The negative directional result helped simplify the next question. E8 tested the more basic claim that **cross-scale disagreement magnitude itself** can predict spectral estimation error in a regular stationary regime. E8 passed that narrower controlled test.

## Provenance status

The result is preserved in the authoritative experiment ledger as an audited historical run. The original package has not yet been migrated as a byte-level reproducibility archive, so this directory records the scientific negative result without inventing source or configuration provenance.