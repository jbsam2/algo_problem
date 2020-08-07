for t in range(int(input())):
    n=int(input());h=[];c=0
    for i in range(n):h.append(int(input()))
    a=sum(h)/n
    for i in range(n):c+=abs(a-h[i])
    print(f'#{t+1}',int(c//2))