d=[0,1,0,-1];D=[1,0,-1,0]
for t in range(int(input())):
    n=int(input());c=0;b=[list(map(int,input().split())) for _ in range(n)];r=1<<30
    for x in range(n):
        for y in range(n):
            k=1;q=[(x,y)]
            while q:
                p=q.pop()
                for i in range(4):
                    X=p[0]+d[i];Y=p[1]+D[i]
                    if 0<=X<n and 0<=Y<n and b[X][Y]-b[p[0]][p[1]]==1:k+=1;q.append((X,Y))
            if k>c:c=k;r=b[x][y]
            elif k==c and b[x][y]<r:r=b[x][y] 
    print(f'#{t+1}',r,c)