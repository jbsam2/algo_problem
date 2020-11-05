import heapq
dx=[1,0,-1,0];dy=[0,1,0,-1]
for t in range(int(input())):
    n=int(input());b=[[*map(int,input().split())]for _ in range(n)];d=[[1<<32]*n for _ in range(n)]
    d[0][0]=0;pq=[];heapq.heappush(pq,[d[0][0],0,0])
    while pq:
        dist,y,x=heapq.heappop(pq)
        if d[y][x]<dist:continue
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                th=b[ny][nx]-b[y][x];td=dist+1+(th if th>0 else 0)
                if d[ny][nx]>td:d[ny][nx]=td;heapq.heappush(pq,[td,ny,nx])
    print(f'#{t+1}',d[n-1][n-1])