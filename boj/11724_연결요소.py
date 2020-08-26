def dfs(s):
    visit.append(s)
    for i in b[s]:
        if i not in visit:dfs(i)
n,m=map(int,input().split());b=[[]for _ in range(n+1)];visit=[];cnt=0
for _ in range(m):s,e=map(int,input().split());b[s].append(e);b[e].append(s)
for i in range(1,n+1):
    if i not in visit:dfs(i);cnt+=1
print(cnt)