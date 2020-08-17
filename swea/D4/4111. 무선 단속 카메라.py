for t in range(int(input())):
    input();k=int(input());c=sorted(list(map(int,input().split())));a=[]
    for i in range(len(c)-1):a.append(c[i+1]-c[i])
    a.sort(reverse=True)
    print(f'#{t+1}',sum(a[k-1:]))