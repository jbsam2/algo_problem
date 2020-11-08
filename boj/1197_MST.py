def root(a):
    if p[a]==a:return a
    else:return root(p[a])
def merge(a,b):
    a=root(a);b=root(b)
    if rank[a]>=rank[b]:p[b]=a
    else:p[a]=b
    if rank[a]==rank[b]:rank[a]+=1
v,e=map(int,input().split())
rank=[0]*(v+1)
p=[i for i in range(v+1)]
adj=[]
ret=0
for _ in range(e):a,b,c=map(int,input().split());adj.append((c,a,b))
adj.sort()
for i in range(e):
    c,a,b=adj[i]
    if root(a)==root(b):continue
    else:merge(a,b);ret+=c
print(ret)


import heapq
v,e=map(int,input().split())
adj=[[]for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    adj[a].append((c,b))
    adj[b].append((c,a))
visit=[0]*(v+1)
pq=[]
heapq.heappush(pq,(0,1))
ret=0
while pq:
    c,b=heapq.heappop(pq)
    if visit[b]==0:
        ret+=c
        visit[b]=1
        for w,n in adj[b]:
            if visit[n]==0:heapq.heappush(pq,(w,n))
print(ret)