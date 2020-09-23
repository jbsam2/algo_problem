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
    cols = [r.count(1) for r in zip(*a)]
    combs = {}

    for c in range(1, m+1):
        for r in range(n+1):
            for r2 in range(n+1):
                a1, b1 = n-r2, r2
                a2, b2 = cols[c-1], n-cols[c-1]
                x2 = (r + a2 - b1)
                if x2 % 2:continue
                x = x2 // 2
                y = r - x
                if 0 <= x <= a2 and 0 <= y <= b2:
                    if (a1, x) not in combs:
                        combs[(a1, x)] = comb(a1, x)
                    if (b1, y) not in combs:
                        combs[(b1, y)] = comb(b1, y)
                    dp[c][r] += (dp[c-1][r2] * combs[(a1, x)] * combs[(b1, y)])
            dp[c][r] %= 10**7 + 19

    return dp[m][n]