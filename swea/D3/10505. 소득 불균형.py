for t in range(int(input())):
    input();n=list(map(int,input().split()));a=sum(n)/len(n);c=0
    for i in n:
        if i<=a:c+=1
    print(f'#{t+1}',c)