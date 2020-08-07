for t in range(int(input())):
    l=list(map(int,input().split()));h=l[0]+l[2];m=l[1]+l[3]
    if m>=60:h+=1;m-=60
    print(f'#{t+1}',(h-1)%12+1,m)