m=1000000007
def solution(n):
    d=[1,0,3]+[0]*(n+2)
    for i in range(4,n+2,2):d[i]=4*d[i-2]%m-d[i-4]%m
    return d[n]%m