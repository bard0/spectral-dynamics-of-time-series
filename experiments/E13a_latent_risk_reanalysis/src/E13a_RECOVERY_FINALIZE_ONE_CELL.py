# E13a recovery/finalization cell: use after a late plotting/reporting error.
# It reuses saved Drive CSV checkpoints and DOES NOT recompute bootstrap or aggregation ladder.
import json,shutil,zipfile,hashlib
from pathlib import Path
import numpy as np,pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from sklearn.isotonic import IsotonicRegression
from google.colab import drive,files

ROOT=Path('/content/koopman_E13a_latent_risk_reanalysis');DRIVE=Path('/content/drive/MyDrive/koopman_E13a_latent_risk_reanalysis')
CSV,PLOTS,REPORTS,CONFIG,CODE=[ROOT/x for x in ('csv','plots','reports','config','code')]
drive.mount('/content/drive',force_remount=False)
for p in (ROOT,CSV,PLOTS,REPORTS,CONFIG,CODE):p.mkdir(parents=True,exist_ok=True)
for source in (DRIVE/'csv',DRIVE/'config'):
    if source.exists():
        for p in source.glob('*'):
            if p.is_file():shutil.copy2(p,(CSV if source.name=='csv' else CONFIG)/p.name)
def require(ok,msg):
    if not ok:raise RuntimeError('E13a recovery cannot continue: '+msg)
def mirror(p):
    q=DRIVE/p.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
def text(s,rel):
    p=ROOT/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf8');mirror(p);return p
def plot(name,fun):
    f,a=plt.subplots(figsize=(7,4.8));fun(f,a);f.tight_layout();p=PLOTS/name;f.savefig(p,dpi=180,bbox_inches='tight');plt.close(f);mirror(p)
def load(name):
    p=CSV/name;require(p.exists(),f'missing checkpoint {p}');return pd.read_csv(p)
C=load('condition_latent_risk.csv');F=load('crossfit_condition_features.csv');R=load('pre_failure_rank_metrics.csv');AS=load('aggregation_ladder_summary.csv');V=load('variance_decomposition.csv');OC=load('original_target_oracle_ceiling.csv');CR=load('frozen_reanalysis_criteria.csv');frozen_predictions=load('pre_failure_frozen_predictions.csv')
# Older interrupted cells can have saved a malformed prediction CSV. Rebuild only these
# tiny development-only isotonic fits from F; no raw E13 simulation/bootstrap/ladder is rerun.
if not {'score_name','fold','target_p_fail','prediction'}.issubset(frozen_predictions.columns):
    SCORES={'P0_median_DK':('median_D_K',1),'P1_median_S2':('median_S2',1),'P2_negative_median_gap_min':('median_gap_min',-1),'P3_median_R_kappa':('median_R_kappa',1),'P4_median_R_sep':('median_R_sep',1),'P5_median_kappa_H':('median_kappa_H',1),'P6_median_kappa_2H':('median_kappa_2H',1),'P7_median_kappa_max':('median_kappa_max',1)}
    rebuilt=[]
    for score_name,(column,sign) in SCORES.items():
        for fold in ('A','B','pooled'):
            q=F[['condition_id','g','c','split','fold','target_p_fail','target_n','target_failures',column]].copy();q['score']=sign*pd.to_numeric(q[column],errors='coerce');q=q.replace([np.inf,-np.inf],np.nan).dropna(subset=['score','target_p_fail'])
            if fold=='pooled':q=q.groupby(['condition_id','g','c','split'],as_index=False).agg(score=('score','mean'),target_p_fail=('target_p_fail','mean'),target_n=('target_n','sum'),target_failures=('target_failures','sum'))
            else:q=q.loc[q.fold.eq(fold)]
            dev,test=q.loc[q.split.eq('development')],q.loc[q.split.eq('test')]
            require(len(dev)>=3 and dev.score.nunique()>=2,'cannot rebuild frozen predictions: insufficient development support')
            increasing=bool(spearmanr(dev.score,dev.target_p_fail).statistic>=0)
            pred=IsotonicRegression(increasing=increasing,out_of_bounds='clip').fit(dev.score,dev.target_p_fail).predict(test.score)
            out=test.copy();out['prediction']=np.clip(pred,1e-6,1-1e-6);out['score_name']=score_name;out['fold']=fold
            rebuilt.append(out[['condition_id','g','c','split','fold','target_p_fail','target_n','target_failures','score','prediction','score_name']])
    frozen_predictions=pd.concat(rebuilt,ignore_index=True)
    path=CSV/'pre_failure_frozen_predictions.csv';frozen_predictions.to_csv(path,index=False);mirror(path)
    print('Rebuilt only frozen prediction CSV from saved cross-fit features; no bootstrap/ladder recomputed.')
def heatmap(f,a,col,title):
    q=C.pivot(index='g',columns='c',values=col).sort_index().sort_index(axis=1);im=a.imshow(q,origin='lower',aspect='auto');a.set(title=title,xlabel='c index',ylabel='g index');f.colorbar(im,ax=a)
plot('01_corrected_support_grid.png',lambda f,a:heatmap(f,a,'support_rate','Corrected all-row probe support rate'))
plot('02_latent_failure_probability.png',lambda f,a:heatmap(f,a,'p_fail','Latent validation failure probability'))
for col,name in [('median_R_kappa','03_pfail_vs_median_Rkappa.png'),('median_kappa_2H','04_pfail_vs_kappa2H.png'),('median_kappa_max','05_pfail_vs_kappa_max.png'),('median_gap_min','06_pfail_vs_gap.png'),('median_schur_sep_min','07_pfail_vs_schur_sep.png')]:
    def draw(f,a,col=col):
        q=F[F.fold.eq('A')];a.scatter(q[col],q.target_p_fail,c=q.split.map({'development':'tab:blue','test':'tab:orange'}));a.set(xlabel=col,ylabel='opposite-half latent p_fail')
    plot(name,draw)
def ranks(f,a):
    q=R[R.fold.eq('pooled')];a.bar(q.score,q.spearman);a.axhline(0,color='k');a.tick_params(axis='x',rotation=60);a.set_ylabel('held-out pooled Spearman')
plot('08_pre_failure_correlations.png',ranks)
def calibration(f,a):
    q=frozen_predictions[(frozen_predictions['score_name'].eq('P3_median_R_kappa'))&(frozen_predictions['fold'].eq('pooled'))];a.scatter(q['target_p_fail'],q['prediction']);a.plot([0,1],[0,1],'k--');a.set(xlabel='actual p_fail',ylabel='frozen isotonic prediction',title='P3 frozen held-out calibration')
plot('09_frozen_calibration.png',calibration)
for metric,name,label in [('spearman_median','10_aggregation_ladder_spearman.png','median held-out Spearman'),('MSE_improvement_median','11_aggregation_ladder_mse_improvement.png','median held-out MSE improvement')]:
    def ladder(f,a,metric=metric,label=label):
        for score,q in AS[AS.fold.eq('pooled')].groupby('score'):a.plot(q.m,q[metric],marker='o',label=score)
        a.set_xscale('log');a.set_xticks([1,2,4,8,16,32,64]);a.set_xticklabels([1,2,4,8,16,32,64]);a.set(xlabel='m independent probe estimates',ylabel=label);a.legend(fontsize=7)
    plot(name,ladder)
def var(f,a):
    V.set_index('feature')[['between_condition_variance','mean_within_condition_variance']].plot.bar(ax=a);a.tick_params(axis='x',rotation=45);a.set_ylabel('log-feature variance')
plot('12_within_between_variance.png',var)
plot('13_support_rate_vs_latent_risk.png',lambda f,a:(a.scatter(1-C.support_rate,C.p_fail,c=C.split.map({'development':'tab:blue','test':'tab:orange'})),a.set(xlabel='1 − support rate (secondary)',ylabel='p_fail')))
def repro(f,a):
    q=R.pivot(index='score',columns='fold',values='spearman')
    for score,x in q.iterrows():a.plot(['A','B'],[x['A'],x['B']],marker='o',label=score)
    a.axhline(0,color='k');a.set_ylabel('held-out Spearman');a.legend(fontsize=7)
plot('14_crossfit_reproducibility.png',repro)
plot('15_oracle_ceiling_original_target.png',lambda f,a:(a.bar(['AUROC','PR-AUC','Brier improvement'],[OC.AUROC.iloc[0],OC.PR_AUC.iloc[0],OC.Brier_improvement_vs_constant.iloc[0]]),a.axhline(.80,color='r',ls='--'),a.axhline(.10,color='purple',ls=':')))
verdict=CR.loc[CR.criterion.eq('frozen reanalysis verdict'),'verdict'].dropna().iloc[0]
text(f'''# E13a — recovery finalization\n\n## Status\n\n**{verdict}**\n\nThis recovery reused saved E13a checkpoints; no bootstrap, aggregation ladder, simulation, or E13 input was recomputed. E13’s official result remains unchanged.\n\nThe full numerical results are in `csv/`; plots were regenerated from those immutable E13a CSV checkpoints. All claims remain **POST-HOC / AUDIT / NOT CLAIM-READY**.\n''','reports/SCIENTIFIC_REPORT.md')
for name,body in {'DESIGN_LIMITATION_AUDIT.md':'Original E13 targeted an independent validation Bernoulli outcome; E13a evaluates condition propensity only.\n','STATISTICAL_AUDIT.md':'Recovery used pre-existing condition-level results; no row bootstrap was run here.\n','CAUSALITY_AUDIT.md':'Recovery creates no trajectories and reads only saved E13a outputs.\n','REANALYSIS_AUDIT.md':'This is a recovery finalization, not a new E13 calculation.\n','CLAIM_AUDIT.md':'No recovery step changes E13 or creates a new method claim.\n','PROJECT_MEMORY_PATCH.md':'PROPOSED ONLY — do not apply automatically. E13 remains INCONCLUSIVE / DESIGN-LIMITED NEGATIVE; E13a remains POST-HOC / AUDIT / NOT CLAIM-READY.\n'}.items():text('# '+name+'\n\n'+body,'reports/'+name)
source=__import__('IPython').get_ipython().history_manager.input_hist_raw[-1];require(bool(source.strip()),'current-cell source unavailable');cp=CODE/'E13a_RECOVERY_FINALIZE_ONE_CELL.py';cp.write_text(source,encoding='utf8');mirror(cp)
required_csv=['condition_latent_risk.csv','condition_support_corrected.csv','crossfit_condition_features.csv','pre_failure_rank_metrics.csv','pre_failure_calibration_metrics.csv','pre_failure_bootstrap.csv','aggregation_ladder.csv','aggregation_ladder_summary.csv','variance_decomposition.csv','support_rate_secondary.csv','original_target_oracle_ceiling.csv','oracle_gc_secondary.csv','frozen_reanalysis_criteria.csv']
required=[*[CSV/x for x in required_csv],*[PLOTS/f'{i:02d}_{name}.png' for i,name in [(1,'corrected_support_grid'),(2,'latent_failure_probability'),(3,'pfail_vs_median_Rkappa'),(4,'pfail_vs_kappa2H'),(5,'pfail_vs_kappa_max'),(6,'pfail_vs_gap'),(7,'pfail_vs_schur_sep'),(8,'pre_failure_correlations'),(9,'frozen_calibration'),(10,'aggregation_ladder_spearman'),(11,'aggregation_ladder_mse_improvement'),(12,'within_between_variance'),(13,'support_rate_vs_latent_risk'),(14,'crossfit_reproducibility'),(15,'oracle_ceiling_original_target')]],*[REPORTS/x for x in ('SCIENTIFIC_REPORT.md','DESIGN_LIMITATION_AUDIT.md','STATISTICAL_AUDIT.md','CAUSALITY_AUDIT.md','REANALYSIS_AUDIT.md','CLAIM_AUDIT.md','PROJECT_MEMORY_PATCH.md')],cp]
require(all(p.exists() and p.stat().st_size>0 for p in required),'incomplete saved artifacts')
text('# E13a recovery artifact manifest\n\n'+'\n'.join('- '+p.relative_to(ROOT).as_posix() for p in required)+'\n','ARTIFACT_MANIFEST.md')
zp=Path('/content/koopman_E13a_latent_risk_reanalysis.zip');zp.unlink(missing_ok=True);shutil.make_archive(str(zp.with_suffix('')),'zip',ROOT)
with zipfile.ZipFile(zp) as z:require(all(p.relative_to(ROOT).as_posix() in z.namelist() for p in required+[ROOT/'ARTIFACT_MANIFEST.md']),'ZIP integrity failed')
gz=Path('/content/drive/MyDrive/koopman_E13a_latent_risk_reanalysis.zip');shutil.copy2(zp,gz)
print('Recovery finalization complete; no bootstrap or ladder was recomputed.')
print('ZIP:',zp,'\nDrive ZIP:',gz)
files.download(str(zp))