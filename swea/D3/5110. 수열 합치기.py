for t in range(int(input())):
    n,m=map(int,input().split())
    a=[*map(int,input().split())]
    for _ in range(m-1):
        l=[*map(int,input().split())]
        for i in range(len(a)):
            if a[i]>l[0]:a[i:0]=l;break
        else:a.extend(l)
    print('#{}'.format(t+1),*a[-1:-11:-1])