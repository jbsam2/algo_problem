import heapq
for t in range(int(input())):
    n=int(input());x=[*map(int,input().split())];y=[*map(int,input().split())];e=float(input());adj={i: [] for i in range(n)}
    for s in range(n):
        for f in range(n):
            if s!=f:adj[s].append([f,(x[s]-x[f])**2+(y[s]-y[f])**2])
    k=[float('inf')]*n;v=[0]*n;pq=[]
    k[0]=0;heapq.heappush(pq,(0,0));ret=0
    while pq:
        w,p=heapq.heappop(pq)
        if v[p]:continue
        v[p]=1;ret+=w
        for d,l in adj[p]:
            if v[d]==0 and l<k[d]:k[d]=l;heapq.heappush(pq,(l,d))
    print(f'#{t+1}',round(ret*e))