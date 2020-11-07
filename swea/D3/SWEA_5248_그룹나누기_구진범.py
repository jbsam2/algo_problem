for t in range(int(input())):
    n,m=map(int,input().split());l=[*map(int,input().split())];p=[i for i in range(n+1)]
    for i in range(m):p=[p[l[2*i+1]]if j==p[l[2*i]] else j for j in p]
    print(f'#{t+1}',len(set(p[1:])))