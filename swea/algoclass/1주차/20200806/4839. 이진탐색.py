def count(p,a):
    s=1;f=p;c=0
    while s<=f:
        m=(s+f)//2
        if m==a:break
        elif m<a:s=m;c+=1
        else:f=m;c+=1
    return c
for t in range(int(input())):
    p,a,b=map(int,input().split())
    i=count(p,a);j=count(p,b)
    if i<j:print(f'#{t+1}','A')
    elif i>j:print(f'#{t+1}','B')
    else:print(f'#{t+1}',0)