def sol(idx):
    if idx>n:return 0
    if tree[idx]:return tree[idx]
    tree[idx]=sol(2*idx)+sol(2*idx+1)
    return tree[idx]

for t in range(int(input())):
    n,m,l=map(int,input().split());tree=[0 for _ in range(n+1)]
    for _ in range(m):a,b=map(int,input().split());tree[a]=b
    print('#{}'.format(t+1),sol(l))