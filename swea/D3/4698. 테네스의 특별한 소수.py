p=list(range(2,1000000));n=2
while n<1000000:
    if p[n-2]:
        t=2*n-2
        while t<999998:p[t]=0;t+=n
    n+=1

for t in range(int(input())):
    d,a,b=map(int,input().split());r=0
    for i in p:
        if i<a:continue
        elif i>b:break
        else:
            if str(d) in str(i):r+=1
    print(f'#{t+1}',r)