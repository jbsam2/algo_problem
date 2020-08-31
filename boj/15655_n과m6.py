def sol(depth):
    global tmp,v
    if depth==m:print(*tmp[1:]);return
    for i in l:
        if i not in v and tmp[-1]<=i:v+=[i];tmp+=[i];sol(depth+1);tmp.pop();v.remove(i)
n,m=map(int,input().split());l=sorted([*map(int,input().split())]);tmp=[0];v=[];sol(0)