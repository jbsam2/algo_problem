#bfs
dx=[1,0,-1,0];dy=[0,1,0,-1]
for t in range(10):
    n=input();b=[list(int(x) for x in input()) for _ in range(16)];r=0;v=[[False for _ in range(16)]for _ in range(16)];r=0
    for i in range(16):
        for j in range(16):
            if b[i][j]==2:
                q=[(j,i)];v[i][j]=1
                while q:
                    qq=q.pop()
                    for i in range(4):
                        ny=qq[0]+dy[i];nx=qq[1]+dx[i]
                        if b[ny][nx]==3:r=1;break
                        if 0<=nx<16 and 0<=ny<16 and v[ny][nx]==0 and b[ny][nx]!=1:q.append((ny,nx));v[ny][nx]=1
                    if r:q.clear()
    print(f'#{t+1}',r)

#dfs
d=[1,0,-1,0];D=[0,1,0,-1]
def s(y,x):
    global v,r
    if b[y][x]==3:r=1;return
    v[y][x]=1
    for i in range(4):
        Y=y+D[i];X=x+d[i]
        if 0<=X<16 and 0<=Y<16 and v[Y][X]==0 and b[Y][X]!=1:s(Y,X)
    v[y][x]=0 
for t in range(10):
    n=input();b=[list(int(x) for x in input()) for _ in range(16)];r=0;v=[[False for _ in range(16)]for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if b[i][j]==2:y=i;x=j
    s(y,x)
    print(f'#{t+1}',r)