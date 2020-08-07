for t in range(int(input())):
    n=int(input());l=[50000,10000,5000,1000,500,100,50,10];d=dict.fromkeys(l,0)
    for i in l:d[i]+=n//i;n%=i
    print(f'#{t+1}')
    for i in l:print(d[i],end=' ')
    print()