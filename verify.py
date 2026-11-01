import random
from power_floor_sums import *
A013936=[1,2,3,5,6,7,8,10,12,13,14,16,17,18,19,22,23,25,26,28,29,30,31,33,35,36,38,40,41,42,43,46,47,48,49,53,54,55,56,58,59,60,61,63,65,66,67,70,72,74,75,77,78,80,81,83,84,85,86,88,89,90,92,96,97,98,99,101,102,103]
A309082=[1,2,3,4,5,6,7,7,8,9,10,11,12,13,14,14,15,16,17,18,19,20,21,21,22,23,25,26,27,28,29,29,30,31,32,33,34,35,36,36,37,38,39,40,41,42,43,43,44,45,46,47,48,50,51,51,52,53,54,55,56,57,58,57,58,59,60,61,62,63,64,64,65,66,67]
assert [fast(n,2,0) for n in range(1,len(A013936)+1)]==A013936
assert [fast(n,3,0)-2*fast(n//8,3,0) for n in range(1,len(A309082)+1)]==A309082
for p in range(2,7):
    for n in range(1,3000):
        for c in (0,0.5,8):assert fast(n,p,c)==direct(n,p),(n,p,c)
random.seed(1)
for p in range(2,7):
    for e in range(4,16):
        for _ in range(40):
            n=random.randrange(10**(e-1),10**e)
            r=direct(n,p) if e<=10 else grouped(n,p)
            for c in (0,1,8):assert fast(n,p,c)==r,(n,p,c)
    print(p,"ok",flush=True)
for p in (2,3,4):
    for e in (16,18,20):
        n=10**e;assert fast(n,p)==grouped(n,p)==fast(n,p,2.0)
print("all ok")
