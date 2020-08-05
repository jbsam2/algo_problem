for t in range(int(input())):
    n,m=map(int,input().split());r='';b=[input() for _ in range(n)]
    for ro in range(n):
        for co in range(n-m+1):
            if b[ro][co:co+m]==b[ro][co:co+m][::-1]:r=b[ro][co:co+m]    
    for ro in range(n-m+1):
        for co in range(n):
            p=[]
            for i in range(m):p.append(b[ro+i][co])
            if p==p[::-1]:r=str(''.join(p))
    print(f'#{t+1}',r)