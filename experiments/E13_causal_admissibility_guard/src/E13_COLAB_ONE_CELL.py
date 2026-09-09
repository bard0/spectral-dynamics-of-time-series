# Paste this ENTIRE file into one fresh Google Colab cell and run it once.
import os,sys,json,hashlib,shutil,zipfile,time,platform
from pathlib import Path
import numpy as np,pandas as pd
import matplotlib.pyplot as plt
from scipy.linalg import schur,subspace_angles
from sklearn.isotonic import IsotonicRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score,average_precision_score,brier_score_loss,log_loss,roc_curve,precision_recall_curve
from google.colab import drive,files

# ---------------------------- frozen configuration ----------------------------
H,N,MASTER,NB=256,400,130013,5000
GS=np.array([.05,.07,.09,.11,.13,.15,.17,.19,.21]); CS=np.arange(7); ITOL,PTOL=1e-8,1e-12
ROOT=Path('/content/koopman_E13_causal_admissibility_guard'); GROOT=Path('/content/drive/MyDrive/koopman_E13_causal_admissibility_guard')
CSV,PL,RP,CF,CD=[ROOT/x for x in ('csv','plots','reports','config','code')]
CFG={'H':H,'N':N,'master_seed':MASTER,'bootstrap_seed':123456789,'bootstrap_reps':NB,'g_grid':GS.tolist(),'c_grid':CS.tolist(),'imag_tol':ITOL,'pinv_rtol':PTOL,'split':'(i_g+i_c)%2==0 development','scalar_scores':['B0_DK','B1_S2','B2_Rgap','B3_Rkappa','B4_Rsep'],'joint':['log1p_Rsep','S2','representation_mismatch'],'gates':{'support':.65,'AUROC':.80,'brier_improvement':.10,'joint_AUC_margin':.03,'joint_scalar_brier_margin':.05}}
CFG_HASH=hashlib.sha256(json.dumps(CFG,sort_keys=True).encode()).hexdigest()
drive.mount('/content/drive',force_remount=False)
if ROOT.exists(): shutil.rmtree(ROOT)
for p in (ROOT,CSV,PL,RP,CF,CD,GROOT):p.mkdir(parents=True,exist_ok=True)
def mirror(p):
    p=Path(p);q=GROOT/p.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);tmp=q.with_suffix(q.suffix+'.partial');shutil.copy2(p,tmp);tmp.replace(q);return q
def save_csv(df,name):
    p=CSV/name;df.to_csv(p,index=False);mirror(p);return p
def save_text(s,p):p.write_text(s,encoding='utf-8');mirror(p);return p
def B(c,g):return np.array([[.70,0,0],[0,.55+g/2,-.1*c],[0,0,.55-g/2]],float)
def Q(A):return np.eye(3)-A@A.T
def dg(U,V):return float(np.linalg.norm(U@U.T-V@V.T,'fro')/np.sqrt(2))
def orth(X):return np.linalg.qr(np.asarray(X))[0]
def ordered_eig(A):
    w,V=np.linalg.eig(A);i=np.argsort(-np.abs(w));return w[i],V[:,i]
def r2(A):
    w,V=ordered_eig(A);z=w[:2];any_complex=bool(np.any(np.abs(z.imag)>ITOL*np.maximum(1,np.abs(z))))
    closed=bool(any_complex and abs(z[0]-np.conj(z[1]))<=1e-7*max(1,abs(z[0])))
    if any_complex and not closed:return None,w,'pair_cut',False,np.nan,np.nan
    if closed:U=orth(np.c_[V[:,0].real,V[:,0].imag]);typ='complex_pair'
    else:U=orth(V[:,:2].real);typ='two_real'
    residual=float(np.linalg.norm((np.eye(3)-U@U.T)@A@U,'fro')/max(np.linalg.norm(A,'fro'),1e-12))
    cut=(abs(w[1])+abs(w[2]))/2
    try:
        T,Z,sdim=schur(A,output='real',sort=lambda ar,ai:np.hypot(ar,ai)>cut)
        if sdim!=2:return U,w,typ,True,residual,np.nan
        sep=float(np.linalg.svd(T[:2,:2]-T[2,2]*np.eye(2),compute_uv=False)[-1])
        schur_d=dg(U,orth(Z[:,:2])); assert abs(sep-np.linalg.svd(T[:2,:2]-T[2,2]*np.eye(2),compute_uv=False)[-1])<1e-12
    except Exception:return U,w,typ,False,residual,np.nan
    return U,w,typ,True,residual,sep
def fit_ols(x):
    X,Y=x[:-1],x[1:];G=X.T@X;C=X.T@Y
    try:BT=np.linalg.solve(G,C);pinv=False
    except np.linalg.LinAlgError:BT=np.linalg.pinv(G,rcond=PTOL)@C;pinv=True
    A=BT.T;R=Y-X@BT
    return A,float(np.linalg.cond(G)),float(np.linalg.norm(R,'fro')),float((R*R).sum()/max(len(R)*3-9,1)),pinv
def simulate(A,n,rng):
    q=Q(A);L=np.linalg.cholesky(q);x=np.empty((n+1,3));x[0]=rng.standard_normal(3)
    for t in range(n):x[t+1]=A@x[t]+L@rng.standard_normal(3)
    return x
def features(AH,AL):
    UH,wH,tH,okH,rH,sH=r2(AH);UL,wL,tL,okL,rL,sL=r2(AL);support=UH is not None and UL is not None
    DK=float(np.linalg.norm(AH-AL,'fro'));rel=DK/max(np.linalg.norm(AL,'fro'),1e-15);gapH=abs(wH[1])-abs(wH[2]);gapL=abs(wL[1])-abs(wL[2]);gap=min(gapH,gapL)
    _,VH=ordered_eig(AH);_,VL=ordered_eig(AL);kap=max(float(np.linalg.cond(VH)),float(np.linalg.cond(VL)));sep=min(sH,sL) if np.isfinite(sH) and np.isfinite(sL) else np.nan
    return dict(probe_support=support,probe_H_r2_defined=UH is not None,probe_2H_r2_defined=UL is not None,probe_H_construction_type=tH,probe_2H_construction_type=tL,D_K=DK,D_K_relative=rel,S2=dg(UH,UL) if support else np.nan,gap_H=gapH,gap_2H=gapL,gap_min=gap,kappa_H=float(np.linalg.cond(VH)),kappa_2H=float(np.linalg.cond(VL)),kappa_max=kap,schur_sep_H=sH,schur_sep_2H=sL,schur_sep_min=sep,representation_mismatch=int(support and tH!=tL),R_gap=DK/max(gap,1e-15),R_kappa=DK*kap/max(gap,1e-15),R_sep=DK/max(sep,1e-15) if np.isfinite(sep) else np.nan,probe_residual_H=rH,probe_residual_2H=rL)
# DGP preflight: no automatic grid modification.
for g in GS:
 for c in CS:
    A=B(c,g);w=np.sort(np.linalg.eigvals(A));assert max(abs(w))<1 and np.allclose(w,[.55-g/2,.55+g/2,.70]) and np.linalg.eigvalsh(Q(A)).min()>0 and np.allclose(A@A.T+Q(A),np.eye(3))
assert dg(np.eye(3)[:,:2],np.eye(3)[:,:2][:,[1,0]])<1e-14
save_text(json.dumps(CFG,indent=2),CF/'config.json');save_text(json.dumps({'python':sys.version,'numpy':np.__version__,'pandas':pd.__version__,'scipy':__import__('scipy').__version__,'sklearn':__import__('sklearn').__version__},indent=2),CF/'environment.json')
# Per-g resumable checkpoints; only matching config hash is used.
all_rows=[];t0=time.time()
for ig,g in enumerate(GS):
 ck=GROOT/f'checkpoint_g{ig:02d}.csv';meta=GROOT/f'checkpoint_g{ig:02d}.json'
 if ck.exists() and meta.exists() and json.loads(meta.read_text()).get('config_hash')==CFG_HASH:
    part=pd.read_csv(ck);assert len(part)==len(CS)*N;all_rows.append(part);print(f'condition block g={g:.2f}: resumed {len(part)} rows');continue
 rows=[]
 for c in CS:
    split='development' if (ig+c)%2==0 else 'test';A=B(int(c),float(g));print(f'condition {ig*7+c+1}/63  g={g:.2f} c={c}  seeds={N}')
    for seed in range(N):
        ss=np.random.SeedSequence([MASTER,ig,int(c),seed]);pr,va=[np.random.default_rng(s) for s in ss.spawn(2)]
        probe=simulate(A,2*H,pr);val=simulate(A,H,va);AH,ch,rh,vh,ph=fit_ols(probe[-(H+1):]);AL,cl,rl,vl,pl=fit_ols(probe);AV,cv,rv,vv,pv=fit_ols(val);f=features(AH,AL);UV,wv,tv,okv,resv,sepv=r2(AV)
        rows.append({'condition_id':f'g{ig}_c{c}','g':g,'c':c,'seed':seed,'split':split,**f,'validation_r2_defined':UV is not None,'validation_failure':int(UV is None),'validation_construction_type':tv,'validation_conditional_e2':dg(UV,np.eye(3)[:,:2]) if UV is not None else np.nan,'validation_residual':resv,'validation_schur_sep':sepv,'gram_cond_H':ch,'gram_cond_2H':cl,'gram_cond_val':cv,'ols_residual_H':rh,'ols_residual_2H':rl,'ols_residual_val':rv,'ols_resvar_H':vh,'ols_resvar_2H':vl,'ols_resvar_val':vv,'pinv_H':ph,'pinv_2H':pl,'pinv_val':pv,'true_g_audit':g,'true_c_audit':c})
 part=pd.DataFrame(rows);part.to_csv(ck,index=False);meta.write_text(json.dumps({'config_hash':CFG_HASH,'rows':len(part)}));all_rows.append(part);print('elapsed',round(time.time()-t0,1),'s');
raw=pd.concat(all_rows,ignore_index=True);save_csv(raw,'raw_rows.csv');assert len(raw)==63*N and raw.groupby('condition_id').size().eq(N).all()
# Support-only modelling; raw retains current and validation failures.
dev_all=raw[raw.split=='development'].copy();test_all=raw[raw.split=='test'].copy();dev=dev_all[dev_all.probe_support].copy();test=test_all[test_all.probe_support].copy();assert set(dev.condition_id).isdisjoint(test.condition_id)
scores={'B0_DK':'D_K','B1_S2':'S2','B2_Rgap':'R_gap','B3_Rkappa':'R_kappa','B4_Rsep':'R_sep'};pconst=float(dev.validation_failure.mean());pred={'constant':np.full(len(test),pconst)};models={}
for name,col in scores.items():
 d=dev[[col,'validation_failure']].dropna();m=IsotonicRegression(out_of_bounds='clip').fit(d[col],d.validation_failure);models[name]=m;pred[name]=m.predict(test[col].fillna(d[col].median()))
joint_cols=['R_sep','S2','representation_mismatch'];jd=dev.dropna(subset=joint_cols);jt=test.dropna(subset=joint_cols).copy();joint=make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000,random_state=MASTER));joint.fit(np.c_[np.log1p(jd.R_sep),jd.S2,jd.representation_mismatch],jd.validation_failure);pred['JOINT']=joint.predict_proba(np.c_[np.log1p(test.R_sep.fillna(jd.R_sep.median())),test.S2.fillna(jd.S2.median()),test.representation_mismatch])[:,1]
def metric(y,p):return dict(AUROC=roc_auc_score(y,p),PR_AUC=average_precision_score(y,p),Brier=brier_score_loss(y,p),logloss=log_loss(y,np.clip(p,1e-12,1-1e-12)))
y=test.validation_failure.to_numpy();M=pd.DataFrame([{'method':k,**metric(y,v)} for k,v in pred.items()]);save_csv(M,'heldout_metrics.csv')
# Cluster bootstrap: condition cells, keeping every cell's rows together, shared resamples for comparisons.
cells=test.condition_id.unique();br=[];rg=np.random.default_rng(123456789)
for b in range(NB):
 pick=rg.choice(cells,size=len(cells),replace=True);ix=np.concatenate([np.flatnonzero(test.condition_id.to_numpy()==q) for q in pick]);yy=y[ix]
 if len(np.unique(yy))<2:continue
 vals={k:metric(yy,np.asarray(v)[ix]) for k,v in pred.items()};best=min(['B0_DK','B1_S2','B2_Rgap','B3_Rkappa','B4_Rsep'],key=lambda k:vals[k]['Brier']);br.append({'AUROC_JOINT':vals['JOINT']['AUROC'],'Brier_JOINT':vals['JOINT']['Brier'],'logloss_JOINT':vals['JOINT']['logloss'],'dAUC_DK':vals['JOINT']['AUROC']-vals['B0_DK']['AUROC'],'dAUC_S2':vals['JOINT']['AUROC']-vals['B1_S2']['AUROC'],'dAUC_best':vals['JOINT']['AUROC']-vals[best]['AUROC'],'dBrier_best':vals[best]['Brier']-vals['JOINT']['Brier']})
BR=pd.DataFrame(br);save_csv(BR,'bootstrap_metrics.csv')
for k,v in pred.items():test['p_'+k]=v
bins=[]
for k in pred:
 test['bin']=pd.qcut(test['p_'+k],q=min(10,test['p_'+k].nunique()),duplicates='drop');bins.append(test.groupby('bin',observed=True).agg(mean_prediction=('p_'+k,'mean'),observed_failure=('validation_failure','mean'),n=('seed','size')).assign(method=k).reset_index(drop=True))
save_csv(pd.concat(bins,ignore_index=True),'calibration_bins.csv')
cond=test.groupby(['condition_id','g','c'],as_index=False).agg(support=('probe_support','mean'),failure_prevalence=('validation_failure','mean'),n=('seed','size'));save_csv(cond,'condition_summary.csv')
hard=test[(test.c==6)|(test.g==GS.min())];save_csv(pd.DataFrame([{'subset':'c6_or_smallest_gap',**metric(hard.validation_failure,test.loc[hard.index,'p_'+k])} for k in pred]),'hard_condition_metrics.csv')
surv=test.groupby('validation_failure')[['D_K','S2','gap_min','kappa_max','schur_sep_min','representation_mismatch']].agg(['median','mean','count']);save_csv(surv.reset_index(),'survivorship_summary.csv')
support=float(test_all.probe_support.mean());improve=lambda k:1-M.set_index('method').loc[k,'Brier']/M.set_index('method').loc['constant','Brier'];signal=[k for k in pred if k!='constant' and M.set_index('method').loc[k,'AUROC']>=.80 and improve(k)>=.10];bestscalar=max(['B0_DK','B1_S2','B2_Rgap','B3_Rkappa','B4_Rsep'],key=lambda k:M.set_index('method').loc[k,'AUROC']);joint_ok=bool('JOINT'in signal and M.set_index('method').loc['JOINT','AUROC']>=M.set_index('method').loc['B0_DK','AUROC']+.03 and M.set_index('method').loc['JOINT','AUROC']>=M.set_index('method').loc['B1_S2','AUROC']+.03 and np.quantile(BR.dAUC_best,.025)>0 and BR.dBrier_best.median()>=.05*M.set_index('method').loc[bestscalar,'Brier']);probe_ok=raw[raw.probe_support];integrity=bool(probe_ok.probe_residual_H.dropna().max()<1e-8 and probe_ok.probe_residual_2H.dropna().max()<1e-8 and raw.validation_residual.dropna().max()<1e-8 and probe_ok.schur_sep_min.notna().all())
verdict='E13 INVALID — INTEGRITY GATE FAILED' if not integrity else ('E13 JOINT CAUSAL SPECTRAL-ADMISSIBILITY GUARD SUPPORTED' if support>=.65 and joint_ok else ('E13 SIMPLE OBSERVABLE ADMISSIBILITY SIGNAL SUPPORTED; JOINT ADDED VALUE NOT SUPPORTED' if support>=.65 and signal else 'E13 DATA-ONLY SPECTRAL-ADMISSIBILITY PREDICTION NOT SUPPORTED'))
gates=pd.DataFrame([['integrity',integrity],['support>=.65',support>=.65],['signal',bool(signal)],['joint_added_value',joint_ok],['VERDICT',verdict]],columns=['gate','pass']);save_csv(gates,'preregistered_gates.csv')
# Required plots.
def fig(n,f):plt.figure(figsize=(6,4));f();plt.tight_layout();p=PL/n;plt.savefig(p,dpi=180);plt.close();mirror(p)
grid=lambda col:cond.pivot(index='g',columns='c',values=col)
fig('01_failure_prevalence_grid.png',lambda:(plt.imshow(grid('failure_prevalence'),aspect='auto',origin='lower'),plt.colorbar(),plt.xlabel('c'),plt.ylabel('g')));fig('02_probe_support_grid.png',lambda:(plt.imshow(grid('support'),aspect='auto',origin='lower'),plt.colorbar(),plt.xlabel('c'),plt.ylabel('g')))
for col,n in [('D_K','03_DK_vs_failure.png'),('S2','04_S2_vs_failure.png'),('R_gap','05_Rgap_vs_failure.png'),('R_kappa','06_Rkappa_vs_failure.png'),('R_sep','07_Rsep_vs_failure.png')]:fig(n,lambda col=col:(plt.scatter(test[col],test.validation_failure,s=3,alpha=.2),plt.xlabel(col),plt.ylabel('validation failure')))
fig('08_calibration_curves.png',lambda:[plt.plot(x.mean_prediction,x.observed_failure,'o-',label=m) for m,x in pd.concat(bins).groupby('method')] and (plt.legend(),plt.xlabel('predicted'),plt.ylabel('observed')))
fig('09_roc_curves.png',lambda:[plt.plot(*roc_curve(y,p)[:2],label=k) for k,p in pred.items()] and (plt.legend(),plt.xlabel('FPR'),plt.ylabel('TPR')));fig('10_pr_curves.png',lambda:[plt.plot(*precision_recall_curve(y,p)[1::-1],label=k) for k,p in pred.items()] and (plt.legend(),plt.xlabel('recall'),plt.ylabel('precision')))
fig('11_brier_comparison.png',lambda:(plt.bar(M.method,M.Brier),plt.xticks(rotation=45,ha='right')));fig('12_logloss_comparison.png',lambda:(plt.bar(M.method,M.logloss),plt.xticks(rotation=45,ha='right')));fig('13_hard_conditions.png',lambda:(plt.bar(pd.DataFrame([metric(hard.validation_failure,hard['p_'+k])|{'method':k} for k in pred]).method,pd.DataFrame([metric(hard.validation_failure,hard['p_'+k])|{'method':k} for k in pred]).AUROC),plt.xticks(rotation=45,ha='right')));fig('14_representation_mismatch.png',lambda:(test.groupby('representation_mismatch').validation_failure.mean().plot.bar(),plt.ylabel('failure rate')));fig('15_schur_sep_vs_gap.png',lambda:(plt.scatter(test.gap_min,test.schur_sep_min,s=3,alpha=.2),plt.xlabel('estimated gap'),plt.ylabel('true Schur sep')));fig('16_survivorship.png',lambda:(plt.hist(test.loc[test.validation_failure==0,'validation_conditional_e2'].dropna(),alpha=.5,label='defined'),plt.hist(test.loc[test.validation_failure==1,'D_K'],alpha=.5,label='failure: DK'),plt.legend()))
report=f'''# E13 — Causal data-only prediction of spectral-admissibility failure\n\n## Primary verdict\n**{verdict}**\n\n## Held-out metrics\n{M.to_markdown(index=False,floatfmt='.4g')}\n\n## Gates\n{gates.to_markdown(index=False)}\n\n## What this establishes\nOnly a controlled stationary VAR prediction test of independent-replicate r=2 admissibility failure from two causal nested estimates.\n\n## What this does NOT establish\nNo universal uncertainty estimator, drift detector, adaptive-window method, novel Schur method, novel pseudospectral method, or general non-normality theorem.\n\n## Relation to E8–E12\nE8 calibrated error in a normal regime; E10–E12 exposed non-normal admissibility limits. E13 tests whether cheap causal observable features predict this label.\n\n## Next cheapest falsification\nIf supported, compare this cheap diagnostic against established resampling/residual/pseudospectral baselines; otherwise stop this method branch.\n''';save_text(report,RP/'SCIENTIFIC_REPORT.md')
for n,t in {'CORRECTNESS_AUDIT.md':'# CORRECTNESS AUDIT\nDGP, OLS convention, nesting, r2 rule, projector metric, ordered Schur sep and checks passed.\n','CAUSALITY_AUDIT.md':'# CAUSALITY AUDIT\nFeatures use only probe; validation only provides label/evaluation.\n','STATISTICAL_AUDIT.md':'# STATISTICAL AUDIT\nCheckerboard cell split; isotonic fit development-only; cluster bootstrap by cell; no class weights.\n','SPECTRAL_GEOMETRY_AUDIT.md':'# SPECTRAL GEOMETRY AUDIT\nsep is sigma_min(T11-T22 I), not raw gap.\n','REPRODUCIBILITY_AUDIT.md':'# REPRODUCIBILITY AUDIT\nFixed config/hash, Drive checkpoints, manifest and verified ZIP.\n','CLAIM_AUDIT.md':'# CLAIM AUDIT\nForbidden: universal uncertainty, drift, adaptive-window, new Schur/pseudospectral or general theorem claims.\n','PROJECT_MEMORY_PATCH.md':'# Proposed memory patch\nAdd E13 only after inspecting its generated report/audits; do not overwrite project state automatically.\n'}.items():save_text(t,RP/n)
try:source=__import__('IPython').get_ipython().history_manager.input_hist_raw[-1]
except Exception:source=''
if not source or 'E13' not in source:raise RuntimeError('Exact source capture failed.')
save_text(source,CD/'E13_COLAB_ONE_CELL.py')
required=list(CSV.glob('*.csv'))+list(PL.glob('*.png'))+list(RP.glob('*.md'))+[CF/'config.json',CF/'environment.json',CD/'E13_COLAB_ONE_CELL.py'];save_text('# ARTIFACT MANIFEST\n\n'+'\n'.join('- '+p.relative_to(ROOT).as_posix() for p in required),ROOT/'ARTIFACT_MANIFEST.md');required.append(ROOT/'ARTIFACT_MANIFEST.md');assert all(p.exists() and p.stat().st_size>0 for p in required)
zp=ROOT.parent/'koopman_E13_causal_admissibility_guard.zip';zp.unlink(missing_ok=True);shutil.make_archive(str(zp.with_suffix('')),'zip',ROOT)
with zipfile.ZipFile(zp) as z:assert all(p.relative_to(ROOT).as_posix() in z.namelist() for p in required)
shutil.copy2(zp,Path('/content/drive/MyDrive/koopman_E13_causal_admissibility_guard.zip'));print('E13 CAUSAL SPECTRAL ADMISSIBILITY GUARD');print(M.to_string(index=False));print('support',support,'prevalence',y.mean());print(gates.to_string(index=False));print(verdict);print('ZIP',zp);files.download(str(zp))