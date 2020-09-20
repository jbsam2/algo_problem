from itertools import accumulate as a
n,k=map(int,input().split())
l=[0,*a(map(int,input().split()))]
print(max(l[i+k]-l[i]for i in range(n-k+1)))