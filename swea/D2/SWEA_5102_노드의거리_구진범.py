def bfs():
    q=[(s,0)];v=[s]
    while len(q):
        n,c=q.pop(0)
        if n==e:return c
        for i in range(1,l+1):
            if i not in v and m[n][i]:q.append((i,c+1));v.append(i)
    return 0
for t in range(int(input())):
    l,k=map(int,input().split());m=[[0]*(l+1)for _ in range(l+1)]
    for i in range(k):a,b=map(int,input().split());m[a][b]=m[b][a]=1
    s,e=map(int,input().split());print('#{} {}'.format(t+1,bfs()))