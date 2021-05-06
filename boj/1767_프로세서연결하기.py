for t in range(int(input())):
    n=int(input());m=[];c=[]
    for i in range(n):
        l=[*map(int, input().split())];m.append(l)
        if 0 < i < n - 1:
            for j in range(1, n - 1):
                if l[j]:c.append((i, j))
    a=[0,n*n];q=[(0,0,0,m)]
    while q:
        i,C,W,b=q.pop()
        if i==len(c):
            if C>a[0] or (C==a[0] and W<a[1]):a=[C,W] 
        else:
            q.append((i+1,C,W,[l[:] for l in b])) 
            for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
                y,x=c[i];y+=dy;x+=dx;w=W;m2=[l[:] for l in b]
                while 0<=y<n and 0<=x<n and b[y][x]==0:m2[y][x]=1;w+=1;y+=dy;x+=dx
                if y==-1 or y==n or x==-1 or x==n:q.append((i+1,C+1,w,m2))
    print(f'#{t+1}',a[1])