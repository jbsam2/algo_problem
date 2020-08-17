def s(v):
    r=0;i=0
    while v//(10**i)>0:
        c=(v%(10**(i+1)))//(10**i)
        if c>4:c-=1
        r+=c*(9**i);i+=1
    return r
for t in range(int(input())):
    a,b=map(int,input().split());A=s(abs(a));B=s(abs(b))
    if a>0:print(f'#{t+1}',B-A)
    elif b<0:print(f'#{t+1}',A-B)
    else:print(f'#{t+1}',B+A-1)