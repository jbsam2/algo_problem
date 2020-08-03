for t in range(int(input())):
    input();d={}
    for i in map(int,input().split()):d[sum(i>d[k]for k in d)]=i
    print(f'#{t+1}',len(d))