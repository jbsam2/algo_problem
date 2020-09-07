from itertools import combinations as cb
for t in range(int(input())):
    n=int(input());l=[[*map(int,input().split())]for _ in range(n)];a=[sum(i)+sum(j)for i,j in zip(l,zip(*l))];b=sum(a)//2;p=[]
    for i in cb(a,n//2):p+=[abs(b-sum(i))]
    print(f'#{t+1}',min(p))