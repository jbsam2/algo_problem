def sol(depth):
    global tmp
    if depth==m:print(*tmp);return
    for i in l:tmp+=[i];sol(depth+1);tmp.pop()
n,m=map(int,input().split())
l=sorted([*map(int,input().split())])
tmp=[]
sol(0)