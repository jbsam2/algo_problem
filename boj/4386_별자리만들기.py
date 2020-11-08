'''import heapq
n=int(input())
rank=[0]*n;p=[i for i in range(n)];ret=0
pos=[[*map(float,input().split())]for _ in range(n)]
d=[[]for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist=round(((pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2)**0.5,2)
        if i==j:continue
        d[i].append([dist,j]);d[j].append([dist,i])
pq=[]
heapq.heappush(pq,[0,0])
ret=0
v=[0]*n
while pq:
    dist,f=heapq.heappop(pq)
    if v[f]:continue
    ret+=dist;v[f]=1
    for dist,e in d[f]:heapq.heappush(pq,[dist,e])
print(ret)'''


def f(v):
    if p[v]!=v:p[v]=f(p[v])
    return p[v]
n=int(input())
k=[[*map(float,input().split())]for i in range(n)]
p=[*range(n+1)]
from itertools import*
s=0
for c,b,a in sorted([(k[i][0]-k[j][0])**2+(k[i][1]-k[j][1])**2,i,j]for i,j in combinations(range(n),2)):
    a,b=f(a),f(b)
    if a!=b:p[a]=b;s+=c**.5
print(s)