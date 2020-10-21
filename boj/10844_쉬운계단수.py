n=int(input());m=1000000000;ans=0
dp=[[0]*10 for _ in range(101)]
for i in range(1,10):dp[1][i]=1
for i in range(2,n+1):
    for j in range(10):
        tmp=0
        if j>=1:tmp+=dp[i-1][j-1]
        if j<=8:tmp+=dp[i-1][j+1]
        dp[i][j]=tmp%m
for i in range(10):ans+=dp[n][i]%m
print(ans%m)