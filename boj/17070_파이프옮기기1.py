import sys
input = sys.stdin.readline
n=int(input())
b=[[1]*(n+1)]+[[1]+[*map(int,input().split())] for i in range(n)]
d=[[[0,0,0]for i in range(n+1)]for j in range(n+1)]
d[1][2][0]=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if b[i][j]:continue
        d[i][j][0]+=d[i][j-1][0]+d[i][j-1][1]
        if b[i-1][j]==0 and b[i][j-1]==0:
            d[i][j][1]+=sum(d[i-1][j-1])
        d[i][j][2]+=d[i-1][j][1]+d[i-1][j][2]
print(sum(d[n][n]))