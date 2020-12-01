dx=[1,-1,0,0];dy=[0,0,1,-1]
def sol(x,y,prev,dig,check):
    global ret
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<n and 0<=nx<n and (ny,nx) not in check:
            if b[ny][nx]<prev:
                sol(nx,ny,b[ny][nx],dig,check+[(ny,nx)])
            elif b[ny][nx]-k<prev and dig:
                sol(nx,ny,prev-1,0,check+[(ny,nx)])
            else:
                ret=max(ret,len(check))
for t in range(int(input())):
    n,k=map(int,input().split())
    b=[[*map(int,input().split())]for _ in range(n)]
    sn=ret=0
    sl=[]
    for i in range(n):
        for j in range(n):
            if sn<b[i][j]:
                sn=b[i][j]
                sl=[(i,j)]
            elif sn==b[i][j]:
                sl.append((i,j))
    for i in sl:
        check=[i]
        sol(i[1],i[0],sn,1,check)
    print(f'#{t+1}',ret)