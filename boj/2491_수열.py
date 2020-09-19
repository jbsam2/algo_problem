n=int(input())
l=[*map(int,input().split())]
I=[1]*n;D=[1]*n
for i in range(1,n):
    if l[i]>=l[i-1]:I[i]=I[i-1]+1
    if l[i]<=l[i-1]:D[i]=D[i-1]+1
print(max(max(I),max(D)))