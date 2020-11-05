def sol(p,s):
    global ret
    if p==n:ret=min(ret,s);return
    if ret<s:return
    for i in range(n):
        if i not in v:v.append(i);sol(p+1,s+b[p][i]);v.remove(i)
for t in range(int(input())):n=int(input());b=[[*map(int,input().split())]for _ in range(n)];v=[];ret=1<<32;sol(0,0);print(f'#{t+1}',ret)

for t in range(int(input())):
    n=int(input());m=1<<n;d=[1<<32]*m;p=[[*map(int,input().split())]for _ in range(n)];d[0]=0
    for i in range(m):
        x=bin(i).count('1')
        for j in range(n):
            if(1<<j)&i==0:d[i|(1<<j)]=min(d[i|(1<<j)],d[i]+p[x][j])
    print(f'#{t+1}',d[-1])