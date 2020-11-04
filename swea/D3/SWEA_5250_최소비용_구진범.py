dx=[1,0,-1,0];dy=[0,1,0,-1]
def sol():
    f=[[1<<32]*n for _ in range(n)]
    chk=[[0]*n for _ in range(n)]
    f[0][0]=0;check=set();check.add((0,0))
    while 1:
        m_f=1<<32
        for r,c in check:
            if f[r][c]<m_f and chk[r][c]==0:m_f=f[r][c];y,x=r,c
        chk[y][x]=1;check.remove((y, x))
        if y==x==n-1:return f[y][x]
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and chk[ny][nx]==0:
                t=b[ny][nx]-b[y][x]
                nf=f[y][x]+1+(t if t>0 else 0)
                if nf<f[ny][nx]:f[ny][nx]=nf;check.add((ny,nx))
for t in range(int(input())):n=int(input());b=[[*map(int,input().split())]for _ in range(n)];print(f'#{t+1}',sol())