def sol(k,n,u,r):
    global a
    if r>=a:return
    if k==n:a=min(a,r);return
    for i in range(n):
        if u&1<<i:continue
        sol(k+1,n,u|1<<i,r+l[k][i])

for t in range(int(input())):
    l=[list(map(int,input().split()))for _ in range(int(input()))];a=1<<32;sol(0,len(l),0,0);print(f'#{t+1}',a)