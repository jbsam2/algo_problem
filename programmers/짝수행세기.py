cache={}
def c(n,k,a=1,b=1):
    if (n,k) in cache:return cache[(n,k)]
    else:
        for i in range(min(n-k,k)):a,b=a*(i+1),b*(n-i)
        cache[(n,k)]=b//a
        return cache[(n,k)]
def solution(a):
    n=len(a);s=[sum(i)for i in zip(*a)];dp=[0]*(n+1);dp[s[0]]=c(n,s[0])
    for v in s[1:]:
        prev=dp[:];dp=[0]*(n+1)
        for u in range(v+1):
            for e,k in enumerate(prev):
                f=e+v-2*u
                if k and 0<=f<=n and 0<=e-u<=n-v:dp[f]+=c(e,u)*c(n-e,v-u)*k;dp[f]%=10000019
    return dp[0]