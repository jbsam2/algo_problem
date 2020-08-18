def cal(n,r=0):
    while n>0:
        r+=(n%10);n//=10
    return r
for t in range(int(input())):
    a,b=map(int,input().split());r=0;i=1
    while a>=0 and b>=0:
        while 1:
            if a%10==0 and b%10==9:break
            if a%10!=0:r+=cal(a)*i;a+=1
            if b%10!=9:r+=cal(b)*i;b-=1
        a//=10;b//=10
        r+=(b-a+1)*45*i
        i*=10
    print(f'#{t+1}',r)