import sys
sys.setrecursionlimit(100000)
def sol(i,u):
    r=l[i]
    if u<r:return i
    k=sol(sol(i+1,r),u);print(r);return k
l=[*map(int,sys.stdin),9**9]
sol(0,9**8)

import sys
sys.setrecursionlimit(20000)
l=[*map(int,sys.stdin)]
ret=[]
def s(a,b):
    if a!=b:
        r=l[a];i=a+1
        while i<b:
            if l[i]>r:break
            i+=1
        s(a+1,i)
        s(i,b)
        ret+=[r]
s(0,len(l))
for i in ret:print(i)