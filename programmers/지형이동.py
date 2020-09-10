import heapq

def solution(land, height):
    n=len(land)
    visit=[[1]*n for _ in range(n)]
    dx=[1,-1,0,0];dy=[0,0,1,-1]
    queue=[(0,0,0)]
    cnt=value=0
    while(cnt<n*n):
        v,y,x=heapq.heappop(queue)
        if visit[y][x]==0:continue
        visit[y][x]=0;cnt+=1;value+=v
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<n and visit[ny][nx]:
                diff=abs(land[ny][nx]-land[y][x])
                if diff>height:heapq.heappush(queue,(diff,ny,nx))
                else:heapq.heappush(queue,(0,ny,nx))
    return value