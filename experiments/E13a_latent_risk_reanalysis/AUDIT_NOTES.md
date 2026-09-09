# E13a implementation audit notes

## Scientific status

The E13a numerical result remains:

**STRONG EXPLORATORY / POST-HOC / NOT CLAIM-READY.**

The implementation audit does not invalidate the reported condition-level associations, but it identifies several issues that must not be inherited by later confirmatory experiments.

## Critical implementation findings

### 1. Original checkpoint logic was not a true resume mechanism

The original E13a computation wrote checkpoints but did not load compatible completed blocks before recomputation. A rerun could therefore repeat the 10,000 condition-bootstrap and 500-replicate aggregation ladder.

Later confirmatory code must bind checkpoints to the active configuration and skip compatible completed blocks.

### 2. Criterion-D fallback was incomplete

The intended fallback logic should account for both association strength and meaningful calibration/MSE improvement. The original implementation used only a maximum pooled-Spearman condition.

This did **not** change the realized E13a verdict because the stronger primary criteria for standalone conditioning candidates already passed.

### 3. Integrity validation was incomplete

The integrity gate should explicitly require:

- no missing validation-failure labels;
- binary `validation_failure`;
- binary probe/validation support and `r=2`-defined flags.

The realized E13 dataset had complete labels, so this is a robustness issue rather than evidence of contaminated reported metrics.

### 4. Automatic reporting was too shallow

The original automatic report did not adequately summarize:

- latent-risk heterogeneity;
- Fold-A/Fold-B reproducibility;
- the `m=1` aggregation result;
- the full aggregation ladder;
- variance decomposition;
- why conditioning appeared mechanistically interesting.

The repository README therefore contains a fuller scientific interpretation than the archived auto-generated report.

### 5. Finite-support checks should fail early

Each score/fold should explicitly verify enough finite held-out conditions before bootstrap or calibration. Fully undefined scores should return a structured unavailable status rather than fail late.

## What was implemented correctly

The following parts were scientifically usable:

- no new simulation was introduced in E13a;
- E13 input was treated as immutable;
- support rate was computed before support filtering;
- even/odd cross-fit separation kept probe summaries and validation targets in disjoint replicate halves;
- development/test split was condition-level;
- primary bootstrap was condition-level;
- aggregation sampling was without replacement;
- `(g,c)` was reserved for oracle/secondary analysis rather than primary scores;
- standalone conditioning candidates were labeled explicitly as post-hoc/exploratory.

## Recovery provenance

The recovery/finalization source in `src/` reused completed CSV checkpoints and regenerated plots/reporting artifacts. It did **not** recompute the expensive scientific core of E13a.

Recovery-source SHA256:

`e788384325352f664468c4e1d086b0b755607f3c5b442f5c79649649f2ce1143`

## Rule inherited by E14 and later

Do not reuse the E13a implementation template unchanged. Later confirmatory code must have:

- real resume;
- complete verdict logic;
- strict integrity checks;
- finite-support fail-fast gates;
- substantive automatic scientific reports;
- explicit source/config/checkpoint provenance.