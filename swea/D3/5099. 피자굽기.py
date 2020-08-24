for t in range(int(input())):
    n,m=map(int,input().split());p=list(map(int,input().split()));q=[];k=0
    for i in range(n):q.append([p[i],i+1])
    while len(q)!=1:
        q[0][0]//=2
        if q[0][0]==0:
            if n+k<m:q.pop(0);q.append([p[n+k],n+k+1]);k+=1
            elif n+k>=m:q.pop(0)
        else:q.append(q.pop(0))
    print(f'#{t+1}',q[0][1])