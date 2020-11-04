def merge(a,b):
    a=root(a);b=root(b)
    if rank[a]>=rank[b]:p[b]=a
    else:p[a]=b
    if rank[a]==rank[b]:rank[a]+=1

def root(a):
    if p[a]==a:return a
    else:return root(p[a])

for t in range(int(input())):
    v,e=map(int,input().split());rank=[0]*(v+1);p=[i for i in range(v+1)];g=[];ret=0
    for _ in range(e):s,f,w=map(int,input().split());g.append((w,s,f))
    g.sort()
    for i in range(e):
        w,s,f=g[i]
        if root(s)==root(f):continue
        else:merge(s,f);ret+=w
    print(f'#{t+1}',ret)