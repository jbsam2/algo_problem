import sys;sys.setrecursionlimit(1000000)
def f(c,r,n):
    if c*r<n: return 0,
    if n<=r:return 1,n
    x,y=f(r,c-1,n-r)
    return 1+y,r-x+1
c,r=map(int,input().split())
n=int(input())
print(*f(c,r,n))