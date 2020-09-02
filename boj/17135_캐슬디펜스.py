from copy import deepcopy
from itertools import combinations as combi
def hunt(h,c):
    for i in range(1,d+1):
        for dx in range(-i,i+1):
            x,y=h+dx,n-(i-abs(dx))
            if 0<=x<m and 0<=y<n and c[y][x]:return x,y
def sol(archers):
    c=deepcopy(b)
    ret=0
    for _ in range(n):
        e=set(hunt(h,c)for h in archers)-{None};ret+=len(e)
        for x,y in e:c[y][x]=0
        for y in range(n-1,0,-1):c[y]=c[y-1][:]
        c[0]=[0]*m
    return ret
n,m,d=map(int,input().split())
b=[[*map(int,input().split())]for _ in range(n)]
print(max(sol(i)for i in combi(range(m),3)))