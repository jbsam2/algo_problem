for t in range(int(input())):
    N=int(input());M=1<<N;D=[0]*M;P=[list(map(lambda x:x*.01,map(int,input().split())))for _ in range(N)];D[0]=1
    for m in range(M):
        x=sum(1 for i in range(N)if(1<<i)&m)
        for j in range(N):
            if(1<<j)&m==0:D[m|(1<<j)]=max(D[m|(1<<j)],D[m]*P[x][j])
    print(f'#{t+1} {D[-1]*100:.6f}')