for t in range(int(input())):
    n=int(input());r=0
    for i in range(1,n+1):
        if i%2:r+=i
        else:r-=i
    print(f'#{t}',r)