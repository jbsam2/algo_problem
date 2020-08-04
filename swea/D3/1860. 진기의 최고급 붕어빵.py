for t in range(int(input())):
    n,m,k=map(int,input().split());times=sorted(list(map(int,input().split())));r='Possible'
    for time in times:
        if (time//m)*k-times.index(time)-1<0:r='Impossible';break
    print(f'#{t+1}',r)