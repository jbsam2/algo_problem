for t in range(int(input())):
    n,m=map(int,input().split());l=[[] for i in range(n+1)];chk=[0]*(n+1)
    for i in range(m):a,b=map(int,input().split());l[a].append(b);l[b].append(a)
    q=[1];chk[1]=1;c=d=0
    while q:
        s=len(q)
        for j in range(s):
            f=q.pop(0)
            for i in l[f]:
                if chk[i]==0:q.append(i);chk[i]=1;c+=1
        d+=1
        if d==2:break
    print(f'#{t+1}',c)