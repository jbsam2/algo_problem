for t in range(int(input())):
    n=int(input());l=list(map(int,input().split()));s=0;m=-1000
    for i in range(n):
        s+=l[i];m=max(m,s)
        if s<0:s=0
    print(f'#{t+1}',m)