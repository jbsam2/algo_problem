for t in range(10):
    n=int(input());b=list(map(int,input().split()));r=0
    for i in range(2,n-2):
        a=max(b[i-1],b[i-2],b[i+1],b[i+2])
        if b[i]>a:r+=b[i]-a
    print(f'#{t+1}',r)