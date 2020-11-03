from itertools import permutations as perm
def leng(a,b):return abs(a[0]-b[0])+abs(a[1]-b[1])
for t in range(int(input())):
    n=int(input())
    c1,c2,h1,h2,*l=map(int,input().split())
    c=(c1,c2);h=(h1,h2)
    customers=[]
    ret=1<<32
    for i in range(n):
        customers.append((l[2*i],l[2*i+1]))
    for i in perm(customers):
        tmp=0
        tmp+=leng(c,i[0])
        tmp+=leng(i[-1],h)
        for j in range(1,len(i)):
            tmp+=leng(i[j],i[j-1])
        ret=min(ret,tmp)
    print(f'#{t+1}',ret)