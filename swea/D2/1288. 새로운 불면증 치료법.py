for t in range(int(input())):
    n=input();s=set();m=int(n)
    while 1:
        for i in n:s.add(i)
        if len(s)==10:break
        n=str(int(n)+m)
    print(f'#{t+1}',n)