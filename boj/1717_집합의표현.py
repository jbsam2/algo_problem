o=open(0)
n,_=map(int,o.readline().split())
s=[-1]*(n+1)
def f(i):
    z=i
    while s[i]+1:i=s[i]
    if s[z]+1:s[z]=i
    return i
for p in o:
    a,b,c=map(int,p.split())
    if a:print('YES'if f(b)==f(c)else'NO');continue
    if b!=c and(x:=f(b))!=(y:=f(c)):s[x]=y



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