I=[0,0,-1,1];J=[-1,1,0,0];D={'left':0,'right':1,'up':2,'down':3}
for t in range(int(input())):
    n,s=input().split();n=int(n);b=[list(map(int,input().split()))for _ in range(n)];c=set()
    k=range(n) if s in 'upleft' else range(n-1,-1,-1)
    for i in k:
        for j in k:
            if b[i][j]:
                y,x=i,j;Y,X=y+I[D[s]],x+J[D[s]]
                while -1<Y<n and -1<X<n:
                    if b[Y][X]==0:b[y][x],b[Y][X]=b[Y][X],b[y][x]
                    elif b[y][x]==b[Y][X] and (Y,X) not in c:c.add((Y,X));b[Y][X]*=2;b[y][x]=0;break
                    else:break
                    y,x=Y,X;Y+=I[D[s]];X+=J[D[s]]
    print(f'#{t+1}')
    for i in b:print(*i)