w,h=map(int,input().split());l=w+h+w+h;s=[];c=0
for i in range(int(input())+1):
    a,b=map(int,input().split())
    s+=[[0,l-b,h+b,b,l-w-b][a]]
for i in s[:-1]:
    t=abs(i-s[-1])
    c+=min(t,l-t)
print(c)