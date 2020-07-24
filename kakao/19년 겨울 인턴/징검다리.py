def check(stones,k,n):
    temp=0
    for stone in stones:
        if stone<=n:
            temp+=1
        else:
            temp=0
        if temp>=k:
            return False
    return True

def solution(stones,k):
    l=0
    r=200000000
    while l<=r:
        n=(l+r)//2
        if check(stones,k,n):
            l=n+1
        else:
            r=n-1
    return l