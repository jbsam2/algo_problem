for t in range(int(input())):
    n = int(input())
    data = [[*map(int, input().split())] for _ in range(n)]
    dist_list = []
    for i in range(n - 1):
        x1, y1, d1, k1 = data[i]
        for j in range(i + 1, n):
            x2, y2, d2, k2 = data[j]
            if d1 == 0:
                if x1 == x2 and y2 > y1 and d2 == 1:
                    dist_list.append((i, j, y2 - y1))
                elif (0 < y2 - y1 == x1 - x2 and d2 == 3) or (0 < y2 - y1 == x2 - x1 and d2 == 2):
                    dist_list.append((i, j, (y2 - y1) * 2))
            elif d1 == 1:
                if x1 == x2 and y1 > y2 and d2 == 0:
                    dist_list.append((i, j, y1 - y2))
                elif (0 < y1 - y2 == x1 - x2 and d2 == 3) or (0 < y1 - y2 == x2 - x1 and d2 == 2):
                    dist_list.append((i, j, (y1 - y2) * 2))
            elif d1 == 2:
                if y1 == y2 and x1 > x2 and d2 == 3:
                    dist_list.append((i, j, x1 - x2))
                elif (0 < x1 - x2 == y1 - y2 and d2 == 0) or (0 < x1 - x2 == y2 - y1 and d2 == 1):
                    dist_list.append((i, j, (x1 - x2) * 2))
            elif d1 == 3:
                if y1 == y2 and x2 > x1 and d2 == 2:
                    dist_list.append((i, j, x2 - x1))
                elif (0 < x2 - x1 == y1 - y2 and d2 == 0) or (0 < x2 - x1 == y2 - y1 and d2 == 1):
                    dist_list.append((i, j, (x2 - x1) * 2))
    dist_list.sort(key=lambda x: x[2])
    dist = 0
    crash = set()
    crashed = []
    for i, j, d in dist_list:
        if d > dist:
            dist = d
            crashed.extend(crash)
            crash = set()
        for cr in crashed:
            if cr == i or cr == j:break
        else:
            crash.add(i)
            crash.add(j)
    crashed.extend(crash)
    ret = 0
    for idx in crashed:
        ret += data[idx][3]
    print(f'#{t+1}',ret)