# Preračun rešenih primerov (dimenzioniranje vodnikov) po tabelah s formul na poklicni maturi.
# Zagon: python3 orodja/preveri_dimenzioniranje.py
import math
# --- Tabela 3 (matura): Iz po presekih; stolpci A1,A2,B1,B2,C,D; (2 obr., 3 obr.)
M = {1.5:[(14.5,13.5),(14,13),(17.5,15.5),(16.5,15),(19.5,17.5),(22,18)],
     2.5:[(19.5,18),(18.5,17.5),(24,21),(23,20),(27,24),(29,24)],
     4:[(26,24),(25,23),(32,28),(30,27),(36,32),(37,30)],
     6:[(34,31),(32,29),(41,36),(38,34),(46,41),(46,38)],
     10:[(46,42),(43,39),(57,50),(52,46),(63,57),(60,50)],
     16:[(61,56),(57,52),(76,68),(69,62),(85,76),(78,64)],
     25:[(80,73),(75,68),(101,89),(90,80),(112,96),(99,82)],
     35:[(99,89),(92,83),(125,110),(111,99),(138,119),(119,98)],
     50:[(119,108),(110,99),(151,134),(133,118),(168,144),(140,116)]}
G = ['A1','A2','B1','B2','C','D']
def Iz(A,g,n): return M[A][G.index(g)][0 if n==2 else 1]
GG=[2,4,6,8,10,13,16,20,25,32,35,40,50,63,80,100,125,160,200]
LS=[6,8,10,13,16,20,25,32,40,50,63,80,100,125]
def k_gG(In): return 2.1 if In<=4 else 1.9 if In<=13 else 1.6
def k_ls(In): return 1.45
def ok(In,Ib,Izp,kf):
    return Ib<=In<=Izp and kf(In)*In<=1.45*Izp
def izberi(Ib,Izp,lst,kf):
    for In in lst:
        if In>=Ib: return In  # najmanjsi In >= Ib
def resi(Ib,A,g,n,fp=1.0):
    Izp=Iz(A,g,n)*fp
    out={}
    for ime,lst,kf in (('gG',GG,k_gG),('LS',LS,k_ls)):
        In=izberi(Ib,Izp,lst,kf)
        out[ime]=(In, ok(In,Ib,Izp,kf) if In else None, round(Izp,2), round(kf(In)*In,1) if In else None, round(1.45*Izp,1))
    return out
def najmanjsi_presek(Ib,g,n,lst,kf,fp=1.0):
    In=izberi(Ib,0,lst,kf)
    for A in sorted(M):
        if ok(In,Ib,Iz(A,g,n)*fp,kf): return A,In
    return None
print("== 2020/2021 zadnja naloga: P=2kW, 230V, A2, 2 obr., gG")
Ib=2000/230; print("Ib=%.2f"%Ib, resi(Ib,1.5,'A2',2))
def du1(l,P,A,lam=56,U=230): return 200*l*P/(lam*A*U**2)
print("du%% pri 2000W: %.2f"%du1(20,2000,1.5), " pri 2500W: %.2f"%du1(20,2500,1.5), "(napacno z dodatnim faktorjem 2: %.2f)"%(2*du1(20,2500,1.5)))
Ib2=2500/230; print("po zamenjavi Ib=%.2f"%Ib2, "gG, 1.5:",resi(Ib2,1.5,'A2',2)['gG'], " 2.5:",resi(Ib2,2.5,'A2',2)['gG'])
print("najmanjsi presek za 2.5 kW (gG):", najmanjsi_presek(Ib2,'A2',2,GG,k_gG), "  (odklopnik):", najmanjsi_presek(Ib2,'A2',2,LS,k_ls))
print("du%% pri 2500W in 2.5mm2: %.2f"%du1(20,2500,2.5))
print("\n== spom 2021: 3f 38kW 400V cos=1, D, 3 obr., gG")
Ib=38000/(math.sqrt(3)*400); print("Ib=%.2f"%Ib, "16mm2:",resi(Ib,16,'D',3)['gG'],"25mm2:",resi(Ib,25,'D',3)['gG'])
print("l_max = %.1f m"%(25*56*1.5*400**2/(100*38000)))
print("\n== zimski 2022: 3f 9kW cos .9, B2, 3 obr., gG")
Ib=9000/(math.sqrt(3)*400*0.9); print("Ib=%.2f"%Ib, "1.5:",resi(Ib,1.5,'B2',3)['gG'],"2.5:",resi(Ib,2.5,'B2',3)['gG'], "odklopnik 2.5:",resi(Ib,2.5,'B2',3)['LS'])
print("\n== poprava testa")
print("1) A=%.3f mm2"%(2*14*10/(56.5*2)), "  2) Ib=%.2f"%(10000/(math.sqrt(3)*400)), "  3) I=%.3f A"%(1.5*56.5*1*230/(200*20)))
print("matura 2023/19: A=%.2f mm2"%(2*14*10/(56*2)))
print("\n== ucbenik, primer 3 (A2, 1.5mm2, 35C, f1=0.94)")
for Iz0,ime in ((15.5,'ucbenik (tabela 20.2)'),(14,'matura tabela 3')):
    Izp=Iz0*0.94; print(ime,'Iz\'=%.2f'%Izp, ' gG:', max([x for x in GG if ok(x,0,Izp,k_gG)] or [None]), ' odklopnik:', max([x for x in LS if ok(x,0,Izp,k_ls)] or [None]))
print("\n== ucbenik, primer 1: B1 1.5, 25C:",17.5*1.06, "  primer 4:",20*1.06*0.8, "  primer 5:",32*0.94*0.9, " primer 6b A2 2.5 3obr:",Iz(2.5,'A2',3))
print("\n== ucbenik pr. CNN: I=%.1f A"%(8000/(math.sqrt(3)*400*0.8)), " Iz'(1.5)=%.1f"%(18.5/ (1.06*0.79*0.86)), " f=%.4f"%(1.06*0.79*0.86))
print("   dU=sqrt3*14.4*0.0175*40/2.5 (rho=0.0175)= %.2f V"%(math.sqrt(3)*14.4*0.0175*40/2.5), " (z gamma=57.1: %.2f)"%(math.sqrt(3)*14.4*40/(57.1*2.5)))
print("\n== ucbenik pralni stroj: I=%.2f A, A=%.2f mm2, l=%.1f m"%(2500/(230*.9), 2*20*12.1*.9/(57.1*6.9), 230*1.5*57.1*3/(2*12.1*.9*100)))
print("\n== najvecji In za vsak presek (brez fp): gG | odklopnik")
for g in G:
  for n in (2,3):
    row=[]
    for A in (1.5,2.5,4,6,10,16,25):
        Izp=Iz(A,g,n); a=max([x for x in GG if x<=Izp and ok(x,0,Izp,k_gG)] or [0]); b=max([x for x in LS if ok(x,0,Izp,k_ls)] or [0])
        row.append(f"{A}:{a}/{b}")
    print(g,n,' '.join(row))
