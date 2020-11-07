'''from collections import deque
dx=[0,0,1,-1];dy=[1,-1,0,0] 
for t in range(int(input())):
    n=int(input());m=[[*map(int, list(input()))]for _ in range(n)]
    d=[[1<<32]*n for _ in range(n)];d[0][0]=0;q=deque();q.append((0,0))
    while q:
        y,x=q.popleft()
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<n:
                if d[ny][nx]>d[y][x]+m[ny][nx]:d[ny][nx]=d[y][x]+m[ny][nx];q.append((ny,nx))
    print(f'#{t+1}',d[n-1][n-1])'''


import heapq
dx=[1,0,-1,0];dy=[0,1,0,-1]
for t in range(int(input())):
    n=int(input());b=[[*map(int,[*input()])]for _ in range(n)];d=[[1<<32]*n for _ in range(n)]
    d[0][0]=b[0][0];pq=[];heapq.heappush(pq,[d[0][0],0,0])
    while pq:
        dist,y,x=heapq.heappop(pq)
        if d[y][x]<dist:continue
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                td=dist+b[ny][nx]
                if d[ny][nx]>td:d[ny][nx]=td;heapq.heappush(pq,[td,ny,nx])
    print(f'#{t+1}',d[n-1][n-1])