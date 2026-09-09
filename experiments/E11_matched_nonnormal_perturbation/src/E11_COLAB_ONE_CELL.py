# Paste this complete file into ONE fresh Google Colab cell. CPU only.
import json,sys,shutil,zipfile,hashlib
from pathlib import Path
import numpy as np,pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import bootstrap
from google.colab import drive

CS=(0,2,4,6); EPS=np.array([.005,.01,.02,.05,.08,.10,.125,.15,.20]); N=5000; BOOT=123456789; NB=10000; ITOL=1e-8
ROOT=Path('/content/koopman_E11_matched_nonnormal_perturbation');GROOT=Path('/content/drive/MyDrive/koopman_E11_matched_nonnormal_perturbation');CSV,PL,RP,CF,CD=[ROOT/x for x in ('csv','plots','reports','config','code')]
if ROOT.exists():shutil.rmtree(ROOT)
drive.mount('/content/drive',force_remount=False)
for p in (ROOT,CSV,PL,RP,CF,CD,GROOT):p.mkdir(parents=True,exist_ok=True)
def mirror(p):
 p=Path(p);q=GROOT/p.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);t=q.with_suffix(q.suffix+'.partial');shutil.copy2(p,t);t.replace(q)
def sc(x,n):p=CSV/n;x.to_csv(p,index=False);mirror(p);return p
def st(x,p):p.write_text(x,encoding='utf-8');mirror(p);return p
def B(c):return np.array([[.7,0,0],[0,.6,-.1*c],[0,0,.5]],float)
def dg(U,V):return float(np.linalg.norm(U@U.T-V@V.T,'fro')/np.sqrt(2))
def orth(X):return np.linalg.qr(np.asarray(X))[0]
def eig(A):w,V=np.linalg.eig(A);i=np.argsort(-np.abs(w));return w[i],V[:,i]
def sub(A):
 w,V=eig(A);a=w[:2]; complex_top=bool(abs(a[0].imag)>ITOL*max(1,abs(a[0])) or abs(a[1].imag)>ITOL*max(1,abs(a[1])));closed=bool(complex_top and abs(a[0]-a[1].conjugate())<=1e-7*max(1,abs(a[0])))
 if complex_top and not closed:return None,w,'undefined','pair_cut',complex_top,closed,np.nan
 if closed:U=orth(np.c_[V[:,0].real,V[:,0].imag]);typ='complex_pair_real_span'
 else:U=orth(V[:,:2].real);typ='two_real_eigenvectors'
 res=float(np.linalg.norm((np.eye(3)-U@U.T)@A@U,'fro')/max(np.linalg.norm(A,'fro'),1e-12));return U,w,typ,'',complex_top,closed,res
def diag(c):
 A=B(c);w,V=eig(A);return {'true_eigenvalues':repr(w.tolist()),'kappa_V':float(np.linalg.cond(V)),'departure_normality':float(np.linalg.norm(A.T@A-A@A.T,'fro')),'spectral_norm':float(np.linalg.norm(A,2)),'spectral_radius':float(max(abs(w))),'true_inner_gap':.1,'true_outer_gap':.1}
E=np.eye(3)[:,:2]; OR={c:diag(c) for c in CS}
# strict preflight and sanity tests
for c in CS:
 A=B(c);U,_,_,reason,_,_,r=sub(A);assert np.allclose(np.sort(np.linalg.eigvals(A)),[.5,.6,.7]) and abs(max(abs(np.linalg.eigvals(A)))-.7)<1e-12 and reason=='' and dg(U,E)<1e-12 and r<1e-8
assert np.all(np.diff([OR[c]['kappa_V'] for c in CS])>0) and np.all(np.diff([OR[c]['departure_normality'] for c in CS])>0)
assert dg(E,E[:,[1,0]])<1e-14 and dg(E,E@np.array([[0,-1],[1,0]]))<1e-14
R=np.array([[0,-.9,0],[.9,0,0],[0,0,.55]]);Ur,_,tr,rr,_,_,resr=sub(R);assert tr=='complex_pair_real_span' and rr=='' and resr<1e-8
rng=np.random.default_rng(202511);G=rng.standard_normal((N,3,3));D=G/np.linalg.norm(G.reshape(N,-1),axis=1)[:,None,None];assert np.allclose(np.linalg.norm(D.reshape(N,-1),axis=1),1)
sc(pd.DataFrame([['unperturbed_exact',True],['basis_invariance',True],['complex_pair_rule',True],['matched_D_once',True]],columns=['check','passed']),'sanity_checks.csv')
rows=[]
for eps in EPS:
 for j in range(N):
  for c in CS:
   A=B(c);T=A+eps*D[j];U,w,typ,why,ct,closed,res=sub(T);defined=U is not None;e=dg(U,E) if defined else np.nan
   rows.append({'seed':j,'epsilon':float(eps),'c':c,**OR[c],'perturbation_fro':float(np.linalg.norm(T-A,'fro')),'direction_sha256':hashlib.sha256(D[j].tobytes()).hexdigest(),'estimated_eigenvalues':repr(w.tolist()),'r2_defined':defined,'construction_type':typ,'undefined_reason':why,'complex_top2':ct,'top2_conjugation_closed':closed,'e2':e,'e2_over_epsilon':e/eps if defined else np.nan,'invariant_residual':res})
 raw=pd.DataFrame(rows);rows=[];sc(raw,f'raw_through_eps_{eps:.3f}.csv') # Drive checkpoint after every epsilon
raw=pd.concat([pd.read_csv(CSV/f'raw_through_eps_{e:.3f}.csv') for e in EPS],ignore_index=True);assert len(raw)==N*len(EPS)*len(CS)
agg=[]
for (c,e),z in raw.groupby(['c','epsilon'],sort=True):
 q=z[z.r2_defined];agg.append({'c':c,'epsilon':e,**OR[c],'n':len(z),'r2_defined_rate':float(z.r2_defined.mean()),'complex_rate':float(z.complex_top2.mean()),'pair_cut_undefined_rate':float((z.undefined_reason=='pair_cut').mean()),'undefined_rate':float((~z.r2_defined).mean()),'median_e2':float(q.e2.median()) if len(q) else np.nan,'mean_e2':float(q.e2.mean()) if len(q) else np.nan,'p90_e2':float(q.e2.quantile(.9)) if len(q) else np.nan,'p95_e2':float(q.e2.quantile(.95)) if len(q) else np.nan,'median_sensitivity':float(q.e2_over_epsilon.median()) if len(q) else np.nan,'max_residual':float(q.invariant_residual.max()) if len(q) else np.nan})
A=pd.DataFrame(agg);sc(A,'aggregated_outcomes.csv')
# Paired seed-level bootstrap for c6 versus c0 at every amplitude.
br=[];g=np.random.default_rng(BOOT)
for e in EPS:
 a=raw[raw.epsilon.eq(e)].pivot(index='seed',columns='c',values=['r2_defined','e2']);d=(a['r2_defined'][6]-a['r2_defined'][0]).to_numpy(float);both=a['r2_defined'][6].to_numpy(bool)&a['r2_defined'][0].to_numpy(bool);de=(a['e2'][6].to_numpy(float)-a['e2'][0].to_numpy(float))[both];rel=((a['e2'][6].to_numpy(float)-a['e2'][0].to_numpy(float))/np.maximum(a['e2'][0].to_numpy(float),1e-15))[both]
 bd=np.array([d[g.integers(N,size=N)].mean() for _ in range(NB)]);be=np.array([np.median(de[g.integers(len(de),size=len(de))]) for _ in range(NB)]) if len(de) else np.full(NB,np.nan)
 br.append({'epsilon':e,'defined_rate_c0':float(a['r2_defined'][0].mean()),'defined_rate_c6':float(a['r2_defined'][6].mean()),'defined_diff_c6_minus_c0':float(d.mean()),'defined_diff_ci_low':float(np.quantile(bd,.025)),'defined_diff_ci_high':float(np.quantile(bd,.975)),'both_defined_n':int(both.sum()),'median_e2_diff_c6_minus_c0':float(np.median(de)) if len(de) else np.nan,'e2_diff_ci_low':float(np.nanquantile(be,.025)),'e2_diff_ci_high':float(np.nanquantile(be,.975)),'median_relative_increase':float(np.median(rel)) if len(rel) else np.nan})
P=pd.DataFrame(br);sc(P,'paired_bootstrap.csv')
R=P[P.epsilon.isin([.10,.125,.15])].copy();Aok=((R.defined_rate_c0-R.defined_rate_c6>=.15)&((R.defined_diff_ci_low>0)|(R.defined_diff_ci_high<0))).any();Bok=((R.median_e2_diff_c6_minus_c0>0)&(R.e2_diff_ci_low>0)&(R.median_relative_increase>=.25)).any();valid=bool(raw.perturbation_fro.sub(raw.epsilon).abs().max()<1e-12 and raw.invariant_residual.dropna().max()<1e-8 and raw.groupby(['seed','epsilon']).direction_sha256.nunique().eq(1).all());verdict='E11 INVALID — INTEGRITY GATE FAILED' if not valid else ('E11 PURE NONNORMAL SPECTRAL-SENSITIVITY MECHANISM SUPPORTED' if Aok or Bok else 'E11 PURE NONNORMAL GEOMETRY INSUFFICIENT TO EXPLAIN E10')
sc(pd.DataFrame([['A defined-rate collapse',Aok,'paired CI excludes zero; drop >=.15'],['B conditional error increase',Bok,'median diff>0, CI low>0, rel>=25%'],['integrity',valid,'matched directions/norm/residual'],['VERDICT',verdict,'mechanical']],columns=['gate','pass','criterion']),'preregistered_gates.csv')
def fig(n,f):plt.figure(figsize=(6,4));f();plt.tight_layout();p=PL/n;plt.savefig(p,dpi=180);plt.close();mirror(p)
for col,n,y in [('r2_defined_rate','defined_rate.png','defined rate'),('median_e2','median_e2.png','median conditional e2'),('p95_e2','p95_e2.png','p95 conditional e2'),('median_sensitivity','sensitivity.png','median e2/epsilon'),('complex_rate','complex_rate.png','complex top2 rate')]:fig(n,lambda col=col,y=y:[plt.plot(z.epsilon,z[col],'o-',label=f'c={c}') for c,z in A.groupby('c')] and (plt.legend(),plt.xlabel('epsilon'),plt.ylabel(y)))
fig('paired_e2_difference.png',lambda:(plt.plot(P.epsilon,P.median_e2_diff_c6_minus_c0,'o-'),plt.fill_between(P.epsilon,P.e2_diff_ci_low,P.e2_diff_ci_high,alpha=.2),plt.axhline(0,color='k'),plt.xlabel('epsilon'),plt.ylabel('paired median e2(c6)-e2(c0)')))
for col,n,title in [('r2_defined_rate','heat_defined.png','defined rate'),('median_e2','heat_median_e2.png','median conditional e2'),('p95_e2','heat_p95_e2.png','p95 conditional e2')]:fig(n,lambda col=col,title=title:(plt.imshow(A.pivot(index='epsilon',columns='c',values=col),aspect='auto',origin='lower'),plt.colorbar(label=title),plt.xticks(range(4),CS),plt.yticks(range(len(EPS)),EPS),plt.xlabel('c'),plt.ylabel('epsilon')))
for e in [.10,.125,.15]:fig(f'distribution_{e:.3f}.png',lambda e=e:[plt.hist(raw[(raw.epsilon.eq(e))&(raw.c.eq(c))&raw.r2_defined].e2,bins=35,alpha=.4,label=f'c={c}') for c in CS] and (plt.legend(),plt.xlabel('conditional e2')))
cfg={'c_grid':CS,'eps_grid':EPS.tolist(),'n_directions':N,'bootstrap_seed':BOOT,'bootstrap_replicates':NB,'primary_eps':[.10,.125,.15],'B_matrices':{str(c):B(c).tolist() for c in CS},'rule':'top two by modulus; real span or complete conjugate pair; pair cut undefined'};st(json.dumps(cfg,indent=2),CF/'config.json');st(json.dumps({'python':sys.version,'numpy':np.__version__},indent=2),CF/'environment.json')
report=f'''# E11 — Matched operator-perturbation falsification\n\n## Design\nSame 5000 normalized Gaussian perturbation directions are used for every c at each frozen epsilon. No time series, OLS, EDMD or Q(c) enters.\n\n## Result\n**{verdict}**\n\n## What this establishes\nOnly a matched finite-perturbation mechanism result for this 3x3 family.\n\n## What this does not establish\nNo universal theorem, no complete explanation of E10, no new score, no drift/uncertainty claim, and no Schur novelty claim.\n\n## Next cheapest falsification\n{'Representation test: eigen-cluster versus published ordered-Schur invariant subspace.' if 'SUPPORTED' in verdict else 'Vary statistical-error geometry at fixed operator-perturbation scale.'}\n''';st(report,RP/'SCIENTIFIC_REPORT.md')
for n,t in {'CORRECTNESS_AUDIT.md':'# CORRECTNESS AUDIT\nAll preflight assertions passed before main perturbations.\n','METHODOLOGY_AUDIT.md':'# METHODOLOGY AUDIT\nMatched D_j across c; no hidden filtering of undefined rows; gates frozen.\n','STATISTICAL_AUDIT.md':'# STATISTICAL AUDIT\nBootstrap unit is matched perturbation seed; 10000 replicates.\n','SPECTRAL_GEOMETRY_AUDIT.md':'# SPECTRAL-GEOMETRY AUDIT\nExact base spectrum/gaps/target preserved; complex-pair rule is primary rule.\n','REPRODUCIBILITY_AUDIT.md':'# REPRODUCIBILITY AUDIT\nFixed RNG/config; raw checkpoints mirrored to Google Drive.\n','CLAIM_AUDIT.md':'# CLAIM AUDIT\nNo universal or E10-complete causal claim is made.\n'}.items():st(t,RP/n)
try:src=__import__('IPython').get_ipython().history_manager.input_hist_raw[-1]
except Exception:src=''
if not src or 'E11' not in src:raise RuntimeError('Source capture failed.')
st(src,CD/'E11_COLAB_ONE_CELL.py')
required=[CSV/x for x in ['sanity_checks.csv','aggregated_outcomes.csv','paired_bootstrap.csv','preregistered_gates.csv']]+list(CSV.glob('raw_through_eps_*.csv'))+list(PL.glob('*.png'))+[CF/'config.json',CF/'environment.json',CD/'E11_COLAB_ONE_CELL.py',RP/'SCIENTIFIC_REPORT.md']+list(RP.glob('*AUDIT.md'));manifest='# ARTIFACT MANIFEST\n\n'+'\n'.join('- '+x.relative_to(ROOT).as_posix() for x in required);st(manifest,ROOT/'ARTIFACT_MANIFEST.md');required.append(ROOT/'ARTIFACT_MANIFEST.md');assert all(p.exists() and p.stat().st_size>0 for p in required)
zp=ROOT.parent/'koopman_E11_matched_nonnormal_perturbation.zip';zp.unlink(missing_ok=True);shutil.make_archive(str(zp.with_suffix('')),'zip',ROOT)
with zipfile.ZipFile(zp) as z:assert all(p.relative_to(ROOT).as_posix() in z.namelist() for p in required);members=z.namelist()
gz=GROOT/zp.name;shutil.copy2(zp,gz)
print('E11 MATCHED NONNORMAL PERTURBATION');print(A.to_string(index=False));print(verdict);print('WHAT THIS ESTABLISHES: matched-perturbation result only.');print('WHAT THIS DOES NOT ESTABLISH: universal theorem or full E10 explanation.');print('NEXT CHEAPEST FALSIFICATION:', 'representation test' if 'SUPPORTED' in verdict else 'error-geometry test');print('ZIP',zp,zp.stat().st_size,'DRIVE',gz,gz.stat().st_size,'files',len(members))