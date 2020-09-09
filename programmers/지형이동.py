from collections import deque
import heapq

def move2(y, x, N, visited):
    if not (0 <= y < N and 0 <= x < N): # 범위 밖
        return 0
    if visited[y][x]: # 방문했을 경우
        return 0
    return 1

def solution(land, height):
    N = len(land)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = []
    queue.append((0,0,0))
    visit_count = 0
    max_count = N * N
    value = 0
    while(visit_count < max_count):
        v, y, x = heapq.heappop(queue)
        if visited[y][x]:
            continue
        visited[y][x] = 1

        visit_count += 1
        value += v

        c_height = land[y][x]
        for ay, ax in move:
            ny, nx = y + ay, x + ax
            if move2(ny, nx, N, visited):
                n_height = land[ny][nx]

                if abs(n_height - c_height) > height:
                    heapq.heappush(queue, (abs(n_height - c_height), ny, nx))
                else:
                    heapq.heappush(queue, (0, ny, nx))

    return value