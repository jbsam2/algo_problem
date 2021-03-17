for t in range(int(input())):
    n,m = map(int, input().split())
    b = [[*map(int, input().split())] for _ in range(n)]
    h = []
    for r in range(n):
        for c in range(n):
            if b[r][c]:
                h.append((r, c))
    ret=1
    for i in range(2, n + 2):
        for r in range(n):
            for c in range(n):
                cnt = 0
                for y, x in h:
                    if abs(r - y) + abs(c - x) < i:
                        cnt += 1
                if cnt > ret and cnt * m >= i**2 + (i-1)**2:
                    ret = cnt
    print(f'#{t+1}',ret)