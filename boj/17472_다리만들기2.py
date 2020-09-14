dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(sx,sy,cnt):
    board[sx][sy] = cnt
    Q = []
    Q.append((sx, sy))
    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 1:
                    board[nx][ny] = cnt
                    Q.append((nx, ny))
    return

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 2
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            bfs(i,j,cnt)
            cnt+=1
G = []
p = list(range(cnt))
for i in range(N):
    for j in range(M):
        if board[i][j] > 1:
            cmp = board[i][j]
            for k in range(4):
                nx, ny = i, j
                t =0
                while True:
                    t+=1
                    nx, ny = nx + dx[k], ny + dy[k]
                    if nx<0 or nx>=N or ny<0 or ny>=M:
                        break
                    if board[nx][ny]==cmp:
                        break
                    if board[nx][ny]!=0 and board[nx][ny]!=cmp:
                        if (cmp-1,board[nx][ny]-1,t-1) not in G and t>2:
                          G.append((cmp-1,board[nx][ny]-1,t-1))
                        break
G.sort(key=lambda x:x[2])
result = 0
def find_set(x):
    if x!=p[x]:
        p[x] = find_set(p[x])
    return p[x]
idx, choice = 0, []
while len(choice)<cnt-3 and G:
    u,v,w = G.pop(0)
    a,b = find_set(u), find_set(v)
    if a != b:
        p[b] = a
        choice.append(G[idx])
        result += w
if not G:
    print(-1)
else:
    print(result)