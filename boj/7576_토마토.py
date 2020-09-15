m,n=map(int,input().split());dx=[0,0,1,-1];dy=[1,-1,0,0]
b=[[i+1 for i in map(int,input().split())]for _ in range(n)]
l=[(i,j)for i in range(n) for j in range(m) if b[i][j]==2]
for i,j in l:b[i][j]=0
c=0
while l:
    q=[]
    for y,x in l:
        for i in range(4):
            ny=y+dy[i];nx=x+dx[i]
            if 0<=ny<n and 0<=nx<m and b[ny][nx]:q+=[(ny,nx)];b[ny][nx]=0
    c+=q!=[];l=q
print([c,-1][any(map(any,b))])