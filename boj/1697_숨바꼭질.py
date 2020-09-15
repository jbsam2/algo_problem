def f(k):
    if k<=n:return n-k
    if k==1:return 1
    if k%2:return 1+min(f(k-1),f(k+1))
    return min(1+f(k//2),k-n)
n,k=map(int,input().split())
print(f(k))