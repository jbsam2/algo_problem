for t in range(int(input())):
    n,r=map(int,input().split());s=a=b=1;p=1234567891
    for i in range(r):a*=n-i;a%=p;b*=i+1;b%=p
    m=p-2
    while m>0:
        if m%2:s*=b;s%=p
        b*=b;b%=p;m//=2
    s*=a;s%=p
    print(f'#{t+1}',s)