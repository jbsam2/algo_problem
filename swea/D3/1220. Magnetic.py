for t in range(10):
    n=int(input());b=[list(map(int,input().split()))for _ in range(n)];r=0
    for j in range(n):
        for i in range(n):
            if b[i][j]==2:b[i][j]=0;break
            elif b[i][j]==1:break
        for i in range(n-1,-1,-1):
            if b[i][j]==1:b[i][j]=0;break
            elif b[i][j]==2:break
    for j in range(n):
        c=0
        for i in range(n):
            if b[i][j]==1 and c==0:c=1
            elif b[i][j]==2 and c==1:c=0;r+=1
    print(f'#{t+1}',r)