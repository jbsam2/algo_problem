dx=[1,0,-1,0];dy=[0,1,0,-1]
for t in range(10):
    n=input();b=[[*map(int,input())]for _ in range(100)];r=0;v=[[0]*100 for _ in range(100)];r=0
    for i in range(100):
        for j in range(100):
            if b[i][j]==2:
                q=[(j,i)];v[i][j]=1
                while q:
                    qq=q.pop(0)
                    for i in range(4):
                        ny=qq[0]+dy[i];nx=qq[1]+dx[i]
                        if b[ny][nx]==3:r=1;break
                        if 0<=nx<100 and 0<=ny<100 and v[ny][nx]==0 and b[ny][nx]!=1:q.append((ny,nx));v[ny][nx]=1
                    if r:q.clear()
    print(f'#{t+1}',r)