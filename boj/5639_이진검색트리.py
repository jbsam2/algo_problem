import sys
def sol(i,u):
    p=l[i]
    if u<p:return i
    k=sol(sol(i+1,p),u);print(p);return k
l=[*map(int,sys.stdin),9**9];sys.setrecursionlimit(100000);sol(0,9**8)