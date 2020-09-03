def s(y,x,k,n):
    for i in range(y,y+k+1):
        for j in range(x,x+k+1):a[i][j]=n
def dfs(p,c):
    global m
    while p<100 and a[p//10][p%10]==0:p+=1
    if p==100:m=min(m,sum(c));return
    if sum(c)>=m:return
    i,j=p//10,p%10
    for k in range(4,-1,-1):
        if c[k]<5 and i+k<10 and j+k<10 and all(sum([a[i1][j:j+k+1] for i1 in range(i,i+k+1)],[])):c[k]+=1;s(i,j,k,0);dfs(p+k+1,c);c[k]-=1;s(i,j,k,1)
a=[[*map(int,input().split())]for _ in range(10)]
m=101
dfs(0,[0]*5)
print(m if m<101 else -1)