def dfs(s):
    global visit,flag
    visit[s]=1
    if s==99:flag=1;return
    for i in range(100):
        if b[s][i] and not visit[i]:dfs(i)

for t in range(10):
    input();l=list(map(int,input().split()));b=[[0]*100 for _ in range(100)];visit=[0]*100;flag=0
    for i in range(0,len(l),2):b[l[i]][l[i+1]]=1
    dfs(0);print(f'#{t+1}',flag)