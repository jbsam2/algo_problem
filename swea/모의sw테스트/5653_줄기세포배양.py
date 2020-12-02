dx = [0, 0, -1, 1];dy = [-1, 1, 0, 0]
for t in range(int(input())):
    n, m, k = map(int, input().split())
    b = [[*map(int, input().split())] + [0] * k for _ in range(n)] + [[0] * (m + k) for _ in range(k)]
    live = [0] + [[] for _ in range(10)]
    for i in range(n):
        for j in range(m):
            if b[i][j]:
                live[b[i][j]].append([i, j, b[i][j]])
    for _ in range(k):
        for power in range(10, 0, -1):
            cells = live[power]
            new = []
            dead = []
            for i in range(len(cells)-1, -1, -1):
                cells[i][2] -= 1
                y, x, HP = cells[i]
                if HP == -1:
                    for d in range(4):
                        ny, nx = (y + dy[d]) % (n + k), (x + dx[d]) % (m + k)
                        if not b[ny][nx]:
                            b[ny][nx] = power
                            new.append([ny, nx, power])
                if HP == - power:
                    dead.append(i)
            for idx in dead:
                cells.pop(idx)
            cells += new
    ret = 0
    for i in range(1, 11):
        ret += len(live[i])
    print(f'#{t+1}',ret)