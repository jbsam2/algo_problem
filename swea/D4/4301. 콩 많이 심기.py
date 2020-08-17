for t in range(int(input())):
    n,m=map(int,input().split());a=0
    for i in range(n):
        for j in range(m):
            if (i//2+j//2)%2==0:a+=1
    print(f'#{t+1}',a)