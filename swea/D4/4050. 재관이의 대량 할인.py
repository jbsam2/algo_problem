for t in range(int(input())):
    input();c=sorted(list(map(int,input().split())),reverse=True);d=[]
    for i,j in enumerate(c):
        if i%3!=2:d.append(j)
    print(f'#{t+1}',sum(d))