for t in range(int(input())):
    s=[0]*200
    for _ in range(int(input())):
        a,b=map(int,input().split());a=(a-1)//2;b=(b-1)//2
        if a>b:a,b=b,a
        for i in range(a,b+1):s[i]+=1
    print(f'#{t+1}',max(s))