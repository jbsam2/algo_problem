n=int(input())
a=[*map(int,input().split())]
e=[[*map(lambda x:int(x)-1,input().split()[1:])]for _ in range(n)]
r=10**9
for b in range(1,(1<<n)-1):
    v=[1]*n;c,f=0,1
    for s in range(n):
        if v[s]:
            if c>1:f=0;break
            v[s]=0;Q=[s]
            while Q:
                q=[]
                for i in Q:
                    for j in e[i]:
                        if((b&1<<i and b&1<<j)or(b&1<<i==0 and b&1<<j==0))and v[j]:v[j]=0;q+=[j]
                Q=q
            c+=1
    if f:r=min(r,abs(sum(a[i]for i in range(n)if b&1<<i)-sum(a[i]for i in range(n)if b&1<<i==0)))
print(r if r<10**9 else -1)