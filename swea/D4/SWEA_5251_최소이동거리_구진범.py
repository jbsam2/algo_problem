import heapq
for t in range(int(input())):
    n,e=map(int,input().split());b=[[]for _ in range(n+1)]
    for _ in range(e):s,f,w=map(int,input().split());b[s].append((f,w))
    d=[1<<32]*(n+1);d[0]=0;pq=[];heapq.heappush(pq,[d[0],0])
    while pq:
        dist,pos=heapq.heappop(pq)
        if d[pos]<dist:continue
        for np,w in b[pos]:
            td=dist+w
            if td<d[np]:d[np]=td;heapq.heappush(pq,[td,np])
    print(f'#{t+1}',d[n])