def sol(depth):
    global answer,tmp,v
    if depth==m:print(*tmp);return
    for i in l:
        if i not in v:v+=[i];tmp+=[i];sol(depth+1);tmp.pop();v.remove(i)
n,m=map(int,input().split());l=sorted([*map(int,input().split())]);answer=[];tmp=[];v=[]
sol(0)