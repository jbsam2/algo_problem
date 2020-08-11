for t in range(int(input())):
    n=int(input());a=b=c=d=e=0
    while n%11==0:n/=11;e+=1
    while n%7==0:n/=7;d+=1
    while n%5==0:n/=5;c+=1
    while n%3==0:n/=3;b+=1
    while n%2==0:n/=2;a+=1
    print(f'#{t+1}',a,b,c,d,e)