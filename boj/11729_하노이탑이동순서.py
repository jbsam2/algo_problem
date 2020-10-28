def sol(n,s,f,e):
    if n:sol(n-1,s,e,f);print(s,f);sol(n-1,e,f,s)
n=int(input())
print(2**n-1)
sol(n,1,3,2)


'''
def sol(n,s,e,f):
    if n==1:print(s,f);return
    sol(n-1,s,f,e);sol(1,s,e,f);sol(n-1,e,s,f);return
n=int(input())
print(2**n-1)
sol(n,1,2,3)
'''