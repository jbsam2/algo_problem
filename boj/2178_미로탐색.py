n,m=map(int,input().split());dx=[0,0,1,-1];dy=[1,-1,0,0]
b=[[int(i)for i in input()]for _ in range(n)]
b[0][0]=0
q=[(0,0)]
while q:
    y,x=q.pop(0)
    for i in range(4):
        nx=x+dx[i];ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and b[ny][nx]==1:b[ny][nx]=b[y][x]+1;q+=[(ny,nx)]
print(b[n-1][m-1]+1)