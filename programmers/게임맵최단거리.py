def solution(maps):
    n=len(maps);m=len(maps[0])
    dx=[1,-1,0,0];dy=[0,0,1,-1]
    q=[(0,0,1)]
    while q:
        y,x,l=q.pop(0)       
        for i in range(4):
            ny=y+dy[i];nx=x+dx[i]
            if ny==n-1 and nx==m-1:return l+1
            if 0<=ny<n and 0<=nx<m and maps[ny][nx]:q.append((ny,nx,l+1));maps[ny][nx]=0
    return -1