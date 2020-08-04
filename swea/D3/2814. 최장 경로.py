def dfs(s,k):
    global r
    visit[s]=1
    r=max(r,k)
    for w in b[s]:
        if visit[w]:continue
        dfs(w,k+1)
    visit[s]=0
 
for t in range(int(input())):
    n,m=map(int,input().split())
    b=[[] for _ in range(n+1)]
    r=-1
    for _ in range(m):
        x,y=map(int,input().split())
        b[x].append(y)
        b[y].append(x)
    for i in range(n):
        visit=[0]*(n+1)
        dfs(i,1)
    print('#%d %d'%(t+1,r))