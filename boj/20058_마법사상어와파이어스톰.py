import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
dir=[(1,0),(0,1),(-1,0),(0,-1)]
n,q=map(int,input().split())
n=2**n
b=[[*map(int,input().split())]for _ in range(n)]
for size in [*map(int,input().split())]:
    ts=2**size
    for i in range(0,n,ts):
        for j in range(0,n,ts):
            tmp=[b[k][j:j+ts]for k in range(i,i+ts)]
            for y in range(ts):
                for x in range(ts):
                    b[i+x][j+ts-1-y]=tmp[y][x]
    c=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for d in dir:
                ni=i+d[0];nj=j+d[1]
                if 0<=ni<n and 0<=nj<n and b[ni][nj]:c[i][j]+=1
    for i in range(n):
        for j in range(n):
            if c[i][j]<3 and b[i][j]:b[i][j]-=1
print(sum(sum(i)for i in b))
ans=0
def dfs(y,x):
    s=1;b[y][x]=0
    for d in dir:
        nx=x+d[0];ny=y+d[1]
        if 0<=nx<n and 0<=ny<n and b[ny][nx]:s+=dfs(ny,nx)
    return s
for i in range(n):
    for j in range(n):
        if b[i][j]:ans=max(ans,dfs(i,j))
print(ans)