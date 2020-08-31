def sol(depth):
    if depth==m:ans.append(tmp[:]);return
    for i in range(n):
        if v[i]==0:v[i]=1;tmp[depth]=l[i];sol(depth+1);v[i]=0
n,m=map(int,input().split())
l=sorted([*map(int,input().split())])
tmp=[0 for i in range(m)]
v=[0 for i in range(n)]
ans=[]
sol(0)
ans.sort()
print(' '.join(map(str,ans[0])))
for i in range(1,len(ans)):
    if ans[i-1]!=ans[i]:
        print(' '.join(map(str,ans[i])))