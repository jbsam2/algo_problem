for t in range(int(input())):
    n=int(input());b=[[] for _ in range(n)];a=0
    for i in range(n):
        for j in input():
            b[i].append(int(j))
    for i in range((n//2)+1):
        a += sum(b[i][(n//2)-i:(n//2)+i+1])
    for i in range((n//2)+1,n):
        a += sum(b[i][i+(n//2)+1-n:(2*n)-(i+(n//2)+1)])
    print(f'#{t+1}',a)