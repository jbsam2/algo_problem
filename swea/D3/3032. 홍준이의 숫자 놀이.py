def sol(a,b):
    global x1,x2,y1,y2
    x1=y2=1;y1=x2=0
    while 1:
        if a==1:return 1
        if b==1:return 2
        if a*b==0: return 0
        x1-=(a//b)*x2;y1-=(a//b)*y2;a%=b
        x2-=(b//a)*x1;y2-=(b//a)*y1;b%=a

for t in range(int(input())):
    a,b=map(int,input().split());r=sol(a,b)
    if r==1:print(f'#{t+1}',x1,y1)
    elif r==2:print(f'#{t+1}',x2,y2)
    else:print(f'#{t+1}',-1)