for t in range(int(input())):
    n,m=map(int,input().split());b=[[0]*(n+1) for _ in range(n+1)];d=[0,1,-1]
    b[n//2][n//2]=2;b[n//2+1][n//2+1]=2;b[n//2+1][n//2]=1;b[n//2][n//2+1]=1
    for _ in range(m):
        y,x,z=map(int,input().split());b[y][x]=z
        for i in d:
            for j in d:
                if i==j==0:continue
                ny=y+i;nx=x+j;c=1
                while 0<nx<=n and 0<ny<=n:
                    if b[ny][nx]==0:break
                    if b[ny][nx]==z:
                        for p in range(c):b[y+i*p][x+j*p]=z
                        break
                    ny+=i;nx+=j;c+=1
    s=sum(b,[]);print('#{} {} {}'.format(t+1,s.count(1),s.count(2)))