for t in range(int(input())):
    b=sorted([[*map(int,input().split())]for _ in range(int(input()))],key=lambda x:x[1]);ret=0;s=0
    for i in b:
        if s<=i[0]:ret+=1;s=i[1]
    print(f'#{t+1}',ret)