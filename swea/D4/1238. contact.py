for t in range(10):
    c=[[]for _ in range(101)];l,s=map(int,input().split());q=[[s]];v=[s];d=[*map(int,input().split())]
    for i in range(l//2):c[d[2*i]]+=[d[2*i+1]]
    while q[-1]:
        q+=[[]]
        for i in q[-2]:
            for j in c[i]:
                if j not in v:v+=[j];q[-1]+=[j]
    print(f'#{t+1}',max(q[-2]))