from collections import deque

def solution(board):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    N = len(board)
    visited = [[-1] * N for _ in range(N)]
    Q = deque()
    Q.append([0, 0, 0, 0]) # 비용, y, x, 방향
    Q.append([0, 0, 0, 1])
    visited[0][0] = 0
    while Q:
        now_cost, y, x, d = Q.popleft()
        for dire in range(4):
            ny = y + dy[dire]
            nx = x + dx[dire]

            # 경계체크
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            # 벽체크
            if board[ny][nx] == 1:
                continue
            # 뒤로가기 체크
            if abs(dire-d) == 2:
                continue
            cost = 100 if dire == d else 600
            new_cost = now_cost + cost
            if visited[ny][nx] == -1 or new_cost <= visited[ny][nx]:
                visited[ny][nx] = new_cost
                Q.append([new_cost, ny, nx, dire]) 

    return visited[N-1][N-1]