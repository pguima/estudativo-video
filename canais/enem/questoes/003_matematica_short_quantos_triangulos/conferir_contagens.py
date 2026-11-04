# conta triângulos numa figura de segmentos (força bruta: 3 pontos ligados 2 a 2 por um mesmo segmento desenhado)
from itertools import combinations
from fractions import Fraction as F
def inter(s, t):
    (x1,y1),(x2,y2)=s; (x3,y3),(x4,y4)=t
    d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if d==0: return None
    u=((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/d; v=-((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/d
    if 0<=u<=1 and 0<=v<=1: return (x1+u*(x2-x1), y1+u*(y2-y1))
def on(p,s):
    (x1,y1),(x2,y2)=s; x,y=p
    if (x2-x1)*(y-y1)-(y2-y1)*(x-x1)!=0: return False
    return min(x1,x2)<=x<=max(x1,x2) and min(y1,y2)<=y<=max(y1,y2)
def conta(segs):
    pts=set(p for s in segs for p in s)
    for s,t in combinations(segs,2):
        p=inter(s,t)
        if p: pts.add(p)
    pts=list(pts)
    lig=lambda a,b: any(on(a,s) and on(b,s) for s in segs)
    n=0
    for a,b,c in combinations(pts,3):
        if (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])==0: continue
        if lig(a,b) and lig(b,c) and lig(a,c): n+=1
    return n
A=(F(0),F(0))
def leque(m,h):
    B=[(F(k),F(1)) for k in range(m+1)]
    segs=[(A,b) for b in B]+[(B[0],B[-1])]
    for f in h: segs.append(((F(0)*f,f),(F(m)*f,f)))
    return segs
def grade(n):
    V=lambda r,c:(F(2*c-r),F(r))
    segs=[]
    for r in range(1,n+1): segs.append((V(r,0),V(r,r)))
    for c in range(n): segs.append((V(c,c),V(n,n))) ; 
    segs=[]
    for r in range(1,n+1): segs.append((V(r,0),V(r,r)))                  # horizontais
    for k in range(n): segs.append((V(k,0),V(n,n-k)))                    # paralelas ao lado direito
    for k in range(n): segs.append((V(k,k),V(n,k)))                      # paralelas ao lado esquerdo
    return segs
print("leque 3:",conta(leque(3,[])),"leque 4 + linha no meio:",conta(leque(4,[F(1,2)])),"grade 4:",conta(grade(4)),"grade 3:",conta(grade(3)))
