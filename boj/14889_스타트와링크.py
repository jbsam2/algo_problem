from itertools import combinations as c
n=int(input())
s=[[*map(int,input().split())]for _ in range(n)]
m=[sum(i)+sum(j)for i,j in zip(s,zip(*s))]
a=sum(m)//2;p=[]
for l in c(m,n//2):p.append(abs(a-sum(l)))
print(min(p))