t = int(input())

for tc in range(1,t+1):
    p, q, r, s, w = map(int, input().split())
    cost_a = p * w
    cost_b = 0
    if w > r:
        cost_b = q + (w-r) * s
    else:
        cost_b = q
    print(f'#{tc} {min(cost_a,cost_b)}')