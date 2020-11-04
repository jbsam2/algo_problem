s=input()
b=input()
l=[]
n=len(b)
for i in s:
    l.append(i)
    if len(l)>=n:
        f=1
        for j in range(1,1+n):
            if l[-j]!=b[-j]:f=0;break
        if f:
            for _ in range(n):l.pop()
print(''.join(l)if l else 'FRULA')



s,p,*r=input(),[*input()];q=len(p)
for c in s:r+=c;r[-q:]*=r[-q:]!=p
print(''.join(r)or'FRULA')