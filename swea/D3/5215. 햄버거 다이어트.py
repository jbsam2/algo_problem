for tc in range(1, int(input())+1):
    c = [0]*10001
    n,l = map(int,input().split())
    for i in range(n):
        t,k = map(int,input().split())
        for j in range(l, k+1, -1):
            if c[j] < c[j-k] + t:
                c[j] = c[j-k] + t
    print(f'#{tc} {c[l]}')