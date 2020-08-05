n=list(range(1,13));L=len(n);l=[]
for i in range(1<<L):
    s=[]
    for j in range(L):
        if i&(1<<j):s.append(n[j])
    l.append(s)
for t in range(int(input())):
    n,k=map(int,input().split());r=0
    for i in l:
        if len(i)==n and sum(i)==k:r+=1
    print(f'#{t+1}',r)