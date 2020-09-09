def sol(k, used,c,n):
    global cnt
    if k==n:
        cnt+=1
        return
    for i in range(n):
        if used&(1<<i):
            continue
        for j in range(k):
            if k-j==abs(i-c[j]):
                break
        else:
            c[k]=i
            sol(k+1,used|(1<<i),c,n)
cnt=0            
def solution(n):
    c=[0]*n
    sol(0,0,c,n)
    return cnt