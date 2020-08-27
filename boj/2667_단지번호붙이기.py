dx=[1,0,-1,0];dy=[0,1,0,-1]
def dfs(y,x):
    global cnt
    cnt+=1;b[y][x]='0'
    for i in range(4):
        nx=x+dx[i];ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and b[ny][nx]=='1':dfs(ny,nx)

n=int(input());ans=[];b=[[*input()]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if b[i][j]=='1':cnt=0;dfs(i,j);ans.append(cnt)
print(len(ans))
for i in sorted(ans):print(i)