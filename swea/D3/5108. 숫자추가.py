for t in range(int(input())):
    n,m,l=map(int,input().split());b=[*input().split()]
    for _ in range(m):i,j=map(int,input().split());b.insert(i,j)
    print('#{}'.format(t+1),b[l])