dx=[1,0,-1,0];dy=[0,1,0,-1]
def sol(y,x):
    global v,r
    if b[y][x]==3:r=1;return
    v[y][x]=1
    for i in range(4):
        ny=y+dy[i];nx=x+dx[i]
        if 0<=nx<16 and 0<=ny<16 and v[ny][nx]==0 and b[ny][nx]!=1:sol(ny,nx)
    v[y][x]=0

for t in range(10):
    n=input();b=[list(int(x) for x in input()) for _ in range(16)];r=0;v=[[False for _ in range(16)]for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if b[i][j]==2:y=i;x=j
    sol(y,x)
    print(f'#{t+1}',r)