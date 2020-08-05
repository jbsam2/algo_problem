for t in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))

    max_val,min_val = 0,987654321
    for i in range(n-m+1):
        tmp = 0
        for j in range(i,i+m):
            tmp += a[j]
        max_val=max(tmp,max_val)
        min_val=min(tmp,min_val)

    print(f'#{t+1}',max_val-min_val)