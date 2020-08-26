visit=[0]*9;arr=[0]*9
def sol(c):
    global visit,arr
    if c==m:
        for i in arr:
            if i:print(i,end=' ')
        return
    for i in range(1,n+1):
        if visit[i]==0 and i > arr[c-1]:
            visit[i]=1
            arr[c]=i
            sol(c+1)
            visit[i]=0
n,m=map(int,input().split())
sol(0)