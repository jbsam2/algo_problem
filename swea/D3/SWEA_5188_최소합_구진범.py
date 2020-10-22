for t in range(int(input())):
    n=int(input())
    b=[[*map(int,input().split())]for _ in range(n)]
    d=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==0 and j==0:d[i][j]=b[i][j]
            elif i==0 and j>0:d[i][j]=d[i][j-1]+b[i][j]
            elif j==0 and i>0:d[i][j]=d[i-1][j]+b[i][j]
            else:d[i][j]=min(d[i-1][j],d[i][j-1])+b[i][j]
    print(f'#{t+1}',d[n-1][n-1])