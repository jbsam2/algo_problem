#1.dfs
d=[0,1,0,-1];D=[1,0,-1,0]
def s(y,x):
    for i in range(4):
        X=x+d[i];Y=y+D[i]
        if b[Y][X]==3:return 1
        if b[Y][X]==0:
            b[Y][X]=1
            if s(Y,X):return 1
for t in range(10):
    input();b=[list(map(int,input()))for _ in range(16)];r=0;x=y=0
    for i in range(16):
        for j in range(16):
            if b[i][j]==2:y=i;x=j
    if s(y,x):r=1
    print(f'#{t+1}',r)

###############################################################################################################################################
#2.bfs
dx=[1,0,-1,0];dy=[0,1,0,-1]
for t in range(10):
    n=input();b=[[*map(int,input())]for _ in range(16)];r=0;v=[[0 for _ in range(16)]for _ in range(16)];r=0
    for i in range(16):
        for j in range(16):
            if b[i][j]==2:
                q=[(j,i)];v[i][j]=1
                while q:
                    qq=q.pop(0)
                    for i in range(4):
                        ny=qq[0]+dy[i];nx=qq[1]+dx[i]
                        if b[ny][nx]==3:r=1;break
                        if 0<=nx<16 and 0<=ny<16 and v[ny][nx]==0 and b[ny][nx]!=1:q.append((ny,nx));v[ny][nx]=1
                    if r:q.clear()
    print(f'#{t+1}',r)