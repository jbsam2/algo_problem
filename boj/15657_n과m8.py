def sol(depth):
    global tmp
    if depth==m:print(*tmp[1:]);return
    for i in l:
        if tmp[-1]<=i:tmp+=[i];sol(depth+1);tmp.pop()
n,m=map(int,input().split())
l=sorted([*map(int,input().split())])
tmp=[0]
sol(0)