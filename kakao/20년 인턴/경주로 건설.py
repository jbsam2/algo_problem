def solution(board):
    dy=[0,1,0,-1];dx=[1,0,-1,0];n=len(board);cost=[[0]*n for _ in range(n)];q=[];q.append([0,0,0,0]);q.append([0,0,0,1])
    while q:
        y,x,c,d=q.pop(0)
        for i in range(4):
            ny=y+dy[i];nx=x+dx[i]
            if ny<0 or ny>=n or nx<0 or nx>=n or board[ny][nx] or abs(d-i)==2:continue
            nc=c+(100 if d==i else 600)
            if cost[ny][nx]==0 or cost[ny][nx]>=nc:cost[ny][nx]=nc;q.append([ny,nx,nc,i])
    return cost[n-1][n-1]