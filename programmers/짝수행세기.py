cache={}
def c(n,k,a=1,b=1):
    if (n,k) in cache:return cache[(n,k)]
    else:
        for i in range(min(n-k,k)):a,b=a*(i+1),b*(n-i)
        cache[(n,k)]=b//a
        return cache[(n,k)]
def solution(a):
    l=len(a);s=[sum(i)for i in zip(*a)];dp=[0]*(l+1);dp[s[0]]=c(l,s[0])
    for v in s[1:]:
        prev=dp[:];dp=[0]*(l+1)
        for u in range(v+1):
            for e,k in enumerate(prev):
                f=e+v-2*u
                if k and 0<=f<=l and 0<=e-u<=l-v:dp[f]+=c(e,u)*c(l-e,v-u)*k;dp[f]%=10000019
    return dp[0]



from math import comb
def solution(a):
    n = len(a); m = len(a[0])
    dp = [[0] * (n+1) for _ in range(m+1)]
    dp[0][n] = 1
    cols = [sum(r) for r in zip(*a)]
    combs = {}

    for c in range(1, m+1):
        for r in range(n+1):
            for r2 in range(n+1):
                x2 = r + cols[c-1] - r2
                if x2 % 2:continue
                x = x2 // 2
                if 0 <= x <= cols[c-1] and 0 <= r-x <= n-cols[c-1]:
                    if (n-r2, x) not in combs:
                        combs[(n-r2, x)] = comb(n-r2, x)
                    if (r2, r-x) not in combs:
                        combs[(r2, r-x)] = comb(r2, r-x)
                    dp[c][r] += (dp[c-1][r2] * combs[(n-r2, x)] * combs[(r2, r-x)])
            dp[c][r] %= 10**7 + 19

    return dp[m][n]