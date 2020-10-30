def sol(c,r,j,i,k,l):
    global f
    if c==n:f+=[r]
    if j: sol(c+1,r+a[c],j-1,i,k,l)
    if i: sol(c+1,r-a[c],j,i-1,k,l)
    if k: sol(c+1,r*a[c],j,i,k-1,l)
    if l: sol(c+1,int(r/a[c]),j,i,k,l-1)
for t in range(int(input())):n=int(input());s=[*map(int,input().split())];a=[*map(int,input().split())];f=[];sol(1,a[0],s[0],s[1],s[2],s[3]);print(f'#{t+1}',max(f)-min(f))