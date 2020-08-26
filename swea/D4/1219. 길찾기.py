def dfs(s):
    global flag
    visit.append(s)
    if s==99:flag=1;return
    for i in b[s]:
        if i not in visit:dfs(i)
 
for t in range(10):
    input();l=list(map(int,input().split()));b=[[] for _ in range(100)];visit=[];flag=0
    for i in range(0,len(l),2):b[l[i]].append(l[i+1])
    dfs(0);print(f'#{t+1}',flag)