import sys
input=sys.stdin.readline
def f(x):
    if p[x]==x:return x
    p[x]=f(p[x])
    return p[x]
def union(x,y):
    x=f(x);y=f(y)
    if x!=y:p[y]=x
n,m=map(int,input().split());p={}
for i in range(n+1):p[i]=i
for _ in range(m):
    z,x,y=map(int,input().split())
    if z:print('YES'if f(x)==f(y)else'NO')
    else:union(x,y)