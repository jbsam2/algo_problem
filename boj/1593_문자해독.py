def s(a):
    if ord('a')<=ord(a)<=ord('z'):return ord(a)-ord('a')
    return ord(a)-ord('A')+26
n,m=map(int,input().split())
g=input();w=input()
G=[0]*52;W=[0]*52
c=0
for i in g:G[s(i)]+=1
for i in range(m):
    W[s(w[i])]+=1
    if i>n-2:
        if W==G:c+=1
        W[s(w[i-n+1])]-=1
print(c)