m,n,h=map(int,input().split())
ze=[];on=[]
for k in range(h):
    for i in range(n):
        for j,c in enumerate(input().split()):
            if c=='0':ze+=[(j,i,k)]
            elif c=='1':on+=[(j,i,k)]
ze=set(ze);on=set(on)
dx=[1,-1,0,0,0,0];dy=[0,0,1,-1,0,0];dz=[0,0,0,0,1,-1]
c=0;q=[]
while on:
    x,y,z=on.pop()
    for i in range(6):
        nx=x+dx[i];ny=y+dy[i];nz=z+dz[i]
        if (nx,ny,nz) in ze:ze-={(nx,ny,nz)};q.append((nx,ny,nz))
    if not on:
        if not q:
            if ze:print(-1)
            else:print(c)
            break
        c+=1;on=q;q=[]