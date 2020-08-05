for t in range(int(input())):
    n,a,b=map(int,input().split());d=987654321
    for c in range(1,(n//2)+1):
        for r in range(c,n//c+1):
            p=a*(r-c)+b*(n-r*c);d=min(d,p)
    print(f'#{t+1}',d)