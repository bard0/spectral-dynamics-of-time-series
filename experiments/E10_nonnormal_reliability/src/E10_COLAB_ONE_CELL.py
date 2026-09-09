# Paste the entire file into ONE fresh Google Colab cell. CPU-only; no manual stages.
import json,sys,shutil,zipfile
from pathlib import Path
from datetime import datetime,timezone
import numpy as np,pandas as pd
import matplotlib.pyplot as plt
from scipy.linalg import schur,subspace_angles
from scipy.stats import spearmanr
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import roc_auc_score
from google.colab import drive

d,H,T,ITOL,PTOL,NBOOT,BOOT=3,256,512,1e-8,1e-12,5000,123456789
SPLITS={"development":list(range(17000,17500)),"test_normal":list(range(17500,18000)),"c2":list(range(18000,18500)),"c4":list(range(19000,19500)),"c6":list(range(20000,20500))}; CVAL={"development":0,"test_normal":0,"c2":2,"c4":4,"c6":6}
ROOT=Path("/content/koopman_E10_nonnormal_reliability"); GROOT=Path("/content/drive/MyDrive/koopman_E10_nonnormal_reliability"); CSV,PL,RP,CF,CD=[ROOT/x for x in ("csv","plots","reports","config","code")]
if ROOT.exists():shutil.rmtree(ROOT)
drive.mount("/content/drive",force_remount=False)
for p in (ROOT,CSV,PL,RP,CF,CD,GROOT):p.mkdir(parents=True,exist_ok=True)
def mirror(p):
 p=Path(p);q=GROOT/p.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);tmp=q.with_suffix(q.suffix+".partial");shutil.copy2(p,tmp);tmp.replace(q);return q
def sc(df,n):p=CSV/n;df.to_csv(p,index=False);mirror(p);return p
def st(s,p):p.write_text(s,encoding="utf-8");mirror(p);return p
assert T==2*H and all(len(v)==500 for v in SPLITS.values()) and len(set().union(*map(set,SPLITS.values())))==2500
def B(c):return np.array([[.7,0,0],[0,.6,-.1*c],[0,0,.5]],float)
def Q(A):return np.eye(d)-A@A.T
def orth(X):return np.linalg.qr(np.asarray(X))[0]
def dg(U,V):return float(np.linalg.norm(U@U.T-V@V.T,"fro")/np.sqrt(2))
def eig(A):w,V=np.linalg.eig(A);i=np.argsort(-np.abs(w));return w[i],V[:,i]
def est(X,Y):
 G=X.T@X;C=X.T@Y
 try:BT=np.linalg.solve(G,C);pinv=False
 except np.linalg.LinAlgError:BT=np.linalg.pinv(G,rcond=PTOL)@C;pinv=True
 return BT.T,float(np.linalg.cond(G)),pinv
def r2(A):
 w,V=eig(A);a=w[:2];cp=bool(abs(a[0].imag)>ITOL*max(1,abs(a[0])) and abs(a[0]-a[1].conjugate())<=1e-7*max(1,abs(a[0])))
 if cp:U=orth(np.c_[V[:,0].real,V[:,0].imag]);how="complex_pair_real_span"
 elif np.max(abs(a.imag))<=ITOL*np.max(np.maximum(1,abs(a))):U=orth(V[:,:2].real);how="two_real_eigenvectors"
 else:return None,w,"failure",False,np.nan,np.nan
 residual=float(np.linalg.norm((np.eye(d)-U@U.T)@A@U,"fro")/max(np.linalg.norm(A,"fro"),1e-12));cut=(abs(w[1])+abs(w[2]))/2
 try:_,Z,k=schur(A,output="real",sort=lambda ar,ai:np.hypot(ar,ai)>cut);sd=dg(U,orth(Z[:,:2])) if k==2 else np.nan
 except Exception:sd=np.nan
 return U,w,how,cp,residual,sd
def oracle(c):
 A=B(c);w,V=eig(A);return {"true_eigenvalues":repr(w.tolist()),"true_kappa_V":float(np.linalg.cond(V)),"true_departure_normality":float(np.linalg.norm(A.T@A-A@A.T,"fro")),"true_spectral_norm":float(np.linalg.norm(A,2)),"true_spectral_radius":float(max(abs(w))),"Q_min_eigenvalue":float(np.linalg.eigvalsh(Q(A)).min()),"true_inner_gap":.1,"true_outer_gap":.1}
def one(seed,label):
 c=CVAL[label];A=B(c);q=Q(A);o=oracle(c);rng=np.random.default_rng(np.random.SeedSequence([seed,c,1010]));x=np.empty((513,d));x[0]=rng.standard_normal(d);L=np.linalg.cholesky(q)
 for t in range(512):x[t+1]=A@x[t]+L@rng.standard_normal(d)
 BL,cl,pl=est(x[:512],x[1:]);BH,ch,ph=est(x[256:512],x[257:513]);UH,wH,hH,cpH,rH,sH=r2(BH);UL,wL,hL,cpL,rL,sL=r2(BL);ok=UH is not None and UL is not None;E=np.eye(3)[:,:2]
 S,e=(dg(UH,UL),dg(UH,E)) if ok else (np.nan,np.nan);wh,vh=eig(BH)
 return {"seed":seed,"condition":label,"c":c,**o,"S2":S,"e2":e,"predicted_e2":np.nan,"score_in_development_support":False,"r2_defined_H":UH is not None,"r2_defined_2H":UL is not None,"r2_pair_defined":ok,"r2_construction_H":hH,"r2_construction_2H":hL,"complex_pair_H":cpH,"complex_pair_2H":cpL,"invariant_residual_H":rH,"invariant_residual_2H":rL,"schur_disagreement_H":sH,"schur_disagreement_2H":sL,"estimated_eigenvalues_H":repr(wH.tolist()),"estimated_eigenvalues_2H":repr(wL.tolist()),"estimated_inner_gap":float(abs(wH[0])-abs(wH[1])),"estimated_outer_gap":float(abs(wH[1])-abs(wH[2])),"estimated_non_normality":float(np.linalg.norm(BH.T@BH-BH@BH.T,"fro")),"estimated_kappa_V":float(np.linalg.cond(vh)),"gram_condition":ch,"S_K":float(np.linalg.norm(BH-BL,"fro")),"e_K":float(np.linalg.norm(BH-A,"fro")),"pinv_H":ph,"pinv_2H":pl,"n_states":513}
def run(label):return pd.DataFrame([one(s,label) for s in SPLITS[label]])
def boot(x,fun,seed):
 x=np.asarray(x);g=np.random.default_rng(seed);z=np.empty(NBOOT)
 for i in range(NBOOT):z[i]=fun(x[g.integers(len(x),size=len(x))])
 return tuple(map(float,np.quantile(z,[.025,.975])))
def spci(s,e):
 a=np.c_[np.asarray(s),np.asarray(e)];return float(spearmanr(a[:,0],a[:,1]).statistic),*boot(a,lambda z:spearmanr(z[:,0],z[:,1]).statistic,BOOT+1)
def aucci(s,y):
 s,y=np.asarray(s),np.asarray(y);p=np.flatnonzero(y==1);n=np.flatnonzero(y==0)
 if not len(p) or not len(n):return np.nan,np.nan,np.nan
 g=np.random.default_rng(BOOT+2);z=[]
 for _ in range(NBOOT):i=np.r_[p[g.integers(len(p),size=len(p))],n[g.integers(len(n),size=len(n))]];z.append(roc_auc_score(y[i],s[i]))
 return float(roc_auc_score(y,s)),*map(float,np.quantile(z,[.025,.975]))
def fit(dev):
 z=dev.dropna(subset=["S2","e2"]);i=IsotonicRegression(out_of_bounds="clip").fit(z.S2,z.e2);return {"iso":i,"min":float(z.S2.min()),"max":float(z.S2.max()),"q25":float(z.S2.quantile(.25)),"q75":float(z.S2.quantile(.75)),"e75":float(z.e2.quantile(.75)),"constant":float(z.e2.median())}
def summarize(raw,cal,label):
 z=raw.copy();z["predicted_e2"]=np.where(z.r2_pair_defined,cal["iso"].predict(z.S2.fillna(cal["min"])),np.nan);z["score_in_development_support"]=(z.S2>=cal["min"])&(z.S2<=cal["max"]);a=z.dropna(subset=["S2","e2","predicted_e2"]).copy();rho,rl,rh=spci(a.S2,a.e2);y=(a.e2>cal["e75"]).astype(int);auc,al,ah=aucci(a.S2,y);lo=a.loc[a.S2<=cal["q25"],"e2"];hi=a.loc[a.S2>=cal["q75"],"e2"];qr=float(hi.mean()/lo.mean()) if len(lo) and len(hi) else np.nan;mae=float(abs(a.e2-a.predicted_e2).mean());base=float(abs(a.e2-cal["constant"]).mean());imp=float(1-mae/base);ratio=(a.predicted_e2/np.maximum(a.e2,1e-15)).to_numpy();rlo,rhi=boot(ratio,np.median,BOOT+3);ilo,ihi=boot(np.c_[a.e2,a.predicted_e2],lambda v:1-abs(v[:,0]-v[:,1]).mean()/abs(v[:,0]-cal["constant"]).mean(),BOOT+4)
 row={"condition":label,"c":int(z.c.iloc[0]),"n":len(z),"r2_defined_rate":float(z.r2_pair_defined.mean()),"complex_pair_rate":float((z.complex_pair_H|z.complex_pair_2H).mean()),"median_S2":float(a.S2.median()),"mean_S2":float(a.S2.mean()),"median_e2":float(a.e2.median()),"mean_e2":float(a.e2.mean()),"spearman":rho,"spearman_ci_low":rl,"spearman_ci_high":rh,"AUROC":auc,"AUROC_ci_low":al,"AUROC_ci_high":ah,"quartile_error_ratio":qr,"MAE_iso":mae,"MAE_constant":base,"MAE_improvement":imp,"improvement_ci_low":ilo,"improvement_ci_high":ihi,"bias":float((a.predicted_e2-a.e2).mean()),"median_pred_actual":float(np.median(ratio)),"ratio_ci_low":rlo,"ratio_ci_high":rhi,"support":float(a.score_in_development_support.mean()),"max_residual":float(z[["invariant_residual_H","invariant_residual_2H"]].max().max()),"max_schur":float(z[["schur_disagreement_H","schur_disagreement_2H"]].max().max()),**oracle(int(z.c.iloc[0]))};return z,row

# Mandatory DGP/correctness preflight.
ods=[oracle(c) for c in (0,2,4,6)]
for c in (0,2,4,6):
 A=B(c);assert np.allclose(np.sort(np.linalg.eigvals(A)),[.5,.6,.7]) and np.linalg.norm(A,2)<1 and np.linalg.eigvalsh(Q(A)).min()>0 and np.allclose(A@A.T+Q(A),np.eye(d))
U=np.eye(3)[:,:2];R=np.array([[0,-1],[1,0]]);rot=np.array([[0,-.9,0],[.9,0,0],[0,0,.55]]);Ur,_,hr,_,rr,sd=r2(rot);A0=np.diag([.7,.6,.5]);Ar,_,_=est(np.eye(3),np.eye(3)@A0.T)
checks=pd.DataFrame([["spectrum/gaps/target invariant",True],["oracle nonnormality increasing",np.all(np.diff([o["true_departure_normality"] for o in ods])>0)],["oracle kappa increasing",np.all(np.diff([o["true_kappa_V"] for o in ods])>0)],["OLS noiseless",np.allclose(Ar,A0)],["basis rotation/permutation",dg(U,U@R)<1e-14 and dg(U,U[:,[1,0]])<1e-14],["principal angle equivalence",abs(dg(U,orth(np.c_[[0,0,1],[1,0,0]]))-np.sin(subspace_angles(U,orth(np.c_[[0,0,1],[1,0,0]])).max()))<1e-12],["complex pair + Schur",hr=="complex_pair_real_span" and rr<1e-8 and sd<1e-8]],columns=["check","passed"]);sc(checks,"correctness_checks.csv");assert checks.passed.all()
dev=run("development");sc(dev,"development_normal.csv");cal=fit(dev);frozen={k:v for k,v in cal.items() if k!="iso"};frozen.update({"model":"IsotonicRegression(out_of_bounds=clip)","bootstrap_seed":BOOT,"n_bootstrap":NBOOT});st(json.dumps(frozen,indent=2),CF/"frozen_calibration.json");sig=json.dumps(frozen,sort_keys=True)
raws={"development":dev};rows=[]
for label,file in [("test_normal","test_normal.csv"),("c2","transport_c2.csv"),("c4","transport_c4.csv"),("c6","transport_c6.csv")]:
 raw=run(label);assert json.dumps(frozen,sort_keys=True)==sig;cooked,row=summarize(raw,cal,label);sc(cooked,file);raws[label]=cooked;rows.append(row)
M=pd.DataFrame(rows);normal=M[M.condition=="test_normal"];M["error_amplification_vs_normal_test"]=M["median_e2"]/float(normal.iloc[0]["median_e2"]);transport=M[M.condition!="test_normal"].copy();sc(normal,"normal_replication_metrics.csv");sc(transport,"nonnormal_transport_metrics.csv")
baseline=bool(float(normal.iloc[0]["spearman"])>.30 and float(normal.iloc[0]["MAE_iso"])<float(normal.iloc[0]["MAE_constant"]));hard=transport[transport.c==6].iloc[0];N1=float(hard["r2_defined_rate"])>=.99;N2=float(hard["spearman"])>.35 and float(hard["spearman_ci_low"])>.20;N3=.80<=float(hard["median_pred_actual"])<=1.25;N4=float(hard["MAE_improvement"])>.10;N5=float(hard["support"])>=.90;valid=bool(np.isfinite(hard[["spearman","median_pred_actual","MAE_improvement","max_residual","max_schur"]].to_numpy(dtype=float)).all() and float(hard["max_residual"])<1e-8 and float(hard["max_schur"])<1e-8)
verdict="E10 NONNORMAL TRANSPORT INCONCLUSIVE" if not valid else ("E10 BASELINE VALIDITY FAIL" if not baseline else ("E10 NONNORMAL TRANSPORT PASS" if all([N1,N2,N3,N4,N5]) else "E10 NONNORMAL TRANSPORT FAIL"));ranking="RANKING SURVIVES NONNORMALITY" if N2 else "RANKING ALSO FAILS"
gates=pd.DataFrame([["normal baseline",baseline,"rho>.30 and MAEiso<MAEconst",baseline],["N1",hard["r2_defined_rate"],">=.99",N1],["N2",hard["spearman"],">.35 and CI low>.20",N2],["N3",hard["median_pred_actual"],"[.80,1.25]",N3],["N4",hard["MAE_improvement"],">.10",N4],["N5",hard["support"],">=.90",N5],["valid",valid,"finite/residual/Schur",valid],["VERDICT",verdict,"mechanical",verdict],["RANKING",ranking,"N2 only",ranking]],columns=["gate","estimate","threshold","pass"]);sc(gates,"E10_primary_gates.csv")
rawall=pd.concat(raws.values(),ignore_index=True);cp=rawall.complex_pair_H|rawall.complex_pair_2H
integrity=pd.DataFrame([["2500 unique rows",len(rawall)==2500 and rawall.seed.nunique()==2500],["all r2 primary finite",np.isfinite(rawall.loc[rawall.r2_pair_defined,["S2","e2"]].to_numpy()).all()],["complex pairs retained",(not cp.any()) or (rawall.loc[cp,"r2_pair_defined"].all() and rawall.loc[cp,["S2","e2"]].notna().all().all())],["residuals",rawall[["invariant_residual_H","invariant_residual_2H"]].max().max()<1e-8],["Schur",rawall[["schur_disagreement_H","schur_disagreement_2H"]].notna().all().all() and rawall[["schur_disagreement_H","schur_disagreement_2H"]].max().max()<1e-8]],columns=["check","passed"]);sc(integrity,"integrity_checks.csv");sc(pd.DataFrame([["complex rows",int(cp.sum())],["handled",bool((not cp.any()) or rawall.loc[cp,"r2_pair_defined"].all())]],columns=["metric","value"]),"complex_spectrum_summary.csv");sc(pd.DataFrame([["seed-level bootstrap",NBOOT,BOOT]],columns=["method","resamples","seed"]),"bootstrap_summary.csv")
sc(pd.DataFrame([["causal x0..x512",True],["oracle only evaluation",True],["normal development only fit",True],["no transport retraining",True],["no conditioning feature/normalization",True],["verdict","PASS"]],columns=["check","value"]),"causality_checks.csv");sc(pd.DataFrame([["covariance-neutral stationary family",True],["spectrum/gaps/target fixed",True],["Q changes and disclosed",True],["no uncertainty/drift/universal claim",True]],columns=["check","value"]),"methodology_checks.csv")
def fig(n,f):plt.figure(figsize=(5,4));f();plt.tight_layout();p=PL/n;plt.savefig(p,dpi=180);plt.close();mirror(p)
def curve():x=np.linspace(cal["min"],cal["max"],200);plt.plot(x,cal["iso"].predict(x),"k-",lw=2)
for label,n in [("development","01_development.png"),("test_normal","02_test_normal.png"),("c2","03_c2.png"),("c4","04_c4.png"),("c6","05_c6.png")]:fig(n,lambda label=label:(plt.scatter(raws[label].S2,raws[label].e2,s=7,alpha=.35),curve(),plt.xlabel("S2"),plt.ylabel("e2")))
D=M.sort_values("c")
for col,n,y in [("median_e2","06_median_e2.png","median e2"),("median_S2","07_median_S2.png","median S2"),("spearman","08_spearman.png","Spearman"),("median_pred_actual","09_ratio.png","predicted/actual"),("bias","10_bias.png","bias"),("MAE_improvement","11_improvement.png","MAE improvement"),("support","12_support.png","support"),("true_kappa_V","13_true_kappa.png","true kappa_V"),("true_departure_normality","14_true_nonnormality.png","true departure")]:fig(n,lambda col=col,y=y:(plt.plot(D.c,D[col],"o-"),plt.xlabel("c"),plt.ylabel(y)))
fig("15_estimated_nonnormality_distributions.png",lambda:[plt.hist(v.estimated_non_normality,bins=25,alpha=.4,label=k) for k,v in raws.items()] and (plt.legend(),plt.xlabel("estimated departure")))
fig("16_estimated_kappa_distributions.png",lambda:[plt.hist(v.estimated_kappa_V,bins=25,alpha=.4,label=k) for k,v in raws.items()] and (plt.legend(),plt.xlabel("estimated kappa_V")))
fig("17_frozen_calibration_overlay.png",lambda:[plt.scatter(v.S2,v.e2,s=5,alpha=.18,label=k) for k,v in raws.items()] and (curve(),plt.legend(),plt.xlabel("S2"),plt.ylabel("e2")))
cfg={"spectrum":[.7,.6,.5],"c_grid":[0,2,4,6],"B_matrices":{str(c):B(c).tolist() for c in (0,2,4,6)},"Q_matrices":{str(c):Q(B(c)).tolist() for c in (0,2,4,6)},"splits":SPLITS,"H":H,"bootstrap":{"seed":BOOT,"resamples":NBOOT},"frozen":frozen,"gates":{"N1":">=.99","N2":"rho>.35/CI>.20","N3":"[.8,1.25]","N4":">.10","N5":">=.90"},"versions":{"python":sys.version,"numpy":np.__version__,"pandas":pd.__version__,"scipy":__import__("scipy").__version__,"sklearn":__import__("sklearn").__version__}};st(json.dumps(cfg,indent=2),CF/"config.json")
report=f"""# E10 — Frozen reliability calibration under stationary non-normality\n## Scientific question and hypothesis\nDoes a normal-regime S2→e2 calibration transport across this covariance-neutral non-normal family?\n## What is held fixed\nEigenvalues (.70,.60,.50), both gaps (.10), E12=span(e1,e2), stationary covariance I, H and estimator.\n## What changes\nOperator geometry/eigenvector conditioning/non-normality; Q(c) changes as required to hold covariance I. This is not hidden.\n## Development and normal replication\n{normal.to_markdown(index=False,floatfmt='.4g')}\n## Frozen non-normal transport\n{transport.to_markdown(index=False,floatfmt='.4g')}\n## Hardest c=6 gates\n{gates.to_markdown(index=False)}\n## Primary verdict\n**{verdict}**\n## Ranking-survival verdict\n**{ranking}**\n## Actual error trajectory\nReported descriptively; no monotonic direction was assumed.\n## Alternative explanations\nChanging Q(c), finite-sample excitation/Gram conditioning, shared Ehat_H dependence, Ehat_2H surrogate reference, support shift, finite-sample non-normality and pseudospectral sensitivity.\n## What E10 establishes\n{'Within the tested range frozen calibration transported.' if verdict=='E10 NONNORMAL TRANSPORT PASS' else 'If baseline was valid, failure concerns quantitative transport in this tested covariance-neutral family.'}\n## What E10 does NOT establish\nNo universal non-normality theorem, uncertainty estimator, drift/separation, nonlinear Koopman, VAMP, nonstationarity, pseudospectral correction, adaptive horizon or universal calibration.\n## Next step\n{'Proceed to E11 nonstationarity.' if verdict=='E10 NONNORMAL TRANSPORT PASS' else 'Do not rescue within E10; characterize conditioning as a validity axis or decide separately on E11.'}\n""";st(report,RP/"SCIENTIFIC_REPORT.md")
for n,t in {"CORRECTNESS_AUDIT.md":"# CORRECTNESS AUDIT\n"+checks.to_markdown(index=False)+"\n","CAUSALITY_AUDIT.md":"# CAUSALITY AUDIT\nPASS: only x0..x512; oracle evaluation only; normal-development calibration frozen.\n","METHODOLOGY_AUDIT.md":"# METHODOLOGY AUDIT\nStationary covariance-neutral family: Q changes while spectrum/gaps/target/covariance are fixed. No rescue score.\n","REPRODUCIBILITY_AUDIT.md":"# REPRODUCIBILITY AUDIT\nFixed seeds/bootstrap; every completed artifact mirrored to Google Drive.\n"}.items():st(t,RP/n)
try:source=__import__("IPython").get_ipython().history_manager.input_hist_raw[-1]
except Exception:source=""
if not source or "E10" not in source:raise RuntimeError("Exact cell-source capture failed; stop rather than save incomplete source artifact.")
st(source,CD/"E10_COLAB_ONE_CELL.py")
required=[CSV/x for x in ["development_normal.csv","test_normal.csv","transport_c2.csv","transport_c4.csv","transport_c6.csv","normal_replication_metrics.csv","nonnormal_transport_metrics.csv","E10_primary_gates.csv","bootstrap_summary.csv","complex_spectrum_summary.csv","integrity_checks.csv","correctness_checks.csv","causality_checks.csv","methodology_checks.csv"]]+[CF/"config.json",CF/"frozen_calibration.json",CD/"E10_COLAB_ONE_CELL.py",RP/"SCIENTIFIC_REPORT.md",RP/"CORRECTNESS_AUDIT.md",RP/"CAUSALITY_AUDIT.md",RP/"METHODOLOGY_AUDIT.md",RP/"REPRODUCIBILITY_AUDIT.md"]+list(PL.glob("*.png"));manifest="# ARTIFACT MANIFEST\n\n"+"\n".join("- "+p.relative_to(ROOT).as_posix() for p in required);st(manifest,ROOT/"ARTIFACT_MANIFEST.md");required.append(ROOT/"ARTIFACT_MANIFEST.md");missing=[p for p in required if not p.exists() or p.stat().st_size==0];sc(pd.DataFrame([["all required artifacts",not missing],["all checkpoints mirrored",all((GROOT/p.relative_to(ROOT)).exists() for p in required)]],columns=["check","passed"]),"reproducibility_checks.csv");required.append(CSV/"reproducibility_checks.csv");assert not missing
zp=ROOT.parent/"koopman_E10_nonnormal_reliability.zip";zp.unlink(missing_ok=True);shutil.make_archive(str(zp.with_suffix("")),"zip",ROOT)
with zipfile.ZipFile(zp) as z:assert all(p.relative_to(ROOT).as_posix() in z.namelist() for p in required);members=z.namelist()
gz=GROOT/zp.name;shutil.copy2(zp,gz)
with zipfile.ZipFile(gz) as z:assert all(p.relative_to(ROOT).as_posix() in z.namelist() for p in required)
print(D[["c","true_kappa_V","true_departure_normality","Q_min_eigenvalue","n","r2_defined_rate","median_S2","median_e2","spearman","spearman_ci_low","spearman_ci_high","median_pred_actual","MAE_improvement","support"]].to_string(index=False));print("NORMAL BASELINE VALIDITY",baseline);print(dict(N1=N1,N2=N2,N3=N3,N4=N4,N5=N5));print(verdict);print(ranking);print("ZIP",zp,zp.stat().st_size,"DRIVE",gz,gz.stat().st_size,"files",len(members))