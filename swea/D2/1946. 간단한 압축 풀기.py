for t in range(int(input())):
    n=int(input());ts=''
    for i in range(n):tc,tv=input().split();ts+=tc*int(tv)        
    print(f'#{t+1}');c=1
    for i in ts:
        print(i,end='')
        if c%10==0:print()
        c+=1
    print()