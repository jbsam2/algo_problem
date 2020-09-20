w,h=map(int,input().split())
r=[];c=[];area=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a:r.append(b)
    else:c.append(b)
rs=[];pr=0
for i in sorted(r):rs.append(i-pr);pr=i
rs.append(w-pr)
cs=[];pc=0
for i in sorted(c):cs.append(i-pc);pc=i
cs.append(h-pc)
for i in rs:
    for j in cs:area.append(i*j)
print(max(area))