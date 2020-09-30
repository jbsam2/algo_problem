n=int(input())
e=[[]for _ in range(n+1)]
for _ in range(n-1):u,v,w=map(int,input().split());e[u]+=[(v,w)];e[v]+=[(u,w)]
def bfs(s):
    dist=[0]*(n+1);dist[s]=0;q=[s]
    while q:
        x=q.pop(0)
        for y,d in e[x]:
            if dist[y]==0:dist[y]=dist[x]+d;q+=[y]
    return dist
print(max(bfs(bfs(1).index(max(bfs(1))))))