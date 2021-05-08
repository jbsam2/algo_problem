n = a = b = c = 0
size = 1000010
s = [0]*size
dp = [0]*size
xpos = [0]*size
stk = [0]*size
scnt = 0

def calc(x):
    return a*x*x + b*x +c

def k(i):
    return -2*a*s[i]

def m(i):
    return a*s[i]*s[i] - b*s[i] + dp[i]

def cross(p, q):
    k1 = k(p)
    m1 = m(p)
    k2 = k(q)
    m2 = m(q)
    return (m1-m2)/(k2-k1)

n = int(input())
a,b,c = map(int,input().split())
v = [0]+[*map(int,input().split())]
for i in range(1,n+1):
    s[i] = s[i-1] + v[i]
pt = 1
for i in range(1,n+1):
    dp[i] = calc(s[i])
    if scnt:
        while pt<scnt and xpos[pt+1]<s[i]:
            pt += 1
        j = stk[pt]
        dp[i] = max(dp[i], dp[j]+calc(s[i]-s[j]))

        while scnt>1 and xpos[scnt]>cross(stk[scnt],i):
            scnt -= 1
        scnt += 1
        stk[scnt] = i
        xpos[scnt] = cross(stk[scnt-1],i)
        if pt>scnt:
            pt = scnt
    else:
        scnt += 1
        stk[scnt] = i
        xpos[scnt] = -1e9
print(dp[n])