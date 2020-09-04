o=["A","B","C","D","E","F"]
def solution(n,t,m,p):
    a="0";i=0
    while 1:
        if len(a)>=t*m:break
        b="";j=i
        while j:
            if j%n>9:b=o[j%n-10]+b
            else:b=str(j%n)+b
            j=j//n
        a+=b;i+=1
    return a[p-1::m][:t]