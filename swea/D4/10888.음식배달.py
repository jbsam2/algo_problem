from itertools import combinations as c
for t in range(int(input())):
 a=[];k=[];r=1<<30;b=[]
 for i in range(int(input())):
  p=[*map(int,input().split())]
  for j in range(len(p)):
   if p[j]>1:a+=[(i,j)]
   elif p[j]==1:k+=[(i,j)]
  b+=[p]
 for i in range(1,len(a)+1):
  for q in c(a,i):
   p=0
   for s in q:p+=b[s[0]][s[1]]
   for h in k:
    l=1<<30
    for s in q:l=min(abs(h[0]-s[0])+abs(h[1]-s[1]),l)
    p+=l
   r=min(r,p)
 print(f'#{t+1}',r)