for t in range(int(input())):
    n,m=map(int,input().split());b=[[int(x) for x in input().split()] for y in range(n)];a=0
    for y in range(n-m+1):
        for x in range(n-m+1):
            k=0
            for i in range(m):
                for j in range(m):k+=b[y+i][x+j]
            a=max(a,k)
    print(f'#{t+1}',a)