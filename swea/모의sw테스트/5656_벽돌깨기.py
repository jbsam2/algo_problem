from collections import deque
from itertools import product
from copy import deepcopy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bomb(power, y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < w and 0 <= nx < h:
            q.append((power - 1, ny, nx, i))


for t in range(int(input())):
    n, w, h = map(int, input().split())
    my_map = [deque() for _ in range(w)]
    b_cnt = [0 for _ in range(w)]
    for _ in range(h):
        temp = [*map(int, input().split())]
        for i in range(w):
            my_map[i].appendleft(temp[i])
            if temp[i]:
                b_cnt[i] += 1

    ret = 1<<32
    q = deque()
    for balls in product(range(w), repeat=n):
        sub_map = deepcopy(my_map)
        block_cnt = b_cnt[:]
        for y in balls:
            remove_cnt = [0 for _ in range(w)]
            if block_cnt[y]:
                x = block_cnt[y] - 1
            else:continue
			
            remove_cnt[y] += 1
            power = sub_map[y][x]
            sub_map[y][x] = 0

            if power > 1:
                bomb(power, y, x)

            while q:
                fire, y, x, i = q.pop()
                if sub_map[y][x]:
                    remove_cnt[y] += 1
                    power = sub_map[y][x]
                    sub_map[y][x] = 0
                    if power > 1:
                        bomb(power, y, x)
                if fire > 1:
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < w and 0 <= nx < h:
                        q.append((fire - 1, ny, nx, i))

            for r in range(w):
                block_cnt[r] -= remove_cnt[r]
                for _ in range(remove_cnt[r]):
                    sub_map[r].remove(0)
                    sub_map[r].append(0)

        cnt = sum(block_cnt)
        ret = min(ret,cnt)
        if not cnt:break
    print(f'#{t+1}',ret)