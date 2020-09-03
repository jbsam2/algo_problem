def sol(depth,s):
    if depth==m:ans.append(tmp[:]);return
    for i in range(s,n):tmp[depth]=l[i];sol(depth+1,i)
n,m=map(int,input().split())
l=sorted([*map(int,input().split())])
tmp=[0 for i in range(m)]
v=[0 for i in range(n)]
ans=[]
sol(0,0)
ans.sort()
print(*ans[0])
for i in range(1,len(ans)):
    if ans[i-1]!=ans[i]:print(*ans[i])