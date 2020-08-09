for t in range(int(input())):
    n,m = map(int, input().split())
    list_n = list(map(int, input().split()))
    list_m = list(map(int, input().split()))
    ret = -987654321
    if n < m:
        for x in range(m-n+1):
            tmp = 0
            for y in range(n):
                tmp += list_n[y] * list_m[y+x]
            if tmp > ret:
                ret = tmp
    else:
        for x in range(n-m+1):
            tmp = 0
            for y in range(m):
                tmp += list_m[y] * list_n[y+x]
            if tmp > ret:
                ret = tmp
    print(f'#{t+1}',ret)