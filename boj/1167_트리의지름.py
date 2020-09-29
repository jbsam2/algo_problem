d,n={},int(input())
for i in range(n):
    v,*w,_=map(int,input().split());d[v]=[]
    for i in range(0,len(w),2):d[v]+=[w[i:i+2]]
def f(i):
    q,m,V=[[0,i]],[0,0],[0]*(n+1);V[i]=1
    while q:
        Q=[]
        for l,e in q:
            if e not in d:continue
            for v,w in d[e]:
                if V[v]==0:V[v]=1;Q+=[[l+w,v]];m=max(m,[l+w,v])
        q=Q
    return m
print(f(f(1)[1])[0])