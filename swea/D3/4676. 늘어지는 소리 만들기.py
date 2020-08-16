for t in range(1,int(input())+1):
    s=list(input());h=int(input());p=sorted(list(map(int,input().split())),reverse=True)
    for i in p:s.insert(i,'-')
    print(f'#{t}',''.join(s))