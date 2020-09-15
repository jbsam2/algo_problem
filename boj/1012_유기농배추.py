dx=[1,0,-1,0];dy=[0,1,0,-1]
for _ in range(int(input())):
    M,N,K=map(int,input().split());m=[[0]*(M+2) for i in range(N+2)];s=0
    for k in range(K):X,Y=map(int,input().split());m[Y+1][X+1]=1
    for y in range(1,N+1):
        for x in range(1,M+1):
            if m[y][x]:
                s+=1;q=[[y,x]]
                while q:
                    o=q.pop(0)
                    for j in range(4):
                        a=o[0]+dx[j];b=o[1]+dy[j]
                        if m[a][b]:q+=[[a,b]];m[a][b]=0
    print(s)