def solution(n, s, a, b, fares):
    ret=1<<32
    adj=[[1<<32]*(n+1)for _ in range(n+1)]
    for i in fares:adj[i[0]][i[1]]=i[2];adj[i[1]][i[0]]=i[2]
    for i in range(n+1):adj[i][i]=0
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if adj[i][j]>adj[i][k]+adj[k][j]:adj[i][j]=adj[i][k]+adj[k][j]
    for i in range(n+1):ret=min(ret,adj[s][i]+adj[i][a]+adj[i][b])
    return ret