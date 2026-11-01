import sys,time
from power_floor_sums import *
def t(f,*a):
    s=time.perf_counter();r=f(*a);return r,time.perf_counter()-s
p=int(sys.argv[1]);es=[int(v) for v in sys.argv[2].split(",")];c=float(sys.argv[3]);eg=int(sys.argv[4]);ed=int(sys.argv[5])
print("p",p,"c",c)
print("e S_p(n) t_direct t_grouped t_fast vertices")
for e in es:
    n=10**e+1;st=[];r,tf=t(fast,n,p,c,st);tg=td=None
    if e<=eg:g,tg=t(grouped,n,p);assert g==r
    if e<=ed:d,td=t(direct,n,p);assert d==r
    print(e,r,td,tg,round(tf,4),st[0],flush=True)
