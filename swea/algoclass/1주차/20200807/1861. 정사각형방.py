dx=[0,1,0,-1];dy=[1,0,-1,0]
for t in range(int(input())):
    n=int(input());c=0;b=[list(map(int,input().split())) for _ in range(n)];r=1<<30
    for x in range(n):
        for y in range(n):
            cnt=1;q=[(x,y)]
            while q:
                qq=q.pop()
                for i in range(4):
                    nx=qq[0]+dx[i];ny=qq[1]+dy[i]
                    if 0<=nx<n and 0<=ny<n and b[nx][ny]-b[qq[0]][qq[1]]==1:cnt+=1;q.append((nx,ny))
            if cnt>c:c=cnt;r=b[x][y]
            elif cnt==c:
                if b[x][y]<r:r=b[x][y] 
    print(f'#{t+1}',r,c)