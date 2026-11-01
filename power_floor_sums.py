from math import isqrt
def iroot(n,p):
    if n<2:return n
    if p==2:return isqrt(n)
    x=1<<-(-n.bit_length()//p)
    while 1:
        y=((p-1)*x+n//x**(p-1))//p
        if y>=x:return x
        x=y
def direct(n,p):return sum(n//k**p for k in range(1,iroot(n,p)+1))
def grouped(n,p):
    m=iroot(n,p+1);t=n//m**p
    return sum(n//i**p for i in range(1,m+1))+sum(iroot(n//j,p) for j in range(1,t+1))-m*t
def hull(n,p,x1,k,st=None):
    c=n+1;y0=n//x1**p+1;x,y=x1,y0;A=B=V=0
    while x<k:
        rem=k-x
        al,bl=1,y-n//(x+1)**p-1
        ar,br=1,bl+1
        while al+ar<=rem:
            u=x+al;w=y-bl
            if (u+ar)**p*(w-br)>=c:
                lo,hi=1,2
                while al+hi*ar<=rem and (u+hi*ar)**p*(w-hi*br)>=c:lo,hi=hi,2*hi
                while hi-lo>1:
                    m=lo+hi>>1
                    if al+m*ar<=rem and (u+m*ar)**p*(w-m*br)>=c:lo=m
                    else:hi=m
                al+=lo*ar;bl+=lo*br
            else:
                u=x+ar;w=y-br
                q=lambda j:ar+j*al>rem or (u+j*al)**p*(w-j*bl)>=c or p*c*al<=bl*(u+j*al)**(p+1)
                lo,hi=0,1
                while not q(hi):lo,hi=hi,2*hi
                while hi-lo>1:
                    m=lo+hi>>1
                    if q(m):hi=m
                    else:lo=m
                if ar+hi*al>rem or (u+hi*al)**p*(w-hi*bl)<c:break
                ar+=(hi-1)*al;br+=(hi-1)*bl;al+=ar;bl+=br
        lo,hi=1,2
        while hi*al<=rem and (x+hi*al)**p*(y-hi*bl)>=c:lo,hi=hi,2*hi
        while hi-lo>1:
            m=lo+hi>>1
            if m*al<=rem and (x+m*al)**p*(y-m*bl)>=c:lo=m
            else:hi=m
        A+=lo*al*(2*(y0-y)+lo*bl);B+=lo;x+=lo*al;y-=lo*bl;V+=1
    if st is not None:st.append(V)
    return (k-x1+1)*y0-((A+B+y0-y+k-x1)//2+1)
def fast(n,p,c=8.0,st=None):
    k=iroot(n,p);x0=int(c*iroot(n,p+2))+1
    if k<x0+3:return direct(n,p)
    return sum(n//i**p for i in range(1,x0+1))+hull(n,p,x0+1,k,st)
