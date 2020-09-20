a=[[*map(int,input().split())]for _ in range(int(input()))]
a.sort()
s=0
l0,h0=a[0]
for l,h in a:
    if h0<h:s+=(l-l0)*h0;l0,h0=l,h
l1,h1=a[-1]
for l,h in a[::-1]:
    if h>h1:s+=(l1-l)*h1;l1,h1=l,h
s+=(l1-l0+1)*h1
print(s)