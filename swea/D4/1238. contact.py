for t in range(10):
    V=[[]for _ in range(101)];l,s=map(int,input().split());q=[[s]];v=[s];D=[*map(int,input().split())]
    for i in range(l//2):V[D[2*i]]+=[D[2*i+1]]
    while q[-1]:
        q+=[[]]
        for i in q[-2]:
            for j in V[i]:
                if j not in v:v+=[j];q[-1]+=[j]
    print(f'#{t+1}',max(q[-2]))