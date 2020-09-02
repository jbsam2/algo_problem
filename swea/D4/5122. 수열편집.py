for t in range(int(input())):
    n,m,l=map(int,input().split());b=[*input().split()];r=0
    for _ in range(m):
        a=input().split()
        if a[0]=='I':b.insert(int(a[1]),a[2])
        if a[0]=='D':b.pop(int(a[1]))
        if a[0]=='C':b[int(a[1])]=a[2]
    try:r=int(b[l])
    except:r=-1
    print('#{}'.format(t+1),r)