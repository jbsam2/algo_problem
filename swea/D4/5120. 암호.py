for t in range(int(input())):
    n,m,k=map(int,input().split());l=[*map(int,input().split())];i=0;s=l[i]
    for _ in range(k):
        i+=m
        if i>len(l):i-=len(l)
        if i==len(l):l.append(l[-1]+s)
        else:l.insert(i,l[i-1]+l[i])
    print('#{}'.format(t+1),*l[-1:-11:-1])