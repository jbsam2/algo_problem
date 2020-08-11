for t in range(int(input())):
    input();s=list(map(int,input().split()));d={};m=l=0
    for e in s:
        if e in d:d[e]+=1
        else:d[e]=1
    for e,f in d.items():
        if m<f:m=f;l=e
        elif m==f and l<e:l=e
    print(f'#{t+1}',l)