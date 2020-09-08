dx=[0,1,0,-1];dy=[1,0,-1,0]
def solution(board):
    n=len(board);cost=[[0]*n for _ in '1'*n];q=[(0,0,0,1)];q.append((0,0,0,0))
    while q:
        y,x,c,d=q.pop(0)
        for i in range(4):
            ny=y+dy[i];nx=x+dx[i]
            if 0<=ny<n and 0<=nx<n and board[ny][nx]==0 and abs(d-i)!=2:
                nc=c+(100 if d==i else 600)
                if cost[ny][nx]==0 or cost[ny][nx]>=nc:cost[ny][nx]=nc;q.append((ny,nx,nc,i))
    return cost[n-1][n-1]