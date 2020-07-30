t = int(input())

for tc in range(1,t+1):
    n, a, b = map(int, input().split())
    ret1= min(a, b)
    if a + b >= n:
        ret2 = a + b - n
    else:
        ret2 = 0
    print(f'#{tc} {ret1} {ret2}')