def solution(strs, t):
    n=len(t)
    dp=[0]+[-1]*n
    for i in range(1,n+1):
        for j in range(1,6):
            if i-j>=0 and t[i-j:i] in strs and dp[i-j]!=-1:
                if dp[i]==-1:dp[i]=dp[i-j]+1
                else:dp[i]=min(dp[i],dp[i-j]+1)
    return dp[-1]