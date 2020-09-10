m=1000000007
def solution(n):
    dp=[1,0,3]+[0]*(n+2)
    for i in range(4,n+2,2):dp[i]=4*dp[i-2]%m-dp[i-4]%m
    return dp[n]%m