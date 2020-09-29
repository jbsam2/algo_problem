n=int(input());p=[0]*(n+1)
m=[[]for _ in range(n+1)]
for _ in range(n-1):a,b=map(int,input().split());m[a].append(b);m[b].append(a)
s=[1]
while s:
    q=s.pop(0)
    for i in m[q]:
        if p[i]==0:p[i]=q;s.append(i)
for i in p[2:]:print(i)