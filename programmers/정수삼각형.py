def solution(triangle):
    n=len(triangle)
    d=[[0]*i for i in range(1,n+1)]
    a=d[0][0]=triangle[0][0]
    for i in range(1,n):
        for j in range(i+1):
            d[i][j]+=triangle[i][j]
            if j==0:d[i][j]+=d[i-1][0]
            elif j==i:d[i][j]+=d[i-1][i-1]
            else:d[i][j]+=max(d[i-1][j-1],d[i-1][j])
            a=max(a,d[i][j])
    return a