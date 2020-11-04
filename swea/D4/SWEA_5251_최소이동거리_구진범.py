for t in range(int(input())):
    n,e=map(int,input().split());b=[[]for _ in range(n)];d=[1<<32]*(n+1);v=[0]*(n+1);chk=set();chk.add(0);d[0]=0
    for _ in range(e):s,f,w=map(int,input().split());b[s].append((f,w))
    while 1:
        m_d=1<<32;s=-1
        for i in chk:
            if d[i]<m_d:m_d=d[i];s=i
        v[s]=1;chk.remove(s)
        if s==n:print(f'#{t+1}',d[s]);break
        for f,w in b[s]:
            if d[f]>d[s]+w and v[f]==0:d[f]=d[s]+w;chk.add(f)