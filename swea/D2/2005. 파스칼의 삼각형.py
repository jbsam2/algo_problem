for t in range(int(input())):
    n=int(input());l=[[1 for i in range(1+j)] for j in range(n)]
    for y in range(2,n):
        for x in range(1,y):l[y][x]=l[y-1][x-1]+l[y-1][x]
    print(f'#{t+1}')
    for i in l:print(*i)