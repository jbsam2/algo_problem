def sol(chk):
    if chk==last:return 1 
    if dp[chk]:return dp[chk]
    for i in range(n):
        if (chk&1<<i)==0 and (chk&r[i])==r[i]:dp[chk]+=sol(chk|1<<i)
    return dp[chk]
 
for t in range(int(input())):
    n,m=map(int, input().split())
    r=[0]*16
    dp=[0]*(1<<n) 
    for i in range(m):
        a,b=map(int, input().split())
        r[b-1]|=1<<(a-1)
    last=(1<<n)-1
    print(f'#{t+1}',sol(0))