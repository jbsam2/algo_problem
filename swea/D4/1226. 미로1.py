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