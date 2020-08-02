for t in range(int(input())):
    d,h,m=map(int,input().split())
    a=d*1440+h*60+m-16511
    print(f'#{t+1} {a if a>=0 else-1}')