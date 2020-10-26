for T in range(int(input())):
    n,m=map(int,input().split());ret=0
    w=sorted([*map(int,input().split())],reverse=True)
    t=sorted([*map(int,input().split())],reverse=True)
    for i in t:
        for j in w:
            if i>=j:ret+=j;w.remove(j);break
    print(f'#{T+1}',ret)