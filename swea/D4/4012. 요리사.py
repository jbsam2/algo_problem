from itertools import combinations as cb
for t in range(int(input())):
    n=int(input())//2;m=2*n;l=[[*map(int,input().split())]for _ in range(m)];a=[sum(i)+sum(j)for i,j in zip(l,zip(*l))];b=sum(a)//2;p=[]
    for i in cb(a[:-1],n):p+=[abs(b-sum(i))]
    print(f'#{t+1}',min(p))