def sol(a):
    while 1:
        n=a[-2]-a[-1]
        if n<0:return a
        a+=[n]
n=int(input())
a=[]
for i in range(1,n+1):
    t=sol([n,i])
    if len(t)>len(a):a=t
print(len(a))
print(*a)