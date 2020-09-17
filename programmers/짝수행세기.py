cache={}
def c(n,k,a=1,b=1):
    if (n,k) in cache:return cache[(n,k)]
    else:
        for i in range(min(n-k,k)):
            a,b=a*(i+1),b*(n-i)
        r=b//a;cache[(n,k)]=r
        return r

def solution(a):
    l=len(a)
    s=[sum(i) for i in zip(*a)];dp=[0]*(l+1)
    dp[s[0]]=c(l,s[0])
    for v in s[1:]:
        prev=dp[:];dp=[0]*(l+1)
        for u in range(v+1):
            for e,k in enumerate(prev):
                f=e+v-2*u
                if k and 0<=f<=l and 0<=e-u<=l-v:
                    dp[f]=(dp[f]+c(e,u)*c(l-e,v-u)*k)%10000019
    return dp[0]