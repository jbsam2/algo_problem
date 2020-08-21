from itertools import combinations

for t in range(int(input())):
    n=int(input());l=[list(map(int, input().split())) for _ in range(n)];r=1<<32
    for g1 in combinations(range(n),n//2):
        g2=[i for i in range(n) if i not in g1];a=b=0
        for i in range(n//2-1):
            for j in range(i+1,n//2):
                a+=l[g1[i]][g1[j]]+l[g1[j]][g1[i]];b+=l[g2[i]][g2[j]]+l[g2[j]][g2[i]]
        r=min(r,abs(a-b))
    print(f'#{t+1}',r)