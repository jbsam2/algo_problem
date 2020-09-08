dx=[1,-1,-1,1];dy=[1,1,-1,-1]
def sol(y,x,d,r):
    global a
    if not (-1<y<n and -1<x<n) or d>3:return
    if d==3 and (y,x)==(i,j):a=max(r,a);return
    if v[b[y][x]]:return
    v[b[y][x]]=1;ny,nx=y+dy[d],x+dx[d];sol(ny,nx,d,r+1);sol(ny,nx,d+1,r+1);v[b[y][x]]=0
for t in range(int(input())):
    n=int(input());b=[[int(x)for x in input().split()]for y in range(n)];a=-1;v=[0]*101
    for i in range(n-2):
        for j in range(1,n-1):sol(i,j,0,0)
    print(f'#{t+1}',a)