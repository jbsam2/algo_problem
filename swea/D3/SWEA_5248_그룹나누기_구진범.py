def merge(a,b):
    a=root(a);b=root(b)
    if rank[a]>=rank[b]:p[b]=a
    else:p[a]=b
    if rank[a]==rank[b]:rank[a]+=1

def root(a):
    if p[a]==a:return a
    else:return root(p[a])

for t in range(int(input())):
    n,m=map(int,input().split());l=[*map(int,input().split())];p=[i for i in range(n+1)];rank=[0]*(n+1);ret=set()
    for i in range(m):merge(l[2*i],l[2*i+1])    
    for i in range(1,n+1):ret.add(root(i))
    print(f'#{t+1}',len(ret))