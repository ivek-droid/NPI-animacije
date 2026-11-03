# Referenčni model za animacijo »Izberi presek« (tabele 1-7 s formul na poklicni maturi).
# Zagon: python3 orodja/ref_presek.py [izpis.json]
import math, json, sys, itertools
M = {1.5:[(14.5,13.5),(14,13),(17.5,15.5),(16.5,15),(19.5,17.5),(22,18)],
     2.5:[(19.5,18),(18.5,17.5),(24,21),(23,20),(27,24),(29,24)],
     4:[(26,24),(25,23),(32,28),(30,27),(36,32),(37,30)],
     6:[(34,31),(32,29),(41,36),(38,34),(46,41),(46,38)],
     10:[(46,42),(43,39),(57,50),(52,46),(63,57),(60,50)],
     16:[(61,56),(57,52),(76,68),(69,62),(85,76),(78,64)],
     25:[(80,73),(75,68),(101,89),(90,80),(112,96),(99,82)],
     35:[(99,89),(92,83),(125,110),(111,99),(138,119),(119,98)],
     50:[(119,108),(110,99),(151,134),(133,118),(168,144),(140,116)]}
G=['A1','A2','B1','B2','C','D']
PF={1:1,2:.8,3:.7,4:.65,5:.6,6:.55}
GG=[2,4,6,8,10,13,16,20,25,32,35,40,50,63,80,100,125,160,200]
LS=[6,8,10,13,16,20,25,32,40,50,63,80,100,125]
LAM=56
def resi(faza,P_kW,cos,l,g,nk,naprava,dumax):
    U=230 if faza==1 else 400
    n=2 if faza==1 else 3
    P=P_kW*1000
    Ib=P/(U*cos) if faza==1 else P/(math.sqrt(3)*U*cos)
    lst=GG if naprava=='gG' else LS
    In=next((x for x in lst if x>=Ib),None)
    if naprava=='gG': k=2.1 if (In or 0)<=4 else 1.9 if In<=13 else 1.6
    else: k=1.45
    pf=PF[nk]; rows=[]
    for A in sorted(M):
        Iz=M[A][G.index(g)][0 if n==2 else 1]; Izp=pf*Iz
        if In is None: rows.append(dict(A=A,Izp=Izp,c1=False,c2=False,du=None,c3=False,ok=False)); continue
        du=(200 if faza==1 else 100)*l*P/(LAM*A*U**2)
        c1=Ib<=In<=Izp+1e-9; c2=k*In<=1.45*Izp+1e-9; c3=du<=dumax+1e-9
        rows.append(dict(A=A,Izp=Izp,c1=c1,c2=c2,du=du,c3=c3,ok=c1 and c2 and c3))
    mn=next((r['A'] for r in rows if r['ok']),None)
    return dict(Ib=Ib,In=In,k=k,pf=pf,rows=rows,min=mn)
if __name__=='__main__':
    if len(sys.argv)>1:
        out=[]
        for faza,P,cos,l,g,nk,nap,du in itertools.product((1,3),(0.5,1,2,2.5,3.5,5,9,15,20),(1,.9,.8),(5,20,40,100,150),G,(1,3,6),('gG','LS'),(3,5,8)):
            r=resi(faza,P,cos,l,g,nk,nap,du)
            out.append(dict(inp=[faza,P,cos,l,g,nk,nap,du],min=r['min'],In=r['In'],Ib=r['Ib']))
        json.dump(out,open(sys.argv[1],'w'))
        print(len(out),'primerov')
    else:
        for name,a in {'grelnik':(1,2.5,1,20,'A2',1,'gG',5),'svetilke':(1,2,1,60,'B2',1,'gG',3),'motor':(3,9,.9,30,'B2',1,'gG',5),'skupina':(3,9,.9,30,'B2',5,'gG',5),'odkl':(1,3.5,1,40,'C',1,'LS',5)}.items():
            r=resi(*a); print(name,'Ib=%.2f In=%s k=%s min=%s'%(r['Ib'],r['In'],r['k'],r['min']))
            for x in r['rows']: print('  ',x['A'],'Iz\'=%.2f'%x['Izp'],x['c1'],x['c2'],'du=%.2f'%x['du'],x['c3'],'OK' if x['ok'] else '')
