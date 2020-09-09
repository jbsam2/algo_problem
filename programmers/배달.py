def solution(N, road, K):
    answer = 0
    b=[[]for _ in range(N+1)]
    for i in road:
        b[i[0]].append((i[1],i[2]))
        b[i[1]].append((i[0],i[2]))
    q=[(1,0)];times=[0,0]+[9999999999]*N
    while q:
        v,time=q.pop()
        for i in b[v]:
            ntime=time+i[1]
            if times[i[0]]>=ntime:
                times[i[0]]=ntime
                q.append((i[0],ntime))
    for i in range(1,N+1):
        if times[i]<=K:answer+=1
    return answer