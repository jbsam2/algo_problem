import sys
sys.setrecursionlimit(100000)
def sol(i,u):
    r=l[i]
    if u<r:return i
    k=sol(sol(i+1,r),u);print(r);return k
l=[*map(int,sys.stdin),9**9]
sol(0,9**8)