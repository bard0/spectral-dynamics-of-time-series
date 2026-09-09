# ONE standalone Google Colab cell; CPU-only, matched-direction E12.
import json,sys,shutil,zipfile,hashlib
from pathlib import Path
import numpy as np,pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score,log_loss
from google.colab import drive
GAPS=np.array([.05,.075,.10,.15,.20]); HS=np.array([0,.1,.2,.4,.6]); EPS=np.array([.001,.002,.005,.01,.02,.04,.08,.12,.16,.20]); CS=np.array([0,2,4,6]);N2,N3,BOOT=10000,5000,123456789
ROOT=Path('/content/koopman_E12_conditioning_scaling');GROOT=Path('/content/drive/MyDrive/koopman_E12_conditioning_scaling');CSV,PL,RP,CF,CD=[ROOT/x for x in ('csv','plots','reports','config','code')]
if ROOT.exists():shutil.rmtree(ROOT)
drive.mount('/content/drive',force_remount=False)
for p in (ROOT,CSV,PL,RP,CF,CD,GROOT):p.mkdir(parents=True,exist_ok=True)
def mir(p):p=Path(p);q=GROOT/p.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
def sc(x,n):p=CSV/n;x.to_csv(p,index=False);mir(p);return p
def st(x,p):p.write_text(x,encoding='utf8');mir(p)
def cond2(g,h):return np.linalg.cond(np.array([[1,-h/g],[0,1.]]))
def B(c,g):return np.array([[.7,0,0],[0,.55+g/2,-.1*c],[0,0,.55-g/2]])
def eig(A):w,V=np.linalg.eig(A);i=np.argsort(-np.abs(w));return w[i],V[:,i]
def orth(X):return np.linalg.qr(X)[0]
def dg(U,V):return float(np.linalg.norm(U@U.T-V@V.T,'fro')/np.sqrt(2))
def sub(A):
 w,V=eig(A);z=w[:2];complex_=np.any(abs(z.imag)>1e-8);closed=complex_ and abs(z[0]-z[1].conjugate())<1e-7*max(1,abs(z[0]))
 if complex_ and not closed:return None,w,'pair_cut',complex_,closed,np.nan
 U=orth(np.c_[V[:,0].real,V[:,0].imag]) if closed else orth(V[:,:2].real);r=np.linalg.norm((np.eye(3)-U@U.T)@A@U,'fro')/max(np.linalg.norm(A,'fro'),1e-12);return U,w,'complex_pair' if closed else 'real',complex_,closed,r
rng=np.random.default_rng(120012);D2=rng.standard_normal((N2,2,2));D2/=np.linalg.norm(D2.reshape(N2,-1),axis=1)[:,None,None];D3=rng.standard_normal((N3,3,3));D3/=np.linalg.norm(D3.reshape(N3,-1),axis=1)[:,None,None]
# Part A exact discriminant (no eigensolver truth variable).
pa=[]
for g in GAPS:
 for h in HS:
  k=cond2(g,h)
  for e in EPS:
   d=D2;disc=(g+e*(d[:,0,0]-d[:,1,1]))**2+4*(-h+e*d[:,0,1])*e*d[:,1,0]
   pa.append(pd.DataFrame({'seed':np.arange(N2),'g':g,'h':h,'epsilon':e,'kappa_boundary':k,'eta':h*e/g**2,'rho':k*e/g,'discriminant':disc,'complexified':disc<0,'d21':d[:,1,0]}))
PA=pd.concat(pa,ignore_index=True);sc(PA,'partA_exact_rows.csv');AA=PA.groupby(['g','h','epsilon'],as_index=False).agg(complex_probability=('complexified','mean'),eta=('eta','first'),rho=('rho','first'));sc(AA,'partA_aggregated.csv')
# Part B fixed split of entire (g,c) cells: parity development, remainder held-out.
dev={(g,c) for i,g in enumerate(GAPS) for j,c in enumerate(CS) if (i+j)%2==0};pb=[];E=np.eye(3)[:,:2]
for g in GAPS:
 for c in CS:
  A=B(c,g);w,V=eig(A);assert np.allclose(np.sort(w),[.55-g/2,.55+g/2,.7]) and .7>(.55+g/2)
  kv=float(np.linalg.cond(V));nn=float(np.linalg.norm(A.T@A-A@A.T,'fro'));sep=g # exact triangular boundary eigenvalue separation
  for e in EPS:
   for j in range(N3):
    T=A+e*D3[j];U,we,typ,co,cl,res=sub(T);defined=U is not None
    pb.append({'seed':j,'g':g,'c':c,'epsilon':e,'split':'development' if (g,c) in dev else 'test','kappa_boundary':cond2(g,.1*c),'kappa_V':kv,'departure_normality':nn,'sep':sep,'eta':.1*c*e/g**2,'rho':cond2(g,.1*c)*e/g,'perturbation_fro':np.linalg.norm(e*D3[j]),'direction_hash':hashlib.sha256(D3[j].tobytes()).hexdigest(),'r2_defined':defined,'undefined':not defined,'complex_top2':co,'conjugation_closed':cl,'construction':typ,'e2':dg(U,E) if defined else np.nan,'e2_over_epsilon':dg(U,E)/e if defined else np.nan,'residual':res,'d21':D3[j,2,1]})
 PB=pd.DataFrame(pb);pb=[];sc(PB,f'partB_through_g{g:.3f}_c{c}.csv')
PB=pd.concat([pd.read_csv(p) for p in CSV.glob('partB_through_*.csv')],ignore_index=True);assert len(PB)==len(GAPS)*len(CS)*len(EPS)*N3 and PB.groupby(['seed','g','epsilon']).direction_hash.nunique().eq(1).all();sc(PB,'partB_raw_rows.csv')
AG=PB.groupby(['g','c','epsilon'],as_index=False).agg(r2_defined_rate=('r2_defined','mean'),undefined_rate=('undefined','mean'),complexification_rate=('complex_top2','mean'),median_e2=('e2','median'),p90_e2=('e2',lambda x:x.quantile(.9)),p95_e2=('e2',lambda x:x.quantile(.95)),eta=('eta','first'),rho=('rho','first'),kappa_boundary=('kappa_boundary','first'),kappa_V=('kappa_V','first'),departure_normality=('departure_normality','first'),sep=('sep','first'));sc(AG,'partB_aggregated.csv')
# Frozen simple logistic models; all fits use development cells only. M5 is preregistered primary.
features={'M0_epsilon':['epsilon'],'M1_eps_over_g':['epsilon','g'],'M2_eps_over_g2':['epsilon','g'],'M3_c_eps_over_g':['c','epsilon','g'],'M4_c_eps_over_g2':['c','epsilon','g'],'M5_kappa_eps_over_g':['rho'],'M6_sep_normalized':['epsilon','sep']}
def X(z,name):
 if name=='M1_eps_over_g':return (z.epsilon/z.g).to_numpy()[:,None]
 if name=='M2_eps_over_g2':return (z.epsilon/z.g**2).to_numpy()[:,None]
 if name=='M3_c_eps_over_g':return (z.c*z.epsilon/z.g).to_numpy()[:,None]
 if name=='M4_c_eps_over_g2':return (z.c*z.epsilon/z.g**2).to_numpy()[:,None]
 if name=='M6_sep_normalized':return (z.epsilon/z.sep).to_numpy()[:,None]
 return z[features[name]].to_numpy()
devrows=PB[PB.split.eq('development')];testrows=PB[PB.split.eq('test')];mets=[];coefs=[]
for name in features:
 m=LogisticRegression(max_iter=300,class_weight='balanced',random_state=BOOT).fit(X(devrows,name),devrows.undefined);p=m.predict_proba(X(testrows,name))[:,1];mets.append({'model':name,'AUROC':roc_auc_score(testrows.undefined,p),'logloss':log_loss(testrows.undefined,p),'monotone_coefficient':float(m.coef_[0,0])});coefs.append({'model':name,'intercept':float(m.intercept_[0]),'coef':repr(m.coef_.tolist())})
MET=pd.DataFrame(mets);sc(MET,'heldout_model_metrics.csv');sc(pd.DataFrame(coefs),'model_coefficients.csv');m5=MET.set_index('model').loc['M5_kappa_eps_over_g'];simple=MET[MET.model.isin(['M0_epsilon','M1_eps_over_g','M2_eps_over_g2','M3_c_eps_over_g','M4_c_eps_over_g2'])];passgate=bool(m5.AUROC>=.80 and m5.logloss<simple.logloss.min() and m5.monotone_coefficient>0 and MET.AUROC.max()==m5.AUROC);verdict='E12 CONDITIONING-NORMALIZED SPECTRAL-ADMISSIBILITY SCALING SUPPORTED' if passgate else 'E12 CONDITIONING-SCALING HYPOTHESIS NOT SUPPORTED';sc(pd.DataFrame([['M5 heldout AUROC>=.80',m5.AUROC>=.80],['M5 lower logloss than simpler',m5.logloss<simple.logloss.min()],['M5 monotone',m5.monotone_coefficient>0],['M5 best preregistered AUROC',MET.AUROC.max()==m5.AUROC],['VERDICT',verdict]],columns=['gate','pass']),'preregistered_gates.csv')
def fig(n,f):plt.figure(figsize=(6,4));f();plt.tight_layout();p=PL/n;plt.savefig(p,dpi=180);plt.close();mir(p)
fig('partA_collapse_eta.png',lambda:(plt.scatter(AA.eta,AA.complex_probability,s=5),plt.xscale('log'),plt.xlabel('eta'),plt.ylabel('complexification probability')));fig('partA_collapse_rho.png',lambda:(plt.scatter(AA.rho,AA.complex_probability,s=5),plt.xscale('log'),plt.xlabel('rho'),plt.ylabel('complexification probability')))
for col,n in [('r2_defined_rate','heat_defined.png'),('median_e2','heat_median_e2.png'),('p95_e2','heat_p95_e2.png')]:fig(n,lambda col=col:(plt.imshow(AG.pivot_table(index='epsilon',columns='c',values=col,aggfunc='mean'),aspect='auto',origin='lower'),plt.colorbar(label=col),plt.xlabel('c'),plt.ylabel('epsilon')))
fig('heldout_auroc.png',lambda:(plt.bar(MET.model,MET.AUROC),plt.xticks(rotation=45,ha='right'),plt.ylabel('held-out AUROC')));fig('survivorship_d21.png',lambda:(plt.hist(PB[PB.r2_defined].d21,bins=60,alpha=.5,label='defined'),plt.hist(PB[PB.undefined].d21,bins=60,alpha=.5,label='undefined'),plt.legend(),plt.xlabel('boundary lower-left D component')))
cfg={'gaps':GAPS.tolist(),'h':HS.tolist(),'c':CS.tolist(),'eps':EPS.tolist(),'N2':N2,'N3':N3,'development_cells':sorted(map(lambda x:[float(x[0]),int(x[1])],dev)),'heldout_cells':sorted(map(lambda x:[float(x[0]),int(x[1])],set((g,c) for g in GAPS for c in CS)-dev)),'models':list(features),'primary':'M5 kappa*epsilon/g','bootstrap_unit':'matched perturbation seed'};st(json.dumps(cfg,indent=2),CF/'config.json');st(json.dumps({'python':sys.version,'numpy':np.__version__,'sklearn':__import__('sklearn').__version__},indent=2),CF/'environment.json')
st(f'# E12 Conditioning Scaling\n\n**{verdict}**\n\nPart A uses the exact discriminant. Part B uses matched directions and held-out condition cells. Standard condition numbers/Schur separation are diagnostics, not novelty or a reliability method. Conditional e2 and D21 selection are reported as survivorship diagnostics.\n',RP/'SCIENTIFIC_REPORT.md')
for n,t in {'CORRECTNESS_AUDIT.md':'# Correctness\nExact discriminant, matched directions and base spectra asserted.\n','METHODOLOGY_AUDIT.md':'# Methodology\nHeld-out split is by whole (g,c) cells; no post-hoc model selection.\n','STATISTICAL_AUDIT.md':'# Statistical\nNo row-wise condition leakage; models are simple logistic regressions.\n','SPECTRAL_GEOMETRY_AUDIT.md':'# Spectral geometry\nPair cut is primary outcome and undefined rows are retained.\n','CLAIM_AUDIT.md':'# Claim audit\nNo universal theorem or reliability-method claim.\n'}.items():st(t,RP/n)
try:src=__import__('IPython').get_ipython().history_manager.input_hist_raw[-1]
except:src=''
if not src or 'E12' not in src:raise RuntimeError('source capture failed')
st(src,CD/'E12_COLAB_ONE_CELL.py');req=[CF/'config.json',CF/'environment.json',CD/'E12_COLAB_ONE_CELL.py',RP/'SCIENTIFIC_REPORT.md']+list(RP.glob('*AUDIT.md'))+list(CSV.glob('*'))+list(PL.glob('*'));st('# ARTIFACT MANIFEST\n\n'+'\n'.join('- '+p.relative_to(ROOT).as_posix() for p in req),ROOT/'ARTIFACT_MANIFEST.md');req.append(ROOT/'ARTIFACT_MANIFEST.md');assert all(p.stat().st_size>0 for p in req);zp=ROOT.parent/'koopman_E12_conditioning_scaling.zip';zp.unlink(missing_ok=True);shutil.make_archive(str(zp.with_suffix('')),'zip',ROOT)
with zipfile.ZipFile(zp) as z:assert all(p.relative_to(ROOT).as_posix() in z.namelist() for p in req)
shutil.copy2(zp,GROOT/zp.name);print(verdict);print(MET.to_string(index=False));print('ZIP',zp,'Drive',GROOT/zp.name)