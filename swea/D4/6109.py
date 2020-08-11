dy=[0, 0, -1, 1];dx=[-1, 1, 0, 0];D={'left':0,'right':1,'up':2,'down':3}
for t in range(int(input())):
    n,s=input().split()
    n=int(n);v=set()
    b=[list(map(int, input().split()))for _ in range(n)]
    if s in 'upleft':k=range(n)
    else:k=range(n-1,-1,-1)
    for i in k:
        for j in k:
            if b[i][j]:
                y,x=i,j
                Y,X=y+dy[D[s]],x+dx[D[s]]
                while 1:
                    if -1<Y<n and -1<X<n:
                        if b[Y][X]==0:
                            b[y][x],b[Y][X]=b[Y][X],b[y][x]
                        elif b[Y][X]==b[y][x] and (Y,X) not in v:
                            v.add((Y,X))
                            b[Y][X]*=2
                            b[y][x]=0
                            break
                        else:break
                        y,x=Y,X
                        Y,X=Y+dy[D[s]],X+dx[D[s]]
                    else:
                        break
    print(f'#{t+1}')
    for i in b:print(*i)