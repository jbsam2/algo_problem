from collections import deque
import heapq

def move2(y,x,n,visit):
    if not (0<=y<n and 0<=x<n):return 0
    if visit[y][x]:return 0
    return 1

def solution(land, height):
    n=len(land)
    visit=[[0 for _ in range(n)]for _ in range(n)]
    dx=[1,-1,0,0];dy=[0,0,1,-1]
    queue=[(0,0,0)]
    cnt=value=0
    while(cnt<n*n):
        v,y,x=heapq.heappop(queue)
        if visit[y][x]:continue
        visit[y][x]=1
        cnt+=1
        value+=v
        c_height=land[y][x]
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if move2(ny,nx,n,visit):
                n_height=land[ny][nx]
                if abs(n_height-c_height)>height:heapq.heappush(queue,(abs(n_height-c_height),ny,nx))
                else:heapq.heappush(queue,(0,ny,nx))
    return value