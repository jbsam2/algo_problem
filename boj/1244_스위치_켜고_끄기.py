n=int(input())
s=[2]+[*map(int,input().split())]
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a%2:
        for i in range(b,n+1,b):s[i]^=1
    else:
        i=b-1;j=b+1;s[b]^=1
        while i>0 and j<=n and s[i]==s[j]:s[i]^=1;s[j]^=1;i-=1;j+=1
for i,e in enumerate(s[1:]):
    if i and not i%20:print()
    print(e,end=' ')