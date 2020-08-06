for t in range(int(input())):
    n=int(input());b=[list(map(int,input().split()))for i in range(n)];print(f'#{t+1}')
    for y in range(n):
        for x in range(n):print(b[n-1-x][y],end='')
        print(' ',end='')
        for x in range(n):print(b[n-1-y][n-1-x],end='')
        print(' ',end='')
        for x in range(n):print(b[x][n-1-y],end='')
        print()