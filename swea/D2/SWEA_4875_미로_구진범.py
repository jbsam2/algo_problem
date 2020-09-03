def sol(y,x):
    global a
    if b[y][x]==3:a=1;return
    v.append((y,x))
    for d in range(4):
        ny=y+dy[d];nx=x+dx[d]
        if 0<=ny<n and 0<=nx<n and b[ny][nx]!=1 and (ny,nx) not in v:sol(ny,nx)

for t in range(int(input())):
    n=int(input());b=[[*map(int,input())]for _ in range(n)];v=[];a=0;dy=[-1,1,0,0];dx=[0,0,-1,1]
    for i in range(n):
        for j in range(n):
            if b[i][j]==2:y,x=i,j    
    sol(y,x);print(f'#{t+1}',a)