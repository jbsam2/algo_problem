n,m,r=map(int,input().split())
v=[[*map(int,input().split())]for i in range(n)]
for i in range(min(n,m)//2):
    l=[]
    for a in range(i,n-i):l+=[v[a][i]]
    for b in range(i+1,m-i):l+=[v[a][b]]
    for c in range(a-1,i-1,-1):l+=[v[c][b]]
    for d in range(b-1,i,-1):l+=[v[c][d]]
    j=r%len(l)
    l=iter(l[-j:]+l[:-j])
    for a in range(i,n-i):v[a][i]=next(l)
    for b in range(i+1,m-i):v[a][b]=next(l)
    for c in range(a-1,i-1,-1):v[c][b]=next(l)
    for d in range(b-1,i,-1):v[c][d]=next(l)
for i in v:print(*i)