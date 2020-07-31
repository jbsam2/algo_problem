for t in range(1,int(input())+1):
    n, m = map(int,input().split())
    edge = list([0 for j in range(n+1)] for i in range(n+1))
    for i in range(m):
        tmp1, tmp2 = map(int,input().split())
        edge[tmp1][tmp2] = 1
        edge[tmp2][tmp1] = 1
    cnt = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if edge[j][i] == 0:
                continue
            for k in range(j+1,n+1):
                if edge[k][i] == 0:
                    continue
                if edge[k][j] == 0:
                    continue
                cnt += 1
    print(f'#{t} {cnt}')