for t in range(int(input())):
    n,m=map(int,input().split());a=[i for i in range(n+1)]
    for i in range(m):x,y=map(int,input().split());a=[a[y]if j==a[x] else j for j in a]
    print(f'#{t+1}',len(set(a[1:])))