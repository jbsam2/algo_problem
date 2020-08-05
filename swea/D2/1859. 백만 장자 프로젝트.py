for t in range(int(input())):
    n=int(input());r=0;l=list(map(int,input().split()));m=l[n-1]
    for i in l[n-2::-1]:
        if i<=m:r+=(m-i)
        else:m=i
    print(f'#{t+1}',r)