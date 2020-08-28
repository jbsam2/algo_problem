def solution(board):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    size = len(board)
    visited = [[-1] * size for x in range(size)]
    q = []
    q.append([0, 0, 0, 0])
    q.append([0, 0, 0, 1])
    visited[0][0] = 0
    while q:
        y, x, cost_now, direction = q.pop(0)
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]            
            if ny < 0 or ny >= size or nx < 0 or nx >= size:
                continue
            if board[ny][nx] == 1:
                continue
            if abs(direction -  d) == 2:
                continue
            new_cost = cost_now + (100 if direction == d else 600)
            if visited[ny][nx] == -1 or visited[ny][nx] >= new_cost:
                visited[ny][nx] = new_cost
                q.append([ny, nx, new_cost, d])
    return visited[size-1][size-1]