def solution(a):
    answer = 0;n=len(a)
    l=r=1<<32
    b=[[0]*2 for _ in range(n)]
    for i in range(n):
        if l>a[i]:l=a[i]
        b[i][0]=l
    for i in range(n-1,-1,-1):
        if r>a[i]:r=a[i]
        b[i][1]=r
    for i in range(n):
        if a[i]<=b[i][0] or a[i]<=b[i][1]:answer+=1
    return answer