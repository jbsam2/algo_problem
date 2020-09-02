def g(x,y,c):
    return x+y if c=='+'else x-y if c=='-'else x*y
def f(i,c):
    return c if i>=n else max( f(i+2,g(c,int(s[i]),s[i-1])), f(i+4,g(c,g(int(s[i]),int(s[i+2]),s[i+1]),s[i-1])) if i<n-2 else -99)
n,s=int(input()),input()
print(f(2,int(s[0])))



n=int(input())
s=[*input()]
for i in range(len(s)):
    if i%2==0:s[i]=int(s[i])
ret=-(2**31)
def cal(c,idx):
    global ret
    if idx==n-1:ret=max(ret,c)
    if idx+2<n:cal(eval(str(c)+s[idx+1]+str(s[idx+2])),idx+2)
    else:ret=max(ret,c)
    if idx+4<n:cal(eval(str(c)+s[idx+1]+'('+str(s[idx+2])+s[idx+3]+str(s[idx+4])+')'),idx+4)
cal(s[0],0)
print(ret)