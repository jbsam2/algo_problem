arr=[0]*9
def sol(c):
    global arr
    if c==m:
        for i in arr:
            if i:print(i,end=' ')
        return
    for i in range(1,n+1):
        arr[c]=i
        sol(c+1)
n,m=map(int,input().split())
sol(0)